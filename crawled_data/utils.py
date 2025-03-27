# crawled_data/utils.py

from pathlib import Path

def save_crawled_html(content: str):
    static_path = Path(__file__).resolve().parent.parent / "static" / "crawled_content.html"
    static_path.parent.mkdir(parents=True, exist_ok=True)
    static_path.write_text(content, encoding="utf-8")
