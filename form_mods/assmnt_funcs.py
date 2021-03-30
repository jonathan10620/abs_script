from helpers import driver
from time import sleep
from driver_shortcuts import *
from selenium.webdriver.common.keys import Keys

from random import randint, uniform

# store date globally
def vital(time):
    # SETUP
    # hit add button and wait for pop up
    standard_click("addVitalSign", mode=id)
    sleep(2)

    # TIME
    # enter time (be sure to distinguish am and pm)
    time_css = "body > div:nth-child(65) > div.k-popup-edit-form.k-window-content.k-content > div > div:nth-child(2) > span > span > input"

    clear_and_enter_keys(time_css, time)

    # BP
    sys_css = "body > div:nth-child(65) > div.k-popup-edit-form.k-window-content.k-content > div > div:nth-child(4) > span > span > input.k-formatted-value.k-input"

    sys_val = str(randint(100, 115))
    clear_and_enter_keys(sys_css, sys)

    dia_css = "body > div:nth-child(65) > div.k-popup-edit-form.k-window-content.k-content > div > div:nth-child(6) > span > span > input.k-formatted-value.k-input"

    if int(sys_val) < 108:
        # enter dias randrange 65-72
        dia_val = str(randint(65 - 72))
        clear_and_enter_keys(dia_css, dia_val)
        # else
        # entre dias range range 70-78
        dia_val = str(randint(70 - 78))
        clear_and_enter_keys(dia_css, dia_val)

    # POSITION
    # if '8' in time:
    # click and send keys('l')
    # else:
    # click and send keys('si')

    # TEMP
    # temp = str(round(uniform(97.8,98.2), 1))

    # click and send keys(temp)

    # taken by
    # click and send keys('a')

    # PUlSE
    # pulse = randint(100,120)
    # click and send keys(pulse)

    # Location
    # click and send keys('a')

    # Breaths per minute
    # breaths = str(randint(22,26))
    # click and send keys(breaths)

    # Spo2
    # spo2 = str(randint(97,99))
    # click and send keys(spo2)

    # taken
    # click and send keys('At')

    # o2
    # click and send keys('off')

    # click update

    # sleep(3)


# DONE!!!
def allergies():
    try:
        driver.find_element_by_xpath('//*[@id="allergiesBar"]/span').click()
        sleep(1)
    except Exception as er:
        print(f"{er}\n could not find allergies bar..")

    sleep(1)

    try:
        allergy_changes_radio = driver.find_element_by_id(
            "VisitAssessment_AllergiesSection_AnyChanges_0"
        )
    except Exception as er:
        print(f"{er}\n could not find no changes in allergies button")

    allergy_changes_radio.click()
    print("Allergy section complete")
    sleep(1)


# DONE!!!
def med_assmnt():
    # click span bar to open up the med section of assmnt
    try:
        driver.find_element_by_css_selector("#medicationBar > span").click()
    except Exception as er:
        print(f"Unable to locate med row bar: {er}")
    sleep(1.5)

    # no changes to medication radio button
    try:
        med_changes_radio = driver.find_element_by_css_selector(
            "#VisitAssessment_MedicationSection_AnyChanges_0"
        )
    except Exception as er:
        print(f'Unable to locate in med "no changes" radio button: {er}')
    sleep(1.5)
    med_changes_radio.click()

    # patient adhering to medication
    try:
        adhering_to_med_radio = driver.find_element_by_css_selector(
            "#VisitAssessment_MedicationSection_AdheringToMedication_true"
        )
    except Exception as er:
        print(f'Unable to locate in med "adhering to med" radio button: {er}')
    adhering_to_med_radio.click()
    sleep(1.5)

    # medication reconciliation
    try:
        med_recon_radio = driver.find_element_by_css_selector(
            "#VisitAssessment_MedicationSection_MedicationReconciliationComplete_true"
        )
    except Exception as er:
        print(f'Unable to locate in med "adhering to med" radio button: {er}')
    med_recon_radio.click()
    sleep(0.5)

    print("Medication section complete")


