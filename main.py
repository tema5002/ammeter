# i absolutely have no idea what am i doing

import disnake, wikipedia, asyncio, math, os, datetime, pickle
from disnake.ext import commands
from random import choice, randint
from defenitely_something import bsgenerator
from temalib import *
from ACHS import *
from embed_lists_maker import *

bot=commands.Bot(command_prefix="hey ammeter ",help_command=None,intents=disnake.Intents.all())

# i store user ids here
hexahedron1=801078409076670494
tema5002=558979299177136164
ammeter=811569586675515433

achs = pickle.load(open("achs.dat", "rb"))

splashes = pickle.load(open("splashes.dat", "rb"))
splashesinfo = pickle.load(open("splashesinfo.dat", "rb"))

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

async def update_presence():
    idiots=0
    for every in bot.guilds:
        idiots += every.member_count
    await bot.change_presence(status=disnake.Status.online,
                              activity=disnake.Activity(type=disnake.ActivityType.watching,
                              name=f"for {idiots} idiots on {len(bot.guilds)} servers"))

@bot.event
async def on_ready():
    print(f"@{bot.user} is now ready")
    print("loaded slash commands:")
    print("\n".join(f"/{i.name}" for i in bot.slash_commands))
    print("loaded non-slash commands:")
    print("\n".join(f"{bot.command_prefix}{i.name}" for i in bot.commands))
    await update_presence()
    
    while True:
        h=open("splashes_channels.txt").read().split()
        for every in h:
            channel=bot.get_channel(int(every))
            if channel!=None:
                await channel.send(choice(splashes))
                print(f"sending splash on {channel} ({channel.guild})")
            else:
                print(f"cant send splash to channel with id {every}")
                #remove_line("splashes_channels.txt", every)
        print("\n")
        await asyncio.sleep(150)

# sends message on proglet software when someone joins
@bot.event
async def on_member_join(member):
    if member.guild==bot.get_guild(1132235625609834596):
        server=bot.get_guild(1132235625609834596)
        members=0
        bots=0
        for every in guild.server:
            if every.bot: bots+=1
            else: members+=1
        
        embed=disnake.Embed(title=f"{member.name}#{member.discriminator} has joined!",
                            description=f"we now have `{bots+members}` total members!!!\n({bots} bots and {members} members)",color=0x00ffff)
        embed.set_image(url=member.avatar.url)
        
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
    h = ctx.component.custom_id
    t = h.split(";")
    if t==["kys"]:
        await ctx.send("<:kysmen:1160939083011469393>", ephemeral=True)
        await ctx.send(embed = giveach("clearly a skill issue", ctx.author))
        return
    elif t[0]=="UPDATELISTEMBED":
        page_to_go = int(t[1])
        files = os.listdir("shitpost")
        embed=make_list_embed(int(t[1]), files)
        await ctx.response.edit_message(embed=embed, components=make_list_components(page_to_go, len(files)))

