# ============================================================
# Supreme Robot Archiver (Premium Only)
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
# Only YOU control these license keys. Distribute them only to paying users.
VALID_LICENSE_KEYS = {
    "SUPREME-OWNER-KEY": "Owner",        # Reserved for you
    "SUPREME-123-KEY": "Personal",
    "SUPREME-456-KEY": "Team",
    "SUPREME-789-KEY": "Enterprise"
}

# --- LICENSE CHECK ---
def check_license():
    license_key = os.getenv("ARCHIVER_LICENSE")
    if license_key in VALID_LICENSE_KEYS:
        tier = VALID_LICENSE_KEYS[license_key]
        if tier == "Owner":
            print("✅ Full control: Owner access granted")
        else:
            print(f"✅ Licensed user ({tier} tier)")
        return True
    else:
        print("❌ No valid license key found. Only the owner can authorize usage.")
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
