# i absolutely have no idea what am i doing

import disnake
import wikipedia
import asyncio
import math
import datetime
from random import choice,randint
from temalib import * # very silly library made by me if you need it then ask :typing:
from disnake.ext import commands
from random import randint, choice
from defenitely_something import bsgenerator

bot=commands.Bot(command_prefix="hey ammeter ",help_command=None,intents=disnake.Intents.all())

# i store user ids here
hexahedron1=801078409076670494
tema5002=558979299177136164
ammeter=811569586675515433

def makeembed(page, list):
    pages = math.ceil(len(list)/10)
    uhhh=""
    if page == pages:
        for every in list[10*(page-1):]:
            uhhh+=f"- {every}\n"
    else:
        for every in list[10*(page-1):10*(page-1)+10]:
            uhhh+=f"- {every}\n"
    return disnake.Embed(title=f"Page {page}/{pages}", description=uhhh)

def makecomponents(uhh):
    if uhh != None:
        components = []
        h = int(uhh[5:uhh.find("/")])
        g = int(uhh[uhh.find("/") + 1:])
        if h != 1:
            components+=[disnake.ui.Button(label="<", style=disnake.ButtonStyle.secondary, custom_id=str(h-1))]
        if h != g:
            components+=[disnake.ui.Button(label=">", style=disnake.ButtonStyle.secondary, custom_id=str(h+1))]
        return components

# holy shit thats more than 100 strings of code just for "funny" text
# splashes
splashes=[
    "abotmin ask ammeter to ask icosahedron to staring cat react him", 
    "currently 76 splashes",
    "how to staring cat emoji",
    "every time bot enables it sends random text thats cool isnt",
    "im a workstahon mini",
    "silly proglet V1; cellua good indev2 xnopyt",
    "hello",
    "undefined is defined as undefined",
    "picardibot plays with my balls and likes it",
    "Also try icosahedron!",
    "did i leak my token",
    "nevermind",
    "cube is unrotatable cube",
    "prohressnet nowhen",
    "https://prohressnet.xtema5002x.repl.co",
    "https://prohressnet.xtema5002x.repl.co/src/eto_i_est_am_nyam.mp4",
    "i have a fact that will definitely shock you but im not gonna tell it because meh",
    "your mom will be deleted by ammeterhahahahhaha",
    "is team5002 real",
    "owner of this bot sometimes wants to be a jellyfish",
    "this splash was removed",
    "theres no progresstation and workstahon flag :skull:",
    "slinx's attic is the most silly discord server you DEFINITELY should join!!!!!!!",
    "\"breaking good\" - 💀💀💀\n\nthats a long story",
    "you're*",
    "jsab stands for **j**ust ||**s**illy **a**ss **b**alls||",
    "lets drink to the health of indie developers!!!!",
    '```py\nwhile True:\n    print("\\n")\n    h=open("splashes_channels.txt").read().split()\n    for every in h:\n        channel=bot.get_channel(int(every))\n        if channel!=None:\n            await channel.send(choice(splashes))\n            print(f"sending splash on {channel} ({channel.guild})")\n        else:\n            print("cant send splash 💀💀💀")\n            with open("splashes_channels.txt","w") as splasheschannels:\n                for everything in h:\n                    if everything!=every:\n                        splasheschannels.write(f"{everything}\\n")\n    print("\\n")\n    await asyncio.sleep(150)```',
    "workstindows 11 professional",
    "🧊",
    "RUSHING DEEZ CATS",
    "voltmatter2",
    "AUGUST 12 2036 THE HEAT DEATH OF THE UNIVERSE",
    "voltmeter killed proglet",
    "Ihatelampadaire",
    "расстрел",
    "https://tryitands.ee",
    "https://media.discordapp.net/attachments/1067491425484296292/1121410297052282931/cat_cat.gif",
    "I declare myself a 600amper power supply unit",
    "im sexually attracted to hydrogen uwu",
    "Tuctdioioeaern",
    "сигма сигма сигма",
    "hog rider attacks!!!!",
    "please do not forget to post cat next 19th date",
    "spider man cowboy 😅😍😄😅😄😊😄🤠🤠🤠",
    "google spread",
    "skull meoji",
    "сюжет очень затягивает, геймплей и графика просто шикарны, постоянно возвращаюсь в эту игру, 10/10",
    "<:p2aperture:1157321484797227108> Aperture Science Sanitizer 564.0.0 Pro Max Ultra Deluxe Bottle Java Edition x86 For Workstations Without SMS And Registration",
    "FRINKIFAIL BAD FRINKIFAIL BAD FRINKIFAIL BA",
    "Be there! Be square!",
    "Tema5002 is a city with the population of 197 million people. It is the capital city of Staring Cat Land.",
    "wamter",
    "the cells moved and i was like wow cool so that was yes play game now",
    "tellurium#8399",
    "Да кто такие эти ваши скибиди туалеты",
    "ампержопа",
    "Competing in пульт от ядерки",
    "https://balls.com/",
    "at the speed of lignt",
    "wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse wouse",
    "ULTRASKILLISSUE",
    "geomeyru dash",
    "HAHA YES I LEAKED ICOSAHEDRON TOKEN",
    "never call me that again stupid nig",
    "waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka",
    "<:ace_flag:1181617159210803330><:ace_flag:1181617159210803330><:ace_flag:1181617159210803330> people from this country are so cool omg",
    "guys lets cook the cake :)",
    "@germancountryball ты играеш в GTA 5",
    "dont go doin drugs kids",
    "Developer Sanity: 47%",
    "Hello hi sir thank",
    "do i really need to live milenakos mods?🤔🤔",
    "speaking fire🗣️🔥🗣️🔥",
    "люди гта 6 вийдет на консось нових поколеня",
    "<:fruit:1187076240612540588><a:arrow:1187076103353925684>"
    ]
