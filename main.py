'''
Pyrogram String Session Generator for Telegram.
By: SOME-1HING [https://github.com/SOME-1HING]
'''

import asyncio
from pyrogram import Client

async def main():
    try:
        api_id = int(input("Please input API ID: "))
    except ValueError:
        print("API ID must be string.")
        return
        
    api_hash = input("Please input API HASH: ")
    
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as pbot:
        try:
            session = await pbot.export_session_string()
        except Exception as e:
            print(f"ERROR Occured: {e}")
            return
            
        await pbot.send_message(
            "me", "Pyrogram String Session: \n\n"
            f"`{session}`"
        )
        
        print("""
Program String Session Generated Successfully!!!.
Please Check your Saved Messages to get the session.
""")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
