# Polish VAT Taxpayer Verification Scraper

This Python script automates the process of checking entities against the official Polish VAT taxpayer list (the "White List" or _Wykaz podatników VAT_). It uses Selenium to control a web browser, fetches data based on a NIP number, and stores results in a local SQLite database and a CSV file.

---

## Features

- ✅ Automates searching the [podatki.gov.pl](https://www.podatki.gov.pl/) portal  
- 📄 Fetches a complete list of active VAT taxpayers into a `lista_firm.csv` file  
- 🔍 Checks a specific NIP number against the list on a given date  
- 💾 Saves query results to a local SQLite database  
- 📥 Downloads a PDF confirmation of the verification  

---

## Setup and Installation

To run this project, you’ll need **Python 3**, **Google Chrome**, and the corresponding **ChromeDriver**.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-vat-scraper.git
cd python-vat-scraper
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Install ChromeDriver

This script uses Selenium with Chrome. You must install the correct version of ChromeDriver for your browser.

- Download ChromeDriver from the [Chrome for Testing dashboard](https://googlechromelabs.github.io/chrome-for-testing/)
- Extract and move the `chromedriver` (or `chromedriver.exe`) to a known location
- In `scraper_vat.py`, set the `chrome_driver_path` variable to the full path of your ChromeDriver executable.

Example:

```python
chrome_driver_path = "/path/to/chromedriver"
```

---

## How to Run

After completing the setup, run the script with:

```bash
python scraper_vat.py
```

The script will:

1. Download a full list of VAT-registered companies to `lista_firm.csv`
2. Prompt you to enter a NIP number
3. Perform a VAT taxpayer check for that NIP
4. Save the result to:
   - An SQLite database
   - A downloadable PDF confirmation

---

## Project Structure

```
python-vat-scraper/
├── scraper_vat.py                 # Main script
├── requirements.txt               # Python dependencies
├── lista_firm.csv                 # Output file with VAT list (generated)
├── vat_checks.db                  # SQLite database (generated)
├── confirmation.pdf               # PDF download (generated)
└── README.md
```

---

## Notes

- Ensure your internet connection is active — the script interacts with the official podatki.gov.pl website.
- This project is intended for educational and non-commercial use.
- For better stability, avoid running too many requests in rapid succession.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

Developed by **mateuszvdl**  
Feel free to contribute, fork, or raise issues if you find bugs or have suggestions!
