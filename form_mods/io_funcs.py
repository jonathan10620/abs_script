from helpers import driver
from time import sleep
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys

from random import choice

from datetime import datetime


def enter_io_section():
    try:
        standard_click("#intake_li > a")
    except:
        standard_click('//*[@id="intake_li"]/a', "x")



def click_new_feed():
    try: 
        standard_click('#gridIntake > div.k-toolbar.k-grid-toolbar > a > span')
    except:
        print('clicking span for new feeed did not work`')
        sleep(2)
        standard_click('#gridIntake > div.k-toolbar.k-grid-toolbar > a')




def weekday_intake():
    raw_day = get_date()

    fday = datetime.strptime(raw_day, '%m/%d/%Y')
    day = fday.strftime('%m/%d/%Y')


    feedings = [
        [day, "4:30PM"],
        [day, "8:00PM"],
    ]

    sleep(3.5)

    for feed in feedings:
        # click add intake#
        click_new_feed()
        
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator("#IoTime")
        clear_and_enter_keys("#IoTime", feed[0])
        date_field.send_keys(Keys.TAB)
        sleep(1)
        clear_and_enter_keys("#IoTime", feed[1])
        sleep(1)
        date_field.send_keys(Keys.TAB)

        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[7]', "x")
        # type field xpath: //*[@id="IoType"] css: #IoType
        sleep(2)
        span_type = element_locator(
            '//*[@id="gridIntake"]/table/tbody/tr/td[7]/span[1]/span/span[1]', "x"
        )
        sleep(2)
        span_type.click()
        sleep(2)

        drop_type = element_locator(
            "#gridIntake > table > tbody > tr > td.k-edit-cell > span.k-widget.k-dropdown"
        )
        drop_type.send_keys("t")

        # Intake Amount
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(8)")
        clear_and_enter_keys("#IoAmount", "300")

        # comment section
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(9)")
        clear_and_enter_keys("#IoComments", "ketocal feeding")

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[1]/a', "x")
        sleep(3)

    free_waters = [
        [day, "7:30PM"],
    ]

    for fw in free_waters:
        # click add intake
        click_new_feed()
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator("#IoTime")
        clear_and_enter_keys("#IoTime", fw[0])
        date_field.send_keys(Keys.TAB)
        clear_and_enter_keys("#IoTime", fw[1])
        sleep(1)
        date_field.send_keys(Keys.TAB)


        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[7]', "x")

        # type --> other
        sleep(1)
        span_type = element_locator(
            '//*[@id="gridIntake"]/table/tbody/tr/td[7]/span[1]/span/span[1]', "x"
        )
        sleep(1)
        span_type.click()
        sleep(1)
        drop_type = element_locator(
            "#gridIntake > table > tbody > tr > td.k-edit-cell > span.k-widget.k-dropdown"
        )
        drop_type.send_keys("o")

        # Intake Amount
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(8)")
        clear_and_enter_keys("#IoAmount", "180")

        # comment section
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(9)")
        clear_and_enter_keys("#IoComments", "free water")

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[1]/a', "x")
        sleep(3)


