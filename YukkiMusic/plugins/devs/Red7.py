""" Team Red7 """
from .. import pgram as Red7
from pyrogram.types import Message
from pyrogram import filters

try:
  from RiZoeLX.functions import Red7_Watch
except:
  import os
  os.system("pip3 install pyRiZoeLX")
  from RiZoeLX.functions import Red7_Watch

@Red7.on_message(filters.group & filters.all)
async def Red7_Scanner(_, message: Message):
    await Red7_Watch(Red7, message)

