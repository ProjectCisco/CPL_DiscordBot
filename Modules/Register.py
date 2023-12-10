import nextcord
import platform
import aiohttp

from config import OAUTH_LINK_BASE, WELCOME_CHANNEL, NEW_REGISTERED_LOG_CHANNEL, ROLES_WHEN_REGISTED, SMURF_IDENTIFIER_LOG_CHANNEL, MOD_CONTACT_CHANNEL
from utils import moderator_command
from .abcModule import abcModule

class SmurfHunter:
    def __init__(self, discord_id):
        self.discord_id = discord_id
        self.build_number = self.get_windows_build_number()

    def get_windows_build_number(self):
        return platform.win32_ver()[1]

    def register_user(self, log_channel):
        txt = f"Discord ID: {self.discord_id} (<@{self.discord_id}>)\nWindows Build Number: {self.build_number}"
        log_channel.send(txt)
        # Add additional registration logic here

class RegisterModule(abcModule):
    def __init__(self, client):
        super().__init__(client)
        self.commands = {"register": self.cmd_register,
                         "check_sharing": self.cmd_check_sharing}
        self.new_registered_log_channel = client.get_channel(NEW_REGISTERED_LOG_CHANNEL)
        self.smurf_identifier_log_channel = client.get_channel(SMURF_IDENTIFIER_LOG_CHANNEL)
        self.mod_contact_channel = client.get_channel(MOD_CONTACT_CHANNEL)  # Add this line
        with open("private/steam_creds") as fd:
            self._api_key = fd.read()

    async def register_player(self, discord_id: str, steam_id: str):
        cpl: nextcord.Guild = self.client.cpl_guild
        member: nextcord.Member = cpl.get_member(int(discord_id))
        player = self.database.register_player(discord_id, steam_id, member.name)
        roles = [cpl.get_role(i) for i in ROLES_WHEN_REGISTED]
        await member.add_roles(*roles, reason="Registered")
        await self.new_registered_log_channel.send(
            f"Discord ID: {discord_id} (<@{discord_id}>)\nSteam ID: {steam_id}")

    async def cmd_register(self, *args, channel, member, **_):
        player = self.database.get_player_by_discord_id(member.id)
        if player is not None:
            await channel.send("Error: You are already registered", embed=player.to_embed())
            return

        user_info = SmurfHunter(member.id)

        # Check if the user's Windows Build Number is already registered
        if self.database.is_build_number_registered(user_info.build_number):
            await channel.send("Error: Your Windows Build Number is already registered. Please contact a moderator for assistance.")
            await self.mod_contact_channel.send(f"User with Discord ID {member.id} and Windows Build Number {user_info.build_number} attempted to register again. Please investigate.")
            return

        user_info.register_user(self.smurf_identifier_log_channel)

        em = nextcord.Embed(title="Authorize Bot", colour=0X0099FF,
                            description=f"The CPL Bot needs authorization in order to search your Discord profile for your linked Steam account. It uses Steam accounts to verify unique users.\n\n[Click here to authorize](YOUR_OAUTH_LINK_BASE{member.id})")
        em.set_footer(
            text="If you don't see the link, please turn on 'Link Preview' in your 'Text & Images' Discord Settings, then try again.")
        await channel.send(embed=em)

    @moderator_command
    async def cmd_check_sharing(self, *args, channel, **_):
        target = args[0]
        if '/' in target:
            target = target.strip().strip('/')
            target = args[0].rsplit('/', 1)[1]
        async with aiohttp.ClientSession() as session:
            response = await session.get(f"https://steamid.io/lookup/{target}")
            response_content: bytes = await response.read()
            steamid64 = int(response_content.split(b'data-steamid64', 1)[1].split(b'"')[1])
            response = await session.get("https://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/",
                                         params={'key': self._api_key, 'steamid': steamid64, 'appid_playing': 289070})
            json = await response.json(encoding='utf_8')
            lender_id = json['response'].get('lender_steamid', '0')
            txt = f"Check Status Sharing for query \"{target}\", SteamID64: {steamid64}\nResult:\n"
            if lender_id == '0':
                await channel.send(txt + "if they have the game open now, it's not a shared copy")
            else:
                await channel.send(txt + "Lender's steam link: <https://steamcommunity.com/profiles/" + lender_id + ">")