def weekend_intake():
    raw_day = get_date()

    fday = datetime.strptime(raw_day, '%m/%d/%Y')
    day = fday.strftime('%m/%d/%Y')

    feedings = [
        [day, "9:00AM"],
        [day, "12:00PM"],
        [day, "4:30PM"],
        [day, "8:00PM"],
    ]

    sleep(3)

    for feed in feedings:
        # click add intake#
        click_new_feed()
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator("#IoTime")
        clear_and_enter_keys("#IoTime", feed[0])
        date_field.send_keys(Keys.TAB)
        sleep(1)
        clear_and_enter_keys("#IoTime", feed[1])
        sleep(1)
        date_field.send_keys(Keys.TAB)


        # driver.find_element_by_xpath("//html").click()

        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[7]', "x")
        # type field xpath: //*[@id="IoType"] css: #IoType
        sleep(2)
        span_type = element_locator(
            '//*[@id="gridIntake"]/table/tbody/tr/td[7]/span[1]/span/span[1]', "x"
        )
        sleep(2)
        span_type.click()
        sleep(2)

        drop_type = element_locator(
            "#gridIntake > table > tbody > tr > td.k-edit-cell > span.k-widget.k-dropdown"
        )
        drop_type.send_keys("t")

        # Intake Amount
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(8)")
        clear_and_enter_keys("#IoAmount", "300")

        # comment section
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(9)")
        clear_and_enter_keys("#IoComments", "ketocal feeding")

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[1]/a', "x")
        sleep(3)

    free_waters = [
        [day, "2:00PM"],
        [day, "7:30PM"],
    ]

    for fw in free_waters:

        # click add intake
        click_new_feed()
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator("#IoTime")
        clear_and_enter_keys("#IoTime", fw[0])
        date_field.send_keys(Keys.TAB)
        clear_and_enter_keys("#IoTime", fw[1])

        driver.find_element_by_xpath("//html").click()

        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[7]', "x")

        # type --> other
        sleep(1)
        span_type = element_locator(
            '//*[@id="gridIntake"]/table/tbody/tr/td[7]/span[1]/span/span[1]', "x"
        )
        sleep(1)
        span_type.click()
        sleep(1)
        drop_type = element_locator(
            "#gridIntake > table > tbody > tr > td.k-edit-cell > span.k-widget.k-dropdown"
        )
        drop_type.send_keys("o")

        # Intake Amount
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(8)")
        clear_and_enter_keys("#IoAmount", "180")

        # comment section
        standard_click("#gridIntake > table > tbody > tr > td:nth-child(9)")
        clear_and_enter_keys("#IoComments", "free water")

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[1]/a', "x")
        sleep(3)


def weekend_output():
    raw_day = get_date()

    fday = datetime.strptime(raw_day, '%m/%d/%Y')
    day = fday.strftime('%m/%d/%Y')

    first_out = ["9:30AM", "10:15AM", "8:15AM"]
    second_out = ["12:00PM", "1:20PM", "2:30PM"]
    third_out = ["3:15PM", "4:10PM", "3:45PM"]
    fourth_out = ["6:50PM", "8:10PM", "7:30PM"]
    fifth_out = ["11:30PM", "10:00PM", "9:50PM"]

    output_times = [
        [day, choice(first_out)],
        [day, choice(second_out)],
        [day, choice(third_out)],
        [day, choice(fourth_out)],
        [day, choice(fifth_out)],
    ]

    for output in output_times:
        # click add ouput
        standard_click("#gridOutput > div.k-toolbar.k-grid-toolbar > a")
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator("#IoTime")
        clear_and_enter_keys("#IoTime", output[0])
        date_field.send_keys(Keys.TAB)
        clear_and_enter_keys("#IoTime", output[1])

        driver.find_element_by_xpath("//html").click()

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('#gridOutput > table > tbody > tr > td:nth-child(1) > a')
        sleep(2)


def weekday_output():
    raw_day = get_date()

    fday = datetime.strptime(raw_day, '%m/%d/%Y')
    day = fday.strftime('%m/%d/%Y')
    first_out = ["4:30PM", "5:00PM", "4:10PM"]
    second_out = ["6:50PM", "8:10PM", "7:30PM"]
    third_out = ["11:30PM", "10:00PM", "9:50PM"]

    output_times = [
        [day, choice(first_out)],
        [day, choice(second_out)],
        [day, choice(third_out)],
    ]

    for output in output_times:
        # click add ouput
        
        standard_click("#gridOutput > div.k-toolbar.k-grid-toolbar > a")
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator("#IoTime")
        clear_and_enter_keys("#IoTime", output[0])
        date_field.send_keys(Keys.TAB)
        clear_and_enter_keys("#IoTime", output[1])

        driver.find_element_by_xpath("//html").click()

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('#gridOutput > table > tbody > tr > td:nth-child(1) > a')
        sleep(2)