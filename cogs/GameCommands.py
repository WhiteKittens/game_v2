from discord.ext.commands import bot
from enums.GameControls import GameControls
from model.Equipment import Equipment
from model import Fill


class GameCommands:
    def __init__(self, sample_bot):
        self.sample_bot = sample_bot

    @bot.command(pass_context=True)
    async def start(self, ctx):
        pls = Fill()
        msg = await ctx.bot.say(pls.get_str())
        for smiley in list(GameControls):
            await ctx.bot.add_reaction(msg, smiley.value[0])

        while True:
            reaction = await ctx.bot.wait_for_reaction(user=ctx.message.author)
            if reaction.reaction.emoji == GameControls.SWORDS.value[0]:
                e = Equipment(65, 25)
                await ctx.bot.say(e)


def setup(sample_bot):
    sample_bot.add_cog(GameCommands(bot))