@bot.event
async def on_guild_remove(guild):
    channel=bot.get_channel(1183416187326038110)
    try: await channel.send(f"**{guild.owner.name}** пидорас тупой он меня по IP забанил с сервера **{guild.name}** :hugging::hugging::hugging::smiling_face_with_3_hearts::smiling_face_with_3_hearts::exploding_head::relaxed::relaxed::relaxed::kissing_heart::kissing_heart::kissing_heart::heart_eyes::heart_eyes::blush::blush::kissing_closed_eyes::kissing_closed_eyes:")
    except: await channel.send("i got removed from some server which name i dont know")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    msg = message.content
    msgl = msg.lower()

    h = str(message.author.id)+".txt"
    if h in os.listdir("scrl"):
        react = False
        h = open(get_file_path(__file__, "scrl", h)).readline()
        if h == "3":
            react = True
        elif h in ["1", "2"]:
            online = is_online(message.guild, 1030817797921583236) #icosahedron
            if h == "1":
                online = online or is_online(message.guild, 1055396314403311616) #abotmin
            if not online:
                react = True
        if react: await message.add_reaction(bot.get_emoji(1068922981197287464))

    if randint (0, 2000) == 0:
        await message.channel.send(embed = giveach("Luck 100", message.author))
    if msgl.startswith("hey ammeter add tag ") or msgl.startswith("hey ammeter remove tag "):
        await message.channel.send(embed = giveach("Wrong bot", message.author))
    
    if "asexuality is not real" in msgl:
        await message.reply("я найду тебя и разобью твой ебальник 😊😊😊😊😊😊")
        try:
            await message.guild.timeout(message.author, duration=3600, reason="who asked")
        except: pass
    if "asexuality is real" in msgl.replace("`",""):
        await message.reply(file=disnake.File(get_file_path(__file__, "src", "kysNOW.jpg")))
        await message.channel.send(embed = giveach("Asexual Supporter", message.author))

    if message.author.id==553093932012011520:
        await message.reply("заткнись курица😤shut up chicken😡πи$daчек прикрыла😋 (я абослют😈)🙀зткнс крца🤐зоткися курапаточка🙄💅З А Т К Н И С Ь🤫К У Р Е Ц А🐓")
        try:
            await message.guild.timeout(message.author, duration=86400, reason="who asked")
        except: pass

    if message.author.id!=ammeter:
        # reply bot's username if message has your username
        if message.author.display_name==message.content:
            await message.channel.send(message.guild.get_member(ammeter).display_name)
        if message.guild.get_member(ammeter).display_name==message.content:
            if "<@" in message.author.display_name or "@here" in message.author.display_name or "@everyone" in message.author.display_name:
                await message.channel.send("stupid pingery")
            else:
                await message.channel.send(message.author.display_name.replace("octopus",":octopus:").replace("Octopus",":octopus:"))
                if message.author.display_name=="битбокс баттл с аботмином":
                    await message.channel.send(embed = giveach("Beatbox", message.author))

        for role_id, role_name in [(1146827011403284601, "everyo"),
                                   (1178336783914770442, "evreyeon"),
                                   (1187758992689209495, "eyvriyon")]:
            if f"<@&{role_id}>" in msgl and not any(_.id==role_id for _ in message.author.roles):
                try:
                    role=disnake.utils.get(message.guild.roles, name=role_name)
                    await message.author.add_roles(role)
                    await message.channel.send(f"Congratulations with your new <@&{role_id}> role!")
                except:
                    await message.channel.send("for some reason i cant give you that role what the hell man")

        # replies :x+1 to :x messages
        if len(msgl)>1 and msgl[0]==":" and msgl[1:].isdigit():
            if msgl[1:]=="2":
                await message.channel.send(f":3||{generate_ip(message.author.name)[1:]}||")
            else:
                await message.channel.send(f":{int(msgl[1:])+1}")

        # ампержопа
        if msgl.startswith("ампержопа скажи"):
            await message.channel.send("не скажу")
        elif "ампержопа помоги"==msgl:
            await message.channel.send("ампержопа")
        elif "ампержопа ты тут?"==msgl:
            await message.channel.send(f"я не ты тут? я {message.guild.get_member(ammeter).display_name}")
        elif len(msgl)>8 and msgl[:9]=="ампержопа":
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
        if msgl.startswith("hey siri"):
            await message.channel.send(choice([
                "SIRI NEEDS A WIRELESES CHRAEAGEER AAAAAAAAAAAAAAAAAAAAA",
                "hello i am silly siri",
                "ask icosahedron",
                "you dont.",
                "ампержопа помоги"
            ]))

    #    # very badly made anti bread good system
    #    bread=msgl
    #    a=0
    #    while 2**a<len(msgl): a+=1
    #    bread=bread.replace("\""," ")
    #    bread=bread.replace("\'"," ") 
    #    bread=bread.replace(" ","")
    #    bread=bread.replace("u","o")
    #    bread=bread.replace("@","a")
    #    bread=bread.replace("3","e")
    #    bread=bread.replace("0","o")
    #    bread=bread.replace("б","b")
    #    bread=bread.replace("р","r")
    #    bread=bread.replace("е","e")
    #    bread=bread.replace("а","a")
    #    bread=bread.replace("д","d")
    #    bread=bread.replace("с","c")
    #    bread=bread.replace("л","l")
    #    bread=bread.replace("г","g")
    #    bread=bread.replace("о","o")
    #    bread=bread.replace("д","d")
    #    bread=bread.replace("a","e")
    #    while a!=0:
    #        bread=bread.replace("bb","b")
    #        bread=bread.replace("rr","r")
    #        bread=bread.replace("ee","e")
    #        bread=bread.replace("dd","d")
    #        bread=bread.replace("cc","c")
    #        bread=bread.replace("ll","l")
    #        bread=bread.replace("gg","g")
    #        bread=bread.replace("oo","o")
    #        bread=bread.replace("dd","d")
    #        a-=1
    #    bread=bread.replace("cel","")
    #    if ("bredgod" in bread) and not("bredgodnt" in bread):
    #        await message.delete()
    #        await message.channel.send(f"{message.author} {choice(sillyis)} `{message.content}`")
    #    if any(i in bread for i in ["bredbed","bredgodnt"]):
    #        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    elif msgl=="битбокс баттл с аботмином": await message.channel.send("АЛИСА ПОМОГИ ЧТО ЭТОТ ДЕБИЛ ХОЧЕТ ОТ МЕНЯ")

    # replies
    if "`[redacted]`" in msgl:
        await message.channel.send("i am going to redact your balls")
    if "hellnaw" in msgl.replace(" ",""):
        await message.channel.send(file=disnake.File(get_file_path(__file__, "src", "KrO95WGn.mp4")))
    if "hey ammeter ask icosahedron to staring cat react you" in msgl:
        await message.channel.send("hey icosahedron staring cat react me")

    if message.webhook_id==None:
        for emoji, text, reply, char in [(":antigrav:",  "яблоко",   "ANGITRAV",    "🍎"),
                                          (":antaegeav:", "ябколко",  "ANTIRAGRABA", "🍏"),
                                          (":anitgrva:",  "ялобобко", "AGNINGRATA",  "🍍")]:
            if emoji in msgl and text in msgl:
                await message.channel.send(reply+char*randint(22,42))

    if "https://tenor.com/view/who-asked-did-i-ask-i-asked-meme-get-real-gif-21114957"==msgl:
        await message.channel.send("real")
    #if "<@979669953865216000>" in msgl: #@thebreadcell
    #    await message.channel.send("please kill that nigget")
    if "indev good" in msgl:
        await message.reply(generate_ip(message.author.name)) #aperture sanity ip address generator
    if f"<@{ammeter}>" in msgl:
        await message.channel.send("hi, it's me")
    if "vvvvvv" in msgl:
        await message.channel.send("https://thelettervsixtim.es")
    if "h"==msgl:
        await message.channel.send("h "+"<:thubm_up:1152506629879758878>"*randint(1,10))
    if "crazy"==msgl:
        await message.channel.send(file=disnake.File(get_file_path(__file__, "src", "crazygears.jpg")))
    if "microsoft" in msgl:
        await message.channel.send("proglet software is better")
    if "1кулон" in msgl.replace("один","1").replace(" ",""):
        await message.channel.send("ОДИН КЛОУН ААХАХАХААХАХАХХАХАХАХХАХХАХАХАХАХАХХАХАХАХХААХХА")
    if "hey ammeter this is not a test"==msgl:
        await message.channel.send("if this is not a test then why are you asking me this you dum dum")
    if "nothing phone" in msgl:
        await message.channel.send("телефон ничего")
    if "gameboy" in msgl.replace(" ",""):
        await message.channel.send("игровой мальчик")
    if "that octopus will soon blow up your house" in msgl:
        await message.channel.send(file=disnake.File(get_file_path(__file__, "src", "kreisi_octopus.png")))
    if "google en passant"==msgl:
        embed=disnake.Embed(title="En Passant",description="In chess, en passant (French: [ɑ̃ pasɑ̃], lit. \"in passing\") describes the capture by a pawn of an enemy pawn on the same rank and an adjacent file that has just made an initial two-square advance. The capturing pawn moves to the square that the enemy pawn passed over, as if the enemy pawn had advanced only one square.",url="https://en.wikipedia.org/wiki/En_passant")
        embed.set_image(url="https://images-ext-1.discordapp.net/external/Uw9DjUP5Lm1OrOFTIlaEFrSB2_GwJwZ0TkYNipgxY44/https/upload.wikimedia.org/wikipedia/commons/0/09/Ajedrez_animaci%25C3%25B3n_en_passant.gif?width=380&height=380")
        await message.channel.send(embed=embed)
    if "nuh uh"==msgl:
        await message.channel.send("yuh uh")
    if ":antigrav:"==msg:
        await message.reply("test success")
    if "define bitches"==msgl:
        await message.channel.send("something you dont have")
    if msg.isdigit() and 8<=len(msg)<=100:
        await message.channel.send(f"{msg} is a wuggy numbers 😂😂😂😂😂")


    if message.author.id==1168880756647526531: # good morning bot
        await message.add_reaction(bot.get_emoji(1180517585561849886)) #rolling_eyes_typing
    if msgl=="да":
        await message.add_reaction(bot.get_emoji(1195762346153488384)) #DA

    if "indevbad" in msgl.replace("is","").replace(" ",""):
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "i like sashley" in msgl:
        await message.add_reaction(bot.get_emoji(1180959241780084787)) #picardia_reading
    if "minkos bad" in msgl.replace("lena","n"):
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "cake is clearly better than sex" in msgl:
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "do you like shirts" in msgl:
        await message.add_reaction(bot.get_emoji(1152506629879758878)) #thubm_up
    if "bread cell is a nig" in msgl:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "i have a skill issue" in msgl:
        await message.add_reaction(bot.get_emoji(1152501628902060042)) #pointlaugh
    if "fuck you" in msgl:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "telgorp" in msgl:
        await message.add_reaction(bot.get_emoji(1152501865905389600)) #telgorp
    if "test success"==msgl:
        await message.add_reaction(bot.get_emoji(1152504159279530054)) #typing
    if "https://youtu.be/Y1b-Yb4npnU" in message.content:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat
    if "nig" in msgl:
        await message.add_reaction(bot.get_emoji(1178290417851183117)) #shark_reaction
    if "sillyballs6969420" in msgl:
        await message.add_reaction(bot.get_emoji(1152507245540683776)) #sillyballs6969420 
    if "yeh" in msgl:
        await message.add_reaction(bot.get_emoji(1180533040871649442)) #yeh
    if "aperture sanity" in msgl:
        await message.add_reaction(bot.get_emoji(1181994734957375549)) #sane
    if "@germancountryball ты играеш в gta 5" in msgl:
        await message.add_reaction(bot.get_emoji(1189619015556022404))
    if "i eat kids" in msgl:
        await message.add_reaction("😋")
    if "add sex"==msgl:
        await message.add_reaction("💀")
    if "bitches" in msgl or "bitchless" in msgl:
        await message.add_reaction("🥰")
    if "august 12 2036 the heat death of the universe" in msgl:
        await message.add_reaction("‼️")
    if "amigger" in msgl:
        await message.add_reaction(bot.get_emoji(1152501238785638491)) #staring_cat


    # prints all members known to ammeter (PLEASE SOMEONE OPTIMIZE THIS CODE FOR ME THANKS)
    if "hey ammeter this is a test"==msgl:
        nuh=[]
        for every in bot.guilds:
            for everyone in every.members:
                nuh += get_username(user, display_name=True, bot=True)
        nuh=sorted(list(set(nuh)))
        with editfile(get_file_path(__file__, "temp", "silly.txt")) as proglet:
            for every in nuh:
                try:
                    proglet.write(every+"\n")
                except:
                    proglet.write("ERROR\n")
        await message.channel.send("Please enjoy this repeats.",
                                   file=disnake.File(get_file_path(__file__, "temp", "silly.txt")))


    elif "hey ammeter send me all splashes"==msgl:
        with editfile(get_file_path(__file__, "temp", "splashes_list.txt")) as splist:
            for every in range(len(splashes)):
                splist.write(f"{every+1}/{len(splashes)}.\n")
                try:
                    splist.write(splashes[every])
                except:
                    splist.write("ERROR")
                splist.write("\n\n")
                splist.write(f"credits: {splashesinfo[every]}\n")
                splist.write("_"*20+"\n")
        await message.channel.send(file=disnake.File(get_file_path(__file__, "temp", "splashes_list.txt")))
    if "button of mute tema5002"==message.content:
        await message.channel.send("", components=[disnake.ui.Button(label="Button of kys",style=disnake.ButtonStyle.blurple,custom_id="kys")])


    # "..." gets typing reacted
    if len(msgl)>2:
        if msgl.endswith("...") and msgl.startswith("..."):
            await message.add_reaction(bot.get_emoji(1152504159279530054)) #typing
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if len(message.content)==1:
        if message.content.lower() in alphabet:
            index=alphabet.find(msgl)
            await message.add_reaction("🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿"[index])
        
    #if msgl == "hey ammeter start flowmeter":
    #    if bot.get_guild(1042064947867287643).get_member(1184192159944028200).status == disnake.Status.offline:
    #        os.startfile("C:\\Users\\User\\Documents\\folder without name\\discord bort\\flowmeter\\main.py")
    #        await message.channel.send("<:thubm_up:1096323451985334363>")
    #    else:
    #        await message.channel.send("flowmeter is already online you dum dujm")
        
    #elif msgl == "hey ammeter start ctqa bto":
    #    if bot.get_guild(1042064947867287643).get_member(1174011590559928330).status == disnake.Status.offline:
    #        os.startfile("C:\\Users\\User\\Documents\\folder without name\\discord bort\\ctqa bto\\main.py")
    #        await message.channel.send("<:thubm_up:1096323451985334363>")
    #    else:
    #        await message.channel.send("ctqa bto is already online you silly")

    if msgl == "hey ammeter start ammeter":
        await message.add_reaction(bot.get_emoji(1196526737048227850))

    elif "start ammeter" in msgl:
        await message.add_reaction(bot.get_emoji(1145359652691923085))


    # if theres 3 "n't" messages bot kindly asks you to shut the fu
    global counter
    async for msge in message.channel.history(limit=3):
        if msge.content.lower()=="n't":
            counter+=1
        else: counter=0
    if counter>2:
        await message.channel.send("stfu")

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
    if hh>=25000:
        await ctx.send(f"FUCKING FUCK IT HAS {hh}MS PING")
    elif hh>=10000:
        await ctx.send(f"hell naw how is {hh}ms ping possible")
    elif hh>=5000:
        await ctx.send(f"ammeter somehow fails to work even more with {hh}ms ping")
    elif hh>=2500:
        await ctx.send(f"ammeter seriously suffers to work with {hh}ms ping")
    elif hh>=1000:
        await ctx.send(f"ammeter has SERIOUS dementia level with {hh}ms ping")
    elif hh>=500:
        await ctx.send(f"ammeter has dementia with {hh}ms ping")
    else:
        await ctx.send(f"ammeter is melting tema5002's laptop with {hh}ms ping")
    if hh>=500:
        await ctx.send(embed = giveach("AMMETER HAS DEMENTIA", ctx.author))
    await update_presence()

