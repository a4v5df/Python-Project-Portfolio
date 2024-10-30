import time
import threading 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from win10toast import ToastNotifier

# 알림 함수 
def send_notification(old_value, new_value):
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{formatted_time} / 알림: 요소가 변경되었습니다! 이전 값: {old_value}, 새로운 값: {new_value}")
    toaster = ToastNotifier()
    toaster.show_toast("수강신청", f"알림: 요소가 변경되었습니다! 이전 값: {old_value}, 새로운 값: {new_value}", duration=30)


# 웹페이지에 접속하여 특정 항목 변화를 감지하는 함수
def monitor_element_change(url, css_list, check_interval=5):
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    previous_value = [None] * len(css_list)
    current_value = [None] * len(css_list)
    
    try:
        while True:
            driver.refresh()
            i = 0
            for css_selector in css_list:
                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
                current_value[i] = element.text
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                # 이전 값과 비교하여 변경되었는지 확인
                if previous_value[i] is None:
                    previous_value[i] = current_value[i]
                    print(f"{formatted_time} / 초기 값: {current_value[i]}")

                elif previous_value[i] != current_value[i]:
                    send_notification(previous_value[i], current_value[i])
                    previous_value[i] = current_value[i]

                else:
                    print(f"{formatted_time} / 변경 없음, #{i+1} current value: {current_value[i]} ")
                i += 1

            time.sleep(check_interval)

    except Exception as e:
        print(f"오류 발생 in {url}: {e}")
        toaster = ToastNotifier()
        toaster.show_toast("에러",duration=10)
    finally:
        driver.quit()

def monitor_multiple_pages(url_css_pairs, check_interval=10):
    threads = []

    for url, css_list in url_css_pairs:
        t = threading.Thread(target=monitor_element_change, args=(url, css_list, check_interval))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

url_css_pairs = ["ex"]

monitor_multiple_pages(url_css_pairs, check_interval=120)
toaster = ToastNotifier()
toaster.show_toast("프로그램 종료",duration=10)
