from random import randint
import codecs, os

def openfile(file):
    return codecs.open(file, encoding="utf-8")

def editfile(file):
    return codecs.open(file, "w", encoding="utf-8")

def smthfile(file, readingmode):
    return codecs.open(file, readingmode, encoding="utf-8")

def get_file_path(folder, filename):
    folder_dir = os.path.dirname(__file__)

    # creates the filename folder if it doesnt exist
    folder_dir = os.path.join(folder_dir, folder)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

    filepath = os.path.join(folder_dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, "w") as f: pass

    return filepath

def altteotf(filepath, line):
    with smthfile(filepath, "a+") as file:
        file.seek(0)
        if file.read():
            file.seek(0, 2)
            file.write("\n")
        file.write(line)

def isWord(word):
    h = 0
    for every in word:
        if any(every==_ for _ in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
            h += 1
    return (len(word)==h)

def isLetter(letter):
    return any(_==letter for _ in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

def hAutoCorrect(hInput):
    hAutoCorrected=""
    up=True
    for hInputFor in hInput:
        if up==True and isLetter(hInputFor):
            hAutoCorrected+="h"+hInputFor.upper()
            up=False
        elif (not up and isLetter(hInputFor)): hAutoCorrected+=hInputFor.lower()
        else:
            hAutoCorrected+=hInputFor
            up=True
    return hAutoCorrected

def generate_ip(name):
    def numip(n):
        ip=""
        for every in [1,2,3,4]:
            c=0
            h=n[every*8-8:every*8]
            for everyone in range(0,8):
                c+=int(h[everyone])*(128//(everyone+1)**everyone+1)
            ip+=str(c)+"."
        return ip[:-1]
    ans=""
    for every in name:
        num=ord(every)
        if num>=100: num=str(num)[1:]
        ans+=str(num)
    ans=int(ans)
    ans=int(bin(ans,"")[2:])
    dis=len(ans)/32
    rawAns=""
    for every in range(0,32):
        every=ans[int(dis*every)]
        rawAns+=str(every)
    ans=rawAns
    return numip(ans)