# TODO
def vital_signs():
    # get shift time to determine number of VS to enter
    shift_time = element_locator(
        "#refreshArea > div > div > div > div:nth-child(2) > div.row > div:nth-child(3) > h5"
    ).text

    standard_click("#vitalSignsBar > span")
    standard_click("#VisitAssessment_VitalSignsSection_VitalSigns_true")

    time_list = ["08:00 AM", "12:00 PM", "04:00 PM", "08:00 PM"]

    # if long shift, enter 4 VS
    if "7" in shift_time:
        for t in time_list:
            vital(s)
    else:
        for t in time_list[2:]:
            vital(t)


# DONE!!!
def pain():
    # click Pain bar
    try:
        driver.find_element_by_css_selector("#painAssessmentBar > span").click()
    except Exception as er:
        print(f"unable to click pain assessment bar: {er}")
    sleep(1)
    try:
        # is client feeling pain radio button
        current_pain_radio = driver.find_element_by_css_selector(
            "#VisitAssessment_PainAssessmentSection_IsClientCurrentlyExperiencingPain_0"
        )
        cureent_pain_radio_id = driver.find_element_by_id(
            "VisitAssessment_PainAssessmentSection_IsClientCurrentlyExperiencingPain_0"
        )
    except Exception as e:
        print(f'Unable to click "client feeling pain" button: {e}')
    try:
        current_pain_radio.click()
    except:
        print("couldin click pain radio button using css locator, attempting by id...")
    try:
        cureent_pain_radio_id.click()
    except:
        print("could not click using id")

    sleep(1)
    print("Pain section complete")


# DONE!!!
def psych():
    # clicking psych bar
    sleep(1)
    standard_click("#psychologicalBar > span")
    sleep(2.5)

    # sleep apnea
    try:
        check_and_click_id("700")
    except:
        print("what the f?")
        check_and_click(driver.find_element_by_id("700"))

    # Other psych problem
    try:
        check_and_click_id("701")
    except:
        print("something fishy going on")
        check_and_click(driver.find_element_by_id("701"))

    # A&O other
    try:
        check_and_click_id("599")
    except:
        print("something fishy going on")
        check_and_click(driver.find_element_by_id("599"))

    # comment and intervention section
    psych_comment = (
        "client responds to pain. does not follow commands. no changes from baseline"
    )

    psych_comment_el = "VisitAssessment_PsychologicalSection_CommentsInterventions"
    clear_and_enter_keys(psych_comment_el, psych_comment, "id")

    print("psych complete")


# DONE!!!
def neuro():
    # click neuro bar
    standard_click("#neurologicalBar > span")

    sleep(1)

    # Non-verbal
    check_and_click_id("708")

    # seizures
    check_and_click_id("716")

    # Tremors
    check_and_click_id("717")

    # right hand grip strength
    try:
        r_hand_check = driver.find_element_by_css_selector(
            "#neurologicalSection > div:nth-child(3) > div > span:nth-child(4) > span > span.k-input"
        ).text
    except:
        print("error finding right hand grip strnegth dropdown")

    if r_hand_check != "Strong":
        try:
            r_hand = driver.find_element_by_css_selector(
                "#neurologicalSection > div:nth-child(3) > div > span:nth-child(4)"
            )
        except:
            print("unable to find r hand grip strenth input field")
        r_hand.click()
        sleep(1)
        r_hand.send_keys("s")
        sleep(1)
        r_hand.send_keys(Keys.ENTER)

    try:
        l_hand_check = driver.find_element_by_xpath(
            '//*[@id="neurologicalSection"]/div[3]/div/span[2]/span/span[1]'
        ).text
    except:
        try:
            l_hand_check = driver.find_element_by_css_selector(
                "#neurologicalSection > div:nth-child(3) > div > span:nth-child(8) > span > span.k-input"
            ).text
        except:
            print("couldnt grab l hand drop down text using css selector")
        print("error finding left hand grip strnegth dropdown")

    # left hand grip strength
    if l_hand_check != "Strong":
        try:
            l_hand = driver.find_element_by_css_selector(
                "#neurologicalSection > div:nth-child(3) > div > span:nth-child(8)"
            )
        except:
            print("unable to find left hand 'strong' in drop down")

        l_hand.click()
        sleep(1)
        l_hand.send_keys("s")
        sleep(1)
        l_hand.send_keys(Keys.ENTER)

    # send keys to neuro comment
    neuro_comment = "Patient displaying no signs of tremors/seizures. No signs of neurological changes."

    clear_and_enter_keys(
        "VisitAssessment_NeurologicalSection_CommentsInterventions", neuro_comment, "id"
    )

    print("Neuro complete")


