from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from scrapperapp.models import PingResult


def scrape_and_save():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    page_url = "https://check-host.net/check-ping?host=google.com"
    driver.get(page_url)

    WebDriverWait(driver, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells if cell.text.strip()]

        if row_data and len(row_data) >= 4:
            PingResult.objects.create(
                location=row_data[0],
                ip_address=row_data[1],
                status=row_data[2],
                response_time=row_data[3],
            )

    driver.quit()
