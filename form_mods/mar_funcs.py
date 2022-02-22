from helpers import driver
from time import sleep, time
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys
from form_mods.mar_data import *

from datetime import datetime

def enter_mar_section():
    standard_click("#mar_li > a")
    sleep(2)

def mar_first_page():
    day_of_week = get_assmnt_date()
    if at_dads():
        if day_of_week == "Friday":
            for x in dad_1_pm:
                time_click_admin(x)
        elif day_of_week == "Saturday" or day_of_week == "Sunday":
            for x in dad_1_all:
                time_click_admin(x)
        elif day_of_week == "Monday":
            for x in dad_1_pm:
                time_click_admin(x)
    else:
        # at moms
        if day_of_week == "Saturday" or day_of_week == "Sunday":
            for x in mom_1_all:
                time_click_admin(x)
            try:
                mar_exception(mom_vitd, 'Given by night nurse')
            except Exception as e:
                print(e)
                input('mar exception for vit. d didnt work, but that is ok')
        else:
            # assume it is monday or friday (PM days)
            for x in mom_1_pm:
                time_click_admin(x)

    print("first mar page complete")

def mar_second_page():
    day_of_week = get_assmnt_date()
    standard_click(
        '#gridCustomerMedication > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > div > ul > li:nth-child(2) > a'
    )
    sleep(5)
    if at_dads():
        if day_of_week == "Friday":
            for x in dad_2_pm:
                time_click_admin(x)
            salt()
        elif day_of_week == "Saturday" or day_of_week == "Sunday":
            for x in dad_2_all:
                time_click_admin(x)
            salt()
        elif day_of_week == "Monday":
            for x in dad_2_pm:
                time_click_admin(x)
            salt()
    else:
        # at moms
        if day_of_week == "Saturday" or day_of_week == "Sunday":
            # do feedings
            for x in mom_feedings:
                exact_time_click_admin(x)
            # do clobazam
            time_click_admin(mom_2_clobazam)
        else:
            # do feedings
            for x in mom_feedings[2:]:
                exact_time_click_admin(x)

    print("second mar page done")


def mar_third_page():
    day_of_week = get_assmnt_date()
    standard_click(
        '#gridCustomerMedication > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > div > ul > li:nth-child(3) > a'
    )
    sleep(5)
    if at_dads():
        if day_of_week == "Friday":
            # 7pm onfi
            time_click_admin('//*[@id="gridCustomerMedication"]/table/tbody/tr[1]/td[4]/ul/li[2]/a')
            sleep(1)
            milk()
        elif day_of_week == "Saturday" or day_of_week == "Sunday":
            # 2pm and 7pm onfi
            time_click_admin('//*[@id="gridCustomerMedication"]/table/tbody/tr[1]/td[4]/ul/li[2]/a')
            sleep(1)
            time_click_admin('//*[@id="gridCustomerMedication"]/table/tbody/tr[2]/td[4]/ul/li/a')
            sleep(1)
            milk()
        elif day_of_week == "Monday":
            time_click_admin('//*[@id="gridCustomerMedication"]/table/tbody/tr[1]/td[4]/ul/li[2]/a')
            sleep(1)
            milk()
