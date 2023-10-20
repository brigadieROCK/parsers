import os
import json
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import csv

import mytoolsparser
from config import url_homepage
from translatepy import Translator
from mytoolsparser import getter, printer
#translator = Translator()

mytoolsparser.getter(['https://www.norgren.com/sg/en/detail/xshc04'], 'safety-valves', r"norgren\safety-valves\range-over-xshc04")


# site_homepage = requests.get(url_homepage)
# soup_homepage = BeautifulSoup(site_homepage.text, 'html.parser')
# mass_homepage = soup_homepage.find_all("a", class_="subtitle")
#
# for i_home in range(0, len(mass_homepage)):
#     mass_homepage[i_home] = str(mass_homepage[i_home])[
#                             str(mass_homepage[i_home]).find('href="') + 6:str(mass_homepage[i_home]).find('">')]
#     if (mass_homepage[i_home][0:3] == '/sg'):
#         mass_homepage[i_home] = 'https://www.norgren.com' + mass_homepage[i_home]
# print(mass_homepage)
# mass_homepage = mass_homepage[6:]
# # mass_homepage = ['https://www.norgren.com/sg/en/list/proportional-valves', 'https://www.imi-precision.com/sg/en/list/imi-norgren-guardian-range', 'https://www.norgren.com/sg/en/list/safety-valves']
# mass_page = []
# for i_cat in range(0, len(mass_homepage)):
#     site_page = requests.get(mass_homepage[i_cat])
#     soup_page = BeautifulSoup(site_page.text, 'html.parser')
#     mass_pag = soup_page.find_all("a", class_="btn btn-sm more-info")
#     # mass_page = soup_page.find_all("a", class_="btn")
#     mass_page += mass_pag
#     print(mass_page)
#
#     for i in range(0, len(mass_page)):
#         if(str(mass_page[i])[0:4] != 'http'):
#             mass_page[i] = str(mass_page[i])[str(mass_page[i]).find('href="') + 6:str(mass_page[i]).find('"',str(mass_page[i]).find('href="') + 7)]
#             if (mass_page[i][0:3] == '/sg'):
#                 mass_page[i] = 'https://www.norgren.com' + mass_page[i]
# print(mass_page)
#
# # mass_page[3] = mass_page[3].replace('amp;', '')
# # mass_page[4] = mass_page[4].replace('amp;', '')
# for ptr in range(0, len(mass_page)):
#     mass_page[ptr] = mass_page[ptr].replace('amp;', '')
#
# # for i_page in range(0, len(mass_page)):
# #     musor = mass_page[i_page].split("/")[-1].split('-')
# #     name_dir_1 = ''
# #     for j in musor:
# #         if (j != musor[-1]):
# #             name_dir_1 += j + '-'
# #         else:
# #             name_dir_1 += j
#
#     # site_podcategory_page = requests.get(mass_page[i_page])
#     # site_podcategory_page = BeautifulSoup(site_podcategory_page.text, 'html.parser')
#     # # if(i_page == 3):
#     # #     mass_podkategory_page = site_podcategory_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
#     # # elif(i_page == 4):
#     # #     mass_podkategory_page = site_podcategory_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
#     # # else:
#     # mass_podkategory_page = site_podcategory_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
#     # for i_pod_cat in range(0, len(mass_podkategory_page)):
#     #     mass_podkategory_page[i_pod_cat] = str(mass_podkategory_page[i_pod_cat])[
#     #                                        str(mass_podkategory_page[i_pod_cat]).find('href="') + 6:str(
#     #                                            mass_podkategory_page[i_pod_cat]).find('"', str(
#     #                                            mass_podkategory_page[i_pod_cat]).find('href="') + 6)]
#     #     if (mass_podkategory_page[i_pod_cat][0:3] == '/sg'):
#     #         mass_podkategory_page[i_pod_cat] = 'https://www.norgren.com' + mass_podkategory_page[i_pod_cat]
#     #     if (mass_podkategory_page[i_pod_cat][0] == ':'):
#     #         mass_podkategory_page[i_pod_cat] = 'https' + mass_podkategory_page[i_pod_cat]
#     #
#     # print(mass_podkategory_page)
# mass_podkategory_page = mass_page
# for i_product in range(0, len(mass_podkategory_page)):
#     musor = mass_podkategory_page[i_product].split("/")[-1].split('-')
#     name_dir_1 = ''
#     for j in musor:
#         if (j != musor[-1]):
#             name_dir_1 += j + '-'
#         else:
#             name_dir_1 += j
#     musor = mass_podkategory_page[i_product].split("/")[-1].split('-')
#     name_dir_2 = ''
#     for j in musor:
#         if (j != musor[-1]):
#             name_dir_2 += j + '-'
#         else:
#             name_dir_2 += j
#     if (name_dir_2.find("?") != -1):
#         name_dir_2 = name_dir_2.replace("?page=list&amp;", "-")
#
#     site_product_page = requests.get(mass_podkategory_page[i_product])
#     soup_product_page = BeautifulSoup(site_product_page.text, 'html.parser')
#     gran = soup_product_page.find("div", class_='paging-information').text
#     gran = int(gran[gran.find('of') + 2:])
#     if gran % 10 != 0:
#         gran = gran / 10 + 1
#     else:
#         gran = gran / 10
#     product_page_mass = []
#     # product_page_mass = soup_product_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
#
#     # flag = True
#     pagenum = 1
#     while (pagenum <= gran):
#         dop_site_product_page = requests.get(
#             mass_podkategory_page[i_product] + f'?pagenum={str(pagenum)}&resultsPerPage=10')
#         # if(dop_site_product_page.ok):
#         dop_soup_product_page = BeautifulSoup(dop_site_product_page.text, 'html.parser')
#         dop_product_page_mass = dop_soup_product_page.find_all("a",
#                                                                class_="btn btn-sm btn-block more-info btn-grey")
#         new_dop_product_page_mass = []
#
#         for znak in dop_product_page_mass:
#             if 'More Information' == znak.text:
#                 # print(znak)
#                 new_dop_product_page_mass.append(znak)
#         # print(pagenum, ' ', new_dop_product_page_mass)
#         product_page_mass += new_dop_product_page_mass
#         pagenum += 1
#         # else:
#         #     flag = False
#     # print('Ебать вышли, ахуеть, фух!' + '\n', product_page_mass)
#     for i_prod in range(0, len(product_page_mass)):
#         product_page_mass[i_prod] = str(product_page_mass[i_prod])[
#                                     str(product_page_mass[i_prod]).find('href="') + 6:str(
#                                         product_page_mass[i_prod]).find('"', str(
#                                         product_page_mass[i_prod]).find('href="') + 6)]
#         if (product_page_mass[i_prod][0:3] == '/sg'):
#             product_page_mass[i_prod] = 'https://www.norgren.com' + product_page_mass[i_prod]
#     # if (product_page_mass[-1] == 'ass='):
#     # #     del product_page_mass[-1]
#     # print('Ебать мы обработали!' + '\n', product_page_mass)
#     # print(len(product_page_mass))
#     os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}")
#     os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\photo")
#     os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\photo\cropped")
#     os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\documentation")
#     getter(product_page_mass, name_dir_2, f"norgren\{name_dir_1}\{name_dir_2}")


