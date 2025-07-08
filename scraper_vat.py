import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import sqlite3
import csv

url = "https://www.podatki.gov.pl/wykaz-podatnikow-vat-wyszukiwarka"

data = {
    "term": "",
    "mimeType": "csv",
    "search": "1",
    "rpp": "50000",
    "sort": "nazwa",
    "sortDirection": "asc"
}

def search_by_nip_and_date(nip, date, cursor):
    chrome_driver_path = 'ścieżka/do/twojego/chromedriver.exe'
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(service=service)

    driver.get(url)

    conn = sqlite3.connect("baza_danych.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS firmy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazwa TEXT,
            nip TEXT,
            status TEXT
        )
    """)

    search_box = driver.find_element(By.CSS_SELECTOR, "input[name='term']")
    search_box.clear()
    search_box.send_keys(nip)

    select = Select(driver.find_element(By.CSS_SELECTOR, "select[name='type']"))
    select.select_by_visible_text("NIP")

    search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    search_button.click()

    time.sleep(2)

    status = "Nieznany"

    cursor.execute("INSERT INTO firmy (nazwa, nip, status) VALUES (?, ?, ?)", (company_name, nip, status))
    conn.commit()

    try:
        nip_element = driver.find_element(By.CSS_SELECTOR, ".results .row:nth-child(2) .col-xs-6")
        date_element = driver.find_element(By.CSS_SELECTOR, ".results .row:nth-child(3) .col-xs-6")
        day_element = driver.find_element(By.CSS_SELECTOR, ".results .row:nth-child(4) .col-xs-6")

        nip_text = nip_element.text
        date_text = date_element.text
        day_text = day_element.text

        print_confirmation_button = driver.find_element(By.CSS_SELECTOR, ".print-confirmation-btn")
        print_confirmation_button.click()

        time.sleep(2)

        pdf_url = driver.current_url

        response = requests.get(pdf_url)
        if response.status_code == 200:
            with open(f"potwierdzenie_{nip_text}_{date_text}.pdf", "wb") as file:
                file.write(response.content)
            print("Pobieranie potwierdzenia zakończone sukcesem.")
        else:
            print("Wystąpił problem podczas pobierania potwierdzenia.")
    except Exception as e:
        print("Wystąpił błąd podczas przetwarzania strony:", str(e))

    driver.quit()

    conn.close()

nip = input("Wprowadź numer NIP: ")

response = requests.post(url, data=data)

if response.status_code == 200:
    with open("lista_firm.csv", "wb") as file:
        file.write(response.content)
    print("Pobieranie zakończone sukcesem. Plik 'lista_firm.csv' został zapisany.")
else:
    print("Wystąpił problem podczas pobierania danych.")

chrome_driver_path = 'ścieżka/do/twojego/chromedriver.exe'
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

conn = sqlite3.connect("baza_danych.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS firmy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nazwa TEXT,
        nip TEXT,
        status TEXT
    )
""")

with open("lista_firm.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)  
    for row in csv_reader:
        
        continue

    company_name = row[0]
    nip = row[1]

    search_by_nip_and_date(nip, "2023-07-12", cursor)

driver.quit()

conn.close()
