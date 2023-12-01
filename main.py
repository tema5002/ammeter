# i absolutely have no idea what am i doing

import disnake
from random import choice,randint
from temalib import * # very silly library made by me if you need it then ask :typing:
from disnake.ext import commands

bot=commands.Bot(command_prefix="hey ammeter ",help_command=None,intents=disnake.Intents.all())

# i store user ids here
hexahedron1=801078409076670494
tema5002=558979299177136164
ilovelampadaire=1056952213056004118
ammeter=811569586675515433

# splashes
splashes=[
    "hey picardibot ask ammeter to ask icosahedron to staring cat react him",
    "currently 66 splashes",
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
    "cub is unrotatable cube",
    "prohressnet nowhen",
    "https://prohressnet.xtema5002x.repl.co",
    "https://prohressnet.xtema5002x.repl.co/src/eto_i_est_am_nyam.mp4",
    "i have a fact that will definitely shock you but im not gonna tell it because meh",
    "your mom will be deleted by ammeterhahahahhaha",
    "is team5002 real",
    "owner of this bot sometimes wants to be a jellyfish",
    "i think that kesslonhender better then slinxhender",
    "theres no progresstation and workstahon flag :skull:",
    "slinx's attic is the most silly discord server you DEFINITELY should join!!!!!!!",
    "\"breaking good\" - 💀💀💀\n\nthats a long story",
    "you're*",
    "jsab stands for **j**ust ||**s**illy **a**ss **b**alls||",
    "lets drink to the health of indie developers!!!!",
    "```channel=bot.get_channel(1132240686675136562)\nawait channel.send(choice(splashes))```",
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
    "waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka waka"
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
    print(f"@{bot.user} is real")

    channel=bot.get_channel(1132240686675136562)
    h=5
    while h!=0:
        await channel.send(choice(splashes))
        h-=1

    idiots=0
    for every in bot.guilds:
        idiots+=every.member_count
    await bot.change_presence(status=disnake.Status.online,activity=disnake.Game(f"with {idiots} idiots on {len(bot.guilds)} servers"))

# sends message on mileankso mods when someone joins
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

# sends message on mileankso mods when someone leaves
@bot.event
async def on_member_remove(member):
    if member.guild==bot.get_guild(1132235625609834596):
        channel=bot.get_channel(1132236506698883082)
        await channel.send(member.mention +" gone <:picardia_dead:1132754518237532260>")

# button of mute tema5002 listener
@bot.listen("on_button_click")
async def help_listener(ctx):
    if ctx.component.custom_id=="kys":
        await ctx.send("<:kysmen:1160939083011469393>",ephemeral=True)
    else:
        await ctx.send(f"i have no clue what is this but\n{ctx.component.custom_id}")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    balls=message.content.lower()
    if message.author.id!=ammeter:

        #shat ap
        if randint(1,3)==1:
            if balls=="insanity" or balls=="nuh uh" or "сарказм" in balls:
                h=open("not_shat_ap_servers.txt").read().split() # does not shat aps you if your server in this file
                if not str(message.guild.id) in h:
                    try:
                        await message.guild.timeout(message.author, duration=60, reason="being silly")
                        await message.reply("заткнись курица 🐔🐔🐥👿👿🤓‼️")
                    except:
                        await message.reply("403 not allowed")


        # slinx's attic messagelogger
        if "<@" in message.content or "@here" in message.content or "@everyone" in message.content:
            channel=bot.get_channel(1174776639939428482)
            await channel.send("there was a ping role in this message so yes")
        elif not message.author.bot:
            if message.content=="": pass
            else:
                channel=bot.get_channel(1174776639939428482)
                await channel.send(message.content)
                try: print(f"{message.channel}   ({message.guild.name})   {message.channel.id}")
                except: print(f"{message.channel}")

        # reply bot's username if message has your username
        if message.author.display_name==message.content:
            await message.channel.send(message.guild.get_member(ammeter).display_name)
        if message.guild.get_member(ammeter).display_name==message.content:
            if "<@" in message.author.display_name or "@here" in message.author.display_name or "@everyone" in message.author.display_name:
                await message.channel.send("stupid pingery")
            else:
                await message.channel.send(message.author.display_name.replace("octopus",":octopus:").replace("Octopus",":octopus:"))

        # @everyo on mileankso mods
        if "<@&1146827011403284601>" in balls:
            h=True
            for every in message.author.roles:
                if every.id==1146827011403284601: h=False
            if h:
                try:
                    role=disnake.utils.get(message.guild.roles,name="everyo")
                    await message.author.add_roles(role)
                    await message.channel.send("Congratulations with your new <@&1146827011403284601> role!")
                except:
                    await message.channel.send("for some reason i cant give you that role what the hell man")

        # @evreyeon on ctqa stnad
        if "<@&1178336783914770442>" in balls:
            h=True
            for every in message.author.roles:
                if every.id==1146827011403284601: h=False
            if h:
                try:
                    role=disnake.utils.get(message.guild.roles,name="evreyeon")
                    await message.author.add_roles(role)
                    await message.channel.send("Congratulations with your new <@&1178336783914770442> role!")
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
                "славянский зажим яйцами",
                "заткнись курица 🐔😂😂😂😔😔😔"
                ]))
        if balls.startswith("hey siri"):
            await message.channel.send(choice([
                "SIRI NEEDS A WIRELESES CHRAEAGEER AAAAAAAAAAAAAAAAAAAAA",
                "hello i am silly siri",
                "ask icosahedron"
            ]))

        # very badly made anti bread good system that im gonna remake one day to anti minkos system
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

    if ":antigrav:" in balls and "яблоко" in balls:
        await message.channel.send("ANGITRAV"+"🍎"*randint(22,42))
    if "minkos is a stupid nig".replace("lena","n") in balls:
        await message.channel.send("TRUTH "*64)
    if any(i in balls for i in ["indev bad","indev2 bad","indev is bad"]):
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "minkos bad" in balls.replace("lena","n"):
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "do you like shirts" in balls:
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "hey ammeter ask icosahedron to staring cat react you" in balls:
        await message.channel.send("hey icosahedron staring cat react me")
    if "https://tenor.com/view/who-asked-did-i-ask-i-asked-meme-get-real-gif-21114957"==balls:
        await message.channel.send("real")
    if "bread cell is a nig" in balls:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "i have a skill issue" in balls:
        await message.add_reaction(bot.get_emoji(1152501628902060042)) #pointlaugh
    if "<@979669953865216000>" in balls:
        await message.channel.send("please kill that nigget")          #@thebreadcell
    if "fuck you" in balls:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "telgorp" in balls:
        await message.add_reaction(bot.get_emoji(1152501865905389600)) #telgorp
    if "test success"==balls:
        await message.add_reaction(bot.get_emoji(1152504159279530054)) #typing
    if "indev good" in balls:
        await message.reply(generate_ip(message.author.name))          #ip_adress
    if "minkos good" in balls.replace("lena","n"):
        await message.reply(generate_ip(message.author.name))          #ip_adress
    if "https://youtu.be/Y1b-Yb4npnU" in message.content:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "nig" in balls:
        await message.add_reaction(bot.get_emoji(1178290417851183117)) #shark_reaction
    if "sillyballs6969420" in balls:
        await message.add_reaction(bot.get_emoji(1152507245540683776)) #sillyballs6969420 
    if "add sex"==balls:
        await message.add_reaction("💀")
    if "bitches" in balls or "bitchless" in balls:
        await message.add_reaction("🥰")
    if "<@{ammeter}>" in balls:
        await message.channel.send("did i stutter")
    if "h"==balls:
        await message.channel.send("h "+"<:thubm_up:1152506629879758878>"*randint(1,10))
    if "august 12 2036 the heat death of the universe" in balls:
        await message.add_reaction("‼️")                #bangbang
    if "amigger" in balls:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat

    # prints all members known to ammeter (PLEASE SOMEONE OPTIMIZE THIS CODE FOR ME THANKS)
    if "hey ammeter this is a test"==balls:
        nuh=[]
        for every in bot.guilds:
            for everyone in every.members:
                if everyone.bot:
                    nuh+=[f"{everyone.name}#{everyone.discriminator} ({everyone.display_name}) BOT"]
                else:
                    nuh+=[f"{everyone.name}#{everyone.discriminator} ({everyone.display_name})"]
        nuh=sorted(list(set(nuh)))
        with open("silly.txt","w") as proglet:
            for every in nuh:
                try:
                    proglet.write(every+"\n")
                except:
                    proglet.write("ERROR\n")
        await message.channel.send("Please enjoy this repeats.",file=disnake.File("silly.txt"))

    if "button of mute tema5002"==message.content:
        await message.channel.send("",components=[disnake.ui.Button(label="Button of kys",style=disnake.ButtonStyle.blurple,custom_id="kys")])
    if len(balls)>2:
        if balls.endswith("...") and balls.startswith("..."):
            await message.add_reaction(bot.get_emoji(1152504159279530054)) #typing
    if "crazy"==balls:
        await message.channel.send(file=disnake.File("crazygears.jpg"))
    
    # if theres 3 "n't" messages bot kindly asks you to shut the fu
    global counter
    async for message in message.channel.history(limit=3):
        if message.content.lower()=="n't":
            counter+=1
        else: counter=0
    if counter>2:
        await message.channel.send("stfu")
    
    if type(message.channel)==disnake.channel.DMChannel:
        channel=bot.get_channel(1142460023746867343)
        await channel.send(f"{message.author} ({message.author.id}) says: \n{message.content}")
    
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

