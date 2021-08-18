import discord
from discord.ext import commands
from utils.LAS import Lol
from utils.util import roman_to_int

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Encendido')
    print(bot.user.name)

@bot.command()
async def hi(ctx):
    await ctx.send('Hola como estas?')


@bot.command()
async def me(ctx, summoner: str, region: str):
    lol = Lol(summoner, region)
    data = lol.greetings()

    greetings = data['greetings']
    icon_url = data['icon_url']

    emb = discord.Embed(title=greetings)
    emb.set_image(url=icon_url)
    await ctx.send(embed=emb)


@bot.command()
async def soloq(ctx, summoner: str, region: str):
    lol = Lol(summoner, region)
    ranks = lol.rank()

    tier = ranks['tier']
    rank = ranks['rank']
    league_points = ranks['leaguePoints']
    wins = ranks['wins']
    losses = ranks['losses']

    num = roman_to_int(rank)
    url = f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}.png?image=q_auto:best&v=1'

    emb = discord.Embed(title='Clasificatoria SoloQ', description=f'{tier} {rank}')
    emb.set_image(url=url)
    emb.insert_field_at(index=0, name='LP', value=league_points)
    emb.insert_field_at(index=1, name='V', value=wins)
    emb.insert_field_at(index=2, name='L', value=losses)
    await ctx.send(embed=emb)

@bot.command()
async def flex (ctx, summoner: str, region: str):
    lol = Lol(summoner, region)
    ranks = lol.flex()

    tier = ranks['tier']
    rank = ranks['rank']
    league_points = ranks['leaguePoints']
    wins = ranks['wins']
    losses = ranks['losses']

    num = roman_to_int(rank)
    url = f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}.png?image=q_auto:best&v=1'

    emb = discord.Embed(title='Clasificatoria Flex', description=f'{tier} {rank}')
    emb.set_image(url=url)
    emb.insert_field_at(index=0, name='LP', value=league_points)
    emb.insert_field_at(index=1, name='V', value=wins)
    emb.insert_field_at(index=2, name='L', value=losses)
    await ctx.send(embed=emb)






bot.run('ODU5NTU5NjE2MjQwODEyMDQy.YNudRg.FO2cUT561AZs1gwDHQ1AS40AoyU')