# parse()
# dop_parse()
# ur = 'https://www.norgren.com/sg/en/detail/f84g_3gn_ad3'
# soup = requests.get(ur)
# souper = BeautifulSoup(soup.text, "html.parser")
# rez = souper.find('ul', class_ = 'features')
# fact_uniq = souper.find('ul', class_ = 'features')
# s_uniq = ''
# if (fact_uniq != None):
#     mass_uniq = fact_uniq.find_all('li')
#     for uni in range(0, len(mass_uniq)):
#         if (uni == 0):
#             s_uniq += mass_uniq[uni].text
#         else:
#             s_uniq += ',' + mass_uniq[uni].text
# print(s_uniq)
# site_homepage = requests.get(url_homepage)
# soup_homepage = BeautifulSoup(site_homepage.text, 'html.parser')
# mass_homepage = soup_homepage.find_all("a", class_="subtitle")
#
# for i_home in range(0, len(mass_homepage)):
#     mass_homepage[i_home] = str(mass_homepage[i_home])[
#                             str(mass_homepage[i_home]).find('href="') + 6:str(mass_homepage[i_home]).find('">')]
#     if (mass_homepage[i_home][0:3] == '/sg'):
#         mass_homepage[i_home] = 'https://www.norgren.com' + mass_homepage[i_home]
# print(mass_homepage)
# for i_cat in range(0, len(mass_homepage)-1):
#     site_page = requests.get(mass_homepage[i_cat])
#     soup_page = BeautifulSoup(site_homepage.text, 'html.parser')
#     mass_page = soup_page.find_all("a", class_="btn btn-sm more-info")
#     # mass_page = soup_page.find_all("a", class_="btn")
#
# for i in range(0, len(mass_page)):
#     mass_page[i] = str(mass_page[i])[str(mass_page[i]).find('href="') + 6:str(mass_page[i]).find('">')]
#     if (mass_page[i][0:3] == '/sg'):
#         mass_page[i] = 'https://www.norgren.com' + mass_page[i]
#
# for i_page in mass_page:
#     musor = i_page.split("/")[-1].split('-')
#     name_dir_1 = ''
#     for j in musor:
#         if (j != musor[-1]):
#             name_dir_1 += j + '-'
#         else:
#             name_dir_1 += j
#
#     site_podcategory_page = requests.get(i_page)
#     site_podcategory_page = BeautifulSoup(site_podcategory_page.text, 'html.parser')
#     mass_podkategory_page = site_podcategory_page.find_all("a", class_="btn btn-sm more-info")
#     for i_pod_cat in range(0, len(mass_podkategory_page)):
#         mass_podkategory_page[i_pod_cat] = str(mass_podkategory_page[i_pod_cat])[str(mass_podkategory_page[i_pod_cat]).find('href="') + 6:str(mass_podkategory_page[i_pod_cat]).find('"',str(mass_podkategory_page[i_pod_cat]).find('href="') + 6)]
#         if (mass_podkategory_page[i_pod_cat][0:3] == '/sg'):
#             mass_podkategory_page[i_pod_cat] = 'https://www.norgren.com' + mass_podkategory_page[i_pod_cat]
#
#     print(mass_podkategory_page)
#     for i_product in range(0, len(mass_podkategory_page)):
#         musor = mass_podkategory_page[i_product].split("/")[-1].split('-')
#         name_dir_2 = ''
#         for j in musor:
#             if (j != musor[-1]):
#                 name_dir_2 += j + '-'
#             else:
#                 name_dir_2 += j
#         if (name_dir_2.find("?") != -1):
#             name_dir_2 = name_dir_2.replace("?page=list&amp;", "-")
#
#         site_product_page = requests.get(mass_podkategory_page[i_product])
#         soup_product_page = BeautifulSoup(site_product_page.text, 'html.parser')
#         gran = soup_product_page.find("div", class_='paging-information').text
#         gran = int(gran[gran.find('of') + 2:])
#         if gran % 10 != 0:
#             gran = gran / 10 + 1
#         else:
#             gran = gran / 10
#         product_page_mass = []
#         # product_page_mass = soup_product_page.find_all("a", class_="btn btn-sm btn-block more-info btn-grey")
#
#         # flag = True
#         pagenum = 1
#         while (pagenum <= gran):
#             dop_site_product_page = requests.get(
#                 mass_podkategory_page[i_product] + f'?pagenum={str(pagenum)}&resultsPerPage=10')
#             # if(dop_site_product_page.ok):
#             dop_soup_product_page = BeautifulSoup(dop_site_product_page.text, 'html.parser')
#             dop_product_page_mass = dop_soup_product_page.find_all("a",
#                                                                    class_="btn btn-sm btn-block more-info btn-grey")
#             new_dop_product_page_mass = []
#
#             for znak in dop_product_page_mass:
#                 if 'More Information' == znak.text:
#                     # print(znak)
#                     new_dop_product_page_mass.append(znak)
#             # print(pagenum, ' ', new_dop_product_page_mass)
#             product_page_mass += new_dop_product_page_mass
#             pagenum += 1
#             # else:
#             #     flag = False
#         # print('Ебать вышли, ахуеть, фух!' + '\n', product_page_mass)
#         for i_prod in range(0, len(product_page_mass)):
#             product_page_mass[i_prod] = str(product_page_mass[i_prod])[
#                                         str(product_page_mass[i_prod]).find('href="') + 6:str(
#                                             product_page_mass[i_prod]).find('"', str(
#                                             product_page_mass[i_prod]).find('href="') + 6)]
#             if (product_page_mass[i_prod][0:3] == '/sg'):
#                 product_page_mass[i_prod] = 'https://www.norgren.com' + product_page_mass[i_prod]
#         # if (product_page_mass[-1] == 'ass='):
#         # #     del product_page_mass[-1]
#         # print('Ебать мы обработали!' + '\n', product_page_mass)
#         # print(len(product_page_mass))
#         os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}")
#         os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\photo")
#         os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\photo\cropped")
#         os.makedirs(f"norgren\{name_dir_1}\{name_dir_2}\documentation")
#         getter(product_page_mass, name_dir_2, f"norgren\{name_dir_1}\{name_dir_2}")












