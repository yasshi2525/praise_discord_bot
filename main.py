import os
import re
import random
import logging
import discord

# 環境変数からトークンを読み込み
TOKEN = os.environ["DISCORD_TOKEN"]

# ログ設定
logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter(
    "%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# クライアント作成
client = discord.Client()

# パターンのコンパイル
prog = re.compile(r"(\S+?)[、。　\s]?(?:がんばった|頑張った)[!！。]?$")

# 褒め方一覧
praiseSigns = ["！", "❗", "♡", "💓", "☆", "★", "🌟"]
praiseComments = ["えらい", "エラい", "かっこいい", "素敵", "ステキ", "いい子", "イイ子", "なで", "ナデ"]


@client.event
async def on_ready():
    print("{0.user} としてログインしました".format(client))


@client.event
async def on_message(message: discord.Message):
    # 自身のメッセージには反応しない
    if message.author == client.user:
        return
    result = prog.match(message.content)
    if result:
        sign = random.choice(praiseSigns)
        comment = random.choice(praiseComments)
        msg = "{0}さん、{1}がんばったね！{2}{3}{2}{3}".format(
            message.author.name, result.group(1), comment, sign)
        await message.channel.send(msg)

client.run(TOKEN)
