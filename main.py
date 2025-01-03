import discord
import os
import requests
import json

from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Crear un objeto Intents
intents = discord.Intents.default()
intents.message_content = True  # Habilitar el acceso al contenido de los mensajes

client = discord.Client(intents=intents)

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
    'Cheer up!',
    'Hang in there.',
    'You are a great person / bot!'
]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in message.content for word in sad_words):
        await message.channel.send(f'{message.author.mention} {random.choice(starter_encouragements)}')

#Ejecuta el cliente en el servidor
client.run(os.getenv('TOKEN'))