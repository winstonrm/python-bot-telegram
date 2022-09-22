from asyncio import run
from email.message import Message
from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from lib.cep import cep

load_dotenv()

app = Client(
    'winbotpy1',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

# async def main():
#     await app.start()
#     print("entrou")
#     await app.send_message('winstonnl', 'Olá')
#     await app.stop()

@app.on_message(filters.sticker & filters.private)
async def sticker(client, message):
    await message.reply('Sticker enviado com sucesso')

@app.on_message(filters.voice | filters.audio & filters.private)
async def voice_audio(client, message):
    await message.reply('Não escuto áudios')

@app.on_message(filters.photo & filters.private)
async def photo(client, message):
    await message.reply('Foto enviada com sucesso')

@app.on_message(filters.command('ajuda') & filters.private)
async def ajuda(client, message):
    print(message.chat.username, message.text)
    await message.reply('Mensagem de ajuda')

@app.on_message(filters.command('cep') & filters.private)
async def consulta_cep(client, message):
    print(message.chat.username, message.text)
    await message.reply(cep((message.text)))

@app.on_message(filters.private)
async def messages(client, message: Message):
    print(message.chat.username, message.text)
    await message.reply(message.text)

app.run()