fri_1_am = [f'//*[@id="gridCustomerTreatment"]/table/tbody/tr[{n}]/td[4]/ul/li[6]/a' for n in range(2,11)]
fri_2_am = [
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[1]/td[4]/ul/li[7]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[2]/td[4]/ul/li[6]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[4]/td[4]/ul/li[6]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[5]/td[4]/ul/li[6]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[6]/td[4]/ul/li[6]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[7]/td[4]/ul/li[11]/a'
]

fri_extra_am = [
    '//*[@id="gridOtherTreatment"]/table/tbody/tr[1]/td[5]/ul/li[6]/a',
    '//*[@id="gridOtherTreatment"]/table/tbody/tr[2]/td[5]/ul/li[6]/a']


sat_1_all = [f'//*[@id="gridCustomerTreatment"]/table/tbody/tr[{n}]/td[4]/ul/li[7]/a' for n in range(2,11)]


sat_2_all = [
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[1]/td[4]/ul/li[8]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[2]/td[4]/ul/li[7]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[4]/td[4]/ul/li[7]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[5]/td[4]/ul/li[7]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[6]/td[4]/ul/li[7]/a',
    '//*[@id="gridCustomerTreatment"]/table/tbody/tr[7]/td[4]/ul/li[13]/a'
]
sat_extra_all = [
    '//*[@id="gridOtherTreatment"]/table/tbody/tr[1]/td[5]/ul/li[7]/a',
    '//*[@id="gridOtherTreatment"]/table/tbody/tr[2]/td[5]/ul/li[7]/a'
    ]

sun_1_all = [f'//*[@id="gridCustomerTreatment"]/table/tbody/tr[{n}]/td[4]/ul/li[1]/a' for n in range(1,11)]

sun_2_all = [f'//*[@id="gridCustomerTreatment"]/table/tbody/tr[{n}]/td[4]/ul/li[1]/a' for n in range(1,7) if n != 3]


sun_extra_all = [
    '//*[@id="gridOtherTreatment"]/table/tbody/tr[1]/td[5]/ul/li[1]/a',
    '//*[@id="gridOtherTreatment"]/table/tbody/tr[2]/td[5]/ul/li[1]/a'
    ]

mon_1_eve = []
mon_2_eve = []
mon_extra_eve = []