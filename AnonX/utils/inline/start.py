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
                text="💥𓆩𝔸ᴅᴅ 𝕄ᴇ 𝕋ᴏ 𝕐ᴏᴜʀ 𝔾ʀᴏᴜᴘ𓆪💥",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💥𓆩ℂᴏᴍᴍᴀɴᴅʟᴇℝ𓆪💥", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💥𓆩𝕌ᴘᴅᴀᴛ𝔼𓆪💥", url=config.SSUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💥𓆩𝕊ᴜᴘᴘᴏʀ𝕋𓆪💥", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="💥𓆩𝔻ᴇᴠᴇʟᴏᴘᴇℝ𓆪💥", user_id=OWNER"
            )
        ],
     ]
    return buttons