#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------













#a = [1,2,3,4]
# ur = 'https://www.norgren.com/sg/en/detail/b73g_3gk_sp3_rmn'
# a = requests.get(ur)
# soup_product_page = BeautifulSoup(a.text, 'html.parser')
# gran = soup_product_page.find('h1')
# print(gran)
# if 'clearfix' in a.text:
#     print('збс')
# else:
#     print('нема')

# def getter(ulling):#, name_cat, dirs):
#     massiv_info = {}
#     massiv_index_info = {'inner_id':0, 'Имя товара':1, 'Артикул':2,'Производитель':3,'Цена':4,'Статус':5}
#
#     massiv_photo = {}
#     massiv_index_photo = {'inner_id':0, 'Имя товара':1, 'Изображение':2,'Дополнительные изображения':3}
#
#     massiv_tovarov = {}
#     mass_index_attr = {'inner_id':0,'url':1, 'Имя товара':2, 'Производитель':3, 'Артикул':4, 'Наименование':5}
#     index_attr = 6
#
#     massiv_cat_ser = {}
#     massiv_index_cat_ser = {'inner_id':0, 'Имя товара':1, 'Категория':2,'Серия':3}
#
#     mass_index_meta = {'inner_id':0, 'Имя товара':1, 'Meta Keyword':2,'Описание':3}
#
#     massiv_docs = {}
#     massiv_index_docs = {'inner_id':0, 'Имя товара':1, 'Имена файлов':2,'Файлы':3}
#
#     #for ulling in mas_url:
#     zapr = requests.get(ulling)
#     souper = BeautifulSoup(zapr.text, "html.parser")
#     sku = souper.find("span", class_="sku").text
#     #name_tovar = name_cat + ' Norgren ' + sku
#     #print(sku.text)
#     #Ебашим атрибуты------------------------------------
#     table_raw = souper.find("div", id="tech-details").find("table", class_ = "table table-attributes")
#     mass_names = table_raw.find_all("th")
#     mass_attr = table_raw.find_all("td")
#
#     del mass_names[0:2]
#     massiv_tovarov[sku] = {}
#     #massiv_tovarov[sku]['Имя товара'] = name_tovar
#     massiv_tovarov[sku]['Производитель'] = 'Norgren'
#     massiv_tovarov[sku]['Артикул'] = sku
#     #massiv_tovarov[sku]['Наименование'] = name_cat
#     for i,j in zip(mass_names, mass_attr):
#
#         name_attr = i.text[:-1]
#         value_attr = j.text
#
#
#         if name_attr == 'Series':
#             name_attr = 'Серия'
#
#         if name_attr == 'Port size':
#             name_attr = 'Присоединение'
#
#         if(not (name_attr in mass_index_attr)):
#             mass_index_attr[name_attr] = index_attr
#             index_attr += 1
#
#
#
#         if name_attr == 'Присоединение':
#             if (not ('Тип присоединения' in mass_index_attr)):
#                 mass_index_attr['Тип присоединения'] = index_attr
#                 index_attr += 1
#             port = ports(value_attr)
#             massiv_tovarov[sku]['Тип присоединения'] = port[0]
#             value_attr = port[1]
#         if ('°C' in value_attr) or ('bar' in value_attr):
#             value_attr = rep_point(value_attr)
#
#         if name_attr in massiv_tovarov[sku]:
#             massiv_tovarov[sku][name_attr] += ', ' + value_attr
#         else:
#             massiv_tovarov[sku][name_attr] = value_attr
#     massiv_tovarov[sku]['url'] = ulling
#     #На выходе ассоциантивный массив атрибутов
#
#     massiv_photo[sku] = {}
#     #Фотки блять
#     photo_address = str(souper.find("img", class_="print-only-product-image"))
#     # print(photo_address)
#     massiv_photo[sku]['Изображение'] = 'Изображение отсутствует'
#     photo_address = photo_address[photo_address.find('src="') + 5:photo_address.find('"/>')]
#     if(not (('img-store-grey' in photo_address) or('no-image' in photo_address)) and len(photo_address) > 1):
#         # print(photo_address)
#         photo_name = photo_address.split("/")[-1].replace('_', '-').lower()
#         # print(photo_name)
#         p = requests.get(photo_address)
#         #open(dirs + '\\' + 'photo' + '\\' + photo_name, 'wb').write(p.content)
#         massiv_photo[sku]['Изображение'] = photo_name
#     #Скачали фотки и подписали к каждому объекту
#
#     massiv_docs[sku] = {}
#     # Документы ебать
#     doc_mas = souper.find_all("div", class_="pdf-link product-detail-link")
#     doc_mas_address = []
#     doc_mas_names = []
#     # print(photo_address)
#     massiv_docs[sku]['Файлы'] = ''
#     massiv_docs[sku]['Имена файлов'] = ''
#     if (len(doc_mas) > 1):
#         for d in range(0, len(doc_mas)):
#             doc_mas_address.append(str(doc_mas[d])[str(doc_mas[d]).find('http'):str(doc_mas[d]).find("')")])
#             doc_mas_names.append(doc_mas[d].text)
#         print(doc_mas_address)
#         for d in range(0, len(doc_mas_address)):
#             doc_name = doc_mas_address[d].split("/")[-1].replace('_', '-').lower()
#             p = requests.get(doc_mas_address[d])
#            # open(dirs + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
#             massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'] + doc_name + ','
#             massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'] + doc_mas_names[d].replace('\n','') + ','
#         massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'][:-1]
#         massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'][:-1]
#     elif(len(doc_mas) == 0):
#         massiv_docs[sku]['Файлы'] = 'Отсутствуют'
#         massiv_docs[sku]['Имена файлов'] = 'Отсутствуют'
#     else:
#         doc_mas_address.append(str(doc_mas[0])[str(doc_mas[0]).find('http'):str(doc_mas[0]).find("')")])
#         doc_mas_names.append(doc_mas[0].text)
#         doc_name = doc_mas_address[0].split("/")[-1].replace('_', '-').lower()
#        # open(dirs + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
#         massiv_docs[sku]['Файлы'] = doc_name
#         massiv_docs[sku]['Имена файлов'] = doc_mas_names[0].replace('\n','')
#     print(massiv_index_info, massiv_photo, massiv_index_photo, massiv_tovarov, mass_index_attr,massiv_docs, massiv_index_docs, massiv_index_cat_ser, mass_index_meta, sep = '\n')
# getter(ur)
# def getter(mas_url, name_cat, dirs):
#     massiv_info = {}
#     massiv_index_info = {'inner_id':0, 'Имя товара':1, 'Артикул':2,'Производитель':3,'Цена':4,'Статус':5}
#
#     massiv_photo = {}
#     massiv_index_photo = {'inner_id':0, 'Имя товара':1, 'Изображение':2,'Дополнительные изображения':3}
#
#     massiv_tovarov = {}
#     mass_index_attr = {'inner_id':0, 'Имя товара':1, 'Производитель':2, 'Артикул':3, 'Наименование':4}
#     index_attr = 5
#
#     massiv_cat_ser = {}
#     massiv_index_cat_ser = {'inner_id':0, 'Имя товара':1, 'Категория':2,'Серия':3}
#
#     mass_index_meta = {'inner_id':0, 'Имя товара':1, 'Meta Keyword':2,'Описание':3}
#
#     massiv_docs = {}
#     massiv_index_docs = {'inner_id':0, 'Имя товара':1, 'Имена файлов':2,'Файлы':3}
#
#     for ulling in mas_url:
#         zapr = requests.get(ulling)
#         souper = BeautifulSoup(zapr.text, "html.parser")
#         sku = souper.find("span", class_="sku").text
#         name_tovar = name_cat + ' Norgren ' + sku
#         #print(sku.text)
#         #Ебашим атрибуты------------------------------------
#         table_raw = souper.find("div", id="tech-details").find("table", class_ = "table table-attributes")
#         mass_names = table_raw.find_all("th")
#         mass_attr = table_raw.find_all("td")
#
#         del mass_names[0:2]
#         massiv_tovarov[sku] = {}
#         massiv_tovarov[sku]['Имя товара'] = name_tovar
#         massiv_tovarov[sku]['Производитель'] = 'Norgren'
#         massiv_tovarov[sku]['Артикул'] = sku
#         massiv_tovarov[sku]['Наименование'] = name_cat
#         for i,j in zip(mass_names, mass_attr):
#
#             name_attr = i.text[:-1]
#             value_attr = j.text
#
#
#             if name_attr == 'Series':
#                 name_attr = 'Серия'
#
#             if name_attr == 'Port size':
#                 name_attr = 'Присоединение'
#
#             if(not (name_attr in mass_index_attr)):
#                 mass_index_attr[name_attr] = index_attr
#                 index_attr += 1
#
#             if name_attr == 'Series':
#                 name_attr = 'Серия'
#
#             if name_attr == 'Присоединение':
#                 if (not ('Тип присоединения' in mass_index_attr)):
#                     mass_index_attr['Тип присоединения'] = index_attr
#                     index_attr += 1
#                 port = ports(value_attr)
#                 massiv_tovarov[sku]['Тип присоединения'] = port[0]
#                 value_attr = port[1]
#             if ('°C' in value_attr) or ('bar' in value_attr):
#                 value_attr = rep_point(value_attr)
#
#
#             massiv_tovarov[sku][name_attr] = value_attr
#         #На выходе ассоциантивный массив атрибутов
#
#         massiv_photo[sku] = {}
#         #Фотки блять
#         photo_address = str(souper.find("img", class_="print-only-product-image"))
#         # print(photo_address)
#         photo_address = photo_address[photo_address.find('src="') + 5:photo_address.find('"/>')]
#         # print(photo_address)
#         photo_name = photo_address.split("/")[-1].replace('_', '-').lower()
#         # print(photo_name)
#         p = requests.get(photo_address)
#         open(dirs + '\\' + 'photo' + '\\' + photo_name, 'wb').write(p.content)
#         massiv_photo[sku]['Изображение'] = photo_name
#         #Скачали фотки и подписали к каждому объекту
#
#         massiv_docs[sku] = {}
#         # Документы ебать
#         doc_mas = souper.find_all("div", class_="pdf-link product-detail-link")
#         doc_mas_address = []
#         doc_mas_names = []
#         # print(photo_address)
#         massiv_docs[sku]['Файлы'] = ''
#         massiv_docs[sku]['Имена файлов'] = ''
#         if (len(doc_mas) > 1):
#             for d in range(0, len(doc_mas)):
#                 doc_mas_address.append(str(doc_mas[d])[str(doc_mas[d]).find('http'):str(doc_mas[d]).find("')")])
#                 doc_mas_names.append(doc_mas[d].text)
#             print(doc_mas_address)
#             for d in range(0, len(doc_mas_address)):
#                 doc_name = doc_mas_address[d].split("/")[-1].replace('_', '-').lower()
#                 p = requests.get(doc_mas_address[d])
#                 open(dirs + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
#                 massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'] + doc_name + ','
#                 massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'] + doc_mas_names[d].replace('\n','') + ','
#             massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'][:-1]
#             massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'][:-1]
#         else:
#             doc_mas_address.append(str(doc_mas[0])[str(doc_mas[0]).find('http'):str(doc_mas[0]).find("')")])
#             doc_mas_names.append(doc_mas[0].text)
#             doc_name = doc_mas_address[0].split("/")[-1].replace('_', '-').lower()
#             open(dirs + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
#             massiv_docs[sku]['Файлы'] = doc_name
#             massiv_docs[sku]['Имена файлов'] = doc_mas_names[0].replace('\n','')
    #print(massiv_tovarov, mass_index_attr)
    #printer(massiv_index_info, massiv_photo, massiv_index_photo, massiv_tovarov, mass_index_attr,massiv_docs, massiv_index_docs, massiv_index_cat_ser, mass_index_meta, dirs, name_cat)