# splashes info
splashesinfo=[
    "me", "me",
    "me trying to realise how does disnake work",
    "me", "me", "me", "me", "me",
    "me (cring)",
    "me", "me",
    "guy wanted to help me with splashes and said this so yes",
    "me", "me", "me", "me", "me", 
    "minkos on sillyballs6969420",
    "me",
    "me after biology lesson",
    "who this could possibly be",
    "me", "me",
    "me after fixing ammeter's bugs",
    "me",
    "cube",
    "me", "me",
    "slinx92 somewhere",
    "rusher7629's display name on cat stand",
    "rusher7629 on cat stand",
    "me after calling ammeter antimatter",
    "me",
    "me after playing worms armageddon",
    "me", "me", "me", "me", "me", "me", 
    "crs25001 was saying something spamming and i copied first several symbols",
    "me", "me", "me",
    "me and slinx92",
    "someone",
    "me",
    "someone in steam reviews on sharex",
    "me", "me",
    "me after mc live 2023 trailer",
    "slinx92",
    "astroleaf in lampadaire's steam profile",
    "nathancrazy's review on cell machine indev",
    "me",
    "someone in telegram",
    "slinx92",
    "the teleporter cell's rich presence",
    "me",
    "cube on slinx's attic",
    "someone on cell machine server",
    "nicejs's status",
    "mileankos's review on geometry dash",
    "ME BEING INSANE",
    "slinx muting bobmaster69",
    "someone on cat stand",
    "me",
    "me (all asexuals are obsessed with cakes there is no exceptions)",
    "maranw on proglet software",
    "random mari0 mappack",
    "cmmm+ splash",
    "someone silly on pinterest",
    "itamar_nudge on milenakos mods in advertisement",
    "sushi2627 on cat stand #memes",
    "this video description: https://youtu.be/lM_qJsAvujg",
    "me"
    ]

sillyis=[
    "tried to say",
    "should touch grass instead of saying",
    "should kys after saying",
    "is that silly so said",
    "didnt want to be normal and said",
    "is definiely motherless because he said",
    "dont be an idiot and stop saying",
    "maybe have dementia if he said"
    ]

@bot.event
async def on_ready():
    print(f"@{bot.user} is now online")

    print("setting presence")
    idiots=0
    for every in bot.guilds:
        idiots+=every.member_count
        print(f"{idiots} people... ({every.member_count} people from {every.name})")
    await bot.change_presence(status=disnake.Status.online,activity=disnake.Game(f"with {idiots} idiots on {len(bot.guilds)} servers"))
    print("presence changed")
    
    while True:
        print("\n")
        h=open("splashes_channels.txt").read().split()
        for every in h:
            channel=bot.get_channel(int(every))
            if channel!=None:
                await channel.send(choice(splashes))
                print(f"sending splash on {channel} ({channel.guild})")
            else:
                print("cant send splash 💀💀💀")
                with open("splashes_channels.txt",'w') as splasheschannels:
                    for everything in h:
                        if everything!=every:
                            splasheschannels.write(f"{everything}\n")
        print("\n")
        await asyncio.sleep(150)

