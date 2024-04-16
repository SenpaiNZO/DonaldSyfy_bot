class script(object):
    START_TXT = """<b>✨ Salut {user}.

Je suis {bot}, un bot de recherche de films/series/anime , je peux partager des films et des series avec toi si tu fais un petit don à <a href="https://t.me/the_boyfriend">Ｓｅｎｐａｉ</a>.</b>

<i>Ajoute moi dans ton groupe et regarde la magie operer ou suis simplement les instructions dans le menu</i> <b> Aide </b>"""

    HELP_TXT = "Bienvenu {}\nVoici mon menu <b> Aide </b>"

    ABOUT_TXT = """<b>🌀 𝔐𝔬𝔫 𝔑𝔬𝔪 🏵️: {}
🌀 𝔇é𝔳𝔢𝔩𝔬𝔭𝔭𝔢𝔲𝔯 🧠: <a href="https://t.me/the_boyfriend">Ｓｅｎｐａｉ</a>
🌀 𝔏𝔞𝔫𝔤𝔞𝔤𝔢 🐍: ᴩʏᴛʜᴏɴ/ᴩʏʀᴏɢʀᴀᴍ
🌀 𝔐𝔞 𝔅𝔞𝔰𝔢 𝔡𝔢 𝔡𝔬𝔫𝔫é𝔢 💦: ᴍᴏɴɢᴏ-ᴅʙ
🌀 𝔐𝔬𝔫 𝔖𝔢𝔯𝔳𝔢𝔲𝔯 👾: ᴀɴʏᴡʜᴇʀᴇ
🌀 𝔐𝔞 𝔙𝔢𝔯𝔰𝔦𝔬𝔫 ☣️: Senpai-Bot ᴠ1.0.0 </b>"""

    SOURCE_TXT = """<b>𝗖𝗼𝗱𝗲 𝗦𝗼𝘂𝗿𝗰𝗲 𝗜𝗖𝗜 🌈™ : <a href="https://t.me/the_boyfriend">Ｓｅｎｐａｉ</a>.</b>

<b>𝗗é𝘃𝗲𝗹𝗼𝗽𝗽𝗲𝘂𝗿 🌈™: <a href="https://t.me/the_boyfriend">Ｓｅｎｐａｉ</a>.</b>"""

    FILE_TXT = """<b>➤ Hᴇʟᴘ Fᴏʀ Fɪʟᴇ Sᴛᴏʀᴇ</b>

<i>En utilisant ce module, vous pouvez stocker des fichiers dans ma base de données et je vous donnerai un lien permanent pour accéder aux fichiers enregistrés.Si vous souhaitez ajouter des fichiers à partir d'un canal public envoie le lien du fichier seulement ou si tu souhaites ajouter des fichiers à partir d'un canal privé tu dois me nommer administrateur du Canal pour accéder aux fichiers</i>

<b>⪼ Commande et Utilisation/b>
➪ /link › Transférez n'importe quel média pour obtenir le lien
➪ /batch › Pour créer un lien pour plusieurs médias

<b>⪼ Petit exemple :/b>
</code>/batch https://t.me/SENPAI_BOT_SUPPORT/1 https://t.me/SENPAI_BOT_SUPPORT/10</code>"""

    FILTER_TXT = "Choisissez Ce Que Vous Voulez...✨"

    GLOBALFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /gfilter - Tᴏ Aᴅᴅ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
• /gfilters - Tᴏ Vɪᴇᴡ Lɪsᴛ Oғ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs
• /delg - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ
• /delallg - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀꜱ

