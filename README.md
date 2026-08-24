# Supreme Robot Archiver - README

## 📋 Overview
The **Supreme Robot Archiver** is a premium, license-protected web content archival tool for authorized users only.

## ✅ Features
- 🔐 License-based access control with multiple tiers
- 🛡️ Base64-encoded keys preventing easy copying
- 📁 Automatic content archival with timestamps
- 🔍 SHA256-based unique file identification
- 📝 Clean text extraction and storage

## ⚠️ IMPORTANT LEGAL NOTICES

### License Required
**This software requires a valid license key to operate.** Unauthorized use is prohibited.

### Compliance Obligations
- ✅ Respect website terms of service
- ✅ Comply with robots.txt directives
- ✅ Obtain necessary permissions for content archival
- ✅ Ensure all archival activities are lawful
- ✅ Do not violate copyright or intellectual property rights

### Prohibited Activities
- ❌ Bypassing access controls
- ❌ Scraping protected or copyrighted content without permission
- ❌ Circumventing license key validation
- ❌ Illegal data collection
- ❌ Violating third-party service agreements

## 🚀 Installation

```bash
# Clone repository
git clone https://github.com/jon052885/jon052885.git
cd jon052885

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
# Edit .env with your valid license key
```

## 🔑 License Keys

| Key | Tier | Access |
|-----|------|--------|
| `SUPREME-OWNER-KEY` | Owner | Full control (Creator only) |
| `SUPREME-123-KEY` | Personal | Single user |
| `SUPREME-456-KEY` | Team | Small teams |
| `SUPREME-789-KEY` | Enterprise | Organization-wide |

## 🏃 Usage

```bash
# Set your license key
export ARCHIVER_LICENSE="SUPREME-OWNER-KEY"

# Run the archiver
python archiver.py
```

## 📁 Output
Archived articles are saved to `archives/` directory with format:
```
archives/YYYYMMDD_HHMMSS_<hash>.txt
```

## 🔒 Security Features
- ✅ Base64-encoded license keys
- ✅ Environment variable-based configuration
- ✅ .gitignore prevents accidental commits
- ✅ No hardcoded sensitive data in main file
- ✅ License validation on startup

## 📋 Terms & Conditions
**Full legal agreement available in [LICENSE.md](LICENSE.md)**

### Key Points:
- Non-exclusive, non-transferable license
- Strictly forbidden: copying, distribution, reverse engineering
- Users responsible for legal compliance with third-party content
- Software provided "AS-IS" with no warranties
- License terminates on violation of terms

## ⚖️ User Responsibilities
By using this software, you agree to:
1. Comply with all applicable laws
2. Respect website terms and robots.txt
3. Obtain necessary permissions for content archival
4. Maintain confidentiality of your license key
5. Report any unauthorized access immediately

## ⚠️ Disclaimer
The copyright holder is **NOT responsible for**:
- Illegal use of this software
- Violations of third-party terms of service
- Copyright infringement from archived content
- Data loss or system failures
- Any damages arising from use of this software

## 🔗 Legal Reference
See [LICENSE.md](LICENSE.md) for complete terms including:
- IP ownership
- Warranty disclaimers
- Liability limitations
- Indemnification clauses
- Termination conditions

## 📞 Support
For legitimate inquiries:
- GitHub: https://github.com/jon052885/jon052885
- Report violations through GitHub issues

---

**COPYRIGHT (c) 2026 Salvador Jon-Jon Manongdo II**  
**All Rights Reserved. Unauthorized copying prohibited.**