# sends message on proglet software when someone joins
@bot.event
async def on_member_join(member):
    if member.guild==bot.get_guild(1132235625609834596):
        guildn=bot.get_guild(1132235625609834596)
        members=0
        bots=0
        for every in guildn.members:
            if every.bot: bots+=1
            else: members+=1
        
        embed=disnake.Embed(
        title=f"{member.name}#{member.discriminator} has joined!",
        description=f"we now have `{bots+members}` total members!!!\n({bots} bots and {members} members)",color=0x00ffff)
        embed.set_image(url=(member.avatar.url))
        
        channel=bot.get_channel(1132236506698883082)
        await channel.send(embed=embed)

# sends message on proglet software when someone leaves
@bot.event
async def on_member_remove(member):
    if member.guild==bot.get_guild(1132235625609834596):
        channel=bot.get_channel(1132236506698883082)
        await channel.send(member.mention +" gone <:picardia_dead:1132754518237532260>")

# button of mute tema5002 + save files listener
@bot.listen("on_button_click")
async def help_listener(ctx):
    if ctx.component.custom_id=="kys":
        await ctx.send("<:kysmen:1160939083011469393>", ephemeral=True)
    else:
        h = ctx.component.custom_id
        embed=makeembed(int(h), os.listdir("shitpost"))
        await ctx.response.edit_message(embed=embed, components=makecomponents(embed.title))

