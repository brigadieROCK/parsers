import os
import json
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import csv
from config import url_homepage
from translatepy import Translator
from mytoolsparser import getter, printer
import traceback
doprl = ['https://www.imi-precision.com/sg/en/list/imi-norgren-guardian-range/air-preparation', 'https://www.imi-precision.com/sg/en/list/imi-norgren-guardian-range/valves', 'https://www.imi-precision.com/sg/en/list/imi-norgren-guardian-range/cylinders', 'https://www.norgren.com/sg/en/list/proportional-valves', 'https://www.norgren.com/sg/en/list/safety-valves', 'https://www.norgren.com/sg/en/list/safety-valves?page=list&amp;refine=range-over-xshc04']
name_dir_1 = 'proportional-valves'
def dop_parse():
    url_actuators = doprl[3]

    #site_actuators = requests.get(url)
    # soup_actuators = BeautifulSoup(site_actuators.text, 'html.parser')
    # mass_actuators= soup_actuators.find_all("a", class_="subtitle")
    site_actuators = requests.get(url_actuators)
    soup_actuators = BeautifulSoup(site_actuators.text, 'html.parser')
    mass_actuators = soup_actuators.find_all("a", class_="btn btn-sm more-info")

    for i in range(0, len(mass_actuators)):
        mass_actuators[i] = str(mass_actuators[i])[str(mass_actuators[i]).find('href="') + 6:str(mass_actuators[i]).find('"', str(mass_actuators[i]).find('href="')+7)]
        if (mass_actuators[i][0:3] == '/sg'):
            mass_actuators[i] = 'https://www.norgren.com' + mass_actuators[i]
        mass_actuators[i] = str(mass_actuators[i]).replace('amp;','')


    print(mass_actuators)

    # site_actuators_podkat = requests.get(mass_actuators[0])
    # soup_actuators_podkat = BeautifulSoup(site_actuators_podkat.text, 'html.parser')
    # mass_actuators_podkat = soup_actuators_podkat.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
    # print(mass_actuators_podkat)
    # for i in range(0, len(mass_actuators_podkat)):
    #     mass_actuators_podkat[i] = str(mass_actuators_podkat[i])[str(mass_actuators_podkat[i]).find('href="') + 6:str(mass_actuators_podkat[i]).find('"',str(mass_actuators_podkat[i]).find('href="') + 8)]
    #     if (mass_actuators_podkat[i][0:3] == '/sg'):
    #         mass_actuators_podkat[i] = 'https://www.norgren.com' + mass_actuators_podkat[i]
    #     # print(str(mass_actuators[i]).find('am'))
    #     # mass_actuators_podkat[i] = mass_actuators_podkat[i].replace('amp;', '')
    # mass_actuators_podkat += mass_actuators[1:-1]
    # print(mass_actuators_podkat)
    # name_dir_1 = 'actuators'
    mass_actuators_podkat = mass_actuators
    for i_product in range(0, len(mass_actuators_podkat)):
        try:
            musor = mass_actuators_podkat[i_product].split("/")[-1].split('-')
            name_dir_2 = ''
            for j in musor:
                if (j != musor[-1]):
                    name_dir_2 += j + '-'
                else:
                    name_dir_2 += j
            if (name_dir_2.find("?") != -1):
                name_dir_2 = name_dir_2.replace("?page=list&", "-")

            site_product_page = requests.get(mass_actuators_podkat[i_product])
            soup_product_page = BeautifulSoup(site_product_page.text, 'html.parser')
            gran = soup_product_page.find("div", class_='paging-information').text
            gran = int(gran[gran.find('of') + 2:])
            if gran % 10 != 0:
                gran = gran / 10 + 1
            else:
                gran = gran / 10
            product_page_mass = []
            # product_page_mass = soup_product_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")

            # flag = True
            pagenum = 1
            while (pagenum <= gran):
                dop_site_product_page = requests.get(
                    mass_actuators_podkat[i_product] + f'&pagenum={str(pagenum)}&resultsPerPage=10')
                # if(dop_site_product_page.ok):
                dop_soup_product_page = BeautifulSoup(dop_site_product_page.text, 'html.parser')
                dop_product_page_mass = dop_soup_product_page.find_all("a",
                                                                       class_="btn btn-sm btn-block more-info btn-grey")
                new_dop_product_page_mass = []

                for znak in dop_product_page_mass:
                    if 'More Information' == znak.text:
                        # print(znak)
                        new_dop_product_page_mass.append(znak)
                # print(pagenum, ' ', new_dop_product_page_mass)
                product_page_mass += new_dop_product_page_mass
                pagenum += 1
                # else:
                #     flag = False
            # print('Ебать вышли, ахуеть, фух!' + '\n', product_page_mass)
            for i_prod in range(0, len(product_page_mass)):
                product_page_mass[i_prod] = str(product_page_mass[i_prod])[
                                            str(product_page_mass[i_prod]).find('href="') + 6:str(
                                                product_page_mass[i_prod]).find('"', str(
                                                product_page_mass[i_prod]).find('href="') + 6)]
                if (product_page_mass[i_prod][0:3] == '/sg'):
                    product_page_mass[i_prod] = 'https://www.norgren.com' + product_page_mass[i_prod]
            # if (product_page_mass[-1] == 'ass='):
            # #     del product_page_mass[-1]
            # print('Ебать мы обработали!' + '\n', product_page_mass)
            # print(len(product_page_mass))
            name_dir_1_dop = ''
            name_dir_2_dop = ''
            for charing in name_dir_1:
                charor = ord(charing)
                if (65 <= charor <= 90) or (97 <= charor <= 122) or (charing == '-'):
                    name_dir_1_dop += charing
            for charing in name_dir_2:
                charor = ord(charing)
                if (65 <= charor <= 90) or (97 <= charor <= 122) or (charing == '-'):
                    name_dir_2_dop += charing

            if (i_product == 2):
                name_dir_2_dop += '10'
            os.makedirs(f"norgren\{name_dir_1_dop}\{name_dir_2_dop}")
            os.makedirs(f"norgren\{name_dir_1_dop}\{name_dir_2_dop}\photo")
            os.makedirs(f"norgren\{name_dir_1_dop}\{name_dir_2_dop}\photo\cropped")
            os.makedirs(f"norgren\{name_dir_1_dop}\{name_dir_2_dop}\documentation")
            getter(product_page_mass, name_dir_2_dop, f"norgren\{name_dir_1_dop}\{name_dir_2_dop}")
        except:
            print(traceback.print_exc())

