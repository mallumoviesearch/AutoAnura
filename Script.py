#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://paisakamalo.in/')
    START_TXT = environ.get("START_TXT", "𝙷𝙴𝙻𝙾 {} 𝖬𝖸 𝖭𝖠𝖬𝖤 𝖨𝖲 𝗥𝗼𝗸𝗲𝘆 𝖨 𝖠𝖬 𝖦𝖱𝖮𝖴𝖯 𝖬𝖠𝖭𝖠𝖦𝖤𝖱 𝖡𝖮𝖳 𝖢𝖱𝖤𝖠𝖳𝖤𝖣 𝖥𝖮𝖱 𝖬𝖠𝖫𝖫𝖴 𝖬𝖮𝖵𝖨𝖤 𝖲𝖤𝖠𝖱𝖢𝖧  𝖮𝖭𝖨𝖸 𝖠𝖴𝖳𝖧𝖮𝖱𝖨𝖲𝖤𝖣 𝖠𝖣𝖬𝖨𝖭𝖲 𝖢𝖠𝖭 𝖠𝖢𝖢𝖤𝖲𝖲   𝖣𝖮𝖭 𝖳 𝖶𝖠𝖲𝖳𝖤 𝖸𝖮𝖴𝖱 𝖳𝖨𝖬𝖤😁•")
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""

    LZTHMB_TEXT = """Hello {},
Glad to see you here. It seems that you really love <a href=https://t.me/LazyDeveloperr >LazyDeveloper's</a> work.\n\n<b>Thumbnail extracting</b> feature will be available soon, please join <a href=https://t.me/LazyDeveloper>Dev Channel</a> and stay tuned for next <a href=https://t.me/LazyDeveloper>update</a>.\n\n  🐞 Report Bug here: <a href=http://t.me/LazyDeveloperSupport>LazyDev Support</a>
    """
    LZLINK_TEXT = """Hey {},
Glad to see you here. It seems that you really love <a href=https://t.me/LazyDeveloperr >LazyDeveloper's</a> work.\n\n<b>File to LiNK converting</b> feature will be available soon, please join <a href=https://t.me/LazyDeveloper>Dev Channel</a> and stay tuned for next <a href=https://t.me/LazyDeveloper>update</a>.\n\n  🐞 Report Bug here: <a href=http://t.me/LazyDeveloperSupport>LazyDev Support</a>
    """
    DNT_TEXT = """Hey sweetie {},
Thanks for thinking about us.\nIt seems that you really love <a href=https://t.me/LazyDeveloperr >LazyDeveloper's</a> work.\n\n<b>For your kind information, we do not ask or force anyone for any kind of payment</b>. But if you really want to donate us then you can send money to us from below links...\n\n💵 Reach Donation Page : <a href=http://t.me/DonateLazyDeveloper>Click here...</a>\n\nT❤️ hank you so much..
    """
    REQ_AUTH_TEXT = """Hello {},
\nSorry sweetie.. You must have to be the Authentic User to complete this operation...\n\n👮‍♀ REPORT ISSUE HERE: <a href=https://t.me/LazyDeveloperSupport>LazyDeveloper Support</a>\n\n
    """

    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</b>
<b>✮ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Am_RoBots>ᴀᴍ_ᴛᴇᴄʜ</a></b>
<b>✮ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
<b>✮ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</b>
<b>✮ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼yehe𝙾𝙽𝙶𝙾-𝙳𝙱</b>
<b>✮ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: ᴀᴍ_ᴛᴇᴄʜ</b>
<b>✮ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: 𝚅1.0.43 [ 𝙱𝙴𝚃𝙰 ]</b>
<b>✮ 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: <a href=https://youtube.com/channel/UCqts9WhhlioK3RB9XQQzoAg>ᎯℕUℛᎯᎶ</a></b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- ᎯℕUℛᎯᎶ is a not open source project. 
- Source - https://github.com/AM-ROBOTS/AM-ROBOTS

<b>DEVS:</b>
- <a href=https://t.me/Am_RoBots>ᴀᴍ_ᴛᴇᴄʜ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᎯℕUℛᎯᎶ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᎯℕUℛᎯᎶ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ᎯℕUℛᎯᎶ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᎯℕUℛᎯᎶ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Am_RoBots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ᎯℕUℛᎯᎶ

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    IMDB_TEMPLATE_TXT = """
🎬 Title: <a href={url}>{title}</a>
🗓 Year: {year}
🔊 Language:<a href={url}/ratings>{languages}</a>
💿 Quality : HDRip 
🔗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞 ☞
"""
    CAPTION = """
{file_name}
╭━━━━━━━━━━━━━━━➣
┣⪼𝐺𝑅𝑂𝑈𝑃
┣⪼ @MALLU_MOVIE_SEARCH
┣⪼𝐹𝐼𝐿𝐸 𝑆𝐼𝑍𝐸:{file_size}
╰━━━━━━━━━━━━━━━➣
"""
    FOND_TXT = """☾︎𝗛𝗘𝗟𝗣 𝗙𝗢𝗥 𝗙𝗢𝗡𝗧𝗦☽︎
𝙵𝙾𝙽𝚃 𝙸𝚂 𝙰 𝙼𝙾𝙳𝚄𝙻𝙴 𝙵𝙾𝚁 𝙼𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝚂𝚃𝚈𝙻𝙸𝚂𝙷.
𝙵𝙾𝚁 𝚄𝚂𝙴 𝚃𝙷𝙰𝚃 𝙵𝙴𝚄𝚃𝚄𝚁𝙴 𝚃𝚈𝙿𝙴 /font <your text> 𝚃𝙷𝙴𝙽 𝚈𝙾𝚄𝚁 𝚃𝙴𝚇𝚃 𝙸𝚂 𝚁𝙴𝙰𝙳𝚈."""
    
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
