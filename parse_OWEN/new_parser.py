import os
import json
import requests
from requests.auth import HTTPBasicAuth
import xlrd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
import csv
import mimetypes                                          # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                # Импортируем энкодер
from email.mime.base import MIMEBase                      # Общий тип
from email.mime.text import MIMEText                      # Текст/HTML
from email.mime.image import MIMEImage                    # Изображения
from email.mime.audio import MIMEAudio
#manufacturer_id = 34
send_addr = 'адрес для отправки'
id = "айди"
token = "токен"
secret = "секретка"
host_server = "imap.yandex.ru"
login='логин'
password = 'пароль'

filepath_up = 'tovars-update-price.csv'
filepath_nl = 'tovars-null-price.csv'
filename_up = os.path.basename(filepath_up)
filename_nl = os.path.basename(filepath_nl)


def send_mes(message:str):
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = send_addr
    msg['Subject'] = Header(f"Обновление цен ОВЕН {datetime.now()}",'utf-8')
    msg.attach(MIMEText(message))

    if os.path.isfile(filepath_nl):  # Если файл существует
        ctype, encoding = mimetypes.guess_type(filepath_nl)  # Определяем тип файла на основе его расширения
        if ctype is None or encoding is not None:  # Если тип файла не определяется
            ctype = 'application/octet-stream'  # Будем использовать общий тип
        maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
        if maintype == 'text':  # Если текстовый файл
            with open(filepath_nl) as fp:  # Открываем файл для чтения
                file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
                fp.close()  # После использования файл обязательно нужно закрыть
        else:  # Неизвестный тип файла
            with open(filepath_nl, 'rb') as fp:
                file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
                file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
                fp.close()
            encoders.encode_base64(file)
    file.add_header('Content-Disposition', 'attachment', filename=filename_nl)
    msg.attach(file)

    if os.path.isfile(filename_up):  # Если файл существует
        ctype, encoding = mimetypes.guess_type(filename_up)  # Определяем тип файла на основе его расширения
        if ctype is None or encoding is not None:  # Если тип файла не определяется
            ctype = 'application/octet-stream'  # Будем использовать общий тип
        maintype, subtype = ctype.split('/', 1)  # Получаем тип и подтип
        if maintype == 'text':  # Если текстовый файл
            with open(filename_up) as fp:  # Открываем файл для чтения
                file = MIMEText(fp.read(), _subtype=subtype)  # Используем тип MIMEText
                fp.close()  # После использования файл обязательно нужно закрыть
        else:  # Неизвестный тип файла
            with open(filename_up, 'rb') as fp:
                file = MIMEBase(maintype, subtype)  # Используем общий MIME-тип
                file.set_payload(fp.read())  # Добавляем содержимое общего типа (полезную нагрузку)
                fp.close()
            encoders.encode_base64(file)
    file.add_header('Content-Disposition', 'attachment', filename=filename_up)
    msg.attach(file)

    mailserver = smtplib.SMTP('smtp.yandex.ru', 587)
    mailserver.ehlo(login)
    mailserver.starttls()
    mailserver.ehlo(login)
    mailserver.login(login, password)
    mailserver.sendmail(login, send_addr, msg.as_string())
    mailserver.quit()

def read_native_table():
    data = {}
    data['client_id'] = 'vvt31323'
    data['query'] = []
    data['query'].append({'select':'product_id, model, price, sku','where':'manufacturer_id = 34'})
    zap_json = str(json.dumps(data))#, ensure_ascii=False)
    zap_json = zap_json.replace(']', '')
    zap_json = zap_json.replace('[', '')
    #print(zap_json)
    basic = HTTPBasicAuth('admin', '^*&GKJG*%*&5312')
    head = {'Content-type':'application/json', 'Content-Length':str(len(zap_json))}
    url = 'https://products.industriation.com/api.php?api=get_product&other_db=ind_db'
    x = requests.post(url, str(zap_json), auth=basic,headers=head)
    x = json.loads(str.encode(x.text, encoding='utf-8'))

    dop_data = {}
    for i in x['results']:
        dop_data[i['model']] = {}
        dop_data[i['model']]['product_id'] = i['product_id']
        dop_data[i['model']]['price'] = i['price']
        dop_data[i['model']]['sku'] = i['sku']

    rez_data = {}
    rez_data['nums'] = {}
    rez_data['strs'] = {}

    for i in dop_data:
        flag = False
        for j in i:
            if (not (j in ('-','.','/')) and ((ord('9') < ord(j)) or (ord(j) < ord('0')))):
                flag = True
                break
        if flag:
            rez_data['strs'][i] = dop_data[i]
        else:
            rez_data['nums'][i] = dop_data[i]

    # for i in rez_data:
    #     print(i,'====', rez_data[i],'\n')
    return rez_data

