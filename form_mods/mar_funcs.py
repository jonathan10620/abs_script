from helpers import driver
from time import sleep
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys
from form_mods.mar_data import *

mode = ""


def enter_mar_section():
    standard_click("#mar_li > a")
    d = element_locator(
        '//*[@id="refreshArea"]/div/div/div/div[2]/div[1]/div[3]/h5', "x"
    )
    if "7" in d.text:
        global mode
        mode = "all"


def mar_first_page():
    if mode == "all":
        med_list_1_all = med_list_1_AM + med_list_1_PM

        for x_path in page_1_meds:
            time_click_admin(x_path)

        # for x_path in med_list_1_all:
        #     time_click_admin(x_path)
        #     sleep(2)
    else:
        for x_path in med_list_1_PM:
            time_click_admin(x_path)

    print("first mar page complete")


def mar_second_page():
    standard_click(
        "#gridCustomerMedication > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > div > ul > li:nth-child(3) > a"
    )
    sleep(5)
    if mode == "all":
        med_list_2_all = med_list_2_AM + med_list_2_PM
        for x_path in med_list_2_all:
            time_click_admin(x_path)
            sleep(2.5)
    else:
        for x_path in med_list_2_PM:
            time_click_admin(x_path)

    print("second mar page done")


def mar_third_page():
    # enter third page
    standard_click(
        "#gridCustomerMedication > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > div > ul > li:nth-child(4) > a"
    )
    sleep(5)
    if mode == "all":
        med_list_3_all = med_list_3_AM + med_list_3_PM
        for x_path in med_list_3_all:
            time_click_admin(x_path)
            sleep(3.5)
    else:
        for x_path in med_list_3_PM:
            time_click_admin(x_path)
    print("third mar page done")