@bot.event
async def on_guild_remove(guild):
    channel=bot.get_channel(1183416187326038110)
    try: await channel.send(f"**{guild.owner.name}** пидорас тупой он меня по IP забанил с сервера **{guild.name}** :hugging::hugging::hugging::smiling_face_with_3_hearts::smiling_face_with_3_hearts::exploding_head::relaxed::relaxed::relaxed::kissing_heart::kissing_heart::kissing_heart::heart_eyes::heart_eyes::blush::blush::kissing_closed_eyes::kissing_closed_eyes:")
    except: await channel.send("i got removed from some server which name i dont know")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    balls=message.content.lower()
    if "asexuality is not real" in balls.replace("are","is"):
        await message.reply("amigger and his family 😂😂😀")
        try:
            await message.guild.timeout(message.author, duration=3600, reason="who asked")
        except: pass
    if "asexuality is real" in balls.replace("`",""):
        await message.reply(file=disnake.File("kysNOW.jpg"))

    if message.author.id==553093932012011520:
        await message.reply("заткнись курица😤shut up chicken😡πи$daчек прикрыла😋 (я абослют😈)🙀зткнс крца🤐зоткися курапаточка🙄💅З А Т К Н И С Ь🤫К У Р Е Ц А🐓")
        try:
            await message.guild.timeout(message.author, duration=86400, reason="who asked")
        except: pass

    if message.author.id!=ammeter:

        # slinx's attic messagelogger
        if not message.author.bot:
            channel=bot.get_channel(1174776639939428482)
            if any(_ in message.content for _ in ["<@", "@here", "@everyone", "битбокс баттл с аботмином"]):
                await channel.send("my creator dont allows me to send this")
            elif message.content!="":
                await channel.send(message.content)

        # reply bot's username if message has your username
        if message.author.display_name==message.content:
            await message.channel.send(message.guild.get_member(ammeter).display_name)
        if message.guild.get_member(ammeter).display_name==message.content:
            if "<@" in message.author.display_name or "@here" in message.author.display_name or "@everyone" in message.author.display_name:
                await message.channel.send("stupid pingery")
            else:
                await message.channel.send(message.author.display_name.replace("octopus",":octopus:").replace("Octopus",":octopus:"))

        # THOSE WILL BE A FUNCTION ONE DAY
        # @everyo on proglet software
        if f"<@&1146827011403284601>" in balls and not any(_.id==1146827011403284601 for _ in message.author.roles):
            try:
                role=disnake.utils.get(message.guild.roles, name="everyo")
                await message.author.add_roles(role)
                await message.channel.send("Congratulations with your new <@&1146827011403284601> role!")
            except:
                await message.channel.send("for some reason i cant give you that role what the hell man")

        # @evreyeon on ctqa stnad
        if f"<@&1178336783914770442>" in balls and not any(_.id==1178336783914770442 for _ in message.author.roles):
            try:
                role=disnake.utils.get(message.guild.roles, name="evreyeon")
                await message.author.add_roles(role)
                await message.channel.send("Congratulations with your new <@&1178336783914770442> role!")
            except:
                await message.channel.send("for some reason i cant give you that role what the hell man")

        # @eyvriyon on a silly server
        if f"<@&1187758992689209495>" in balls and not any(_.id==1187758992689209495 for _ in message.author.roles):
            try:
                role=disnake.utils.get(message.guild.roles, name="eyvriyon")
                await message.author.add_roles(role)
                await message.channel.send("Congratulations with your new <@&1187758992689209495> role!")
            except:
                await message.channel.send("for some reason i cant give you that role what the hell man")

        # replies :x+1 to :x messages
        if len(balls)>1 and balls[0]==":" and balls[1:].isdigit():
            if balls[1:]=="2":
                await message.channel.send(f":3||{generate_ip(message.author.name)[1:]}||")
            else:
                await message.channel.send(f":{int(balls[1:])+1}")

        # ампержопа
        if balls.startswith("ампержопа скажи"):
            await message.channel.send("не скажу")
        elif "ампержопа помоги"==balls:
            await message.channel.send("ампержопа")
        elif len(balls)>8 and balls[:9]=="ампержопа":
            await message.channel.send(choice([
                "сам ты жопа",
                "зачем я тебе нужен",
                "<:typing:1152504159279530054>⤴️",
                "обратись в aperture sanity sanity centre",
                "ЧТО ТТЕБЕ НАБДО ==ОТСАТИЬНЬ ОТ МЕНЯДьаазЛАЩУПЗАЛЗУ",
                "баба это ты",
                "маруся хуй",
                "почему ты просто не можешь открыть гугл ты что silly",
                "я не ампержопа ты что тупой",
                "ДУ Ю СПИК ИНГЛИШ",
                "да фиг знает",
                "тебе говорить нельзя",
                "иди ка ты знаешь куда",
                "заткнись курица 🐔😂😂😂😔😔😔",
                "ябколко\n"+"<:antaegeav:1184160903512461392>"*10
                ]))
        if balls.startswith("hey siri"):
            await message.channel.send(choice([
                "SIRI NEEDS A WIRELESES CHRAEAGEER AAAAAAAAAAAAAAAAAAAAA",
                "hello i am silly siri",
                "ask icosahedron",
                "you dont.",
                "ампержопа помоги"
            ]))

        # very badly made anti bread good system
        bread=balls
        a=0
        while 2**a<len(balls): a+=1
        bread=bread.replace("\""," ")
        bread=bread.replace("\'"," ") 
        bread=bread.replace(" ","")
        bread=bread.replace("u","o")
        bread=bread.replace("@","a")
        bread=bread.replace("3","e")
        bread=bread.replace("0","o")
        bread=bread.replace("б","b")
        bread=bread.replace("р","r")
        bread=bread.replace("е","e")
        bread=bread.replace("а","a")
        bread=bread.replace("д","d")
        bread=bread.replace("с","c")
        bread=bread.replace("л","l")
        bread=bread.replace("г","g")
        bread=bread.replace("о","o")
        bread=bread.replace("д","d")
        bread=bread.replace("a","e")
        while a!=0:
            bread=bread.replace("bb","b")
            bread=bread.replace("rr","r")
            bread=bread.replace("ee","e")
            bread=bread.replace("dd","d")
            bread=bread.replace("cc","c")
            bread=bread.replace("ll","l")
            bread=bread.replace("gg","g")
            bread=bread.replace("oo","o")
            bread=bread.replace("dd","d")
            a-=1
        bread=bread.replace("cel","")
        if ("bredgod" in bread) and not("bredgodnt" in bread):
            await message.delete()
            await message.channel.send(f"{message.author} {choice(sillyis)} `{message.content}`")
        if any(i in bread for i in ["bredbed","bredgodnt"]):
            await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up


    # replies
    if "`[redacted]`" in balls:
        await message.channel.send("i am going to redact your balls")
    if "hellnaw" in balls.replace(" ",""):
        await message.channel.send(file=disnake.File("KrO95WGn.mp4"))
    if "hey ammeter ask icosahedron to staring cat react you" in balls:
        await message.channel.send("hey icosahedron staring cat react me")
    if message.webhook_id==None and ":antigrav:" in balls and "яблоко" in balls:
        await message.channel.send("ANGITRAV"+"🍎"*randint(22,42))
    if "https://tenor.com/view/who-asked-did-i-ask-i-asked-meme-get-real-gif-21114957"==balls:
        await message.channel.send("real")
    if "<@979669953865216000>" in balls: #@thebreadcell
        await message.channel.send("please kill that nigget")
    if "indev good" in balls:
        await message.reply(generate_ip(message.author.name)) #aperture sanity ip address generator
    if f"<@{ammeter}>" in balls:
        await message.channel.send("hi, it's me")
    if "vvvvvv" in balls:
        await message.channel.send("https://thelettervsixtim.es")
    if "h"==balls:
        await message.channel.send("h "+"<:thubm_up:1152506629879758878>"*randint(1,10))
    if "crazy"==balls:
        await message.channel.send(file=disnake.File("crazygears.jpg"))
    if "microsoft" in balls:
        await message.channel.send("proglet software is better")
    if "1кулон" in balls.replace("один","1").replace(" ",""):
        await message.channel.send("ОДИН КЛОУН ААХАХАХААХАХАХХАХАХАХХАХХАХАХАХАХАХХАХАХАХХААХХА")
    if "hey ammeter this is not a test"==balls:
        await message.channel.send("if this is not a test then why are you asking me this you dum dum")
    if "nothing phone" in balls:
        await message.channel.send("телефон ничего")
    if "gameboy" in balls.replace(" ",""):
        await message.channel.send("игровой мальчик")
    if "that octopus will soon blow up your house" in balls:
        await message.channel.send(file=disnake.File("kreisi_octopus.png"))
    if "google en passant"==balls:
        embed=disnake.Embed(title="En Passant",description="In chess, en passant (French: [ɑ̃ pasɑ̃], lit. \"in passing\") describes the capture by a pawn of an enemy pawn on the same rank and an adjacent file that has just made an initial two-square advance. The capturing pawn moves to the square that the enemy pawn passed over, as if the enemy pawn had advanced only one square.",url="https://en.wikipedia.org/wiki/En_passant")
        embed.set_image(url="https://images-ext-1.discordapp.net/external/Uw9DjUP5Lm1OrOFTIlaEFrSB2_GwJwZ0TkYNipgxY44/https/upload.wikimedia.org/wikipedia/commons/0/09/Ajedrez_animaci%25C3%25B3n_en_passant.gif?width=380&height=380")
        await message.channel.send(embed=embed)
    if "nuh uh"==balls:
        await message.channel.send("yuh uh")
    if ":antigrav:"==message.content:
        await message.reply("test success")
    if "define bitches"==balls:
        await message.channel.send("something you dont have")


    # random reactions
    if message.author.id==1168880756647526531: # good morning bot
        await message.add_reaction(bot.get_emoji(1180517585561849886)) #rolling_eyes_typing

    if "indevbad" in balls.replace("is","").replace(" ",""):
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "i like sashley" in balls:
        await message.add_reaction(bot.get_emoji(1180959241780084787)) #picardia_reading
    if "minkos bad" in balls.replace("lena","n"):
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "cake is clearly better than sex" in balls:
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "do you like shirts" in balls:
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "bread cell is a nig" in balls:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "i have a skill issue" in balls:
        await message.add_reaction(bot.get_emoji(1152501628902060042)) #pointlaugh
    if "fuck you" in balls:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "telgorp" in balls:
        await message.add_reaction(bot.get_emoji(1152501865905389600)) #telgorp
    if "test success"==balls:
        await message.add_reaction(bot.get_emoji(1152504159279530054)) #typing
    if "https://youtu.be/Y1b-Yb4npnU" in message.content:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "nig" in balls:
        await message.add_reaction(bot.get_emoji(1178290417851183117)) #shark_reaction
    if "sillyballs6969420" in balls:
        await message.add_reaction(bot.get_emoji(1152507245540683776)) #sillyballs6969420 
    if "yeh" in balls:
        await message.add_reaction(bot.get_emoji(1180533040871649442)) #yeh
    if "aperture sanity" in balls:
        await message.add_reaction(bot.get_emoji(1181994734957375549)) #sane
    if "i eat kids" in balls:
        await message.add_reaction("😋")
    if "add sex"==balls:
        await message.add_reaction("💀")
    if "bitches" in balls or "bitchless" in balls:
        await message.add_reaction("🥰")
    if "august 12 2036 the heat death of the universe" in balls:
        await message.add_reaction("‼️") #bangbang
    if "amigger" in balls:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat


    # prints all members known to ammeter (PLEASE SOMEONE OPTIMIZE THIS CODE FOR ME THANKS)
    if "hey ammeter this is a test"==balls:
        nuh=[]
        for every in bot.guilds:
            for everyone in every.members:
                h=everyone.name
                if everyone.discriminator!=0:
                    h+=f"#{everyone.discriminator}"
                h+=f" ({everyone.display_name})"
                if everyone.bot: h+=" BOT"
                nuh+=[h]
        nuh=sorted(list(set(nuh)))
        with editfile("silly.txt") as proglet:
            for every in nuh:
                try:
                    proglet.write(every+"\n")
                except:
                    proglet.write("ERROR\n")
        await message.channel.send("Please enjoy this repeats.",file=disnake.File("silly.txt"))


    if "hey ammeter send me all splashes"==balls:
        with editfile("splashes_list.txt") as splist:
            for every in range(len(splashes)):
                splist.write(f"{every+1}/{len(splashes)}.\n")
                try:
                    splist.write(splashes[every])
                except:
                    splist.write("ERROR")
                splist.write("\n\n")
                splist.write(f"credits: {splashesinfo[every]}\n")
                splist.write("_"*20+"\n")
        await message.channel.send(file=disnake.File("splashes_list.txt"))
    if "button of mute tema5002"==message.content:
        await message.channel.send("",components=[disnake.ui.Button(label="Button of kys",style=disnake.ButtonStyle.blurple,custom_id="kys")])


    # "..." gets typing reacted
    if len(balls)>2:
        if balls.endswith("...") and balls.startswith("..."):
            await message.add_reaction(bot.get_emoji(1152504159279530054)) #typing


    # if theres 3 "n't" messages bot kindly asks you to shut the fu
    global counter
    async for message in message.channel.history(limit=3):
        if message.content.lower()=="n't":
            counter+=1
        else: counter=0
    if counter>2:
        await message.channel.send("stfu")


    if message.guild.id==1142510583699226744 and message.author.id==966695034340663367 and ("has appeared!" in message.content):
        await message.channel.send("cat")

