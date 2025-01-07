import discord
import os
import requests
import json
import sqlite3
import random
from dotenv import load_dotenv

load_dotenv() # Cargar las variables de entorno del archivo .env

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

conn = sqlite3.connect("encouragements.db")
cursor = conn.cursor()

def initialize_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS encouragements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT
    )
    """)
    conn.commit()

def add_encouragement(message):
    cursor.execute("INSERT INTO encouragements (message) VALUES (?)", (message,)) #Agregar mensaje de ánimo
    conn.commit()

def list_encouragements():
    cursor.execute("SELECT message FROM encouragements") #Listar los mensajes de ánimo
    return [row[0] for row in cursor.fetchall()]

def remove_encouragement(message):
    cursor.execute("DELETE FROM encouragements WHERE message = ?", (message,)) #Eliminar mensaje de ánimo
    conn.commit()

def get_random_encouragement():
    cursor.execute("SELECT message FROM encouragements ORDER BY RANDOM() LIMIT 1") #Obtener mensaje de ánimo aleatorio
    result = cursor.fetchone()
    return result[0] if result else None

def get_quote():
    response = requests.get('https://zenquotes.io/api/random') #Obtener una cita de API
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote

initialize_db() # Inicializar la base de datos y llenar mensajes iniciales si están vacíos
starter_encouragements = ['Cheer up!', 'Hang in there.', 'You are a great person / bot!']
if not list_encouragements():
    for msg in starter_encouragements:
        add_encouragement(msg)

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

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

    if any(word in message.content.lower() for word in sad_words):
        encouragement = get_random_encouragement()
        if encouragement:
            await message.channel.send(f'{message.author.mention} {encouragement}')

    if message.content.startswith('$add '):
        new_message = message.content[5:].strip()
        add_encouragement(new_message)
        await message.channel.send(f'Encouragement added: {new_message}')

    if message.content.startswith('$list'):
        encouragements = list_encouragements()
        if encouragements:
            await message.channel.send("Encouragements:\n" + "\n".join(encouragements))
        else:
            await message.channel.send("No encouragements found.")

    if message.content.startswith('$remove '):
        remove_message = message.content[8:].strip()
        remove_encouragement(remove_message)
        await message.channel.send(f'Removed encouragement: {remove_message}')

client.run(os.getenv('TOKEN')) # Ejecutar el cliente de Discord
