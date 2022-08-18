import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ui import Button, View, Select

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")


class Cog(commands.Cog):
    def __init__(self, client):
        self.client: commands.bot = client

    @discord.slash_command(
        guild_ids=[GUILD_ID],
        description="Example command",
    )
    async def example(self, ctx):
        embed = discord.Embed(title="Example", color=0x00FF00)
        embed.add_field(name="Hello", value="World", inline=False)
        await ctx.respond(embed=embed, view=None, ephemeral=True)


def setup(client):
    client.add_cog(Cog(client))
