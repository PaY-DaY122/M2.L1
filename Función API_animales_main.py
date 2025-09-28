import discord
from discord.ext import commands
import random, requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)

animal_APIS = {
    "dog": "https://some-random-api.com/animal/dog",
    "cat": "https://some-random-api.com/animal/cat",
    "panda": "https://some-random-api.com/animal/panda",
    "fox": "https://some-random-api.com/animal/fox",
    "koala": "https://some.random-api.com/animal/koala",
}

def get_random_animal_url():
    animal, url = random.choice(list(animal_APIS.items()))
    res = requests.get(url)
    data = res.json()
    return animal, data["image"]

@bot.command(name="animal")
async def animal(ctx):
    """Muestra una imagen aleatoria de un animal"""
    animal, image_url = get_random_animal_url()
    await ctx.send(f"Aquí tienes una imagen de un {animal}: {image_url}")

bot.run("TU-TOKEN-AQUÍ")
