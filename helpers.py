from selenium import webdriver
from private import log_in_site, username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

from nurse_form import *

from time import sleep
from sys import exit
from nurse_form import (
    complete_mar_section,
    complete_tar_section,
    covid_survey,
)
driver.implicitly_wait(15)

def execute_nursing_form():
    covid_survey()
    complete_assmnt_section()
    complete_mar_section()
    complete_tar_section()


def log_in():
    driver.get(log_in_site)
    try:
        driver.find_element_by_id("UserName").send_keys(username)
        driver.find_element_by_id("Password").send_keys(password)
    except Exception as er:
        print(
            f"{er}\nIssue with log in credentials, please check username and/or password"
        )
    sleep(1.1)
    try:
        driver.find_element_by_xpath(
            "/html/body/div[@class='container body-content']/div[@class='row']/div[@class='col-md-4 content-border']/section/form/div[@class='form-group'][3]/button[@class='btn btn-default']"
        ).click()
    except Exception as er:
        print(f"{er}\nError finding log in button")


def assmnt_setup():
    sleep(2)
    driver.get("https://abscore.brightstarcare.com/General/Dashboard?dashboardId=1460")
    sleep(2)

    table_body_element = driver.find_element_by_css_selector(
        "#SkilledWorkInProcessData > div.k-grid-content.k-auto-scrollable > table > tbody"
    )

    rows = table_body_element.find_elements_by_tag_name("tr")
    # determine number of assessments to d
    num_rows = len(rows)
    # important list containing clickable elemnts of nursing forms

    assmnt_list = [
        f'//*[@id="SkilledWorkInProcessData"]/div[2]/table/tbody/tr[{n}]/td[4]/button'
        for n in range(1, num_rows + 1)
    ]

    # Iterate through all of the nursing forms in row, calling execute_form for each

    for n, i in enumerate(rows, start=1):
        print(i.text[:8], n, sep="-->")

    while True:
        selected_row = int(
            input(f"detected {num_rows} row(s). Which row would you like to enter?\n")
        )
        if selected_row not in range(1, num_rows + 1):
            print("enter valid row number!")
            continue
        else:
            break

    for num, elem in enumerate(assmnt_list, start=1):
        if selected_row == num:

            print(f"entering assessment {num}...")
            driver.find_element_by_xpath(elem).click()
            sleep(1)
            driver.switch_to_window(driver.window_handles[1])