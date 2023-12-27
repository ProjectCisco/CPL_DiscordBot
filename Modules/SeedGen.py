import nextcord
import random

from .abcModule import abcModule
from exc import BotException

class SeedGenModule(abcModule):
    def __init__(self, client):
        super().__init__(client)
        self.commands = {"mapseed": self.cmd_seed}

    async def cmd_seed(self, *args, channel, member, message, **_):
        try:
            combined_game_name = 'for ' + ' '.join(args) if args else ""
            map_seed = str(random.randint(-(2**31), (2**31)-1))
            embed = nextcord.Embed(
                title=f"Random Map Seed {combined_game_name}",
                description=map_seed,
                color=0xF85252
            )

            await message.channel.send(embed=embed)

        except Exception as e:
            # Handle exceptions or errors
            raise BotException(f"An error occurred: {e}")