import discord
import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Crear un objeto Intents
intents = discord.Intents.default()
intents.message_content = True  # Habilitar el acceso al contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#Ejecuta el cliente en el servidor
client.run(os.getenv('TOKEN'))