def get_attr(old_price):
    file = requests.get('https://owen.ru/upl/obmen_files/price_dealer.xls')
    open('parsetable_owen.xls', 'wb').write(file.content)

    book_read = xlrd.open_workbook("parsetable_owen.xls")
    sheet_read = book_read.sheet_by_index(0)
    index_article, index_price, index_sku = 0,0,0
    fl_sku, fl_atr, fl_prs = False, False, False
    for scan in range(sheet_read.nrows):
        for i,j in enumerate(sheet_read.row(3)):
            if ('наименование рабочее' in str(j.value).lower()):
                index_sku = i
                fl_atr = True
            if ('артикул' in str(j.value).lower()):
                index_article = i
                fl_atr = True

            if ('цена' == str(j.value).lower()):
                index_price = i
                fl_prs = True
        if(fl_atr and fl_prs):
            break
    massOfSku = sheet_read.col_values(index_sku)
    massOfArticle = sheet_read.col_values(index_article)
    massOfPrice = sheet_read.col_values(index_price)
    ind = 0
    #Ищем индекс с которого начинаются строки с ценами и артикулами
    for i in massOfSku:
        if (i.lower() =='наименование рабочее'):
            break
        else:
            ind += 1
    ind += 1
    massOfSku = massOfSku[ind:]
    massOfArticle = massOfArticle[ind:]
    massOfPrice = massOfPrice[ind:]
    new_price = {}
    for j in range(len(massOfArticle)):
        new_price[massOfArticle[j]] = {}
        new_price[massOfArticle[j]]['sku'] = massOfSku[j]
        new_price[massOfArticle[j]]['price'] = massOfPrice[j]
    # for j in new_price:
    #     print(j, '====', new_price[j], '\n')
        #----------------------------------------------------------------------------------
    # # Собираем JSON для передачи
    data = {}
    data['client_id'] = 'vvt31323'
    data['products'] = []

    count_num, count_st = 0,0
    for i in old_price['nums']:
        if i in new_price.keys():
            if(str(old_price['nums'][i]['sku']).replace('-', '') == str(new_price[i]['sku']).replace('-','').replace('.','').replace('/','')):
                data['products'].append({"product_id":old_price['nums'][i]['product_id'], "price": float(new_price[i]['price'].replace(',','.'))})
                count_num+=1
    for i in old_price['strs']:
            for j in new_price:
                if(str(i).replace('-', '') == str(new_price[j]['sku']).replace('-','').replace('.','').replace('/','')):
                    data['products'].append({"product_id":old_price['strs'][i]['product_id'], "price": float(new_price[j]['price'].replace(',','.'))})
                    #print(i, ' sootvetstvuet ', j, '\n')
                    count_st+=1
                    break

    return count_num + count_st, data
    #     if(str(old_price[i]['sku']).replace('-', '') == str(old_price[i]['sku']).replace('-', ''))
    #     except:
    #         continue
    # os.remove("parsetable_owen.xls")
    # return count, json.dumps(data)

def post_read(old, data):
    f = open('tovars-null-price.csv', 'w', encoding='utf-8')
    names = ['product_id', 'model', 'date']
    wr = csv.DictWriter(f, delimiter=';', lineterminator="\r", fieldnames=names)
    wr.writeheader()
    wr.writerow({'date': str(datetime.now())})
    # for i in bad_data['nums']:
    #     wr.writerow({'product_id': bad_data['nums'][i]['product_id'], 'model': i})
    # for i in bad_data['strs']:
    #     wr.writerow({'product_id': bad_data['strs'][i]['product_id'], 'model': i})


    mass_null = []
    for i in old['nums']:
        flag = True
        for j in data['products']:
            if (old['nums'][i]['product_id'] == j['product_id']):
                flag = False
                break
        if(flag):
            mass_null.append(str(old['nums'][i]['product_id']))
            wr.writerow({'product_id': old['nums'][i]['product_id'], 'model': i})
    for i in old['strs']:
        flag = True
        for j in data['products']:
            if (old['strs'][i]['product_id'] == j['product_id']):
                flag = False
                break
        if(flag):
            mass_null.append(str(old['strs'][i]['product_id']))
            wr.writerow({'product_id': old['strs'][i]['product_id'], 'model': i})
    for s in mass_null:
        data['products'].append({"product_id":s, "price": float(0.0000)})

    f.close()
    return len(mass_null), data


old = read_native_table()
updt_price, data = get_attr(old)
f = open('tovars-update-price.csv', 'w', encoding='utf-8')
names = ['product_id', 'price', 'date']
wr = csv.DictWriter(f, delimiter = ';',lineterminator="\r", fieldnames=names)
wr.writeheader()
wr.writerow({'date':str(datetime.now())})
for i in data['products']:
    wr.writerow(i)
f.close()
nulls, data = post_read(old, data)





send_mes('Количество обновленных товаров : ' + str(updt_price) + '\nКоличество товаров без цены : ' + str(nulls))

#Связка с API Михала, просто снять коммент
rez_json = json.dumps(data)
basic = HTTPBasicAuth('admin', '^*&GKJG*%*&5312')
head = {'Content-type':'application/json', 'Content-Length':str(len(rez_json))}
url = 'https://products.industriation.com/api.php?api=update_product&other_db=ind_db'
x = requests.post(url, str(rez_json), auth=basic,headers=head)
