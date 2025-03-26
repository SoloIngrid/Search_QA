from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


def test_bing_search():
    try:
        driver.get("https://www.bing.com")
        driver.maximize_window()

        time.sleep(2)

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("QA Engineer")
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        results = driver.find_elements(By.CSS_SELECTOR, "h2")
        assert len(results) > 0, "No se encontraron resultados en la búsqueda"

        driver.save_screenshot("bing_search_result.png")
        print("Prueba completada con éxito. Captura de pantalla guardada.")

    except Exception as e:
        print(f"Error en la prueba: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_bing_search()
