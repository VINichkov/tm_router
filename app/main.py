import config
import os
import re
import asyncio
from log import logger
from telethon import TelegramClient, events
from telethon.sessions import StringSession

logger.info('Start:')

client = TelegramClient(
    StringSession(os.getenv('SESSION')),
    os.getenv('API_ID'), 
    os.getenv('APU_HASH')
)

for cl in os.getenv('SOURCE').split(','):
    logger.info(cl.strip())
    @client.on(events.NewMessage(chats=int(cl.strip())))
    async def normal_handler(event):
        msg = event.message
        msg.message = re.sub('\nПодписаться на @truekpru|Подписаться на @truekpru|@kommersant', '', msg.message)
        logger.debug(msg.message)
        await client.send_message(int(os.getenv('RECIPIENT')), msg.message)

# async def main():
#     logger.info((await client.get_input_entity("РБК")).stringify())
#     await client.send_message('me', 'Hello to myself!')

# with client:
#      client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()
logger.info('End:')