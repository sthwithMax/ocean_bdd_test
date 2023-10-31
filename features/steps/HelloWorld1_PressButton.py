from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


s = Service(r"C:\Driver\chromedriver_v118_win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['disable-popup-blocking', 'enable-automation', 'enable-logging'])
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--user-data-dir=C:/User/Administrator/AppData/Local/Google/Chrome/User Data/Default")


# Start a new browser session
driver = webdriver.Chrome(service=s, options=options)


# Control window size
window_width = 1436 #px
window_height = 945 #px
driver.set_window_size(window_width, window_height)


@given('I visit "{homepage_url}"')
def visitHomepage(context, homepage_url):
    driver.get(homepage_url)
    driver.implicitly_wait(30)


@when('I press a button')
def pressAButton(context):
    outtest_ele = driver.find_element(By.CLASS_NAME, "synergy")
    shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", outtest_ele).find_element( By.CSS_SELECTOR, "uxc-header")
    shadow_root2 = driver.execute_script("return arguments[0].shadowRoot", shadow_root1)
    check_button = shadow_root2.find_element(By.CSS_SELECTOR, "uxc-bed-info")
    driver.execute_script("arguments[0].click()", check_button)


@then('I should check the result')
def checkHTMLResult(context):
    outtest_ele_CR = driver.find_element(By.CLASS_NAME, "synergy")
    shadow_root1_CR = driver.execute_script("return arguments[0].shadowRoot", outtest_ele_CR).find_element(By.CSS_SELECTOR, "uxc-header")
    shadow_root2_CR = driver.execute_script("return arguments[0].shadowRoot", shadow_root1_CR)
    target_ele = shadow_root2_CR.find_element(By.CSS_SELECTOR, "uxc-other-beds-info")

    target_ele.screenshot('cur_results.png') # more scripts can be added to do the visual comparison later

    status = target_ele.is_displayed()
    assert status is True
