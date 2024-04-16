import asyncio, re, ast, math, logging, pyrogram
from pyrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
from utils import get_shortlink
from info import AUTH_USERS, PM_IMDB, SINGLE_BUTTON, PROTECT_CONTENT, SPELL_CHECK_REPLY, IMDB_TEMPLATE, IMDB_DELET_TIME, PMFILTER, G_FILTER, SHORT_URL, SHORT_API
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import get_size, is_subscribed, get_poster, search_gagala, temp, get_settings, save_group_settings
from database.users_chats_db import db
from database.ia_filterdb import Media, get_file_details, get_search_results
from plugins.group_filter import global_filters

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@Client.on_message(filters.private & filters.text & filters.chat(AUTH_USERS) if AUTH_USERS else filters.text & filters.private)
async def auto_pm_fill(b, m):
    if PMFILTER:
        if G_FILTER:
            kd = await global_filters(b, m)
            if kd == False: await pm_AutoFilter(b, m)
        else: await pm_AutoFilter(b, m)
    else: return

@Client.on_callback_query(filters.create(lambda _, __, query: query.data.startswith("pmnext")))
async def pm_next_page(bot, query):
    ident, req, key, offset = query.data.split("_")
    try: offset = int(offset)
    except: offset = 0
    search = temp.PM_BUTTONS.get(str(key))
    if not search: return await query.answer("Vous utilisez un de mes anciens messages,s'il vous plait envoyez une nouvelle requête.", show_alert=True)

    files, n_offset, total = await get_search_results(search.lower(), offset=offset, filter=True)
    try: n_offset = int(n_offset)
    except: n_offset = 0
    if not files: return

    if SHORT_URL and SHORT_API:
        if SINGLE_BUTTON:
            btn = [[InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=files_{file.file_id}"))] for file in files ]
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=files_{file.file_id}")),
                    InlineKeyboardButton(text=f"{get_size(file.file_size)}", url=await get_shortlink(f"https://telegram.dog/{temp.U_NAME}?start=files_{file.file_id}"))] for file in files ]
    else:
        if SINGLE_BUTTON:
            btn = [[InlineKeyboardButton(text=f"[{get_size(file.file_size)}] {file.file_name}", callback_data=f'pmfile#{file.file_id}')] for file in files ]
        else:
            btn = [[InlineKeyboardButton(text=f"{file.file_name}", callback_data=f'pmfile#{file.file_id}'),
                    InlineKeyboardButton(text=f"{get_size(file.file_size)}", callback_data=f'pmfile#{file.file_id}')] for file in files ]

    btn.insert(0, [InlineKeyboardButton("🔗 Comment télécharger 🔗", "howdl")])
    if 0 < offset <= 10: off_set = 0
    elif offset == 0: off_set = None
    else: off_set = offset - 10
    if n_offset == 0:
        btn.append(
            [InlineKeyboardButton("⬅️ Précédent", callback_data=f"pmnext_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"❄️ ραgє(ѕ) {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages")]
        )
    elif off_set is None:
        btn.append(
            [InlineKeyboardButton(f"❄️ {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
             InlineKeyboardButton("Suivant ➡️", callback_data=f"pmnext_{req}_{key}_{n_offset}")])
    else:
        btn.append([
            InlineKeyboardButton("⬅️ Précédent", callback_data=f"pmnext_{req}_{key}_{off_set}"),
            InlineKeyboardButton(f"❄️ ραgє(ѕ) {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
            InlineKeyboardButton("Suivant ➡️", callback_data=f"pmnext_{req}_{key}_{n_offset}")
        ])
    try:
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(btn))
    except MessageNotModified:
        pass
    await query.answer()


@Client.on_callback_query(filters.create(lambda _, __, query: query.data.startswith("pmspolling")))
async def pm_spoll_tester(bot, query):
    _, user, movie_ = query.data.split('#')
    if movie_ == "close_spellcheck":
        return await query.message.delete()
    movies = temp.PM_SPELL.get(str(query.message.reply_to_message.id))
    if not movies:
        return await query.answer("Vous utilisez un de mes anciens messages,s'il vous plait envoyez une nouvelle requête.", show_alert=True)
    movie = movies[(int(movie_))]
    await query.answer('Recherche de films dans la base de données...')
    files, offset, total_results = await get_search_results(movie, offset=0, filter=True)
    if files:
        k = (movie, files, offset, total_results)
        await pm_AutoFilter(k)

async def pm_AutoFilter(client, msg, pmspoll=False):
    if not pmspoll:
        message = msg
        if message.text.startswith("/"): return  # ignore commands
        k = await msg.reply("Pour les requêtes envoyez les uniquement dans le groupe.", quote=True)
        await asyncio.sleep(10)
        return await k.delete()