@bot.slash_command(description="talk as a bot")
async def say(ctx, text: str = "", reply_to: str = None, file: disnake.Attachment = None):

    if not(ctx.author.id==tema5002 or ctx.author.id==ctx.guild.owner_id):
        await ctx.send("naaah bro this arent yours 💀💀💀💀", ephemeral=True)
        return

    if reply_to==None:
        pass
    elif not reply_to.isdigit():
        await ctx.send("enter a digit for `reply_to`.", ephemeral=True)
        return
    else:
        reply_to = bot.get_message(int(reply_to))

    msg = reply_to or ctx.channel
    try:
        await msg.send(text, file=await file.to_file() if file else None)
    except disnake.NotFound:
        await ctx.send("message to reply to not found", ephemeral=True)
        return

    await ctx.send("message sent", ephemeral=True)

@bot.slash_command(name="upload_avatar",description="upload someone's avatar as an emoji (NOT WORKING)")
@commands.has_permissions(manage_emojis=True)
async def upload_avatar(ctx, member: disnake.Member, name: str):
    if len(name)<3: await ctx.send("emoji name must be at least 2 characters long", ephemeral=True)
    else:
        embed=disnake.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} uploaded {member.name}#{member.discriminator}'s avatar as a :{name}: emoji")
        embed.set_image(url=(member.avatar.url))
        await ctx.send(embed=embed)
        await ctx.guild.create_custom_emoji(name=name,
                                            url=member.avatar.url,
                                            reason=f"User {ctx.author} uploaded emoji {name} through ammeter")