• /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    MANUELFILTER_TXT = """<b>Hᴇʟᴘ Fᴏʀ Fɪʟᴛᴇʀs</b>

<i>Fɪʟᴛᴇʀ Is Tʜᴇ Fᴇᴀᴛᴜʀᴇ Wᴇʀᴇ Usᴇʀs Cᴀɴ Sᴇᴛ Aᴜᴛᴏᴍᴀᴛᴇᴅ Rᴇᴘʟɪᴇs Fᴏʀ A Pᴀʀᴛɪᴄᴜʟᴀʀ Kᴇʏᴡᴏʀᴅ Aɴᴅ Bᴏᴛ  Wɪʟʟ Rᴇsᴘᴏɴᴅ Wʜᴇɴᴇᴠᴇʀ A Kᴇʏᴡᴏʀᴅ Is Fᴏᴜɴᴅ Tʜᴇ Mᴇssᴀɢᴇ</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tʜɪs Bᴏᴛ Sʜᴏᴜʟᴅ Hᴀᴠᴇ Aᴅᴍɪɴ Pʀɪᴠɪʟʟᴀɢᴇ.
𝟸. Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ.
𝟹. Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs Hᴀᴠᴇ A Lɪᴍɪᴛ Oғ 𝟼𝟺 Cʜᴀʀᴀᴄᴛᴇʀs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /filter - Aᴅᴅ A Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /filters - Lɪsᴛ Aʟʟ Tʜᴇ Fɪʟᴛᴇʀs Oғ A Cʜᴀᴛ
• /del - Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪғɪᴄ Fɪʟᴛᴇʀ Iɴ Cʜᴀᴛ
• /delall - Dᴇʟᴇᴛᴇ Tʜᴇ Wʜᴏʟᴇ Fɪʟᴛᴇʀs Iɴ A Cʜᴀᴛ (Cʜᴀᴛ Oᴡɴᴇʀ Oɴʟʏ)

• /g_filter off Usᴇ Tʜɪs Cᴏᴍᴍᴏᴀɴᴅ + on/offғ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Tᴏ Cᴏɴᴛʀᴏʟ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ"""

    BUTTON_TXT = """<b>Hᴇʟᴘ Fᴏʀ Bᴜᴛᴛᴏɴs</b>

<i>Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴏᴛʜ Uʀʟ Aɴᴅ Aʟᴇʀᴛ Iɴʟɪɴᴇ Bᴜᴛᴛᴏɴs.</i>

<b>Nᴏᴛᴇ:</b>
𝟷. Tᴇʟᴇɢʀᴀᴍ Wɪʟʟ Nᴏᴛ Aʟʟᴏᴡs Yᴏᴜ Tᴏ Sᴇɴᴅ Bᴜᴛᴛᴏɴs Wɪᴛʜᴏᴜᴛ Aɴʏ Cᴏɴᴛᴇɴᴛ, Sᴏ Cᴏɴᴛᴇɴᴛ Is Mᴀɴᴅᴀᴛᴏʀʏ.
𝟸. Tʜɪs Bᴏᴛ Sᴜᴘᴘᴏʀᴛs Bᴜᴛᴛᴏɴs Wɪᴛʜ Aɴʏ Tᴇʟᴇɢʀᴀᴍ Mᴇᴅɪᴀ Tʏᴘᴇ.
𝟹. Bᴜᴛᴛᴏɴs Sʜᴏᴜʟᴅ Bᴇ Pʀᴏᴘᴇʀʟʏ Pᴀʀsᴇᴅ As Mᴀʀᴋᴅᴏᴡɴ Fᴏʀᴍᴀᴛ

<b>Uʀʟ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonurl:xxxxxxxxxxxx)

<b>Aʟᴇʀᴛ Bᴜᴛᴛᴏɴs:</b>
[Bᴜᴛᴛᴏɴ Tᴇxᴛ](buttonalert:Tʜɪs Is Aɴ Aʟᴇʀᴛ Mᴇssᴀɢᴇ)"""

    AUTOFILTER_TXT = """<b>Aide pour la commande <code>/autofilter</code></b>

<i>Le filtre automatique est la fonction pour filtrer et enregistrer les fichiers automatiquement depuis un canal à un groupe.  Vous pouvez utiliser la commande suivante pour on/off le autofiltre dans votre groupe.</i>

• /autofilter on - activé dans votre groupe
• /autofilter off - désactivé dans votre groupe

<b>Autres Commandes ❄️:</b>
• /set_template - définir le modèle imdb pour votre groupe
• /get_template - le modèle imdb actuel pour votre croupe"""

    CONNECTION_TXT = """<b>Hᴇʟᴘ Fᴏʀ Cᴏɴɴᴇᴄᴛɪᴏɴs</b>

<i> Usᴇᴅ Tᴏ Cᴏɴɴᴇᴄᴛ Bᴏᴛ Tᴏ Pᴍ Fᴏʀ Mᴀɴᴀɢɪɴɢ Fɪʟᴛᴇʀs. Iᴛ Hᴇʟᴘs Tᴏ Aᴠᴏɪᴅ Sᴘᴀᴍᴍɪɴɢ Iɴ Gʀᴏᴜᴘs</i>

<b>Nᴏᴛᴇ:</b>
• Oɴʟʏ Aᴅᴍɪɴs Cᴀɴ Aᴅᴅ A Cᴏɴɴᴇᴄᴛɪᴏɴ.
• Sᴇɴᴅ /connect Fᴏʀ Cᴏɴɴᴇᴄᴛɪɴɢ Mᴇ Tᴏ Uʀ Pᴍ

<Cb>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:</b>
• /connect - Cᴏɴɴᴇᴄᴛ A Pᴀʀᴛɪᴄᴜʟᴀʀ Cʜᴀᴛ Tᴏ Yᴏᴜʀ Pᴍ
• /disconnect - Dɪsᴄᴏɴɴᴇᴄᴛ Fʀᴏᴍ A Cʜᴀᴛ
• /connections - Lɪsᴛ Aʟʟ Yᴏᴜʀ Cᴏɴɴᴇᴄᴛɪᴏɴs"""

    ADMIN_TXT = """<b>Hᴇʟᴩ Fᴏʀ Aᴅᴍɪɴꜱ</b>

<i>Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs</i>

<b>Cᴏᴍᴍᴀɴᴅ & Uꜱᴀɢᴇ</b>
• /logs - Tᴏ Gᴇᴛ Tʜᴇ Rᴇᴄᴇɴᴛ Eʀʀᴏʀꜱ
• /delete - Tᴏ Dᴇʟᴇᴛᴇ A Sᴘᴇᴄɪꜰɪᴄ Fɪʟᴇ Fʀᴏᴍ DB
• /deleteall - Tᴏ Dᴇʟᴇᴛᴇ Aʟʟ Fɪʟᴇs Fʀᴏᴍ DB
• /users - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Uꜱᴇʀꜱ Aɴᴅ Iᴅꜱ
• /chats - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Mʏ Cʜᴀᴛꜱ Aɴᴅ Iᴅꜱ
• /channel - Tᴏ Gᴇᴛ Lɪꜱᴛ Oꜰ Tᴏᴛᴀʟ Cᴏɴɴᴇᴄᴛᴇᴅ Cʜᴀɴɴᴇʟꜱ
• /broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀꜱᴛ A Mᴇꜱꜱᴀɢᴇ Tᴏ Aʟʟ Uꜱᴇʀꜱ
• /group_broadcast - Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ A Mᴇssᴀɢᴇ Tᴏ Aʟʟ Cᴏɴɴᴇᴄᴛᴇᴅ Gʀᴏᴜᴘs
• /leave  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Lᴇᴀᴠᴇ Fʀᴏᴍ A Cʜᴀᴛ
• /disable  - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Dɪꜱᴀʙʟᴇ A Cʜᴀᴛ
• /invite - Wɪᴛʜ Cʜᴀᴛ Iᴅ Tᴏ Gᴇᴛ Tʜᴇ Iɴᴠɪᴛᴇ Lɪɴᴋ Oғ Aɴʏ Cʜᴀᴛ Wʜᴇʀᴇ Tʜᴇ Bᴏᴛ Is Aᴅᴍɪɴ
• /ban_user  - Wɪᴛʜ Iᴅ Tᴏ Bᴀɴ A Uꜱᴇʀ
• /unban_user  - Wɪᴛʜ Iᴅ Tᴏ Uɴʙᴀɴ A Uꜱᴇʀ
• /restart - Tᴏ Rᴇsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ
• /clear_junk - Cʟᴇᴀʀ Aʟʟ Dᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ & Bʟᴏᴄᴋᴇᴅ Aᴄᴄᴏᴜɴᴛ Iɴ Dᴀᴛᴀʙᴀsᴇ
• /clear_junk_group - Cʟᴇᴀʀ Aᴅᴅ Rᴇᴍᴏᴠᴇᴅ Gʀᴏᴜᴘ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ Gʀᴏᴜᴘs Oɴ Dʙ"""


    STATUS_TXT = """<b>💠 ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
💠ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
💠ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
💠 ᴜꜱᴇᴅ ᴅʙ ꜱɪᴢᴇ: <code>{}</code>
💠 ꜰᴇᴇᴇ ᴅʙ ꜱɪᴢᴇ: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#ɴᴇᴡ_ɢʀᴏᴜᴩ

💠 ɢʀᴏᴜᴩ: {a}
💠 ɢ-ɪᴅ: <code>{b}</code>
💠 ʟɪɴᴋ: @{c}
💠 ᴍᴇᴍʙᴇʀꜱ: <code>{d}</code>
💠ᴀᴅᴅᴇᴅ ʙʏ: {e}

💠 ʙʏ: @{f}</b>"""

    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ

