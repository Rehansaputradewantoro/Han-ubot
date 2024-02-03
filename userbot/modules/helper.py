""" Userbot module for other small commands. """
from userbot import ALIVE_NAME
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import zelda_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(zelda_cmd(outgoing=True, pattern=r"ihelp$"))
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✣ **Group Support :** [ZONEDANGERSEX](t.me/ZoneDangerSex)\n"
        f"✣ **Channel :** [Revan Store](t.me/Revanstoreya)\n"
        f"✣ **Owner :** [Lord Revans](t.me/Revans505)\n"
        f"✣ **Repo :** [Revans USERBOT](https://github.com/Rehansaputradewantoro/Han-Ubot)\n"
    )


@bot.on(zelda_cmd(outgoing=True, pattern=r"listvar$"))
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://telegra.ph/List-Variabel-Heroku-untuk-Revans USERBOT-09-22)"
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk REVANS USERBOT.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository REVANS USERBOT.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String REVANS USERBOT.\
    "
    }
)
