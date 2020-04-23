from selenium import webdriver
import time
import math

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    new_window = browser.window_handles[1]
    #first_window = browser.windows_handles[0]
    browser.switch_to.window(new_window)
   
    x = browser.find_element_by_id("input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    time.sleep(1)
    button = browser.find_element_by_tag_name("button.btn").click()

finally:
    time.sleep(6)
    browser.quit()

# не забываем оставить пустую строку в конце файла

