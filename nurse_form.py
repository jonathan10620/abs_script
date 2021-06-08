from form_mods.assmnt_funcs import *
from form_mods.mar_funcs import *
from form_mods.tar_funcs import *
from helpers import driver

"""
nurse form handles highlevel completion of nursing form in whole
calls upon functions from assmnt_funcs and others to modularize functionality
"""


def covid_survey():
    # bypasses section if no covid survey prompt, saves time

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