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
import base64

# --- OBFUSCATION & PROTECTION ---
def _decode_key(encoded):
    return base64.b64decode(encoded).decode()

OWNER_KEY = _decode_key("U1VQREVNRS1PV05FUi1LRVk=")  # SUPREME-OWNER-KEY
PERSONAL_KEY = _decode_key("U1VQREVNRS0xMjMtS0VZ")    # SUPREME-123-KEY
TEAM_KEY = _decode_key("U1VQREVNRS00NTYtS0VZ")        # SUPREME-456-KEY
ENTERPRISE_KEY = _decode_key("U1VQREVNRS03ODktS0VZ")   # SUPREME-789-KEY

# --- CONFIG ---
VALID_LICENSE_KEYS = {
    OWNER_KEY: "Owner",
    PERSONAL_KEY: "Personal",
    TEAM_KEY: "Team",
    ENTERPRISE_KEY: "Enterprise"
}

# --- LICENSE CHECK ---
def check_license():
    license_key = os.getenv("ARCHIVER_LICENSE")
    if not license_key:
        print("❌ No license key provided. Set ARCHIVER_LICENSE environment variable.")
        return False
    
    if license_key in VALID_LICENSE_KEYS:
        tier = VALID_LICENSE_KEYS[license_key]
        if tier == "Owner":
            print("✅ Full control: Owner access granted")
        else:
            print(f"✅ Licensed user ({tier} tier)")
        return True
    else:
        print("❌ Invalid license key. Only authorized users can access this tool.")
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
