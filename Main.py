import os
import sys
import time
import requests
import CloudFlare
import discord
import asyncio
import traceback

import CloudflareController
import config

client = discord.Client()

class Main:
    def __init__(self):
        self.cf = CloudflareController.CloudFlareController(config.cf_email, config.cf_token)
        client.run(config.discord_token)


    @client.event
    def on_message(self):
        print('shrug')



def main():
    try:
        print('Starting up...')
    except:
        traceback.print_exc()
        time.sleep(10)





if __name__ == '__main__':
    main()