#
# def test():
#     f = open('test.txt')
# massiv_docs = {}
# massiv_index_docs = {'inner_id': 0, 'Имя товара': 1, 'Имена файлов': 2, 'Файлы': 3}
#
# ulling = 'https://www.norgren.com/sg/en/detail/b84g_3ak_qd1_rfg'
# zapr = requests.get(ulling)
# souper = BeautifulSoup(zapr.text, "html.parser")
# sku = souper.find("span", class_="sku").text
# #print(sku.text)
# #Ебашим атрибуты------------------------------------
# table_raw = souper.find("div", id="tech-details").find("table", class_ = "table table-attributes")
# mass_names = table_raw.find_all("th")
# mass_attr = table_raw.find_all("td")
#
# name = souper.find("span", class_="sku").text


# massiv_docs[sku] = {}
#
# doc_mas = souper.find_all("div", class_="pdf-link product-detail-link")
# doc_mas_address = []
# doc_mas_names = []
#         # print(photo_address)
# if(len(doc_mas) > 1):
#     massiv_docs[sku]['Файлы'] = ''
#     massiv_docs[sku]['Имена файлов'] = ''
#     for d in range(0, len(doc_mas)):
#         doc_mas_address.append(str(doc_mas[d])[str(doc_mas[d]).find('http'):str(doc_mas[d]).find("')")])
#         doc_mas_names.append(doc_mas[d].text)
#     print(doc_mas_address)
#     for d in range(0, len(doc_mas_address)):
#         doc_name = doc_mas_address[d].split("/")[-1].replace('_', '-').lower()
#         p = requests.get(doc_mas_address[d])
#         open(r'norgen\air-preparation\combination-units-frl' + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
#         massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'] + doc_name + ','
#         massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'] + doc_mas_names[d].replace('\n', '') + ','
#     massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'][:-1]
#     massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'][:-1]
#     print(massiv_docs)