# get useless @someone role on mileankso mods 
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
    if randint(1,10)==1:
        hh=randint(100000000,1000000000)
        await ctx.send(f"ammeter is melting tema5002's laptop with {hh}ms ping")
    elif hh>=100000:
        await ctx.send(f"would be funny if ammeter will ever reach this ping\n\n{hh}ms ping")
    elif hh>=10000:
        await ctx.send(f"ammeter has serious dementia level with {hh}ms ping")
    elif hh>=1000:
        await ctx.send(f"ammeter has dementia with {hh}ms ping")
    else:
        await ctx.send(f"ammeter is melting tema5002's laptop with {hh}ms ping")
    idiots=0
    for every in bot.guilds:
        idiots+=every.member_count
    await bot.change_presence(status=disnake.Status.online,activity=disnake.Game(f"with {idiots} idiots on {len(bot.guilds)} servers"))

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
async def upload_avatar(ctx,member:disnake.Member,name:str):
    if len(name)<3: await ctx.send("emoji name must be at least 2 characters long",ephemeral=True)
    else:
        embed=disnake.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} uploaded {member.name}#{member.discriminator}'s avatar as a :{name}: emoji")
        embed.set_image(url=(member.avatar.url))
        await ctx.send(embed=embed)
        await ctx.guild.create_custom_emoji(name,url=(member.avatar.url),reason=f"User {ctx.author} uploaded emoji {name} through \"Ammeter\" bot")

