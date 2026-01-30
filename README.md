# imap-settings-scraper 🚀

An automated tool to discover IMAP server hostnames and port settings for a list of domains using Selenium and the imapsettings.com database.

## 🛠️ Features
- **Batch Processing:** Reads multiple domains from a text file.
- **Automated Search:** Uses Selenium to interact with the web interface automatically.
- **Clean Output:** Saves results in a Python-dictionary-ready format (`'domain': ('server', 'port')`).
- **Error Handling:** Gracefully handles missing information by marking results as `none`.

## 📋 Requirements
- Python 3.x
- Google Chrome Browser
- Selenium Library

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Tetherium/imap-settings-scraper.git](https://github.com/Tetherium/imap-settings-scraper.git)
cd imap-settings-scraper
```

### 2. Install Dependencies
Install the required Selenium library using pip:

```bash

pip install -r requirements.txt
```

### 3. Prepare Input Data
Create a file named INPUT.txt in the root directory. Add the domains you want to scan, one domain per line.

Example INPUT.txt:

Plaintext

gmail.com
yahoo.com
outlook.com
yandex.com

💻 Usage
Run the scraper using the following command:

```bash

python find_imap_adress.py
```
📂 Output
Once the process is complete, the results will be saved to OUTPUT.txt in the following format:

Python

'gmail.com': ('imap.gmail.com', '993'),
'example.com': ('none', 'none'),
⚠️ Important Notes
Web Driver: Ensure you have Google Chrome installed. Selenium will attempt to manage the driver automatically.

Rate Limiting: If you have a very large list, consider increasing the sleep() duration in the script to avoid being flagged as a bot by the source website.

Formatting: Ensure INPUT.txt has no empty lines or spaces for the best results.


Developed by Tetherium

