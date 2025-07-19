from pyrogram import Client, filters
from terabox_api import get_direct_link

# Replace with your credentials
API_ID = 24187778
API_HASH ="7b440c12e9f662ad20c2d2339582c4f6"
BOT_TOKEN = "7120527421:AAEgfETAyOEuN2a8dGScXNwIrXxIwCqyjyw"

app = Client("terabox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Hi! Send me a **Terabox** link and I’ll send you the video!")

@app.on_message(filters.text & ~filters.command("start"))
async def handle_link(client, message):
    link = message.text.strip()

    # Convert 1024terabox.com to terabox.com
    link = link.replace("1024terabox.com","terabox.club","terabox.com")

    if "terabox.com" not in link:
        await message.reply("⚠️ Please send a valid Terabox link.")
        return

    await message.reply("🔗 Generating direct link, please wait...")

    direct_link = get_direct_link(link)
    if not direct_link:
        await message.reply("❌ Failed to generate direct link. Link may be private or expired.")
        return

    try:
        await message.reply_video(direct_link, caption="✅ Here's your video!")
    except Exception as e:
        await message.reply(f"⚠️ Error sending video: {e}")

app.run()
