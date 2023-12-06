from random import randint
def bin(n,c):
    if n==0: return c
    c+=str(bin(n//2,c))
    c+=str(n%2)
    return c
def randomip():
    return f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
def isWord(letter):
    bool=""
    for number in range(len(letter)):
        for every in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            if letter[number]==every:
                bool+="t"
                break
            if every=="z": bool+="f"
    if bool.find("f")>0: return False
    else: return True
def isLetter(letter):
    for every in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        if letter==every: return True
        if letter==every: break
        if every=="z": return False
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
    ans=bin(ans,"")
    dis=len(ans)/32
    rawAns=""
    for every in range(0,32):
        every=ans[int(dis*every)]
        rawAns+=str(every)
    ans=rawAns
    return numip(ans)