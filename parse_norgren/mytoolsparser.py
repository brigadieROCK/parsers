import os
import json
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import csv
from config import url_homepage
from translatepy import Translator
import itertools
from translatepy import Translator
import xlrd
import xlwt
from attrhandler import ports, rep_point, photos

translator = Translator()





#testgetter()






#Старая версия
# def getter(mas_url):
#     massiv_tovarov = {}
#     for ulling in mas_url:
# #    ulling = 'https://www.norgren.com/sg/en/detail/b84g_3ak_qd1_rfg'
#         zapr = requests.get(ulling)
#         souper = BeautifulSoup(zapr.text, "html.parser")
#         sku = souper.find("span", class_="sku")
#         print(sku.text)
#         table_raw = souper.find("div", id="tech-details").find("table", class_ = "table table-attributes")
#         mass_names = table_raw.find_all("th")
#         mass_attr = table_raw.find_all("td")
#         del mass_names[0:2]
#         massiv_tovarov[sku.text] = {}
#         for i,j in zip(mass_names, mass_attr):
#
#             name_attr = i.text[:-1]
#             value_attr = j.text
#
#             if name_attr == 'Port size':
#                 if 'PTF' in value_attr:
#                     massiv_tovarov[sku.text]['Тип присоединения'] = 'PTF'
#                     value_attr.replace('PTF', '')
#                 elif 'G' in value_attr:
#                     massiv_tovarov[sku.text]['Тип присоединения'] = 'G'
#                     value_attr.replace('G', '')
#
#             massiv_tovarov[sku.text][name_attr] = value_attr
#     print(massiv_tovarov)
#     return massiv_tovarov

#{
#   sku:{
#           attr's
#       },
#   sku1:{
#           attr's
#       }
#}
#врайт(стр, колон, знач)



def printer(mas_ind_info, mas_ph, mas_ind_ph, mas_attr, mas_ind_attr, mas_doc, mas_ind_doc, mas_ind_cat_ser, mas_ind_meta, dirs, category):
    # f = open("clean-table.xls", "r")
    # re = open("rez-table.xls", "w")
    # re.write(f.read(),)
    # f.close()
    # re.close()
    book = xlwt.Workbook(encoding="utf-8")
    sheet_info = book.add_sheet('Данные')
    st = 1
    for i in mas_ind_info:
        sheet_info.write(0, mas_ind_info[i], str(i))

    for i in mas_attr:
        sheet_info.write(st, mas_ind_info['Статус'], str(1))
        for j in mas_attr[i]:
            if(j in mas_ind_info):
                sheet_info.write(st, mas_ind_info[j], str(mas_attr[i][j]))
        st+=1

    sheet_photos = book.add_sheet('Изображения')
    st = 1
    for i in mas_ind_ph:
        sheet_photos.write(0, mas_ind_ph[i], str(i))

    for i in mas_attr:
        sheet_photos.write(st,mas_ind_ph['Изображение'], mas_ph[i]['Изображение'])
        for j in mas_attr[i]:
            if (j in mas_ind_ph):
                sheet_photos.write(st, mas_ind_ph[j], str(mas_attr[i][j]))
        st += 1


    sheet_atr = book.add_sheet('Атрибуты')
    flag = True
    st = 1
    for i in mas_ind_attr:
        sheet_atr.write(0, mas_ind_attr[i], str(i))

    for i in mas_attr:
        #sheet.write(st, 0, str(i))
        for j in mas_attr[i]:
            sheet_atr.write(st, mas_ind_attr[j], str(mas_attr[i][j]))
        st += 1

    sheet_cat_ser = book.add_sheet('Категории_Серия')
    st = 1
    for i in mas_ind_cat_ser:
        sheet_cat_ser.write(0, mas_ind_cat_ser[i], str(i))

    for i in mas_attr:
        for j in mas_attr[i]:
            if (j in mas_ind_cat_ser):
                sheet_cat_ser.write(st, mas_ind_cat_ser[j], str(mas_attr[i][j]))
        st += 1

    sheet_meta = book.add_sheet('Meta данные')
    st = 1
    for i in mas_ind_meta:
        sheet_meta.write(0, mas_ind_meta[i], str(i))

    for i in mas_attr:
        for j in mas_attr[i]:
            if (j in mas_ind_meta):
                sheet_meta.write(st, mas_ind_meta[j], str(mas_attr[i][j]))
        st += 1

    sheet_docs = book.add_sheet('Документация')
    st = 1
    for i in mas_ind_doc:
        sheet_docs.write(0, mas_ind_doc[i], str(i))

    for i in mas_attr:
        sheet_docs.write(st, mas_ind_doc['Имена файлов'], mas_doc[i]['Имена файлов'])
        sheet_docs.write(st, mas_ind_doc['Файлы'], mas_doc[i]['Файлы'])
        for j in mas_attr[i]:
            if (j in mas_ind_doc):
                sheet_docs.write(st, mas_ind_doc[j], str(mas_attr[i][j]))
        st += 1
    # name_file = ''
    # for charing in category:
    #     charor = ord(charing)
    #     if (65 <= charor <= 90) or (97 <= charor <= 122) or (charing  == '-'):
    #         name_file += charing
    book.save(dirs + '\\' + f'norgren-{category}-demo.xls')
    photos(dirs + '\\' +'photo')


