# Discord Encouragement Bot - NOne

Este es un bot de Discord diseñado para enviar mensajes de ánimo a los usuarios y compartir citas inspiradoras. Usa una base de datos SQLite para almacenar mensajes personalizados y una API externa para generar citas motivadoras.

## Funcionalidades

- **Mensajes de ánimo aleatorios:** Responde con un mensaje positivo si detecta palabras tristes en el chat.
- **Citas inspiradoras:** Usa el comando `$inspire` para obtener una cita aleatoria de [ZenQuotes API](https://zenquotes.io).
- **Gestión de mensajes de ánimo personalizados:**
  - `$add <mensaje>`: Añade un nuevo mensaje de ánimo.
  - `$list`: Lista todos los mensajes de ánimo.
  - `$remove <mensaje>`: Elimina un mensaje de ánimo existente.

---

## Requisitos previos

1. **Python 3.8 o superior**: Asegúrate de tener Python instalado en tu sistema.
2. **Dependencias**: Instala las siguientes bibliotecas usando `pip`:
   - `discord.py`: Manejo de la API de Discord.
   - `requests`: Para interactuar con ZenQuotes API.
   - `python-dotenv`: Para cargar variables de entorno desde un archivo `.env`.
3. **Archivo `.env`**: Crea un archivo `.env` con tu token de bot de Discord:

   ```env
   TOKEN=tu_token_de_discord

## Instalación

1. Clona este repositorio en tu máquina local.
   ```bash
   git clone https://github.com/AJPadillo/Discord-Bot-NOne.git
   cd Discord-Bot-NOne
2. Instala las dependencias.
   ```bash
   pip install -r requirements.txt
3. Crea la base de datos SQLite para los mensajes de ánimo.
   ```bash
   touch encouragements.db
4. Ejecuta el bot.
   ```bash
   python main.py

## Uso

- Invita al bot a tu servidor de Discord utilizando un enlace generado en el [Portal de Desarrolladores de Discord](https://discord.com/developers/applications).
- Usa los comandos disponibles directamente en cualquier canal de texto donde esté el bot.

## Comandos disponibles

- **`$inspire`**: Devuelve una cita motivadora obtenida de la API de ZenQuotes.
- **`$add [mensaje]`**: Agrega un nuevo mensaje de ánimo personalizado a la base de datos.
- **`$list`**: Muestra una lista de todos los mensajes de ánimo almacenados.
- **`$remove [mensaje]`**: Elimina un mensaje específico de la base de datos.

## Personalización

El bot permite personalizar las siguientes funcionalidades:

1. **Mensajes de ánimo**:
   - Puedes agregar tus propios mensajes motivadores usando el comando `$add [mensaje]`.
   - Para eliminar mensajes que ya no sean relevantes, utiliza `$remove [mensaje]`.

2. **Palabras clave de tristeza**:
   - Edita la lista `sad_words` en el código fuente para ajustar las palabras que el bot reconoce como indicadores de tristeza. Ejemplo:
     ```python
     sad_words = ['triste', 'deprimido', 'enojado', 'desesperado']
     ```

3. **Mensajes iniciales**:
   - Modifica la lista `starter_encouragements` para agregar mensajes predeterminados al inicio:
     ```python
     starter_encouragements = ['¡Ánimo!', 'Tú puedes con esto.', 'Eres increíble.']
     ```

## Tecnologías utilizadas

Este proyecto fue desarrollado utilizando las siguientes tecnologías y herramientas:

- **[Python](https://www.python.org/)**: Lenguaje de programación principal del bot.
- **[Discord.py](https://discordpy.readthedocs.io/)**: Biblioteca para interactuar con la API de Discord.
- **[SQLite](https://www.sqlite.org/)**: Base de datos ligera para almacenar los mensajes de ánimo.
- **[Requests](https://docs.python-requests.org/)**: Biblioteca para realizar solicitudes HTTP.
- **[ZenQuotes API](https://zenquotes.io/)**: API utilizada para obtener citas motivadoras.
- **[Dotenv](https://pypi.org/project/python-dotenv/)**: Manejo de variables de entorno de forma segura.

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Consulta el archivo [`LICENSE`](./LICENSE) para más detalles.
