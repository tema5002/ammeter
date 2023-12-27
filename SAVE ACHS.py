import pickle

class Ach:
    title="Unknown"
    description="not defined achievement"
    emoji="<:regular:1188527241039204452>"
    noemoji="<:no_regular:1188527234693210243>"

# defining achs
unknown, sixAmperes, zyzzyzus, luck, aceSupporter, kys, dementia, wrongBot = Ach(), Ach(), Ach(), Ach(), Ach(), Ach(), Ach(), Ach()

# defining achs info
sixAmperes.title, sixAmperes.description = "6 Amperes", "AAAAAA"
zyzzyzus.title, zyzzyzus.description, zyzzyzus.emoji, zyzzyzus.noemoji = "Zyzzyzus", "what is zyzzyzus", "<:question_mark:1188527237583097926>", "<:no_question_mark:1188527231937564822>"
luck.title, luck.description, luck.emoji, luck.noemoji = "Luck 100", "There is 0.5% of getting this ach everytime you send messages", "<:luck:1188527217395912886>", "<:no_luck:1188527229026709635>"
aceSupporter.title, aceSupporter.description, aceSupporter.emoji, aceSupporter.noemoji = "Asexual Supporter", "YOU SHOULD KEEP YOURSELF SAFE NOW", "<:ace:1188527210580160532>", "<:no_ace:1188527220017352727>"
kys.title, kys.description, kys.emoji, kys.noemoji = "clearly a skill issue", "Find a way to die in ammeter", "<:kys:1188527215005155459>", "<:no_kys:1188527226992480416>"
dementia.title, dementia.description, dementia.emoji, dementia.noemoji = "AMMETER HAS DEMENTIA", "Get ping higher than 500ms in /ping", "<:dementia:1188527213390340096>", "<:no_dementia:1188527223880290334>"
wrongBot.title, wrongBot.description = "Wrong bot", "flowmigger and his family :joy::joy::grinning:"

achs=[unknown, sixAmperes, zyzzyzus, luck, aceSupporter, kys, dementia, wrongBot]

pickle.dump(achs, open("achs.dat", "wb"))