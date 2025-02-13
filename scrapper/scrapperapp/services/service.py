from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from scrapperapp.models import PingResult, Domain
import time


def scrape_and_save(host):
    print(f"Scraping başlıyor: {host}")

    domain, created = Domain.objects.get_or_create(name=host)
    if created:
        print(f"Yeni domain oluşturuldu: {domain.name}")
    else:
        print(f"Var olan domain kullanılıyor: {domain.name}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    page_url = f"https://check-host.net/check-ping?host={host}"
    driver.get(page_url)

    WebDriverWait(driver, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

    time.sleep(5)

    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

    if not rows:
        print("HATA: Tablo içeriği bulunamadı!")
    else:
        print(f"{len(rows)} adet satır bulundu.")

    results = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells if cell.text.strip()]

        if row_data and len(row_data) >= 4:
            print(f"Yeni kayıt: {row_data}")
            ping_result = PingResult.objects.create(
                domain=domain,
                location=row_data[0],
                ip_address=row_data[1],
                status=row_data[2],
                response_time=row_data[3],
            )
            results.append(
                {
                    "domain": ping_result.domain.name,
                    "location": ping_result.location,
                    "ip_address": ping_result.ip_address,
                    "status": ping_result.status,
                    "response_time": ping_result.response_time,
                }
            )

    driver.quit()

    if results:
        print("Scraping başarıyla tamamlandı.")
    else:
        print("HATA: Hiç veri kaydedilemedi!")

    return results