@bot.slash_command(name="info",description="info")
async def info(ctx):
    embed=disnake.Embed(title="Ammeter",color=0x00FFFF,description=
        "very bad bot made by tema5002\n\nthanks to \n**slinx92**\n**thebreadcell** (dont ask)\n\n"+
        "[proglet software](https://discord.gg/gpRkkYjpGR): used for announcements\n"+
        "[a silly server](https://discord.gg/rckcGzxKBR): probably official ammeter server\n"+
        "[my honest reaction](https://discord.gg/SRM7CrSKRT): 99% of all emojis\n"+
        "[Slinx's attic](https://discord.gg/9acZNWYSfN): i test ammeter mostly there")
    await ctx.send(embed=embed)

@bot.slash_command(name="pi_search", description="Search for digits in pi")
async def send_file(ctx, digits: int):
    await ctx.send("this is not added yet <:typing:1133071627370897580>")

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
        await ctx.send(file=disnake.File(get_file_path(__file__, "src", "metal_pipe_falling_sound.mp3")))
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
    except Exception as e1:
        e1=str(e1)
        if len(e1)>150: e1 = e1[:150]+"..."
        try:
            page = wikipedia.page(search, auto_suggest=True)
            embed=disnake.Embed(
                title=page.title,
                description=wikipedia.summary(search, sentences=3),
                url=page.url)
            embed.set_image(url=page.images[0])
            await ctx.send(f"found with one exception:\n{e1}",embed=embed)
        except Exception as e2:
            e2=str(e2)
            if len(e2)>150: e2 = e2[:150]+"..."
            await ctx.send(f"couldn't find {search} with two exceptions:\n\n{e1}\n{e2}")

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

