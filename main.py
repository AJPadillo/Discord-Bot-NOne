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

#Ejecuta el cliente en el servidor
client.run(os.getenv('TOKEN'))