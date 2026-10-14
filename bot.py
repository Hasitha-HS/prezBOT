import os
import discord
import aiohttp
import asyncio

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'🤖 ShadowBot is online as {client.user}!')


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Process messages sent in the #help channel
    if message.channel.name == "help":
        print(f"📩 Message received from {message.author}: {message.content}")

        payload = {
            "message": message.content,
            "user_id": str(message.author.id)
        }

        try:
            # 30-second timeout allows n8n time to perform retries if Gemini rate limits
            async with aiohttp.ClientSession() as session:
                async with session.post(N8N_WEBHOOK_URL, json=payload, timeout=30) as response:
                    print(f"🔍 n8n Response Status: {response.status}")

                    if response.status == 200:
                        data = await response.json()
                        print(f"📦 Raw JSON from n8n: {data}")

                        # Inspect all possible key outputs from AI Agent or fallback basic nodes
                        ai_reply = data.get("output") or data.get("text") or data.get("reply")

                        if ai_reply:
                            await message.channel.send(ai_reply)
                        else:
                            print("⚠️ Warning: Output key was empty in response JSON.")
                            await message.channel.send("My brain stalled for a second. Try asking again!")
                    else:
                        print(f"❌ n8n returned error status: {response.status}")
                        await message.channel.send("Give me a moment, server lagged out. Try asking again in a second!")

        except asyncio.TimeoutError:
            print("⏱️ Error: n8n webhook timed out after 30 seconds.")
            await message.channel.send("Request timed out waiting for the AI response. Please try again.")
        except Exception as e:
            print(f"❌ Error communicating with n8n: {e}")
            await message.channel.send("An unexpected connection error occurred.")


client.run(BOT_TOKEN)