💠 ᴜꜱᴇʀ-ɪᴅ: <code>{}</code>
💠ᴀᴄᴄ-ɴᴀᴍᴇ: {}
💠 ᴜꜱᴇʀɴᴀᴍᴇ: @{}

💠 ʙʏ: @{}</b>"""

    GROUPMANAGER_TXT = """<b>Aide pour gérer groupe

<i>C'est l'aide pour la gestion de votre groupe , ceci fonctionnera uniquement pour les admins du groupe</i>

Commandes et utilisation:

 /inkick - commande avec arguments requis et je vais expulser les membres de ce groupe.
 /instatus - pour vérifier l'état actuel d'un membre de groupe
/dkick - pour exclure les comptes supprimés
/ban - pour interdire le groupe à un utilisateur
/unban - débannir l'utilisateur interdit
 /tban - interdire temporairement un utilisateur
 /mute - pour mettre en sourdine un utilisateur
 /unmute - pour réactiver l'utilisateur en sourdine
 /tmute - avec valeur à mute jusqu'à
 temps particulier par exemple :
/tmute 2h to mute
 valeurs sur 2 heures is (m/h/d)
 /pin - pour épingler un message sur votre chat
 /unpin - pour dépincer le message sur votre chat
 /purge - supprimer tous les messages de la réponse au message, au courant message</b> """

    EXTRAMOD_TXT = """<b>Aide pour le module supplémentaire

