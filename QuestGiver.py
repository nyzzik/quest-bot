# Quest Giver bot by nyzzik

import asyncio
import discord
from discord.ext import commands
import sqlite3
import math
import time
import questDatabase



prefix: str = 'r-'
pmHelp: bool = True
welcomeChannel: str = ''
bot = commands.Bot(command_prefix=prefix, pm_help=pmHelp)
qb = questDatabase
#roles = ['appretice', 'conjurer', 'archmage', 'crook', 'thief', 'assassin', 'squire', 'knight', 'crusader', 'scout', 'ranger', 'high elf', 'bard', 'druid', 'healer']



apprentice = "408024338806210561"
crook = "407943998670503947"
squire = "407945542836944897"
scout = "408023991740137474"
bard = "408024021981200414"
conjurer = "412450315313348608"
thief = "407940881145135104"
knight = "407945065734995968"
archer = "414927749367726082"
druid = "412450269515874304"
assassin = "407941252571594753"
crusader = "408665976419254282"
high_elf = "408666094241447947"
healer = "408666022623576064"
pyromancer = "407942305614528513"
cryomancer = "414927473633918977"
necromancer = "414927522518663179"
luxmancer = "414927547155873793"
umbramancer = "414927560074592257"
electromancer = "414927493368119300"
juggernaut = "414927608103567361"
paladin = "414927641590628372"
barbarian = "414927671617781761"
rogue = "414927733697544203"
crossbowman = "414927706782826498"
ranger = "407942682200244226"
hunter = "414929143004921877"
beast_master = "414927768770576395"
dark_knight = "414927803327184899"
spell_sword = "414927820951781376"
jester = "414927841789214722"
terramancer = "414927593234759680"