# :typing::arrow_left::typing:
@bot.event
async def on_reaction_add(reaction,user):
    if type(reaction.emoji)!=type("str"):
        if reaction.message.author.id==ammeter:
            if reaction.emoji.name=="typing":
                await reaction.message.add_reaction("⬅️")
                await reaction.message.add_reaction(bot.get_emoji(1142453563700817960))

# get useless @someone role on proglet software
@bot.slash_command(name="someone",description="Get \"someone\" role")
async def someone(ctx):
    if ctx.guild.id==1132235625609834596:
        role=disnake.utils.get(ctx.guild.roles, name="someone")
        await ctx.author.add_roles(role)
        await ctx.send("perhaps")
    else:
        await ctx.send("do that here ok\nhttps://discord.gg/Dh8g6UwUN2",ephemeral=True)

@bot.slash_command(name="ping",description="shows ping+updates presence")
async def ping(ctx):
    await ctx.response.defer()
    hh=round(bot.latency*1000)
    if hh>=100000:
        await ctx.send(f"ammeter seriously suffers with {hh}ms ping")
    elif hh>=10000:
        await ctx.send(f"ammeter has serious dementia level with {hh}ms ping")
    elif hh>=1000:
        await ctx.send(f"ammeter has dementia with {hh}ms ping")
    else:
        await ctx.send(f"ammeter is melting tema5002's laptop with {hh}ms ping")

