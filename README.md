# Advanced OSINT Tool

An advanced **Open Source Intelligence (OSINT)** command-line tool built in Python for gathering information from multiple platforms and data sources. It supports scanning emails, phone numbers, IP addresses, domain names, usernames, and metadata extraction from files.

---

## Features

- Scan multiple **emails**, **phone numbers**, **IPs**, **domains**, **usernames**, and **files** in one run  
- Checks email validity, MX records, breaches (HaveIBeenPwned API)  
- Performs IP geolocation & ASN lookup (using ipwhois.io API)  
- Social media username presence checks across many platforms  
- Domain data retrieval  
- File metadata extraction  
- Beautiful CLI with colored output, progress bars, and informative icons  
- Generates reports in **JSON** and **PDF** formats  
- Supports multiple targets per argument (e.g. scan many emails at once)  

---

## Installation

1. Clone the repo:

```bash
   git clone https://github.com/anbuinfosec/advanced-osint-tool.git
   cd advanced-osint-tool
```

2. Create a virtual environment and activate it (recommended):

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the CLI tool with desired options:

```bash
python ossint.py --email test@example.com another@example.com --ip 8.8.8.8 --output json
```

### Arguments

| Argument     | Alias | Description                                                 | Multiple Allowed? |
| ------------ | ----- | ----------------------------------------------------------- | ----------------- |
| `--email`    | `-e`  | Email address(es) to scan                                   | Yes               |
| `--phone`    | `-p`  | Phone number(s) to scan                                     | Yes               |
| `--ip`       | `-i`  | IP address(es) to scan                                      | Yes               |
| `--domain`   | `-d`  | Domain name(s) to scan                                      | Yes               |
| `--username` | `-u`  | Social media username(s) to scan                            | Yes               |
| `--file`     | `-f`  | File(s) to scan for metadata                                | Yes               |
| `--output`   | `-o`  | Report output format: `json`, `pdf`, `both` (default: both) | No                |

---

## Example

```bash
python ossint.py --email john@example.com jane@example.com --ip 8.8.8.8 --username alice bob --output both
```

---

## Developer Info

**Name:** Mohammad Alamin
**GitHub:** [https://github.com/anbuinfosec](https://github.com/anbuinfosec)

---

## License

MIT License. See `LICENSE` file for details.

---

## Contributions

Contributions and suggestions are welcome! Feel free to open issues or pull requests.

---

## Disclaimer

This tool is intended for ethical and legal use only. Always have permission before scanning any target.