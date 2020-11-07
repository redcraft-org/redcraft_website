import requests
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

    def sendContactMessage(self, nickname, message, ip, client_type):
        webhook = DiscordWebhook(
            url = settings.URL_WEBHOOK_CONTACT_DISCORD, 
            # url='https://discord.com/api/webhooks/thisIsAFakeWebhook', 
            username='Page contact du site'
        )

        embed = DiscordEmbed(title='Message', description=message, color=242424)

        # set author
        embed.set_author(name=nickname)
        # set timestamp (default is now)
        embed.set_timestamp()
        # add embed object to webhook
        webhook.add_embed(embed)

        response = webhook.execute()

        if response[0].status_code < 200 or response[0].status_code >= 300:
            return response[0].json()['message']

        return False