@bot.slash_command(name="say",description="talk as a bot")
async def say(ctx,text:str):
    if ctx.author.id in [tema5002,hexahedron1] or ctx.author.id==ctx.guild.owner_id:
        await ctx.send("ok", ephemeral=True)
        await ctx.channel.send(text)
        print(f"{ctx.author.name} used /say to say\n{text}")
    else:
        await ctx.send("naaah bro this arent yours 💀💀💀💀",ephemeral=True)

@bot.slash_command(name="upload_avatar",description="upload someone's avatar as an emoji (NOT WORKING)")
@commands.has_permissions(manage_emojis=True)
async def upload_avatar(ctx, member:disnake.Member, name:str):
    if len(name)<3: await ctx.send("emoji name must be at least 2 characters long",ephemeral=True)
    else:
        embed=disnake.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} uploaded {member.name}#{member.discriminator}'s avatar as a :{name}: emoji")
        embed.set_image(url=(member.avatar.url))
        await ctx.send(embed=embed)
        await ctx.guild.create_custom_emoji(name=name, url=(member.avatar.url), reason=f"User {ctx.author} uploaded emoji {name} through ammeter")

@bot.slash_command(name="file",description="send files as a bot")
async def file(ctx,file: disnake.Attachment):
    if ctx.author.id in [tema5002,hexahedron1] or ctx.author.id==ctx.guild.owner_id:
        await ctx.send("ok", ephemeral=True)
        await ctx.channel.send(file=await file.to_file())
    else:
        await ctx.send("naaah bro this arent yours 💀💀💀💀",ephemeral=True)

