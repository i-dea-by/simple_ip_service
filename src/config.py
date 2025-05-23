from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

BASE_URL = getenv("BASE_URL", "https://your-domain.com").strip("/")  # without trailing slash

PORT = getenv("PORT", "8000")
WORKERS = getenv("WORKERS", "1")
