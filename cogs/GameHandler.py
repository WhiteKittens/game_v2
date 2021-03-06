# import discord
# from discord.ext.commands import bot
#
# from enums.GameControls import GameControls
# from model.Player import Player
# from view.PrintHandler import PrintHandler
#
#
# class GameHandler:
#     x = PrintHandler()
#     e = discord.Embed()
#
#     def __init__(self, sample_bot):
#         self.msg = None
#         self.msg_screen = None
#         self.ctx = None
#         self.player = None
#         self.sample_bot = sample_bot
#
#     @bot.command(pass_context=True)
#     async def start(self, ctx):
#         self.ctx = ctx
#         self.player = Player(ctx.message.author.id)
#         await self.init_image()
#         self.msg_screen = await self.ctx.bot.say(".")
#         await self.login_screen()
#
#     async def login_screen(self):
#         if not self.player.player_has_character():
#             await self.ctx.bot.edit_message(self.msg_screen, self.x.print_file("WELCOME_SCREEN", self.ctx))
#             emoji = await self.wait_on_control(GameControls.SWORDS.value[0])
#             if emoji == GameControls.SWORDS.value[0]:
#                 self.player.create_character(self.ctx.message.author.display_name)
#                 await self.login_screen()
#         else:
#             welcome = self.x.open("CHARACTER_SELECTION")
#             response = await self.x.get_print_options(welcome, self.player.get_characters(), self, self.ctx)
#             if response is None:
#                 self.player.create_character(self.ctx.message.author.display_name)
#                 await self.login_screen()
#             else:
#                 self.player.set_current_character(response)
#         await self.wait_on_control(GameControls.all_emojis())
#
#
#         return None
#
#     async def init_image(self):
#         self.e.set_image(
#             url="https://cdn.discordapp.com/attachments/501831331035086861/506085028392992768/DarkForest.png")
#         self.msg = await self.ctx.bot.send_message(self.ctx.message.channel, embed=self.e)
#         await self.set_controls()
#
#     async def set_controls(self):
#         for smiley in list(GameControls):
#             await self.ctx.bot.add_reaction(self.msg, smiley.value[0])
#
#     async def change_background(self, url):
#         self.e.set_image(url=url)
#         await self.ctx.bot.edit_message(self.msg, embed=self.e)
#
#     async def get_ctx(self):
#         return self.ctx
#
#
# def setup(sample_bot):
#     sample_bot.add_cog(GameHandler(bot))
