import pickle, os
from temalib import openfile, add_line

class Ach:
    title="Unknown"
    description="not defined achievement"
    emoji="<:regular:1188527241039204452>"
    noemoji="<:no_regular:1188527234693210243>"

# defining achs
unknown, sixAmperes, zyzzyzus, luck, aceSupporter, kys, dementia, wrongBot, bbox = Ach(), Ach(), Ach(), Ach(), Ach(), Ach(), Ach(), Ach(), Ach()

# defining achs info
sixAmperes.title, sixAmperes.description = "6 Amperes", "AAAAAA"
zyzzyzus.title, zyzzyzus.description, zyzzyzus.emoji, zyzzyzus.noemoji = "Zyzzyzus", "what is zyzzyzus", "<:question_mark:1188527237583097926>", "<:no_question_mark:1188527231937564822>"
luck.title, luck.description, luck.emoji, luck.noemoji = "Luck 100", "There is 0.05% of getting this ach everytime you send messages", "<:luck:1188527217395912886>", "<:no_luck:1188527229026709635>"
aceSupporter.title, aceSupporter.description, aceSupporter.emoji, aceSupporter.noemoji = "Asexual Supporter", "YOU SHOULD KEEP YOURSELF SAFE NOW", "<:ace:1188527210580160532>", "<:no_ace:1188527220017352727>"
kys.title, kys.description, kys.emoji, kys.noemoji = "clearly a skill issue", "Find a way to die in ammeter", "<:kys:1188527215005155459>", "<:no_kys:1188527226992480416>"
dementia.title, dementia.description, dementia.emoji, dementia.noemoji = "AMMETER HAS DEMENTIA", "Get ping higher than 500ms in /ping", "<:dementia:1188527213390340096>", "<:no_dementia:1188527223880290334>"
wrongBot.title, wrongBot.description = "Wrong bot", "flowmigger and his family :joy::joy::grinning:"
bbox.title, bbox.description = "Beatbox", "Make ammeter beatbox"

def get_ach(string):
    for every in achs:
        if every.title==string:
            return every
    if string!="": return achs[0]

def getachs(id):
    
    folder_dir = os.path.join(os.path.dirname(__file__), "achs")
    if not os.path.exists(folder_dir): os.makedirs(folder_dir)

    filepath=os.path.join(folder_dir, str(id) + ".txt")
    if not os.path.exists(filepath):
        with open(filepath, "w") as f: pass

    h = []
    for every in openfile(filepath).read().split("\n"):
        if every!="": h += [get_ach(every)]
    return h

def giveach(ach, member):
    ach = get_ach(ach)
    
    # created the achs folder
    folder_dir = os.path.join(os.path.dirname(__file__), "achs")
    if not os.path.exists(folder_dir): os.makedirs(folder_dir)

    # creates the member.id.txt
    filepath = os.path.join(folder_dir, str(member.id)+".txt")
    if not os.path.exists(filepath):
        with open(filepath, "w") as f: pass

    if not ach.title in openfile(filepath).read().split("\n"):
        add_line(filepath, ach.title)
        embed = disnake.Embed(title = "New achievement!")
        embed.add_field(name = f"{ach.emoji} {ach.title}", value = ach.description)
        footer_dict={"text": f"Unlocked by {member.name}"}
        embed.set_footer(**footer_dict)
        return embed

achs=[unknown, sixAmperes, zyzzyzus, luck, aceSupporter, kys, dementia, wrongBot, bbox]

pickle.dump(achs, open("achs.dat", "wb"))