# a = translator.translate("Hello", "French")
# print(a)
# google_url = 'https://translate.googleapis.com/v3beta1:translateText'
# dop = '/v3beta1/{parent=projects/*}:detectLanguage'
# zap = {}
# zap['contents'] = []
# zap['contents'].append("good")
# zap_j = json.dumps(zap)
# a = requests.post(google_url, str(zap_j))
# print(a.text)
# print(requests.get('https://www.googleapis.com/language/translate/v2?key=INSERT-YOUR-KEY&q=hello%20world&source=en&target=de').text)


# a = {}
# a['li'] = 23
# a['models'] = [])
# for i in a:
#     print(a[i])

# def value_redact(val:str):
#     variator = {
#
#     }
#     if "..." in val:
#         val.replace('...', 'до')
#         val = 'От '+ val
#     elif 'µm' in val:
#         val.replace('µm', 'мкм')
#
#
#
#
# def getter():
#     ulling = 'https://www.norgren.com/sg/en/detail/b84g_3ak_qd1_rfg'
#     zapr = requests.get(ulling)
#     souper = BeautifulSoup(zapr.text, "html.parser")
#     sku = souper.find("span", class_="sku")
#     print(sku.text)
#     table_raw = souper.find("div", id="tech-details").find("table", class_ = "table table-attributes")
#     mass_names = table_raw.find_all("th")
#     mass_attr = table_raw.find_all("td")
#     del mass_names[0:2]
#     massiv_tovarov = {}
#     massiv_tovarov[sku.text] = {}
#     for i,j in zip(mass_names, mass_attr):
#         # print(i.text, "-->", j.text)
#         #massiv_tovarov[translator.translate(i.text, "Russian").result] = translator.translate(j.text, "Russian").result
#         name_attr = i.text
#         value_attr = j.text
#         name_attr = name_attr[:-1]
#         if name_attr =='Port size':
#             if 'PTF' in value_attr:
#                 massiv_tovarov[sku.text]['Тип присоединения'] = 'PTF'
#                 value_attr.replace('PTF', '')
#             elif 'G' in value_attr:
#                 massiv_tovarov[sku.text]['Тип присоединения'] = 'G'
#                 value_attr.replace('G', '')
#         massiv_tovarov[sku.text][name_attr] = value_attr
#     print(massiv_tovarov)
#
# def printer(mas_tovar):
#     pass
#
# getter()



