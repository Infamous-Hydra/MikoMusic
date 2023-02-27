""" Team Red7 """
from pyrogram import filters
from pyrogram.types import Message

from .. import app as Red7

try:
    from RiZoeLX.functions import Red7_Watch
except:
    import os

    os.system("pip3 install pyRiZoeLX")
    from RiZoeLX.functions import Red7_Watch


@Red7.on_message(filters.group & filters.all)
async def Red7_Scanner(_, message: Message):
    await Red7_Watch(Red7, message)
