from PIL import Image
import os


def ports(s:str):
    new_st = ''
    for i in s:
        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
            new_st += i
    s = s.replace(new_st, '')
    #a = [new_st, s]
    return [new_st, s]

def rep_point(s:str):
    new_st = ''
    if ('...' in s):
        new_st = 'От ' + s.replace('...', 'до').replace('bar', 'бар')
    else:
        new_st = s
    return new_st




def photos(fol_dir):

    mass_photo = []
    ext = ('jpg')
    for files in os.listdir(fol_dir):
        if files.endswith(ext):
            mass_photo.append(files)
    for p in mass_photo:
        f_name = p
        try:
            #print(f_name)
            cor = x, y = 0, 0
            with Image.open(fol_dir+'\\'+f_name) as im:
                max_x, max_y = im.size
                cor = x, y = 0, 0
                flag = True
                b = 0
                while (flag):
                    for i in range(0, max_x):
                        cor = x, y = i, b
                        if (im.getpixel(cor)[0] <= 248 and im.getpixel(cor)[1] <= 248 and im.getpixel(cor)[2] <= 248):
                            flag = False
                            break
                    b += 1
                x1 = b
                b = max_y - 1
                flag = True
                while (flag):
                    for i in range(0, max_x):
                        cor = x, y = i, b
                        if (im.getpixel(cor)[0] <= 248 and im.getpixel(cor)[1] <= 248 and im.getpixel(cor)[2] <= 248):
                            flag = False
                            break
                    b -= 1
                x2 = b
                b = 0
                flag = True
                while (flag):
                    for i in range(0, max_y):
                        cor = x, y = b, i
                        if (im.getpixel(cor)[0] <= 248 and im.getpixel(cor)[1] <= 248 and im.getpixel(cor)[2] <= 248):
                            flag = False
                            break
                    b += 1
                y1 = b

                b = max_x - 1
                flag = True
                while (flag):
                    for i in range(0, max_y):
                        cor = x, y = b, i
                        if (im.getpixel(cor)[0] <= 248 and im.getpixel(cor)[1] <= 248 and im.getpixel(cor)[2] <= 248):
                            flag = False
                            break
                    b -= 1
                y2 = b
                #print(x1, y1, y2, x2, sep=" ")
                im.crop((y1, x1, y2, x2)).save(fol_dir+'\\'+'cropped'+'\\'+f_name)
        except:
            print(f_name)


#ports('Rc1/8')