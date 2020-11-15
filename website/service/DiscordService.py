import requests
import time
from django.conf import settings
from django.core.cache import cache
from discord_webhook import DiscordWebhook, DiscordEmbed


class DiscordService:
    def __init__(self):
        self.server_data = cache.get('discord_data')
        if self.server_data is None:
            id_redcraft = '609755577878577153'
            url = 'https://discordapp.com/api/guilds/{}/widget.json'.format(id_redcraft)
            response = requests.get(url)
            self.server_data = response.json()
            cache.set('discord_data', self.server_data, 60)

    def countPlayersOnline(self):
        return len(self.server_data['members'])

    def sendContactMessage(self, username, message, ip, request_type):
        webhook = DiscordWebhook(
            url = settings.DISCORD_CONTACT_WEBHOOK_URL,
            username='Page contact du site'
        )

        color = None

        if request_type == "player":
            color = 10659500        # grey
        elif request_type == "other":
            color = 11290182        # red

        # set ember parameters
        embed = DiscordEmbed(title='Message :', description=message, color=color)
        embed.add_embed_field(name='Author', value=username)
        embed.add_embed_field(name='Request type', value=request_type)
        embed.add_embed_field(name='IP address', value=ip)
        embed.set_timestamp()
        webhook.add_embed(embed)

        # Necessary in order to have a good feedback in the front end
        # (a well-visible spinning cog animation)
        time.sleep(0.3)

        response = webhook.execute()

        if response[0].status_code < 200 or response[0].status_code >= 300:
            return response[0].json()['message']

        return False
