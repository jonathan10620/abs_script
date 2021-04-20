sat_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(7) > a"
    for n in range(2, 11)
]

temp = [
    "#gridCustomerTreatment > table > tbody > tr:nth-child(1) > td:nth-child(4) > ul > li:nth-child(8) > a"
]
temp_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(7) > a"
    for n in range(2, 7)
    if n != 3
]

sat_list_2 = temp + temp_1

sat_list_extra = [
    "#gridOtherTreatment > table > tbody > tr:nth-child(1) > td:nth-child(5) > ul > li:nth-child(7) > a",
    "#gridOtherTreatment > table > tbody > tr.k-alt > td:nth-child(5) > ul > li:nth-child(7) > a",
]


sun_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(1) > a"
    for n in range(1, 11)
]

sun_list_2 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(1) > a"
    for n in range(1, 7)
    if n != 3
]

sun_list_extra = [
    "#gridOtherTreatment > table > tbody > tr:nth-child(1) > td:nth-child(5) > ul > li:nth-child(1) > a",
    "#gridOtherTreatment > table > tbody > tr.k-alt > td:nth-child(5) > ul > li:nth-child(1) > a",
]


# monday tars functioning
mon_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(2) > a"
    for n in range(2, 11)
]

mon_list_2 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(2) > a"
    for n in range(1, 7)
    if n != 3
]

mon_list_extra = [
    "#gridOtherTreatment > table > tbody > tr:nth-child(1) > td:nth-child(5) > ul > li:nth-child(2) > a",
    "#gridOtherTreatment > table > tbody > tr.k-alt > td:nth-child(5) > ul > li:nth-child(2) > a",
]

tues_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(3) > a"
    for n in range(2, 11)
]

wens_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(4) > a"
    for n in range(2, 11)
]

thurs_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(5) > a"
    for n in range(2, 11)
]

fri_list_1 = [
    f"#gridCustomerTreatment > table > tbody > tr:nth-child({n}) > td:nth-child(4) > ul > li:nth-child(6) > a"
    for n in range(2, 11)
]