def getter(mas_url, name_cat, dirs):
    massiv_info = {}
    massiv_index_info = {'inner_id':0, 'Имя товара':1, 'Артикул':2,'Производитель':3,'Цена':4,'Статус':5}

    massiv_photo = {}
    massiv_index_photo = {'inner_id':0, 'Имя товара':1, 'Изображение':2,'Дополнительные изображения':3}

    massiv_tovarov = {}
    mass_index_attr = {'inner_id':0,'url':1, 'Имя товара':2, 'Производитель':3, 'Артикул':4, 'Наименование':5, 'Особенности':6}
    index_attr = 7

    massiv_cat_ser = {}
    massiv_index_cat_ser = {'inner_id':0, 'Имя товара':1, 'Категория':2,'Серия':3}

    mass_index_meta = {'inner_id':0, 'Имя товара':1, 'Meta Keyword':2,'Описание':3}

    massiv_docs = {}
    massiv_index_docs = {'inner_id':0, 'Имя товара':1, 'Имена файлов':2,'Файлы':3}

    for ulling in mas_url:
        try:
            zapr = requests.get(ulling)
            souper = BeautifulSoup(zapr.text, "html.parser")
            sku = souper.find("span", class_="sku").text
            name_tovar = name_cat + ' Norgren ' + sku
            #print(sku.text)
            #Ебашим атрибуты------------------------------------
            table_raw = souper.find("div", id="tech-details").find("table", class_ = "table table-attributes")
            mass_names = table_raw.find_all("th")
            mass_attr = table_raw.find_all("td")

            fact_uniq = souper.find('ul', class_ = 'features')
            s_uniq = ''
            if (fact_uniq != None):
                mass_uniq = fact_uniq.find_all('li')
                for uni in range(0, len(mass_uniq)):
                    if(uni == 0):
                        s_uniq += mass_uniq[uni].text
                    else:
                        s_uniq += ',' + mass_uniq[uni].text

            del mass_names[0:2]
            massiv_tovarov[sku] = {}
            massiv_tovarov[sku]['Имя товара'] = souper.find('h1').text + ' Norgren ' + sku
            massiv_tovarov[sku]['Производитель'] = 'Norgren'
            massiv_tovarov[sku]['Артикул'] = sku
            massiv_tovarov[sku]['Наименование'] = name_cat
            massiv_tovarov[sku]['Особенности'] = s_uniq
            for i,j in zip(mass_names, mass_attr):

                name_attr = i.text[:-1]
                value_attr = j.text


                if name_attr == 'Series':
                    name_attr = 'Серия'

                if name_attr == 'Port size':
                    name_attr = 'Присоединение'

                if(not (name_attr in mass_index_attr)):
                    mass_index_attr[name_attr] = index_attr
                    index_attr += 1



                if name_attr == 'Присоединение':
                    if (not ('Тип присоединения' in mass_index_attr)):
                        mass_index_attr['Тип присоединения'] = index_attr
                        index_attr += 1
                    port = ports(value_attr)
                    massiv_tovarov[sku]['Тип присоединения'] = port[0]
                    value_attr = port[1]
                if ('°C' in value_attr) or ('bar' in value_attr):
                    value_attr = rep_point(value_attr)

                if name_attr in massiv_tovarov[sku]:
                    massiv_tovarov[sku][name_attr] += ', ' + value_attr
                else:
                    massiv_tovarov[sku][name_attr] = value_attr
            massiv_tovarov[sku]['url'] = ulling
            #На выходе ассоциантивный массив атрибутов

            massiv_photo[sku] = {}
            #Фотки блять
            photo_address = str(souper.find("img", class_="print-only-product-image"))
            # print(photo_address)
            massiv_photo[sku]['Изображение'] = 'Изображение отсутствует'
            photo_address = photo_address[photo_address.find('src="') + 5:photo_address.find('"/>')]
            if(not (('img-store-grey' in photo_address) or('no-image' in photo_address)) and len(photo_address) > 1):
                # print(photo_address)
                photo_name = photo_address.split("/")[-1].replace('_', '-').lower()
                # print(photo_name)
                p = requests.get(photo_address)
                open(dirs + '\\' + 'photo' + '\\' + photo_name, 'wb').write(p.content)
                massiv_photo[sku]['Изображение'] = photo_name
            #Скачали фотки и подписали к каждому объекту

            massiv_docs[sku] = {}
            # Документы ебать
            doc_mas = souper.find_all("div", class_="pdf-link product-detail-link")
            doc_mas_address = []
            doc_mas_names = []
            # print(photo_address)
            massiv_docs[sku]['Файлы'] = ''
            massiv_docs[sku]['Имена файлов'] = ''
            if (len(doc_mas) > 1):
                for d in range(0, len(doc_mas)):
                    doc_mas_address.append(str(doc_mas[d])[str(doc_mas[d]).find('http'):str(doc_mas[d]).find("')")])
                    doc_mas_names.append(doc_mas[d].text)
                # print(doc_mas_address)
                for d in range(0, len(doc_mas_address)):
                    doc_name = doc_mas_address[d].split("/")[-1].replace('_', '-').lower()
                    p = requests.get(doc_mas_address[d])
                    open(dirs + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
                    massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'] + doc_name + ','
                    massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'] + doc_mas_names[d].replace('\n','') + ','
                massiv_docs[sku]['Файлы'] = massiv_docs[sku]['Файлы'][:-1]
                massiv_docs[sku]['Имена файлов'] = massiv_docs[sku]['Имена файлов'][:-1]
            elif(len(doc_mas) == 0):
                massiv_docs[sku]['Файлы'] = 'Отсутствуют'
                massiv_docs[sku]['Имена файлов'] = 'Отсутствуют'
            else:
                doc_mas_address.append(str(doc_mas[0])[str(doc_mas[0]).find('http'):str(doc_mas[0]).find("')")])
                doc_mas_names.append(doc_mas[0].text)
                doc_name = doc_mas_address[0].split("/")[-1].replace('_', '-').lower()
                p = requests.get(doc_mas_address[0])
                open(dirs + '\\' + 'documentation' + '\\' + doc_name, 'wb').write(p.content)
                massiv_docs[sku]['Файлы'] = doc_name
                massiv_docs[sku]['Имена файлов'] = doc_mas_names[0].replace('\n','')
        except:
            print(ulling)
    #print(massiv_tovarov, mass_index_attr)
    #Под доп парсер
    printer(massiv_index_info, massiv_photo, massiv_index_photo, massiv_tovarov, mass_index_attr, massiv_docs,massiv_index_docs, massiv_index_cat_ser, mass_index_meta, dirs, 'file')
    #printer(massiv_index_info, massiv_photo, massiv_index_photo, massiv_tovarov, mass_index_attr,massiv_docs, massiv_index_docs, massiv_index_cat_ser, mass_index_meta, dirs, name_cat)
