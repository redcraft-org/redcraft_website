import requests
from django.core.cache import cache

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