# DONE!!!
def endocrine():
    standard_click("#endocrineBar > span")
    sleep(1)
    check_and_click_id("720")
    print("endocrine section complete")


# DONE!!!
def cardio():
    standard_click('//*[@id="cardiovascularBar"]/span', "x")
    sleep(1)
    # no idnentifed problem
    check_and_click_id("725")
    # heart sounds reguar
    check_and_click_id("205")
    # pink skin color
    check_and_click_id("207")
    # skin temp
    check_and_click_id("213")

    # cap refill < 3
    standard_click("VisitAssessment_CardiovascularSection_CapillaryRefill_Id_1", "id")

    # cap refill fingers
    cap_fingers_locator = (
        "VisitAssessment_CardiovascularSection_CapillaryRefillLocation"
    )

    clear_and_enter_keys(cap_fingers_locator, "fingers", "id")

    peri_pulse_upper_css = "#cardiovascularSection > div:nth-child(7) > div:nth-child(1) > div.k-widget.k-multiselect.k-multiselect-clearable > div > input"

    peri_pulse_lower_xpath = "#cardiovascularSection > div:nth-child(7) > div:nth-child(2) > div.k-widget.k-multiselect.k-multiselect-clearable > div > input"

    # upper pulses
    drop_down_handler(peri_pulse_upper_css, "S")

    # lower pulses
    drop_down_handler(peri_pulse_lower_xpath, "S")

    # no endurance limitations

    standard_click(
        "VisitAssessment_CardiovascularSection_EnduranceLimitations_true", "id"
    )

    endur_css = (
        "#cardiovascularSection > div:nth-child(9) > div > div > div > div > input"
    )

    drop_down_handler(endur_css, "with >")

    cardio_comment = "S1 S2 noted. No signs of cardiovascular changes."
    cardio_comment_id = "VisitAssessment_CardiovascularSection_CommentsInterventions"
    clear_and_enter_keys(cardio_comment_id, cardio_comment, "id")

    print("cardio section complete")


# DONE!!!
def respiratory():
    sleep(1)
    standard_click("#respiratoryBar > span")
    sleep(2)

    # no id'd problem
    check_and_click_id("752")
    # apnea
    check_and_click_id("524")
    # regular
    check_and_click_id("515")
    # unlabored
    check_and_click_id("516")
    # clear breath sounds
    check_and_click_id("227")

    # no ventilator
    vent_no_css = "VisitAssessment_RespiratorySection_VentilatorInUse_false"
    standard_click(vent_no_css, "id")
    # no trach
    trach_no_css = "VisitAssessment_TracheostomySection_HasTracheostomy_false"
    standard_click(trach_no_css, "id")

    resp_comment_id = "VisitAssessment_RespiratorySection_CommentsInterventions"

    resp_comm = "Patient respiratory system intact. Breathing treatments tolerated, no signs of respiratory infection. CPAP present at bedside, settings per order. SPO2 values within normal values throughout shift."

    # entering comment into rrespiratory intevention comment
    clear_and_enter_keys(resp_comment_id, resp_comm, "id")

    print("Respiratory system complete")


# DONE!!!
def gastro():

    sleep(1)
    standard_click("#gastrointestinalNutritionalBar > span")
    sleep(2)
    # enteral feeding
    check_and_click_id("739")

    # fecal incontinence
    check_and_click_id("751")

    # appetite good
    check_and_click_id("250")

    # feeding type bolus
    check_and_click_id("271")

    # feeding type pump
    check_and_click_id("271")

    # TUBE type mickey
    check_and_click_id("269")

    # type of formula
    clear_and_enter_keys(
        "VisitAssessment_GastrointestinalNutritionalSection_EnteralFeeding_FormulaType",
        "ketocal nutrition formula",
        "id",
    )

    clear_and_enter_keys(
        "VisitAssessment_GastrointestinalNutritionalSection_EnteralFeeding_Rate",
        "285",
        "id",
    )

    # site assessment dry & intact
    check_and_click_id("273")

    # BOWEL SOUNDS present
    check_and_click_id("282")
    sleep(2)

    stools_day_css = "#gastrointestinalNutritionalSection > div:nth-child(7) > div > span > span > input.k-formatted-value.k-input"
    # entering stools per day field
    clear_and_enter_keys(stools_day_css, "1")

    last_bowel_date = (
        "VisitAssessment_GastrointestinalNutritionalSection_LastBowelMovement"
    )
    # entering assment date to last BM
    current_assmnt_date = get_date()

    clear_and_enter_keys(last_bowel_date, current_assmnt_date, "id")

    gastro_comment = "Patient tolerating feeds. GI tube site dry and intact, cleaned site with mild soap and water. Flushed Mickey tube with free water following med administration."

    gasto_comm_id = (
        "VisitAssessment_GastrointestinalNutritionalSection_CommentsInterventions"
    )
    clear_and_enter_keys(gasto_comm_id, gastro_comment, "id")

    print("gastro section completed")


