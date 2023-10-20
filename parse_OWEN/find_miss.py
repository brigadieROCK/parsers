import os
import json
import requests
from requests.auth import HTTPBasicAuth
import xlrd
import csv
import openpyxl
import xlwt
#В строке 16

def read_native_table():
    f = open('XN6Fk7FAo9g3adpIpqiXQCZVq.csv', newline='')
    read = csv.DictReader(f, dialect='excel',delimiter=';') #Собираем словарь из CSV-шника
    mass_id = {}
    #Выбираем OWEN в массив формата mass_id =[{ овен_айди : наш_айди},{овен_айди : наш_айди}]
    for i in read:
        if(i['supplier_id'] == '2'):
            mass_id[i['supplier_code']] = i['product_id']
    return mass_id

def fun():

    file = requests.get('https://owen.ru/upl/obmen_files/price_dealer.xls')
    open('parsetable_owen.xls', 'wb').write(file.content)
    massiv_home_id = read_native_table()


    book_write = xlwt.Workbook(encoding="utf-8")
    sheet_info = book_write.add_sheet('Отсутствующая на сайте овна')
    write_count = 1
    book_read = xlrd.open_workbook("parsetable_owen.xls")
    sheet_read = book_read.sheet_by_index(0)
    for i, j in enumerate(sheet_read.row(5)):
        sheet_info.write(0, i, str(j.value))
    for scan in range(sheet_read.nrows):
        # print(sheet_read.row(scan)[1].value)
        if not (sheet_read.row(scan)[1].value in massiv_home_id.keys()):
            for i, j in enumerate(sheet_read.row(scan)):
                sheet_info.write(write_count, i, str(j.value))
            write_count += 1
    book_write.save('Отсутствующая на сайте овна.xls')
fun()
