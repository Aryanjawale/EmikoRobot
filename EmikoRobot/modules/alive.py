import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/998ee63a369c5935c6b3a.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),I'ᴍ Sᴄᴏʀʙᴜɴɴʏ.** \n\n"
  TEXT += f"⍟Iғ Aɴʏ Pʀᴏʙʟᴇᴍ Rᴇᴘᴏʀᴛ Tᴏ Mʏ [Mᴀsᴛᴇʀ](t.me/Aryanjawale) ᴏʀ [Sᴜᴘᴘᴏʀᴛ](t.me/trainer_zone) \n\n"
  TEXT += f"⍟📚Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ;: {telever} \n\n"
  TEXT += f"⍟📺Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ: {tlhver} \n\n"
  TEXT += f"⍟🗃️**Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ** : {pyrover} \n\n"
  TEXT += "**Tʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ**"
  BUTTON = [[Button.url("🚨HELP", "https://t.me/Scorbunnyrobot?start=help"), Button.url("🔥SUPPORT", "https://t.me/trainer_zone")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