@bot.slash_command(name="rate",description="rate something in the unit of electric current")
async def rate(ctx, something: str):
    message=f"i would rate **{something}** "
    if something.lower()=="asexuality":
        message+="11 amperes! "+"<:kreisi_ampere:1181984050156687452>"*11
    elif something.lower()=="zyzzyzus":
        message=""
        await ctx.send(embed = giveach("Zyzzyzus", ctx.author))
    else:
        if something[1:].replace('s','')==" ampere" and something[0].isdigit():
            h=int(something[0])
        elif something.lower().replace("lena", "n")=="minkos": h = 0

        else: h=randint(0,5)
        if h==1: message+="1 ampere! <:ampere:1181978287677915306>"+"<:no_ampere:1181978300462149642>"*4
        elif h==0 or 2<=h<=4: message+=f"{h} amperes! "+"<:ampere:1181978287677915306>"*h+"<:no_ampere:1181978300462149642>"*(5-h)
        elif h==6:
            message=""
            await ctx.send(embed = giveach("6 Amperes", ctx.author))
        else: message+="5 amperes! "+"<:grass_ampere:1181978296695664650>"*5
    if message!="": await ctx.send(message)

@bot.slash_command(name="achs", description="Lists your achievements")
async def achievements(ctx):
    embed = disnake.Embed(title=f"Achievements ({len(getachs(ctx.author.id))}/{len(achs)})")
    for every in achs:
        if every in getachs(ctx.author.id):
            embed.add_field(name = f"{every.emoji} {every.title}", value = every.description)
        else:
            embed.add_field(name = f"{every.noemoji} {every.title}", value = every.description)
    await ctx.send(embed = embed)

