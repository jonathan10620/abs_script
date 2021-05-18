from helpers import driver, at_dads
from time import sleep
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys
from form_mods.mar_data import *

from datetime import datetime



def enter_mar_section():
    standard_click("#mar_li > a")
    sleep(2)

def mar_first_page():
    day_of_week = get_assmnt_date()
    if at_dads:
        if day_of_week == 'Friday':
            # do friday dad meds
            for x in dad_1_morn:
                time_click_admin(x)

        elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
            for x in dad_1_all:
                time_click_admin(x)


        elif day_of_week == 'Monday':
            pass
            # do evening meds at dads
    else:
        # we are at moms
        if day_of_week == 'Friday':
            # do morning mom meds
        elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
            # do all meds
        elif day_of_week == 'Monday':
            # evening meds at mom

    print("first mar page complete")


def mar_second_page():
    standard_click(
        "#gridCustomerMedication > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > div > ul > li:nth-child(3) > a"
    )
    sleep(5)
    if at_dads:
        if day_of_week == 'Friday':
            # do friday dad meds
        elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
            # do all meds
        elif day_of_week == 'Monday':
            # do evening meds at dads
    else:
        # we are at moms
        if day_of_week == 'Friday':
            # do morning mom meds
        elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
            # do all meds
        elif day_of_week == 'Monday':
            # evening meds at mom

    print("second mar page done")


def mar_third_page():
    # enter third page
    standard_click(
        "#gridCustomerMedication > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > div > ul > li:nth-child(4) > a"
    )
    sleep(5)

    if at_dads:
        if day_of_week == 'Friday':
            # do friday dad meds
        elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
            # do all meds
        elif day_of_week == 'Monday':
            # do evening meds at dads
    else:
        # we are at moms
        if day_of_week == 'Friday':
            # do morning mom meds
        elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
            # do all meds
        elif day_of_week == 'Monday':
            # evening meds at mom