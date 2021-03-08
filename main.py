import discord
import json
import time
import random
from discord.ext import commands
from discord.ext .commands import has_permissions
from discord.utils import get
from Reping import Reping

client = commands.Bot(command_prefix=('!'))
client.remove_command("help")

@client.event
async def on_ready():
    print('Tá online')
    print('Hacked_TV | Bot online!\n------------------------\nBot feito por Hacked_TV\n------------------------' + '{0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='BOT RESETADO'))
    time.sleep(2)
    await client.change_presence(activity=discord.Game(name='4KR>>ALL'))

@client.command()
@commands.has_permissions(administrator=True)
async def adv(ctx, user: discord.Member, *, motivo):
    await user.send("Você foi advertido, caso tenha um explicação para retirar sua advertencia, fale com algum superior!")
    channel=client.get_channel(808874427474247720)
    await channel.send(f"**ADVERTENCIA:**\n\n**Membro:** {user.name}\n**Motivo:** {motivo}")

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
    guild=ctx.guild
    await member.kick()
    await ctx.send('Membro retirado!')
    await member.send(f'Você foi retirado do server {guild.name}.')

@client.command()
@commands.has_permissions(administrator=True)
async def stsr(ctx):
  stsrem=discord.Embed(title='Reset!', description='O command e o historico de **!sts** foi resetado.')
  await ctx.send(embed=stsrem)
  await client.change_presence(activity=discord.Game(name='4KR>>ALL'))

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, user: discord.Member, *, reason=None):
  guild=ctx.guild
  muterole=discord.utils.get(guild.roles, name="Muted")
  await user.remove_roles(muterole, reason=reason)
  emd=discord.Embed(
    title="DESMUTADO",
    description=f"Você foi desmutado **{guild.name}**\n**Motivo:** {reason}\n**Desmutado por **{ctx.author.name}."
  )
  await user.send(embed=emd)

@client.command()
@commands.has_permissions(administrator=True)
async def sts(ctx, *, stas):
  st=discord.Embed(title='Status Alterados!', description='os status do bot foram alterados para: ' + stas)
  await client.change_presence(activity=discord.Game(name=stas))
  await ctx.send(embed=st)

@client.command()
async def d(ctx, max):
  maxi = float(max)
  nun = random.randint(1, maxi)
  emd=discord.Embed(title='Dice Roll', description=nun)
  await ctx.send(embed=emd)

@client.command()
@commands.has_permissions(administrator=True)
async def anunciar(ctx, *, msg):
  channel = client.get_channel(759886241906556960)
  await channel.send(f"{msg}\n\n||@here||")

@client.command()
@commands.has_permissions(administrator=True)
async def anunciar4kr(ctx, *, msg):
  channel = client.get_channel(808723363043868712)
  ebd=discord.Embed(title="ANUNCIO!", description=f"{msg}")
  await channel.send(embed=ebd)
  await channel.send("||@here||")

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  guild=ctx.guild
  await user.ban(reason=reason)
  await user.send(f'Você foi banido do server {guild.name}\n**Motivo:** {reason}\n**Autor da Punição:** {ctx.author.name}')
  channel=client.get_channel(771907616262586368)
  await channel.send(f"Ban!\n**Nick:** {user.name}\n**Motivo:** {reason}\n**Autor da punição:** {ctx.author.name}")

@client.command()
async def ajuda(ctx):
  aj=discord.Embed(title="Commands", description=f"**!d**: Gira o dado em um numero de 1 ao numero especificado.\n\n**!cvt**: manda 1 convite ao seu privado!")
  await ctx.send(f"{ctx.author.mention}", embed=aj)

@client.command()
@commands.has_permissions(administrator=True)
async def info(ctx, user: discord.Member):
  await ctx.author.send(f'Usuario: {user}\nid: {user.id}\n')

@client.command()
@commands.has_permissions(administrator=True)
async def createtc(ctx, *, channelname):
  guild=ctx.guild
  await guild.create_text_channel(name=f"{channelname}")
  await ctx.send(f"Channel Created!\n**NAME:** {channelname}")

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member, *, motivo):
    guild=ctx.guild
    muterole=discord.utils.get(guild.roles, name="Muted")
    channel=client.get_channel(771907616262586368)
    embed=discord.Embed(
        title="MUTE!",
        description=f"**Nick:** {user.name}\n**Motivo:** {motivo}\n**Autor da punição:** {ctx.author.name}"
    )
    emd=discord.Embed(
      title="MUTED",
      description=f"Você foi mutado do server **{guild.name}**\n**Motivo:** {motivo}\n**Autor da Punição:** {ctx.author.name}\n\nFaça uma revisão em (EM BREVE)"
    )
    await user.add_roles(muterole, reason=motivo)
    await channel.send(embed=embed)
    await user.send(embed=emd)

@client.command()
@commands.has_permissions(administrator=True)
async def deletechannel(ctx, *, channel: discord.TextChannel):
  await channel.delete()
  await ctx.send(f"Channel Deleted!\n**NAME:** {channel}")

@client.command()
async def cvt(ctx):
  user=ctx.author
  await user.send("discord.gg/yr2DpHk7SJ")

Reping()
f = open('token.json')
token = json.load(f)['token']
client.run(token)