@bot.slash_command(name="send_splash_here",description="make ammeter send splashes here on start (OWNER ONLY)")
async def send_splash_here(ctx):
    if ctx.guild.owner_id in [ctx.author.id, tema5002]:
        h=openfile("splashes_channels.txt").read().split("\n")
        channel_id = str(ctx.channel.id)
        if channel_id in h:
            remove_line("splashes_channels.txt", channel_id)
            await ctx.send(f"**#{ctx.channel}** was removed from splashes channels list ❌")
        else:
            add_line("splashes_channels.txt", channel_id)
            await ctx.send(f"**#{ctx.channel}** was added to splashes channels list ✅")
    else:
        await ctx.send("you are not the server owner ‼️",ephemeral=True)

bot.load_extension("cogs.files")

@bot.slash_command(name="staring_cat_react_me", description="make ammeter staring cat react you")
async def staring_cat_react_me(ctx, h: str):
    if not any(h==_ for _ in "0123"):
        await ctx.send("# staring cat react list parameters\n0 - never\n1 - only when icosahedron and abotmin offline/not on this server\n2 - only when icosahedron offline/not on this server\n3 - always")
    else:
        filepath = get_file_path(__file__, "scrl", str(ctx.author.id)+".txt")
        currenth = openfile(filepath).read()
        if len(currenth)!=1:
            currenth="suprisingly nothing"
        editfile(filepath).write(h)
        await ctx.send(f"your staring_cat_react_me setting was set to **{h}** from **{currenth}**")

#e_count_cooldowns = {}

#@bot.slash_command(name="e_count", description="counts messages for each user in e war channel")
#async def e_count(ctx):
#    await ctx.response.defer()
#    now = datetime.datetime.now()
#    last_used = e_count_cooldowns.get(ctx.author.id)

#    if last_used is not None:
#        # time since last use
#        when_used = (now - last_used).total_seconds()

#        if when_used < 60:
#            await ctx.send(f"this command is on cooldown <:typing:1133071627370897580>\ntry again in {round(60 - when_used)} seconds", ephemeral=True)
#            return
#    e_count_cooldowns[ctx.author.id] = now

#    channel = bot.get_channel(1191694739578298469) # e war
#    e_count = {}
#    async for message in channel.history(limit=None):
#        id = message.author.id
#        if id in e_count:
#            e_count[id] = e_count.get(id) + 1
#        else: e_count[id] = 1

#    description = ""
#    for user, count in e_count.items():
#        try:
#            description += f"- {bot.get_user(user).mention}: {count}\n" 
#        except Exception as e: description += f"epic error {e}"
#    embed = disnake.Embed(description=description[:-1])

#    await ctx.send("e count", embed=embed)

bot.run(open("TOKEN.txt").read())