import discord
import os
import requests
import json
import sqlite3
import random

from dotenv import load_dotenv

load_dotenv() # Cargar las variables de entorno del archivo .env

intents = discord.Intents.default()
intents.message_content = True  # Habilitar el acceso al contenido de los mensajes

client = discord.Client(intents=intents)

conn = sqlite3.connect("encouragements.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS encouragements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT
)
""")
conn.commit()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
    'Cheer up!',
    'Hang in there.',
    'You are a great person / bot!'
]

cursor.execute("SELECT COUNT(*) FROM encouragements")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO encouragements (message) VALUES (?)",
                       [(msg,) for msg in starter_encouragements])
    conn.commit()

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote

def get_random_encouragement():
    cursor.execute("SELECT message FROM encouragements ORDER BY RANDOM() LIMIT 1") #Obtener un mensaje de ánimo aleatorio desde la base de datos.
    return cursor.fetchone()[0]

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

    if message.content.startswith('$add '):
        new_message = message.content[5:].strip() #Crear un nuevo mensaje de ánimo
        cursor.execute("INSERT INTO encouragements (message) VALUES (?)", (new_message,))
        conn.commit()
        await message.channel.send(f'Encouragement added: {new_message}')
    
    if message.content.startswith('$list'): #Listar todos los mensajes de ánimo
        cursor.execute("SELECT message FROM encouragements")
        all_encouragements = cursor.fetchall()
        formatted = "\n".join([msg[0] for msg in all_encouragements])
        await message.channel.send(f"Encouragements:\n{formatted}")
    
    if message.content.startswith('$remove '): #Eliminar un mensaje de ánimo
        remove_message = message.content[8:].strip()
        cursor.execute("DELETE FROM encouragements WHERE message = ?", (remove_message,))
        conn.commit()
        await message.channel.send(f'Removed encouragement: {remove_message}')

#Ejecuta el cliente en el servidor
client.run(os.getenv('TOKEN'))