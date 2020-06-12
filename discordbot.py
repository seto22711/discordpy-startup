from discord.ext import commands
import os
import traceback
import random

# さいころの和を計算する用の関数
# from func import  diceroll

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# ユーザー作成コマンド
@bot.command()
def __init__(self, bot):
        self.bot = bot

async def dice(self, ctx, max: int = 6):
        rand = random.randrange(max) + 1
        if max == 6:
            await ctx.send(file=discord.File('images/dice_{}.png'.format(rand)))
        else:
            await ctx.send(rand)

    @dice.error
    async def dice_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('引数は整数で！')

def setup(bot):
    bot.add_cog(UsefulCog(bot))

    
@bot.command()
async def ping(ctx):
    await ctx.send('pang')
    
#@bot.event
#async def on_message(message):
#    if message.author.bot:
#        return
#    if message.content.startswith("/dice"):
        # 入力された内容を受け取る
#        say = message.content 

#        await ctx.send(say)
        
        # [/dice ]部分を消し、AdBのdで区切ってリスト化する
#        order = say.strip('/dice ')
#        cnt, mx = list(map(int, order.split('d'))) # さいころの個数と面数
#        dice = diceroll(cnt, mx) # 和を計算する関数(後述)
#        await message.channel.send(dice[cnt])
#        del dice[cnt]

        # さいころの目の総和の内訳を表示する
#        await message.channel.send(dice)


bot.run(token)