# DONE!!!
def urinary():
    sleep(1)
    standard_click("#genitourinaryBar > span")
    sleep(1)
    check_and_click_id("760")
    genito_comm = "Voiding appropriately. No changes to urinary system noted."
    genito_comm_id = "VisitAssessment_GenitourinarySection_CommentsInterventions"
    clear_and_enter_keys(genito_comm_id, genito_comm, "id")

    print("Urinary section complete")


# DONE!!!
def musculo():
    standard_click("#musculoskeletalBar > span")
    sleep(1)
    # limited ROM
    check_and_click_id("808")

    lim_rom_comm = "client is non ambulatory, fine motor deficit present"

    clear_and_enter_keys(
        "VisitAssessment_MusculoskeletalSection_LimitedRomMobilityText",
        lim_rom_comm,
        "id",
    )

    musc_comm = "Standing therapy tolerated. Passive Range of motion exercises performed. no signs of changes. passive ROM tolerated. Mild cantractures to Bilateral ankles, no changes from baseline. No signs of worsening musculoskeletal system."

    clear_and_enter_keys(
        "#VisitAssessment_MusculoskeletalSection_CommentsInterventions", musc_comm
    )

    print("musculo section complete")


# DONE!!!
def sensory():
    standard_click("#sensoryBar > span")
    sleep(1)
    standard_click("#VisitAssessment_SensorySection_ReviewedInformationChanges_true")

    sensory_comm = "No sensory changes noted on shift"

    clear_and_enter_keys(
        "#VisitAssessment_SensorySection_CommentsInterventions", sensory_comm
    )

    print("Sensory section complete")


# DONE!!!
def integ():
    standard_click("#integumentaryBar > span")
    sleep(1)
    # no stated problem
    check_and_click_id("772")
    standard_click("#VisitAssessment_IntegumentarySection_Wound_false")

    print("Integumentaary Done")


# DONE!!!
def ped():
    standard_click("#pediatricsBar > span")
    sleep(1)
    check_and_click_id("881")

    drop_down_handler(
        "#pediatricsSection > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > span",
        "c",
    )
    drop_down_handler(
        "#pediatricsSection > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > span",
        "2",
    )
    drop_down_handler(
        "#pediatricsSection > div:nth-child(3) > div:nth-child(5) > div:nth-child(1) > span",
        "2",
    )
    drop_down_handler(
        "#pediatricsSection > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > span",
        "4",
    )

    check_and_click_id("886")
    check_and_click_id("889")
    check_and_click_id("891")
    check_and_click_id("893")
    check_and_click_id("899")
    check_and_click_id("902")
    check_and_click_id("908")

    print("pediatric section complete")


# DONE!!!
def iv():
    standard_click("#intravenousBar > span")
    sleep(1)
    standard_click("#VisitAssessment_IntravenousSection_CurrentIvSiteWnl_false")
    print("IV status done")


# DONE!!!
def education():
    standard_click("#educationTeachingBar > span")
    sleep(1)
    education_comm = "infection control/seizure precautions"
    clear_and_enter_keys(
        "#VisitAssessment_EducationTeachingSection_LearningNeeds", education_comm
    )

    print("education section done")


# DONE!!!
def poc():
    standard_click("#planOfCareReviewCareCoordinationBar > span")
    sleep(1)
    check_and_click_id("795")
    print("poc done")


# DONE!!!
def state():
    standard_click("#stateRequirementsSectionBar > span")
    sleep(1)
    standard_click(
        "#VisitAssessment_StateRequirementsSection_StateSpecificRequirements_false"
    )

    print("state reqs done")
