from helpers import driver
from time import sleep
from datetime import date 
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys
from form_mods.tar_data import *
import sys

day = ""

# works as of 4/23/2022
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
        if at_dads():
            for x in sat_1_all:
                tar_click(x)
                sleep(3)
        else:
            # at moms tar Sat
            pass
    elif day == "Sunday":
        if at_dads():
            for x in sun_1_all:
                tar_click(x)
                sleep(3)
        else:
            # at at moms tar Sunday
            pass

    print("first tar page complete")


def tar_second_page():
    go_to_second_tar_page()
    sleep(3)
    input('press enter to continue for second tar')
    
    if day == "Saturday":
        for css in sat_2_all:
            tar_click(css)
            sleep(3)
        sleep(5)
        input('ready for tar extra?')
        tar_click(sat_extra_all[1])
        sleep(3)
        input('ready for tar extra 2?')
        tar_click_custom(sat_extra_all[0])

    elif day == "Sunday":
        for css in sun_2_all:
            tar_click(css)
            sleep(2.5)
        sleep(3)

        # record input tar
        tar_click('//*[@id="gridCustomerTreatment"]/table/tbody/tr[7]/td[4]/ul/li[1]/a')
        sleep(3)

        try:
            sleep(3)
            input('ready for tar extra?')
            tar_click_custom('//*[@id="gridOtherTreatment"]/table/tbody/tr[2]/td[5]/ul/li[1]/a')
        except:
            print('error when trying to do mom tar')
        sleep(3)
        try:
            input('ready for tar extra 2?')
            tar_click_custom('//*[@id="gridOtherTreatment"]/table/tbody/tr[1]/td[5]/ul/li[1]/a')
        except:
            print('error doing pain/fever tar')
        
        
    print("second tar page done")
