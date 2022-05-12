async def help(ctx):
  embed=discord.Embed(
  title="The Arsonists Handbook", 
  description="This has all of the bots commands.",
  embed.add_field(name="/Help", value="Shows the following message.", inline=False)
  embed.add_field(name="/Ping", value="Bot Latency Meter.", inline=False)
  embed.add_field(name="/Invite", value="Sends a bot invite to add the bot to your server (In DM).", inline=False)
  embed.add_field(name="/Molotov", value="Burns up to 500 channel messages at a time.", inline=False)
  embed.add_field(name="/Burn", value="COMMING SOON", inline=False)
  embed.add_field(name="/Lockdown", value="COMMING SOON", inline=False)
  embed.set_footer(text="Bot By LAB-W", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
  color=0xFF5733)
  await ctx.send(embed=embed) 

@slash.slash(name= 'Invite', description='Invite the bot to your own server!')
async def invite(ctx):
  embed=discord.Embed(
  title="Invite Me!", url="https://discord.com/api/oauth2/authorize?client_id=797181865630629938&permissions=4228902135&scope=applications.commands%20bot", description="Click above to invite me to your own server!", 
  color=0xFF5733)
  await ctx.send(embed=embed)