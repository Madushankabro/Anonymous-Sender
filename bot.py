#    Copyright (C) 2021 - SDBOTs Inifinity
#    This programme is a part of SDBOTs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import logging
import functools
from telethon import TelegramClient, events, Button
from decouple import config

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

bottoken = None
# start the bot
print("Starting...")
apiid = 6
apihash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
try:
    bottoken = config("BOT_TOKEN")
except:
    print("Environment vars are missing!")
    print("Bot is quiting...")
    exit()

if bottoken != None:
    try:
        JEBotZ = TelegramClient("bot", apiid, apihash).start(bot_token=bottoken)
    except Exception as e:
        print(f"ERROR!\n{str(e)}")
        print("Bot is quiting...")
        exit()
else:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()
    

@JEBotZ.on(events.NewMessage(pattern="^/start"))
async def start(event):
    if event.is_private:
       await event.reply("Hey, I'm 𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 𝐒𝐄𝐍𝐃𝐄𝐑 𝐁𝐎𝐓 \n\nClick on help to find out how to use me\n\n**@epusthakalaya_bots**", 
                         buttons=[[Button.inline("🆘 Help 🆘", data="help")], 
                                  [Button.url("📣 Bot Channel 📣", url="https://t.me/epusthakalaya-bots"), Button.url("💾 Source 💾", url="https://github.com/kasunthamadushanka/Anonymous-Sender")]]),
                                  [Button.url("⛑ Developer ⛑", url="https://t.me/kasu_bro")]
       return
    if event.is_group:
       await event.reply("Hey, I'm 𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 𝐒𝐄𝐍𝐃𝐄𝐑 𝐁𝐎𝐓") 
     
 
@JEBotZ.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
     await event.edit("**🆘 Help 🆘**\n\nUsing me you can anonymize the sender and add or change caption of a media file\n\n**🎛 Available Commands 🎛**\n\n- /send (reply to media): Anonymize the sender\n- /send (caption) (reply to media): Add or change the caption and anonymize the sender\n\n*⃣ This bot works on both groups and private, but only admins can use the bot in groups\n\n**@epusthakalaya_bots**", 
                        buttons=[[Button.inline("Back", data="start")]])
    
@JEBotZ.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
     await event.edit("Hey, I'm 𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 𝐒𝐄𝐍𝐃𝐄𝐑 𝐁𝐎𝐓 \n\nClick on help to find out how to use me\n\n**@epusthakalaya_bots**", 
                       buttons=[[Button.inline("🆘 Help 🆘", data="help")], 
                                [Button.url("📣Bot Channel 📣", url="https://t.me/epusthakalaya_bots"), Button.url("💾 Source 💾", url="https://github.com/kasunthamadushanka/Anonymous-Sender")]]),
                                [Button.url("⛑ Developer ⛑", url="https://t.me/kasu_bro")]
         
@JEBotZ.on(events.NewMessage(pattern="^/send ?(.*)"))
async def caption(event):
   if event.is_private:
        return
   a = await event.client.get_permissions(event.chat_id, event.sender_id)
   if a.is_admin:
      try:
        lel = await event.get_reply_message()
        cap = event.pattern_match.group(1)
        await JEBotZ.send_file(event.chat.id, lel, caption=cap)
      except Exception:
         await event.reply("Reply to a media file 🥴")
         return
   if not a.is_admin:
      await event.reply("Only admins can execute this command!")

@JEBotZ.on(events.NewMessage(pattern="^/send ?(.*)"))
async def caption(event):
   if event.is_group:
        return
   try:
     lel = await event.get_reply_message()
     cap = event.pattern_match.group(1)
     await JEBotZ.send_file(event.chat.id, lel, caption=cap)
   except Exception:
      await event.reply("Reply to a media file 🥴")
      return 
      
       
print("𝐀𝐍𝐎𝐍𝐘𝐌𝐎𝐔𝐒 𝐒𝐄𝐍𝐃𝐄𝐑 𝐁𝐎𝐓 has started!")
print("visit @epusthakalaya_bots for mor info.")
JEBotZ.run_until_disconnected()
  
