from typing import Optional

import discord
from discord.ext import commands
from discord import app_commands
import discord.utils

class BanCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ban", aliases=["b"])
  async def ban_prefix(self, ctx, member: discord.Member = None, length: Optional[int] = 0):    
    if not member:
      embed = Discord.embed(
          title="Error: No member specified",
          description="You cannot ban thin air. Please mention a user or their ID.\n\n **Did you mean?**\n> $ban @user/ID time",
          color=discord.Color.orange(),
      )
      embed.set_footer(text=f"User: {ctx.author}", )
      return