@bot.event
async def on_ready():
    print("ready")
    print("I'm running on " + bot.user.name)
    print("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='r-help', type=0))
    

@bot.event
async def on_server_join(server: discord.Server):
    print(server.default_channel)
    await bot.send_message(server.default_channel, "Hello i am the Quest Giver RPG Bot! Please use r-setup to complete the bot initialization.")
    qb.create_table(server.name)
    server.channels


@bot.command(pass_context=True)
async def setup(ctx):
    await bot.say("")

@bot.event
async def on_member_join(user: discord.Member):
    role = discord.utils.get(user.server.roles, name="new")
    await bot.add_roles(user, role) 
    msg2 = await bot.send_message(bot.get_channel("408009948153249792"), " Welcome "+ user.mention)
    msg = await bot.send_message(bot.get_channel("408009948153249792"), "Choose a class by adding a reaction")    
    #await bot.wait_for_reaction(emoji=,*,user=Member,timeout=None,message=msg,check=None)
    #botmsg = bot.get_message(408009948153249792, id="Welcome")
    #cache_msg = discord.utils.get(bot.messages, id=msg.id)
    await bot.add_reaction(msg, u"\U0001F574")
    await bot.add_reaction(msg, u"\U0001F4B0")
    await bot.add_reaction(msg, u"\u2694")
    await bot.add_reaction(msg, u"\U0001F3F9")
    await bot.add_reaction(msg, u"\U0001F3B8")
    res = await bot.wait_for_reaction([u"\U0001F574", u"\U0001F4B0", u"\u2694", u"\U0001F3F9", u"\U0001F3B8"], user = user, message = msg)
    #bot.send_message("408009948153249792", res.reaction)
    if("{0.reaction.emoji}".format(res) == u"\U0001F574"):
        rolee = discord.utils.get(user.server.roles, name="apprentice")
        await bot.add_roles(user, rolee)
        qb.data_entry(user.id, 0, apprentice)
        #print("success mage")
    elif("{0.reaction.emoji}".format(res) == u"\U0001F4B0"):
        rolee = discord.utils.get(user.server.roles, name="crook")
        await bot.add_roles(user, rolee)
        qb.data_entry(user.id, 0, crook)
        #print("success bard")
    elif("{0.reaction.emoji}".format(res) == u"\u2694"):
        rolee = discord.utils.get(user.server.roles, name="squire")
        await bot.add_roles(user, rolee)
        qb.data_entry(user.id, 0, squire)
        #print("success squire")
    elif("{0.reaction.emoji}".format(res) == u"\U0001F3F9"):
        rolee = discord.utils.get(user.server.roles, name="scout")
        await bot.add_roles(user, rolee)
        qb.data_entry(user.id, 0, scout)
        #print("success crook")
    elif("{0.reaction.emoji}".format(res) == u"\U0001F3B8"):
        rolee = discord.utils.get(user.server.roles, name="bard")
        await bot.add_roles(user, rolee)
        qb.data_entry(user.id, 0, bard)
        #print("success bard")
    role = discord.utils.get(user.server.roles, name="new")
    await bot.remove_roles(user, role)
    await bot.delete_message(msg)
    await bot.delete_message(msg2)
    
@bot.event
async def on_member_remove(user: discord.Member):
    qb.delete_user(user.name)
    



@bot.event
async def on_message(message):
    if(message.author.id != "408025638356779008" and message.author.id != "322740024619827211"):
        if(message.channel != bot.get_channel('414228340740718593')):
            if(len(message.content) > 10 and not message.content.startswith("r-") and not message.content.startswith("s-")):    
                qb.user_level_up(message.author.name)
                tempLev = qb.get_user_level(message.author.name)
                temprole = qb.user_get_role(message.author.name)
                # print(temprole)
                # print(message.author.name)
                # print(tempLev)
                if(tempLev == 15):
                    await classCheck(15, temprole, message.author, bot, message.server)
                elif(tempLev == 50):
                    await classCheck(50, temprole, message.author, bot, message.server)
    await bot.process_commands(message)

    message.content.startswith
@bot.command(pass_context=True)
async def rank(ctx):
    await bot.say('Your current level is {}'.format(math.floor(qb.get_user_level(ctx.message.author.name))))

@bot.command(pass_context=True)
async def setclass(ctx, rank):
#your code starts here:
    team_list = ["apprentice", "bard", "squire", "crook", "scout"]
    #entered_team = ctx.message.content[6:].lower()
    role = discord.utils.get(ctx.message.server.roles, name=rank)
    roles = [
        # IDs of the roles for the teams
        "408024338806210561",
        "407943998670503947",
        "407945542836944897",
        "408023991740137474",
        "408024021981200414"
    ]
    for r in ctx.message.author.roles:
        if r.id in roles:
            # If a role in the user's list of roles matches one of those we're checking
            rolemsg = await bot.send_message(ctx.message.channel, "You already have a class role. If you want to switch, message a moderator.")
            time.sleep(5)
            bot.delete_message(rolemsg)
            return
    if role is None or role.name not in team_list:
        # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
        stuffmsg = await bot.send_message(ctx.message.channel, "Class doesn't exist. Classes that do are `apprentice`, `bard`, `squire`, `crook` and `scout`.")
        time.sleep(5)
        bot.delete_message(stuffmsg)
        return
    elif role in ctx.message.author.roles:
        # If they already have the role
        testmsg = await bot.send_message(ctx.message.channel, "You already have this role.")
        time.sleep(5)
        bot.delete_message(testmsg)
    else:
        try:
            await bot.add_roles(ctx.message.author, role)
            msg = await bot.send_message(ctx.message.channel, "Successfully added role {0}".format(role.name))
            qb.data_entry(ctx.message.author.name, 0, rank)
            #print(ctx.message.author.name)
            time.sleep(5)
            bot.delete_message(msg)
        except discord.Forbidden:
            errormsg = await bot.send_message(ctx.message.channel, "I don't have perms to add roles.")
            time.sleep(5)
            bot.delete_message(errormsg)

@setclass.error
async def setclass_on_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        msg = await bot.send_message(ctx.message.channel, "you messed up try again")
        time.sleep(3)
        await bot.delete_message(msg)
        await bot.delete_message(ctx.message)
    else:
        print(error)
        print(commands.MissingRequiredArgument)
        await bot.send_message(ctx.message.author, "ehh")

async def classCheck(level, role, user: discord.Member, bot, server):
    while True:
        try:
            if(level == 15):
                if(role == "apprentice"):
                    role = discord.utils.get(user.server.roles, name='Conjurer')
                    await bot.add_roles(user, role)
                    # print('success')
                elif(role == "crook"):
                    role = discord.utils.get(user.server.roles, name='Thief')
                    await bot.add_roles(user, role)
                elif(role == "squire"):
                    role = discord.utils.get(user.server.roles, name='Knight')
                    await bot.add_roles(user, role)
                elif(role == "scout"):
                    role =  discord.utils.get(user.server.roles, name='Archer')
                    await bot.add_roles(user, role)
                elif(role == "bard"):
                    role = discord.utils.get(user.server.roles, name='Druid')
                    await bot.add_roles(user, role)

            elif(level == 50):
                if(role == "apprentice"):
                    await bot.add_roles(user, discord.utils.get(server.roles, name='temp'))
                    stif = await bot.send_message(bot.get_channel("418164625763205122"), "{}! Which class do you want, Pyromancer, Cryomancer, Necromancer, Electromancer, or Terramancer?".format(user.mention))
                    msg = await bot.wait_for_message(author=user, channel=bot.get_channel("418164625763205122"))
                    if(msg.content.lower().title() == "Pyromancer"):
                        role = discord.utils.get(server.roles, name='Pyromancer')
                    elif(msg.content.lower().title() == "Cryomancer"):
                        role = discord.utils.get(server.roles, name='Cryomancer')
                    elif(msg.content.lower().title() == "Necromancer"):
                        role = discord.utils.get(server, name='Necromancer')
                    elif(msg.content.lower().title() == "Electromancer"):
                        role = discord.utils.get(server.roles, name='Electromancer')
                    elif(msg.content.lower().title() == "Terramancer"):
                        role = discord.utils.get(server.roles, name='Terramancer')
                    elif(msg.content.lower().title() == "Luxmancer"):
                        role = discord.utils.get(server.roles, name='Luxmancer')
                    elif(msg.content.lower().title() == "Umbramancer"):
                        role = discord.utils.get(server.roles, name='Umbramancer')
                    elif(msg.content.lower().title() == "Light and dark" and user.id == "171395218258657281"):
                        role1 = discord.utils.get(server.roles, name='Umbramancer')
                        role = discord.utils.get(server.roles, name='Luxmancer')
                        await bot.add_roles(user, role1)
                    await bot.add_roles(user, role)
                    await bot.delete_message(msg)
                    await bot.delete_message(stif)
                elif(role == "crook"):
                    stif = await bot.send_message(bot.get_channel("418164625763205122"), "Which class do you want, Assassin or Rogue")
                    msg = await bot.wait_for_message(author=user, channel=bot.get_channel("418164625763205122"))
                    if(msg.content.lower() == "assassin"):
                        role = discord.utils.get(user.server.roles, name='assassin')
                    elif(msg.content.lower() == "rogue"):
                        role = discord.utils.get(user.server.roles, name='rogue')
                    #elif(msg.content.lower() == "necromancer"):
                    # role = discord.utils.get(user.server.roles, name='necromancer')
                    await bot.add_roles(user, role)
                elif(role == "squire"):
                    stif = await bot.send_message(bot.get_channel("418164625763205122"), "Which class do you want, Paladin, Juggernaut, Barbarian, Electromancer, or Terramancer?")
                    msg = await bot.wait_for_message(author=user, channel=bot.get_channel("418164625763205122"))
                    if(msg.content.lower().title() == "Paladin"):
                        role = discord.utils.get(user.server.roles, name='Paladin')
                    elif(msg.content.lower().title() == "Juggernaut"):
                        role = discord.utils.get(user.server.roles, name='Juggernaut')
                    elif(msg.content.lower().title() == "Necromancer"):
                        role = discord.utils.get(user.server.roles, name='Barbarian')
                    await bot.add_roles(user, role)
                elif(role == "scout"):
                    role = discord.utils.get(user.server.roles, name='high elf')
                    await bot.add_roles(user, role)
                elif(role == "bard"):
                    role = discord.utils.get(user.server.roles, name='healer')
                    await bot.add_roles(user, role)
                await bot.remove_roles(user, discord.utils.get(server.roles, name='temp'))
            break
        except:
            await bot.delete_message(msg)
            await bot.delete_message(stif)
            continue
bot.run(token.token)
