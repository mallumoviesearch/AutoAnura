# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot
# License Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot/blob/Auto-Approved-Bot/LICENSE

from os import environ
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest





AUTH_CHANNEL = [int(pr0fess0r_99) for pr0fess0r_99 in environ.get("AUTH_CHANNEL", "-1001687739032").split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "ʜᴇʟʟᴏ {mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴄʜᴀɴɴᴇʟ. {title}\n\nᴏɴʟʏ ɴᴇᴡ ᴀɴᴅ ʟᴏᴡ ꜱɪᴢᴇ ᴍᴏᴠɪᴇ ᴀᴠᴀɪʟᴀʙʟᴇ. ᴇɴᴊᴏʏɪɴɢ🔥🔥")
APPROVED = environ.get("APPROVED_WELCOME", "off").lower()

@Client.on_message(filters.private & filters.command(["aprv"]))
async def start(client, Message):
    approvedbot = await client.get_me() 
    button = [[ InlineKeyboardButton("📦 Repo", url="https://github.com/PR0FESS0R-99/Auto-Approved-Bot"), InlineKeyboardButton("Updates 📢", url="t.me/Mo_Tech_YT") ],
              [ InlineKeyboardButton("➕️ Add Me To Your Chat ➕️", url=f"http://t.me/{approvedbot.username}?startgroup=botstart") ]]
    await client.send_message(chat_id=message.chat.id, text=f"**__Hello {message.from_user.mention} Iam Auto Approver Join Request Bot Just [Add Me To Your Group Channnl](http://t.me/{approvedbot.username}?startgroup=botstart) || Repo https://github.com/PR0FESS0R-99/Auto-Approved-Bot||**__", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(AUTH_CHANNEL) if AUTH_CHANNEL else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} Joined 🤝") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        buttons = [[
            InlineKeyboardButton('🧩𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏🧩', url=f'https://t.me/nasrani_update')
            
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML
    )
        
