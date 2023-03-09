from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⚡️ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ⚡️",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐇ᴇʟᴘ ✨", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💫 𝐒ᴜᴩᴩᴏʀᴛ 💫", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 𝐌ᴀɪɴᴛᴀɪɴᴇʀ 🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐒ᴏᴜʀᴄᴇ ✨", url=f"https://t.me/ll_ITZ_ALONE_ll"
            )
        ],
     ]
    return buttons
