from helpers import driver
from time import sleep
from datetime import date 
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys
from form_mods.tar_data import *
import sys

day = ""


def enter_tar_section():
    standard_click("#tar_li > a")
    sleep(4)
    month, _day, year = [int(x) for x in get_date().split("/")]
    print(month, _day, year)
    ans = date(year, month, _day)
    global day
    day = ans.strftime("%A")


def tar_first_page():
    if day == "Saturday":
        for css in sat_1_all:
            tar_click(css)
            sleep(2.5)
    elif day == "Sunday":
        for css in sun_1_all:
            tar_click(css)
            sleep(2.5)
    elif day == "Monday":
        for css in mon_list_1:
            tar_click(css)
            sleep(2.5)
    elif day == "Tuesday":
        for css in tues_list_1:
            tar_click(css)
            sleep(2.5)
    elif day == "Wednesday":
        for css in wens_list_1:
            tar_click(css)
            sleep(2.5)
    elif day == "Thursday":
        for css in thurs_list_1:
            tar_click(css)
            sleep(2.5)
    elif day == "Friday":
        for css in fri_1_am:
            tar_click(css)
            sleep(2.5)

    print("first tar page complete")


def tar_second_page():
    go_to_second_tar_page()
    sleep(5)
    if day == "Saturday":
        for css in sat_2_all:
            tar_click(css)
            sleep(2.5)
        tar_click_custom(sat_extra_all[0])
        sleep(3)
        tar_click(sat_extra_all[1])
    elif day == "Sunday":
        for css in sun_2_all:
            tar_click(css)
            sleep(2.5)
        tar_click_custom(sun_extra_all[0])
        sleep(3)
        tar_click(sun_extra_all[1])
    elif day == "Monday":
        for css in mon_list_2:
            tar_click(css)
            sleep(2.5)
        tar_click_custom(mon_list_extra[0])
        sleep(3)
        tar_click(mon_list_extra[1])
    elif day == "Friday":
        for css in fri_2_am:
            tar_click(css)
            sleep(2.5)
        tar_click_custom(fri_extra_am[0])
        sleep(3)
        tar_click(fri_extra_am[1])


    print("second tar page done")
