"""Generate the Shapescape Content Guide PDF.

Self-contained PDF builder shipped by the Shapescape Content Guide Generator
filter. After `regolith install`, this script lives next to TEMPLATE.md,
styling/, and images/ inside the consuming project's filter-data folder.

Usage:
    python generate_content_guide.py <version>

The script auto-detects the project root by walking up from its own location
looking for a release.json (or release_test.json) — no .scripts/ dependency.
Requires Node.js + md-to-pdf available on PATH.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"%%[A-Z0-9_]+%%")


def find_project_root(start: Path) -> Path:
    for parent in [start, *start.parents]:
        if (parent / "release.json").exists() or (parent / "release_test.json").exists():
            return parent
    raise FileNotFoundError("Could not locate release.json / release_test.json from " + str(start))


def strip_jsonc(text: str) -> str:
    text = re.sub(r"//[^\n]*", "", text)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text


def load_release(project_root: Path) -> dict:
    release_path = project_root / "release.json"
    if release_path.exists():
        data = json.loads(strip_jsonc(release_path.read_text(encoding="utf-8")))
        if PLACEHOLDER_RE.search(json.dumps(data)):
            fallback = project_root / "release_test.json"
            if fallback.exists():
                return json.loads(strip_jsonc(fallback.read_text(encoding="utf-8")))
        return data
    fallback = project_root / "release_test.json"
    if fallback.exists():
        return json.loads(strip_jsonc(fallback.read_text(encoding="utf-8")))
    raise FileNotFoundError(f"No release.json or release_test.json under {project_root}")


def install_fonts(fonts_dir: Path) -> None:
    if not fonts_dir.exists():
        return
    if sys.platform == "win32":
        user_fonts = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "Windows" / "Fonts"
    else:
        user_fonts = Path.home() / ".fonts"
    try:
        user_fonts.mkdir(parents=True, exist_ok=True)
        for font in fonts_dir.glob("*.ttf"):
            dest = user_fonts / font.name
            if not dest.exists():
                shutil.copy2(font, dest)
                print(f"Installed font: {font.name}")
        if sys.platform != "win32":
            subprocess.run(["fc-cache", "-f", "-v"], capture_output=True)
    except Exception as e:
        print(f"[WARNING] Could not install fonts: {e}")


def ensure_md_to_pdf() -> bool:
    try:
        result = subprocess.run(["npm", "list", "-g", "md-to-pdf"], capture_output=True, text=True)
        if "md-to-pdf" in result.stdout:
            return True
    except Exception:
        pass
    print("Installing md-to-pdf globally...")
    try:
        subprocess.run(["npm", "install", "-g", "md-to-pdf"], check=True)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to install md-to-pdf: {e}")
        return False


def locate_output_md(project_root: Path, filter_dir: Path) -> Path | None:
    candidates = [
        filter_dir / "OUTPUT.md",
        project_root / ".regolith" / "tmp" / "data" / "shapescape_content_guide_generator" / "OUTPUT.md",
        project_root / ".regolith" / "tmp" / "data" / "OUTPUT.md",
        project_root / ".regolith" / "tmp" / "OUTPUT.md",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None


def build_footer_template(product_name: str) -> str:
    safe = product_name.replace('"', '\\"')
    return (
        "<style>"
        ".cg-footer{width:100%;padding:0 22mm;font-family:'Inter','Helvetica',sans-serif;"
        "font-size:8pt;color:#041c3b;display:flex;justify-content:space-between;"
        "align-items:center;-webkit-print-color-adjust:exact;}"
        ".cg-footer .left{display:flex;align-items:center;gap:6pt;}"
        ".cg-footer .dot{width:6pt;height:6pt;background:#cfb7f5;border-radius:1.5pt;display:inline-block;}"
        ".cg-footer .right{letter-spacing:0.06em;text-transform:uppercase;}"
        "</style>"
        f"<div class='cg-footer'><div class='left'><span class='dot'></span>"
        f"<span>{safe}</span></div>"
        "<div class='right'>Page <span class='pageNumber'></span> / <span class='totalPages'></span></div></div>"
    )


def generate(version: str) -> Path | None:
    print("\n" + "=" * 60)
    print("CONTENT GUIDE GENERATION")
    print("=" * 60)

    filter_dir = Path(__file__).resolve().parent
    project_root = find_project_root(filter_dir)
    styling_dir = filter_dir / "styling"
    css_file = styling_dir / "CGG.css"
    fonts_dir = styling_dir / "fonts"
    images_dir = filter_dir / "images"
    template_file = filter_dir / "TEMPLATE.md"

    if not css_file.exists():
        print(f"[ERROR] CSS not found: {css_file}")
        return None

    release = load_release(project_root)
    product_name = release.get("product_name", "Project")

    install_fonts(fonts_dir)
    if not ensure_md_to_pdf():
        return None

    md_source = locate_output_md(project_root, filter_dir)
    if md_source is None:
        if template_file.exists():
            print(f"[WARNING] No OUTPUT.md found, using template: {template_file}")
            md_source = template_file
        else:
            print("[ERROR] No markdown source available")
            return None
    print(f"Using markdown: {md_source}")

    out_dir = project_root / "out" / "content_guide"
    out_dir.mkdir(parents=True, exist_ok=True)
    safe_pn = product_name.replace(" ", "_").replace("%%", "").strip("_") or "Project"
    output_path = out_dir / f"Content_Guide_{safe_pn}-{version}.pdf"

    work_dir = project_root / ".regolith" / "tmp" / "content_guide_work"
    if work_dir.exists():
        shutil.rmtree(work_dir, ignore_errors=True)
    work_dir.mkdir(parents=True, exist_ok=True)

    temp_md = work_dir / "content_guide.md"
    shutil.copy2(md_source, temp_md)
    shutil.copy2(css_file, work_dir / "CGG.css")
    if fonts_dir.exists():
        shutil.copytree(fonts_dir, work_dir / "fonts")
    if images_dir.exists():
        shutil.copytree(images_dir, work_dir / "images")

    footer_template = build_footer_template(product_name)
    config = (
        "---\n"
        f"dest: {output_path.as_posix()}\n"
        "stylesheet:\n"
        f"  - {(work_dir / 'CGG.css').as_posix()}\n"
        "body_class: markdown-body\n"
        "highlight_style: monokai\n"
        "pdf_options:\n"
        "  format: A4\n"
        "  margin:\n"
        "    top: 22mm\n"
        "    right: 22mm\n"
        "    bottom: 22mm\n"
        "    left: 22mm\n"
        "  printBackground: true\n"
        "  displayHeaderFooter: true\n"
        f"  headerTemplate: {json.dumps('<div></div>')}\n"
        f"  footerTemplate: {json.dumps(footer_template)}\n"
        "---\n\n"
    )

    md_text = temp_md.read_text(encoding="utf-8")
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]
    md_text = md_text.replace("PRODUCTNAME", product_name)
    temp_md.write_text(config + md_text, encoding="utf-8")

    print(f"\nGenerating PDF: {output_path.name}")
    cmd = ["npx", "md-to-pdf", str(temp_md)]
    if os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true":
        cmd.extend(["--launch-options", '{"args":["--no-sandbox","--disable-setuid-sandbox"]}'])

    try:
        result = subprocess.run(cmd, cwd=str(work_dir), capture_output=True, text=True, timeout=180)
        if result.returncode != 0:
            print(f"[ERROR] md-to-pdf failed:\n{result.stderr}")
            return None
    except subprocess.TimeoutExpired:
        print("[ERROR] md-to-pdf timed out")
        return None
    except Exception as e:
        print(f"[ERROR] Failed to run md-to-pdf: {e}")
        return None
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

    if output_path.exists():
        print(f"[OK] Content guide generated: {output_path}")
        return output_path
    print("[ERROR] PDF file was not created")
    return None


def main() -> int:
    env_vars = ("PACKAGE_VERSION", "PROJECT_VERSION", "VERSION", "TEST_VERSION")
    version = next((v for v in (os.getenv(name) for name in env_vars) if v), None)
    args = sys.argv[1:]
    if args and not args[0].startswith("--"):
        version = args[0]
    if not version:
        print("Usage: python generate_content_guide.py <version>")
        print("  Or set one of: " + ", ".join(env_vars))
        return 1
    result = generate(version)
    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
