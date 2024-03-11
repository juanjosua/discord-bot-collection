import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

# step 0 : load our token from somewhere safe
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# print(TOKEN)

# step 1 : bot setup
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# step 2 : message functionality
async def send_message(message, user_message) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    # is_private = user_message[0] == '?'
    if is_private := user_message[0] == '?':
        # the ? is for private message
        user_message = user_message[1:]

    try:
        response = get_responses(user_message)
        
        # if the message is in private send directly to the author
        # if not, send to the channel instead
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# step 3 : handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# step 4 : handling incoming messages
@client.event
async def on_message(message) -> None:
    # make sure that the bot not response to itself
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# step 5 : main entry point
def main() -> None:
    client.run(token=TOKEN)



if __name__ == '__main__':
    main()