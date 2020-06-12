from discord.ext import commands
import os
import traceback

# さいころの和を計算する用の関数
from func import  diceroll

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pang')
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("/dice"):
        # 入力された内容を受け取る
        say = message.content 

        await ctx.send(say)
        
        # [/dice ]部分を消し、AdBのdで区切ってリスト化する
        order = say.strip('/dice ')
        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
        await message.channel.send(dice[cnt])
        del dice[cnt]

        # さいころの目の総和の内訳を表示する
        await message.channel.send(dice)


bot.run(token)