@bot.slash_command(name="info",description="info")
async def info(ctx):
    embed=disnake.Embed(title="Ammeter",color=0x00FFFF,description=
        f"very bad bot made by tema5002\n\nthanks to \n**slinx92**\n**thebreadcell** (dont ask)\n\n"+
        "join [mileankso mods](https://discord.gg/WCTzD3YQEk) or i will do uhhhh idk")
    await ctx.send(embed=embed)

@bot.slash_command(name="stats",description="stats")
async def stats(ctx):
    idiots=0
    record=0
    for every in bot.guilds:
        idiots+=every.member_count
        if every.member_count>record:
            h=every.name
            record=every.member_count
    embed=disnake.Embed(title="amigger stats",color=0x00FFFF,description=
        f"{len(bot.guilds)} servers and {idiots} servers"+
        f"{len(splashes)} splashes currently\n"+
        f"biggest server is **{h}** with **{record}** members")

@bot.slash_command(name="splashes",description="sends splash")
async def sendsplash(ctx,id:int):
    id-=1
    hh=len(splashes)
    if 0<=id<hh:
        embed=disnake.Embed(title=f"splash №{id+1}/{hh}",description=splashes[id])
    else:
        id=randint(0,hh-1)
        embed=disnake.Embed(title=f"here is your random splash (№{id+1}/{hh})",description=splashes[id])
    footer_dict={"text": splashesinfo[id]}
    embed.set_footer(**footer_dict)
    await ctx.send(embed=embed)

@bot.command()
async def death(ctx):
    if ctx.author.id==tema5002:
        await ctx.send(file=disnake.File("metal_pipe_falling_sound.mp3"))
        exit()
    else:
        await ctx.send("perm issue",delete_after=3.0)

@bot.command()
async def test(ctx):
    if ctx.author.id==tema5002:
        await ctx.send("hello ammeter please make this command work")
    else:
        await ctx.send("perm issue",delete_after=3.0)

@bot.slash_command(name="hautocorrect",description="hHautocorrects hYour hMessahes")
async def hautocorrect(ctx,hinput:str):
    hinput=hinput.replace("g","h")
    hinput=hinput.replace("G","H")
    await ctx.send(hAutoCorrect(hinput))

@bot.slash_command(name="serious_buisness_application",description="defenitely will find use for sanitizers names")
async def insanity(ctx, something: str):
    await ctx.send(bsgenerator(something))

@bot.slash_command(name="wikipedia_search",description="Search for something on wikipedia")
async def search(ctx,search):
    await ctx.response.defer()
    try:
        page = wikipedia.page(search, auto_suggest=False) # auto suggest is false but it wont work anyway???????
        embed=disnake.Embed(
            title=page.title,
            description=wikipedia.summary(search, sentences=3),
            url=page.url)
        embed.set_image(url=page.images[0])
        await ctx.send(embed=embed)
    except:
        try:
            page = wikipedia.page(search, auto_suggest=True)
            embed=disnake.Embed(
                title=page.title,
                description=wikipedia.summary(search, sentences=3))
            embed.set_image(url=page.images[0])
            await ctx.send(embed=embed)
        except:
            await ctx.send(f"{search} is fake")

@bot.slash_command(name="wikipedia_searches",description="test command :typing:")
async def searches(ctx,search):
    await ctx.response.defer()
    h=wikipedia.search(search)
    if h==[]: await ctx.send("empty :typignr:e")
    else:
        uhhh=""
        for every in h:
            uhhh+=f"- {every}\n"
        await ctx.send(embed=disnake.Embed(
            title=f"\"{search}\" search results",
            description=uhhh))

@bot.slash_command(name="rate",description="meter something in the unit of electric current")
async def rate(ctx, something: str):
    message=f"i would rate **{something}** "
    if something.lower()=="asexuality":
        message+="11 amperes! "+"<:kreisi_ampere:1181984050156687452>"*11
    else:
        if something[1:].replace('s','')==" ampere" and something[0].isdigit():
            h=int(something[0])
        else: h=randint(0,5)
        if h==1: message+="1 ampere! <:ampere:1181978287677915306>"+"<:no_ampere:1181978300462149642>"*4
        elif h==0 or 2<=h<=4: message+=f"{h} amperes! "+"<:ampere:1181978287677915306>"*h+"<:no_ampere:1181978300462149642>"*(5-h)
        elif h==5: message+="5 amperes! "+"<:grass_ampere:1181978296695664650>"*5
        else: message="im planning to add achievements so yes live with this here"
    await ctx.send(message)

