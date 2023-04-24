from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import discord
import os
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-fullscren")
# options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-features=site-per-process")
driver = webdriver.Chrome(options=options)
driver.get("https://store.epicgames.com/pt-BR")
jogosGratis = driver.find_elements(By.CLASS_NAME, 'css-5auk98')
mensagens = []
for jogo in jogosGratis:
    if "GRÁTIS" in str(jogo.text):
        nomeJogo = jogo.text.split("\n")[1]
        linkJogo = jogo.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        mensagem = "Jogo gratuito: "+nomeJogo+"\n"+"Link: "+str(linkJogo)
        mensagens.append(mensagem)

print(mensagens)

# Substitua o ID do canal pelo ID do canal em que você deseja enviar a mensagem
channel_id = 1080950286002167910

# Substitua o token pelo token do seu bot
token = os.getenv("TOKEN")


intents = discord.Intents.default()  # habilita as intenções padrão (todas exceto as privadas)
intents.members = True  # habilita a intenção de membros
client = discord.Client(intents=intents)  # passa as intenções ao criar o objeto Client

@client.event
async def on_ready():
    print('Bot está online!')
    channel = client.get_channel(channel_id)
    for msg in mensagens:
        print(msg)
        await channel.send(msg)

client.run(token)