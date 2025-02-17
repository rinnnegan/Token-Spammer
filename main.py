import discord
from discord.ext import commands
import pyfiglet
from rich import print
import json
import asyncio

def tokens_del_jsonxd(archivo='tokens.json'):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("[bold red]Error: No se encontró el archivo tokens.json[/bold red]")
        return []

async def enviar_mensaje(token, guild_id, canal):
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    
    cliente = discord.Client(intents=intents)
    
    @cliente.event
    async def on_ready():
        try:
            guild = cliente.get_guild(guild_id)
            if not guild:
                print(f"[bold red]Error: El ID de servidor {guild_id} no es válido.[/bold red]")
                await cliente.close()
                return

            await canal.send("Token Spammer By Lissan\nJoin Now! https://discord.com/invite/Lissan")
            print(f"[bold green]Mensaje enviado a {canal.name} con el token {token[:4]}***[/bold green]")
        except Exception as e:
            print(f"[bold red]Error enviando mensaje: {e}[/bold red]")
        finally:
            await cliente.close()
    
    await cliente.start(token)
  
async def main():
    print(pyfiglet.figlet_format("Token Spammer"))
    
    try:
        guild_id = int(input("Ingresa la ID del servidor: "))
    except ValueError:
        print("[bold red]Error: La ID del servidor debe ser un número válido.[/bold red]")
        return

    tokens = tokens_del_jsonxd()
    if not tokens:
        return
    
    cantidad_mensajes = int(input("Ingresa la cantidad de mensajes a enviar: "))
    
    intents = discord.Intents.default()
    cliente = discord.Client(intents=intents)

    @cliente.event
    async def on_ready():
        guild = cliente.get_guild(guild_id)
        if not guild:
            print(f"[bold red]Error: El ID {guild_id} no es válido.[/bold red]")
            await cliente.close()
            return
        
        canales_texto = guild.text_channels[:cantidad_mensajes]
        
        for token, canal in zip(tokens, canales_texto):
            await enviar_mensaje(token, guild_id, canal)
            await asyncio.sleep(1)  
        
        await cliente.close()
    
    await cliente.start(tokens[0])

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
