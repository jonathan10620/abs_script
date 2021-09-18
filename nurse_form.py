from form_mods.assmnt_funcs import *
from form_mods.mar_funcs import *
from form_mods.tar_funcs import *
from form_mods.io_funcs import *

from helpers import *

from datetime import datetime

from random import randint


"""
nurse form handles highlevel completion of nursing form in whole
calls upon functions from assmnt_funcs and others to modularize functionality
"""


def covid_survey():
    # bypasses section if no covid survey prompt, saves time1

    check = driver.find_element_by_id("hasCovidNo")

    if not check.is_displayed():
        return None

    try:
        driver.find_element_by_id("hasCovidNo").click()
        driver.find_element_by_id("hasCovidSymptomsNo").click()
        driver.find_element_by_id("btnSaveCovidResponse").click()
    except Exception as er:
        print(f"{er} covid screening failed..")

def complete_assmnt_section():
    assmnt_funcs = [
        allergies,
        med_assmnt,
        vital_signs,
        pain,
        psych,
        neuro,
        endocrine,
        cardio,
        respiratory,
        gastro,
        urinary,
        musculo,
        sensory,
        integ,
        ped,
        iv,
        education,
        poc,
        state,
    ]

    [f() for f in assmnt_funcs]

def complete_mar_section():
    enter_mar_section()
    mar_first_page()
    
    if at_dads():
        sleep(2.5)
        mar_second_page()
        sleep(2.5)
        mar_third_page()

def complete_tar_section():
    enter_tar_section()
    sleep(2.5)
    tar_first_page()
    sleep(2.5)
    tar_second_page()


def complete_io_section():
    enter_io_section()
    sleep(2)
    day = get_date()

    weekday = datetime.strptime(day, '%m/%d/%Y').weekday()

    if weekday == 0 or weekday == 4:
        weekday_intake()
        sleep(3)
        weekday_output()
        

    else:
        weekend_intake()
        sleep(3)
        weekend_output()

def complete_note_section():
    standard_click('#notes_li > a')
    sleep(2)
    standard_click('#refreshArea > div > div > div > div:nth-child(2) > div:nth-child(3) > a')
    sleep(2)

    note = f'CPAP placed on patient at 8:{randint(0,3)}{randint(0,9)}pm'
    date = f'{get_date()} 9:{randint(1,3)}0 PM'

    try:
        clear_and_enter_keys('#NoteDate', date)
    except:
        input('error sending string to notedate')
    
    clear_and_enter_keys('#NurseNote', note)
    sleep(1)
    standard_click('#btnSave')
