from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from scrapperapp.models import PingResult, Domain
import time


def scrape_and_save(host, request_type):
    print(f"Scraping başlıyor: {host, request_type}")

    # Domain'i kaydet veya getir
    domain, _ = Domain.objects.get_or_create(name=host)

    # Selenium başlat
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    page_url = f"https://check-host.net/check-{request_type}?host={host}"
    driver.get(page_url)

    try:
        WebDriverWait(driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        time.sleep(5)  # Sayfanın yüklenmesini beklemek için

        # Tablo satırlarını bul
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

        if not rows:
            print("HATA: Tablo içeriği bulunamadı!")
            driver.quit()
            return []

        print(f"{len(rows)} adet satır bulundu.")

        results = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text.strip() for cell in cells if cell.text.strip()]

            if row_data:
                print(f"Yeni kayıt: {row_data}")

                # JSON olarak listeyi sakla
                ping_result = PingResult.objects.create(domain=domain, data=row_data)
                results.append(ping_result.data)

    except Exception as e:
        print(f"HATA: {str(e)}")

    finally:
        driver.quit()

    if results:
        print("Scraping başarıyla tamamlandı.")
    else:
        print("HATA: Hiç veri kaydedilemedi!")

    return results