@bot.slash_command(name="send_splash_here",description="make ammeter send splashes here on start (OWNER ONLY)")
async def send_splash_here(ctx):
    if ctx.guild.owner_id==ctx.author.id or ctx.author.id==tema5002:
        h=open("splashes_channels.txt").read().split()
        if str(ctx.channel.id) in h:
            with open("splashes_channels.txt",'w') as splasheschannels:
                for every in h:
                    if int(every)!=ctx.channel.id:
                        splasheschannels.write(f"{every}\n")
            await ctx.send(f"**#{ctx.channel}** was removed from splashes channels list ❌")
        else:
            with open("splashes_channels.txt",'w') as splasheschannels:
                for every in h:
                    splasheschannels.write(f"{every}\n")
                splasheschannels.write(str(ctx.channel.id))
            await ctx.send(f"**#{ctx.channel}** was added to splashes channels list ✅")
    else:
        await ctx.send("you are not a server owner ‼️",ephemeral=True)

@bot.slash_command(name="file_data", description="Returns information about an attached file")
async def file_data_handler(ctx, file: disnake.Attachment):

    embed = disnake.Embed(title="File Data", color=0x00FF00)

    filename = file.filename
    size = file.size
    url = file.url
    content_type = file.content_type
    duration = file.duration
    waveform = file.waveform

    embed.add_field(name="Filename",       value=filename)
    embed.add_field(name="Size",           value=f"{size} bytes")
    embed.add_field(name="Content Type",   value=content_type)
    embed.add_field(name="URL",            value=url, inline = False)
    if duration != None:
        embed.add_field(name="Duration",   value=f"{duration} seconds")
    if waveform != None:
        embed.add_field(name="Waveform",   value=waveform)

    await ctx.send(embed=embed)

save_file_cooldowns = {} # dictionary to store save_file user cooldowns

@bot.slash_command(name="save_file", description="saves file to a folder on my laptop")
async def file_saver(ctx, file: disnake.Attachment, filename: str):
    await ctx.response.defer()
    if file.size > 4*1024*1024:
        await ctx.send(f"this file weights more than **4** MB! (~**{math.ceil(file.size/1024)}** KB)")
    else:

        now = datetime.datetime.now()
        last_used = save_file_cooldowns.get(ctx.author.id)

        if last_used is not None:
            # time since last use
            when_used = (now - last_used).total_seconds()

            if when_used < 60:
                await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {round(60 - when_used)} seconds", ephemeral=True)
                return

        save_file_cooldowns[ctx.author.id] = now

        if "." in file.filename:
            filepath = get_file_path("shitpost", filename+file.filename[file.filename.rfind("."):])
        else:
            filepath = get_file_path("shitpost", filename)
        try:
            await file.save(filepath)
            await ctx.send(f"File saved successfully as '{filepath}'.")
            channel=bot.get_channel(1187779030892675193)
            await channel.send(f"**{ctx.author.name}** `{ctx.author.id}` added next file:\n{filename}")
        except Exception as e:
            await ctx.send(f"An error occurred while saving the file: {e}")

@bot.slash_command(name="list_files", description="lists all files saved with /save_file")
async def list_files(ctx):
    embed=makeembed(1, os.listdir("shitpost"))
    await ctx.send(embed=embed, components=makecomponents(embed.title))

send_file_cooldowns = {} # dictionary to store save_file user cooldowns

@bot.slash_command(name="send_file", description="sends any file saved using with /save_file")
async def send_file(ctx, filename: str):
    await ctx.response.defer()
    if not filename in os.listdir("shitpost"):
        await ctx.send(f"file `{filename}` doesnt exist", ephemeral=True)
    else:
        now = datetime.datetime.now()
        last_used = save_file_cooldowns.get(ctx.author.id)

        if last_used is not None:
            # time since last use
            when_used = (now - last_used).total_seconds()

            if when_used < 20:
                await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {round(20 - when_used)} seconds", ephemeral=True)
                return

        save_file_cooldowns[ctx.author.id] = now
        await ctx.send(filename, file=disnake.File(get_file_path("shitpost", filename)))

bot.run(open("TOKEN.txt").read())