<i>Envoyez juste n'importe quelle image pour modifier l'image</i>

 Commandes et utilisation :

 /id - Avoir id d'un utilisateur spécifique
 /info - Avoir desinformations sur un utilisateur
 /imdb - Obtenir les informations sur le film à partir de la source imdb
 /paste [text] - coller le texte donné sur pâteux
 /tts [texte] - convertir le texte en parole
 /telegraph - envoyez-moi cette commande en reponse
 avec photo ou vidéo sous (5mb)
 /json - répondre avec pour avoir des informations sur le message (utile pour le groupe)
 /written - répondre avec un texte pour obtenir un fichier
 (utile pour les codeurs)
 /carbon - répondre avec un texte pour obtenir image carbonée
 /font [texte] - pour changer vos polices de texte à la police fantaisie
 /share - répondre avec texte pour obtenir du texte lien partageable
 /song [nom] - pour rechercher la chanson dans youtube
 /video [lien] - pour télécharger une video youtube</b>"""

    CREATOR_REQUIRED = "❗<b>Yᴏᴜ Hᴀᴠᴇ To Bᴇ Tʜᴇ Gʀᴏᴜᴩ Cʀᴇᴀᴛᴏʀ Tᴏ Dᴏ Tʜᴀᴛ</b>"

    INPUT_REQUIRED = "❗ **Aʀɢᴜᴍᴇɴ Rqᴜɪʀᴇᴅ**"

    KICKED = "✔️ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Kɪᴄᴋᴇᴅ {} Mᴇᴍʙᴇʀꜱ Acᴄᴏʀᴅɪɴɢ To Tʜᴇ Aʀɢᴜᴍᴇɴᴛꜱ Prᴏᴠɪᴅᴇᴅ"

    START_KICK = "Rᴇᴍᴏᴠɪɴɢ Iɴᴀᴄᴛɪᴠᴇ Mᴇᴍʙᴇʀs Tʜɪs Mᴀʏ Tᴀᴋᴇ A Wʜɪʟᴇ"

    ADMIN_REQUIRED = "❗<b>Iᴀᴍ Nᴏᴛ Aᴅᴍɪɴ Iɴ Tʜɪꜱ Cʜᴀᴛ Sᴏ Pʟᴇᴀꜱᴇ Aᴅᴅ Mᴇ Aɢᴀɪɴ Wɪᴛʜ Aʟʟ Pᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ</b>"

    DKICK = "✔️ Kɪᴄᴋᴇᴅ {} Dᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛꜱ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"

    FETCHING_INFO = "<b>Wᴀɪᴛ I Wɪʟʟ Tᴀᴋᴇ Tʜᴇ Aʟʟ Iɴꜰᴏ</b>"

    SERVER_STATS = """Stats du serveur:

Lancé à: {}
CPU Utilisé: {}%
RAM utilisée: {}%
Espace total: {}
ESpace utilisé: {} ({}%)
Espace libre: {}"""

    BUTTON_LOCK_TEXT = "Bro {query}\nCe n'est pas ta requête. Lance ta propre requête."

    FORCE_SUB_TEXT = "Désolé l'ami(e), tu n'es pas membre de mon canal. Pour être membre de mon canal VIP, écris à [Ｓｅｎｐａｉ](https://t.me/the_boyfriend) fais un don de 6€ (7$) (3900 fcfa). Et après tu auras accès a ce bot et au groupe VIP de plus de 80000 fichiers. On t'attend dans le meilleur endroit sur Telegram Francophone. ✅"

    WELCOM_TEXT = """Hᴇʏ {user} 💞

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {chat}.

ꜱʜᴀʀᴇ & ꜱᴜᴩᴩᴏʀᴛ, ʀᴇqᴜᴇꜱᴛ ʏᴏᴜ ᴡᴀɴᴛᴇᴅ ᴍᴏᴠɪᴇꜱ"""

    IMDB_TEMPLATE = """<b>𝗥𝗲𝗾𝘂𝗲̂𝘁𝗲: {query}</b>

🏷 Titre: <a href={url}>{title}</a>
🎭 Genre: {genres}
📆 Année de diffusion: <a href={url}/releaseinfo>{year}</a>
🌟 Avis: <a href={url}/ratings>{rating}</a>/10"""










