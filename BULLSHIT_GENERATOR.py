# i seriously need someone to optimize it too like everything in ammeter
from random import choice,randint
def bsgenerator(h):
    randomnt1=["New", "Super", "Improved", "Solution", "Multi-tier", "Life-changing", "kreisi"]
    rand1=""
    i=0
    p=randint(2,6)
    while i!=p:
        rand1+=randomnt1.pop(randint(0,len(randomnt1)-1))
        if i!=p-1: rand1+=' '
        i+=1

    rand2=choice(['+','-'])*randint(1,5)

    randomnt3=["Pro","Max","Ultra","Deluxe"]
    rand3=""
    i=0
    p=randint(1,2)
    while i!=p:
        rand3+=randomnt3.pop(randint(0,len(randomnt3)-1))
        if i!=p-1: rand3+=' '
        i+=1

    rand4=f"v{randint(2,20)}."+\
          f"{randint(1,9999)}."+\
          '9'*randint(1,5)

    rand5='X'*randint(1,12)+'L'

    rand6=(choice(["Java",
                   "Bedrock",
                   "Grass Block"])+" Editon") if randint(0,1)==0 else ' '

    rand7=choice(["(Extended)",""])

    rand8=choice(["(Beta Version)",
                  "(Beta Version) (Beta Version) (Beta Version)",
                  "(Delta Version)",
                  "(Sigma Version)"]) if randint(0,1)==0 else ' '

    rand9=choice(["(Demo)",""])

    rand10=choice(["24/7",f"{randint(12,24)}/{randint(1,7)}",""])

    rand11=choice(['('+str(choice([0,3,6,9,12,15,18]))+'+)',""])

    rand12=choice(["Offline",
                  "Online",
                  ""])

    rand13=choice(["PC","Mobile","PS Vita","Windows NT 4.0 For Workstations","Ammeter","Discord Nitro","Pressure Cooker","Your Mom"])+" Release"

    rand14=choice(["Half-Life","Portal 2","Doom (1993)","Free Month Of Discord Nitro","Adobe Photoshop","Windows Notepad"])+" Not Included"

    return f"{rand1} {h}™️{rand2} {rand3} {rand4} {rand5} {rand6} {rand7} {rand8} {rand9} {rand10} {rand11} {rand12} ({rand13}) ({rand14})".replace("  "," ").replace("  "," ").replace("  "," ")