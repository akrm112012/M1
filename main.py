import asyncio
from pyrogram import Client, filters
from ntgcalls import ntgcalls
from yt_dlp import YoutubeDL

# بياناتك البرمجية
API_ID = 15731676
API_HASH = "9308ff9a58ceefe0a1e8b56dfee9fc82"
SESSION = "AgDwC9wAokT0gL3YYDUZqVpD-j_YjchvE7-qP5xn-RoBY_K1Mlm5vJB0ex-amlNEtjXp0oMMPl78OpqvWXzllYq_ZAUg2XxTmIPFFGLc_KrlYPs1kbFy9dm2yFum60Ec8B-V1GtYFEzOEqho9W5YmCe87CBGcbPQ29GEXETu6uwshToLJ_HrvD86oYfbBcuJ93vnNMkQEuOPn3jvTHJXno8i5iiymayPIB0UKghmQG1-nBCfbdMq0QGYb8Sm-b_bQHdmhbMp8kyIYWU6D2XiZWpTp3kOPocbCgCSmqy170wObfTzid5aMlvyLCavA8AsGuDFAQiYNTMYMUDX6sbdKY5JAS48LgAAAAHs_zJwAQ"

app = Client("MyVideoBot", API_ID, API_HASH, session_string=SESSION)
rtc = ntgcalls.NTGCalls()

@app.on_message(filters.command("vplay") & filters.group)
async def vplay(client, message):
    if len(message.command) < 2:
        return await message.reply("📡 أرسل رابط الفيديو بعد الأمر /vplay")
    
    url = message.text.split(None, 1)[1]
    msg = await message.reply("⏳ جاري جلب البث...")
    
    try:
        with YoutubeDL({"format": "best[height<=480]", "quiet": True}) as ydl:
            link = ydl.extract_info(url, download=False)['url']
        
        await rtc.create_call(message.chat.id, link, video=True)
        await msg.edit("🎬 بدأ البث بنجاح!")
    except Exception as e:
        await msg.edit(f"❌ خطأ: {e}")

app.run()
