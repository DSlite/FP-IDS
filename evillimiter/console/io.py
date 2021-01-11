import re
import colorama
from discord_webhook import DiscordWebhook

from . import shell

DISCORD_WEBHOOK = 'https://discord.com/api/webhooks/797797383206469662/xgTQ54_WslKJEXuYQoN3NVkIa2yjpsSocQ_SvWNcyq0cCyWe9-2G8Nrtu6bUcFhISUcS'

class IO(object):
    _ANSI_CSI_RE = re.compile('\001?\033\\[((?:\\d|;)*)([a-zA-Z])\002?') 

    Back = colorama.Back
    Fore = colorama.Fore
    Style = colorama.Style
    DiscordUrl = DISCORD_WEBHOOK

    colorless = False

    @staticmethod
    def initialize(colorless=False):
        """
        Initializes console input and output.
        """
        IO.colorless = colorless
        if not colorless:
            colorama.init(autoreset=True)

    @staticmethod
    def print(text, end='\n', flush=False):
        """
        Writes a given string to the console.
        """
        if IO.colorless:
            text = IO._remove_colors(text)

        print(text, end=end, flush=flush)

    @staticmethod
    def ok(text, end='\n'):
        """
        Print a success status message
        """
        IO.print('{}OK{}   {}'.format(IO.Style.BRIGHT + IO.Fore.LIGHTGREEN_EX, IO.Style.RESET_ALL, text), end=end)

    @staticmethod
    def error(text):
        """
        Print an error status message
        """
        IO.print('{}ERR{}  {}'.format(IO.Style.BRIGHT + IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL, text))

    @staticmethod
    def spacer():
        """
        Prints a blank line for attraction purposes
        """
        IO.print('')

    @staticmethod
    def input(prompt):
        """
        Prompts the user for input.
        """
        if IO.colorless:
            prompt = IO._remove_colors(prompt)

        return input(prompt)

    @staticmethod
    def clear():
        """
        Clears the terminal screen
        """
        shell.execute('clear')

    @staticmethod
    def _remove_colors(text):
        edited = text

        for match in IO._ANSI_CSI_RE.finditer(text):
                s, e = match.span()
                edited = edited.replace(text[s:e], '')

        return edited

    @staticmethod
    def discord(text):
        """
        Writes a given string to the discord webhook.
        """
        webhook = DiscordWebhook(url=IO.DiscordUrl, content=text)
        webhook.execute()