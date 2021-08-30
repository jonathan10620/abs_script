from helpers import driver
from time import sleep
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys

from random import choice

from datetime import datetime


# add intake button 
# xpath: //*[@id="gridIntake"]/div[1]/a
# css:  #gridIntake > div.k-header.k-grid-toolbar > a

# save button 
# xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a
# css: #gridIntake > table > tbody > tr > td:nth-child(1) > a

# date/time field
# xpath: //*[@id="IoTime"]
# css: #IoTime

# type field
# xpath: //*[@id="IoType"]
# css: #IoType

# amount field
# xpath: //*[@id="IoAmount"]
# css: #IoAmount

# comment field
# xpath: //*[@id="IoComments"]
# css: #IoComments


def enter_io_section():
    # io section
    # css: #intake_li > a
    # xpath: //*[@id="intake_li"]/a
    try:
        standard_click('#intake_li > a')
    except:
        standard_click('//*[@id="intake_li"]/a', 'x')

def weekday_intake():
    # INTAKE
    # depending on shift enter 5 feedings and 3 free water intakes
    # feeding times can be 10am, 1pm, 5pm, 8pm
    # free water times: 7:30pm

    # if weekend:
        # do feeding entries for all
        # do water time entries for all
    # else:
        # do entries list[2:]
        # do entries for free water 7:30pm
    
    # save the entry 
    # sleep 2 second
    pass



def weekend_intake():
    day = get_date()

    feedings = [
        [day, '9:00AM'],
        [day, '12:00PM'],
        [day, '4:30PM'],
        [day, '8:00PM'],
    ]


    sleep(1.5)

    for feed in feedings:
        #click add intake#
        standard_click('#gridIntake > div.k-header.k-grid-toolbar > a')
        sleep(2)

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator('#IoTime')
        clear_and_enter_keys('#IoTime', feed[0])
        date_field.send_keys(Keys.TAB)
        clear_and_enter_keys('#IoTime', feed[1])

        driver.find_element_by_xpath('//html').click()



        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[7]', 'x')
        # type field xpath: //*[@id="IoType"] css: #IoType
        sleep(1)
        span_type = element_locator('//*[@id="gridIntake"]/table/tbody/tr/td[7]/span[1]/span/span[1]', 'x')
        sleep(1)
        span_type.click()
        sleep(1)

        drop_type = element_locator('#gridIntake > table > tbody > tr > td.k-edit-cell > span.k-widget.k-dropdown')
        drop_type.send_keys('t')

        # Intake Amount
        standard_click('#gridIntake > table > tbody > tr > td:nth-child(8)')
        clear_and_enter_keys('#IoAmount', '300')

        # comment section
        standard_click('#gridIntake > table > tbody > tr > td:nth-child(9)')
        clear_and_enter_keys('#IoComments', 'ketocal feeding')
        

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[1]/a', 'x')
        sleep(3)



def weekend_output():
    day = get_date()

    first_out = ['9:30AM', '10:15AM', '8:15AM']
    second_out = ['12:00PM', '1:20PM', '2:30PM']
    third_out = ['3:15PM', '4:10PM', '3:45PM']
    fourth_out = ['6:50PM', '8:10PM', '7:30PM']
    fifth_out = ['11:30PM', '10:00PM', '9:50PM']

    

    output_times = [
        [day, choice(first_out)],
        [day, choice(second_out)],
        [day, choice(third_out)],
        [day, choice(fourth_out)],
        [day, choice(fifth_out)]
    ]

    for output in output_times:
        # click add ouput
        standard_click('#gridOutput > div.k-header.k-grid-toolbar > a')
        sleep(2)

        

        # date/time field xpath: //*[@id="IoTime"] css: #IoTime
        date_field = element_locator('#IoTime')
        clear_and_enter_keys('#IoTime', output[0])
        date_field.send_keys(Keys.TAB)
        clear_and_enter_keys('#IoTime', output[1])

        driver.find_element_by_xpath('//html').click()
        

        # save button xpath: //*[@id="gridIntake"]/table/tbody/tr/td[1]/a css: #gridIntake > table > tbody > tr > td:nth-child(1) > a
        standard_click('//*[@id="gridIntake"]/table/tbody/tr/td[1]/a', 'x')
        sleep(3)
    

def weekday_output():
    pass