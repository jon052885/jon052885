# ============================================================
# Supreme Robot Archiver
# Copyright (c) 2026 Salvador Jon-Jon Manongdo II
# All rights reserved. Unauthorized copying prohibited.
# ============================================================

import requests
from bs4 import BeautifulSoup
import hashlib
import os
import datetime
import sys

# --- CONFIG ---
TRIAL_DAYS = 30
INSTALL_DATE = datetime.date(2026, 8, 24)  # set when first installed
VALID_LICENSE_KEYS = {
    "SUPREME-123-KEY": "Personal",
    "SUPREME-456-KEY": "Team",
    "SUPREME-789-KEY": "Enterprise"
}

# --- LICENSE CHECK ---
def check_license():
    today = datetime.date.today()
    days_used = (today - INSTALL_DATE).days

    if days_used <= TRIAL_DAYS:
        print(f"✅ Trial active: {TRIAL_DAYS - days_used} days left")
        return True

    license_key = os.getenv("ARCHIVER_LICENSE")
    if license_key in VALID_LICENSE_KEYS:
        print(f"✅ Licensed user ({VALID_LICENSE_KEYS[license_key]} tier)")
        return True
    else:
        print("❌ Trial expired. Please purchase a license to continue.")
        return False

# --- ARCHIVER FUNCTION ---
def archive_article(url, save_dir="archives"):
    os.makedirs(save_dir, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "Untitled"
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        content = "\n".join(paragraphs)

        hash_id = hashlib.sha256(url.encode()).hexdigest()[:12]
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{save_dir}/{timestamp}_{hash_id}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n\n")
            f.write(content)

        print(f"✅ Article archived: {filename}")
        return filename

    except Exception as e:
        print(f"❌ Failed to archive {url}: {e}")
        return None

# --- MAIN ---
if __name__ == "__main__":
    if not check_license():
        sys.exit(1)

    # Example usage
    url = "http://m.timesofindia.com/articleshow/133420662.cms"
    archive_article(url)