@bot.slash_command(name="file",description="send files as a bot")
async def file(ctx,file: disnake.Attachment):
    if ctx.author.id in [tema5002,hexahedron1,ilovelampadaire] or ctx.author.id==ctx.guild.owner_id:
        await ctx.send("ok", ephemeral=True)
        await ctx.channel.send(file=await file.to_file())
    else:
        await ctx.send("naaah bro this arent yours 💀💀💀💀",ephemeral=True)

@bot.slash_command(name="info",description="info")
async def info(ctx):
    embed=disnake.Embed(title="Ammeter",color=0x00FFFF,description=
        f"very bad bot made by tema5002\n\nthanks to \n**slinx92**\n**thebreadcell** (dont ask)\n\n"+
        f"{len(splashes)} splashes currently\n"+
        "join [mileankso mods](https://discord.gg/WCTzD3YQEk) or i will do uhhhh idk")
    await ctx.send(embed=embed)

@bot.slash_command(name="splashes",description="sends splash")
async def sendsplash(ctx,id:int):
    hh=len(splashes)
    print(hh)
    if 0<id<hh+1:
        await ctx.send(embed=disnake.Embed(title=f"splash №{id}/{hh}",description=splashes[id-1]))
    else:
        h=randint(0,hh)
        await ctx.send(embed=disnake.Embed(title=f"here is your random splash (№{h}/{hh})",description=splashes[h]))

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

bot.run(token)