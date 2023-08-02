import discord
from discord.ext import commands
import requests
from flask import Flask, jsonify
app = Flask(__name__)

clients = commands.Bot(command_prefix = "MANEGER_KEY", intents = discord.Intents.all())

Members = []

@clients.event
async def on_ready():
    print("Bot2 is ready")
    print("________________")

@clients.event
async def on_member_join(member):
    channel = clients.get_channel(1132445836492685385)
    game = getattr(member.activity, 'name', None) if member.activity else None
    Members.append(f'Name: {member.name}, Status: {member.status}, Game: {game}' )

@app.route('/members_status', methods = ['GET'])
def get_members_status():
    guild_id = 1132445836492685382
    guild = clients.get_guild(guild_id)
    members_status = []
    for member in guild.members:
        if member.status == discord.status.online:
            game = getattr(member.activity, 'name', None) if member.activity else None
            members_status.append({
                "Name" : member.name,
                "Status" : member.status,
                "Game" : game
            })

if __name__ == "__main__":
    app.run(debug = True)


clients.run('MTEzMjQ0MDQxNDQ1Mjk5NDA2OA.G_PBC4.7BGlBpLutaTbRLAyZY8MBypBUCLVABwgrqd34k')