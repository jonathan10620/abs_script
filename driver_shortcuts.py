from time import sleep
from helpers import driver
import random
from selenium.webdriver.common.keys import Keys
from datetime import datetime

"""
helper functions that define common driver patterns used in browse
"""

def click_clear_keys_to_element(element, keys):

    """
    This is an all around trouble shooting function that attempts to click, clear and send_keys to an element. Used as a fail safe for uncoperative elements.
    """
    sleep(1)
    try:
        element.click()
    except Exception:
        print(f"{element}:click didnt work")
        input("acknowledge error by pressing anything..")

    try:
        element.clear()
    except Exception:
        print(f"{element}:clearing it didnt work")
        input("acknowledge error by pressing anything..")

    try:
        element.send_keys(keys)
    except Exception:
        print(f"{element}:sending it keys didnt work!")
        input("acknowledge error by pressing anything..")

    sleep(1)
    element.send_keys(Keys.ENTER)

def check_and_click_id(id):
    """this function recieves a web elements id, and performs a check to see if that element is selected, and clicks it if not.

    This funcion ensures that radio buttons are not 'unselected'
    """
    sleep(1)
    try:
        element = driver.find_element_by_id(id)
    except:
        print(f"element: cannot be found")
        input("acknowledge error by pressing anything..")

    if not (element.is_selected()):
        try:
            element.click()
        except:
            print(f"element {element} cannot be clicked!")
            input("acknowledge error by pressing anything..")

def clear_and_enter_keys(element, str, mode="c"):
    """This function recieves an element and the keys to be entered. it clears the selecteed textfield (if found), and then reenters the text to ensure double entry does not happen"""
    sleep(1)
    temp = element_locator(element, mode)

    try:
        temp.clear()
    except:
        print("Element field cannot be cleared")
        input("acknowledge error by pressing anything..")
    sleep(1)
    try:
        temp.send_keys(str)
    except:
        print("Element cannot be sent keys!")
        input("acknowledge error by pressing anything..")

def check_and_click(element, mode="c"):
    """This function recieves an element and checks to see if element is unselected before clicking it, if it is selected, nothing is done"""
    temp = element_locator(element, mode)
    sleep(1)
    try:
        if not (temp.is_selected()):
            try:
                temp.click()
            except:
                print(f"Element, {element} cannot be clicked")
                input("acknowledge error by pressing anything..")
    except:
        print("issue checking to see if element is selected found!")
        input("acknowledge error by pressing anything..")

def standard_click(element, mode="c"):
    driver.implicitly_wait(10)
    """
    function that handles errors for varying specied modes of elements
    default is css selector, howvwer can use:
    'id' for id elements
    'x' for xpath
    or c (default) for css selectors
    """
    temp = element_locator(element, mode)
    sleep(1)
    temp.click()

def element_locator(element, mode="c"):
    driver.implicitly_wait(10)
    if mode == "c":
        try:
            temp = driver.find_element_by_css_selector(element)
        except:
            print(f"Unable to find element:\n{element}!")
            input("acknowledge error by pressing anything..")
            return
        return temp

    elif mode == "x":
        try:
            temp = driver.find_element_by_xpath(element)
            return temp
        except:
            print(f"Unable to find element:\n{element}!")
            input("acknowledge error by pressing anything..")
            return

    elif mode == "id":
        try:
            temp = driver.find_element_by_id(element)
        except:
            print(f"Unable to find element:\n{element}!")
            input("acknowledge error by pressing anything..")
            return
        return temp

def drop_down_handler(element, str, mode="c"):
    temp = element_locator(element, mode)
    sleep(1)
    try:
        temp.clear()
    except:
        pass
    sleep(1)

    try:
        temp.click()
    except:
        print("element not clikcable")
        input("acknowledge error by pressing anything..")
    sleep(1)

    try:
        temp.send_keys(str)
        sleep(1)
        temp.send_keys(Keys.ENTER)
    except:
        print("element not recieving keys")
        input("acknowledge error by pressing anything..")

def get_date():
    date_text = driver.find_element_by_css_selector(
        "#refreshArea > div > div > div > div:nth-child(2) > div.row > div.col-md-2 > h5"
    ).text

    current_assmnt_date = "".join([c for c in date_text if c.isnumeric() or c == "/"])
    return current_assmnt_date

# MAR helpers
random_str_time_tail = str(random.randint(1, 9)).zfill(2)

def time_click_admin(x_str):
    time_click = element_locator(x_str, mode="x")
    try:
        sleep(1)
        time_click.click()
    except:
        print("unable to find/click elemnt")
        return
    sleep(2)

    # click admin by field 'Brightstar'
    drop_down_handler(
        "#divRequiredComment > div.row > div > span.k-widget.k-dropdown", "b"
    )
    sleep(1)

    clear_and_enter_keys("#AdminDate", get_date())
    sleep(1)

    time_to_enter = time_click.text.replace("00", random_str_time_tail)
    clear_and_enter_keys("#AdminDateTime", time_to_enter)
    sleep(1.5)

    # TODO
    standard_click("btnSubmit", "id")

# TAR helpers
def tar_click(css):
    standard_click(css, "x")
    sleep(2)
    clear_and_enter_keys("#TreatmentDate", get_date())
    sleep(1)
    clear_and_enter_keys("#TreatmentDateTime", "8:15 PM")

    standard_click("#btnSubmit")
    sleep(1)

def tar_click_custom(css):
    standard_click(css, "x")
    sleep(2)
    clear_and_enter_keys("#TreatmentDate", get_date())
    sleep(2)
    clear_and_enter_keys("#TreatmentDateTime", "8:15 PM")
    clear_and_enter_keys("#Comment", "No evidence of pain/fever")

    standard_click("#btnSubmit")
    sleep(2)

def go_to_second_tar_page():
    try:
        driver.find_element_by_css_selector(
            "#gridCustomerTreatment > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > a.k-link.k-pager-nav.k-pager-last > span"
        ).click()
        print("clicking two worked")
    except Exception:
        pass
    try:
        driver.find_element_by_css_selector(
            "#gridCustomerTreatment > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > a:nth-child(4)"
        ).click()
        print("clicking right button worked")
    except Exception:
        pass
    try:
        driver.find_element_by_css_selector(
            "#gridCustomerTreatment > div.k-pager-wrap.k-grid-pager.k-widget.k-floatwrap > a.k-link.k-pager-nav.k-pager-last > span"
        ).click()
        print("clicking far right button worked")
    except Exception:
        pass

def get_assmnt_date():
    # function return day of the week in str format of assmnt date
    date_text = driver.find_element_by_xpath(
        '//*[@id="refreshArea"]/div/div/div/div[2]/div[1]/div[2]/h5'
    ).text

    day_of_week = datetime.strptime(date_text, "Visit Date: %m/%d/%Y").strftime("%A")

    return day_of_week

def at_dads():
    return 'DAD' in element_locator('//*[@id="CustomerName"]', 'x').text