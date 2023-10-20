import os
import json
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import csv
from config import url_homepage
from translatepy import Translator
from mytoolsparser import getter, printer
translator = Translator()


def parse():

    site_homepage = requests.get(url_homepage)
    soup_homepage = BeautifulSoup(site_homepage.text, 'html.parser')
    mass_homepage = soup_homepage.find_all("a", class_="subtitle")

    for i_home in range(0, len(mass_homepage)):
        mass_homepage[i_home] = str(mass_homepage[i_home])[
                                str(mass_homepage[i_home]).find('href="') + 6:str(mass_homepage[i_home]).find('">')]
        if (mass_homepage[i_home][0:3] == '/sg'):
            mass_homepage[i_home] = 'https://www.norgren.com' + mass_homepage[i_home]
    print(mass_homepage)
    mass_homepage = mass_homepage[5:]
    # mass_homepage = ['https://www.norgren.com/sg/en/list/proportional-valves', 'https://www.imi-precision.com/sg/en/list/imi-norgren-guardian-range', 'https://www.norgren.com/sg/en/list/safety-valves']

    for i_cat in range(0, len(mass_homepage)):
        site_page = requests.get(mass_homepage[i_cat])
        soup_page = BeautifulSoup(site_page.text, 'html.parser')
        mass_page = soup_page.find_all("a", class_="btn btn-sm more-info")
        # mass_page = soup_page.find_all("a", class_="btn")
        print(mass_page)


    for i in range(0, len(mass_page)):
        mass_page[i] = str(mass_page[i])[str(mass_page[i]).find('href="') + 6:str(mass_page[i]).find('">')]
        if (mass_page[i][0:3] == '/sg'):
            mass_page[i] = 'https://www.norgren.com' + mass_page[i]

    for i_page in mass_page:
        musor = i_page.split("/")[-1].split('-')
        name_dir_1 = ''
        for j in musor:
            if (j != musor[-1]):
                name_dir_1 += j + '-'
            else:
                name_dir_1 += j

        site_podcategory_page = requests.get(i_page)
        site_podcategory_page = BeautifulSoup(site_podcategory_page.text, 'html.parser')
        mass_podkategory_page = site_podcategory_page.find_all("a", class_="btn btn-sm more-info")
        for i_pod_cat in range(0, len(mass_podkategory_page)):
            mass_podkategory_page[i_pod_cat] = str(mass_podkategory_page[i_pod_cat])[str(mass_podkategory_page[i_pod_cat]).find('href="') + 6:str(mass_podkategory_page[i_pod_cat]).find('"',str(mass_podkategory_page[i_pod_cat]).find('href="') + 6)]
            if (mass_podkategory_page[i_pod_cat][0:3] == '/sg'):
                mass_podkategory_page[i_pod_cat] = 'https://www.norgren.com' + mass_podkategory_page[i_pod_cat]

        print(mass_podkategory_page)
        for i_product in range(0, len(mass_podkategory_page)):
            musor = mass_podkategory_page[i_product].split("/")[-1].split('-')
            name_dir_2 = ''
            for j in musor:
                if (j != musor[-1]):
                    name_dir_2 += j + '-'
                else:
                    name_dir_2 += j
            if (name_dir_2.find("?") != -1):
                name_dir_2 = name_dir_2.replace("?page=list&amp;", "-")

            site_product_page = requests.get(mass_podkategory_page[i_product])
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
                    mass_podkategory_page[i_product] + f'?pagenum={str(pagenum)}&resultsPerPage=10')
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
            os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}")
            os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\photo")
            os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\photo\cropped")
            os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\documentation")
            getter(product_page_mass, name_dir_2, f"norgren\{name_dir_1}\{name_dir_2}")


parse()

    # for i_product in range(0, len(mass_podkategory_page)):
    #     musor = mass_podkategory_page[i_product].split("/")[-1].split('-')
    #     name_dir_2 = ''
    #     for j in musor:
    #         if (j != musor[-1]):
    #             name_dir_2 += j + '-'
    #         else:
    #             name_dir_2 += j
    #     if(name_dir_2.find("?")!= -1):
    #         name_dir_2 = name_dir_2.replace("?page=list&amp;", "-")
    #     #os.makedirs(f"norgen\{translator.translate(name_dir_1, 'Russian')}\{translator.translate(name_dir_2, 'Russian')}")
    #     os.makedirs(f"norgen\{name_dir_1}\{name_dir_2}")
        #print(name_dir_1 + '\\'+ name_dir_2)
                    # site_product_page = requests.get(mass_podkategory_page[i_product])
                    # soup_product_page = BeautifulSoup(site_product_page.text, 'html.parser')
                    # product_page_mass = soup_product_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
                    # print(product_page_mass)