dop_parse()
# for ulling in range(0, len(mass_actuators)-1):
#     if ulling == 0:
    #     for i in range(0, len(mass_actuators_podkat)-1):
    #         mass_actuators_podkat[i] = str(mass_actuators_podkat[i])[str(mass_actuators_podkat[i]).find('href="') + 6:str(mass_actuators_podkat[i]).find('"',str(mass_actuators_podkat[i]).find('href="') + 8)]
    #         if (mass_actuators_podkat[i][0:3] == '/sg'):
    #             mass_actuators_podkat[i] = 'https://www.norgren.com' + mass_actuators_podkat[i]
    #     mass_actuators_podkat_tovars = soup_actuators_podkat.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
    #     for i in range(0, len(mass_actuators_podkat_tovars)-1):
    #         mass_actuators_podkat_tovars[i] = str(mass_actuators_podkat_tovars[i])[str(mass_actuators_podkat_tovars[i]).find('href="') + 6:str(mass_actuators_podkat_tovars[i]).find('"',str(mass_actuators_podkat_tovars[i]).find('href="') + 8)]
    #         if (mass_actuators_podkat_tovars[i][0:3] == '/sg'):
    #             mass_actuators_podkat_tovars[i] = 'https://www.norgren.com' + mass_actuators_podkat_tovars[i]
    #     print(mass_actuators_podkat)
    #     print(mass_actuators_podkat_tovars)
    # else:
    #     site_actuators_podkat = requests.get(mass_actuators[ulling])
    #     soup_actuators_podkat = BeautifulSoup(site_actuators_podkat.text, 'html.parser')
    #     mass_actuators_podkat = soup_actuators_podkat.find_all("a", class_="btn btn-sm more-info")
    #     mass_actuators_podkat_tovars = soup_actuators_podkat.find_all("a",class_="btn btn-sm btn-block more-info btn-grey")
    #     for i in range(0, len(mass_actuators_podkat_tovars)-1):
    #         mass_actuators_podkat_tovars[i] = str(mass_actuators_podkat_tovars[i])[str(mass_actuators_podkat_tovars[i]).find('href="') + 6:str(mass_actuators_podkat_tovars[i]).find('"',str(mass_actuators_podkat_tovars[i]).find('href="') + 8)]
    #         if (mass_actuators_podkat_tovars[i][0:3] == '/sg'):
    #             mass_actuators_podkat_tovars[i] = 'https://www.norgren.com' + mass_actuators_podkat_tovars[i]
    #     print(mass_actuators_podkat)
    #     print(mass_actuators_podkat_tovars)