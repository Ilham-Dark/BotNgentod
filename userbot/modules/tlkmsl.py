from time import sleep
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.events import register

# response 1


@register(outgoing=True, pattern=r"^\.tlkmsl")
async def _(event):
    if event.fwd_from:
        return
    chat = "@telkomsel_official_bot"
    now = "cek kuota"
    agere = "Ya"
    tart = "/start"
    await event.edit("Processing..")
    async with event.client.conversation(chat) as conv:
        try:
            await bot.send_message(chat, tart)
            sleep(3)
            await bot.send_message(chat, now)
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=266446332))
            sleep(3)
            await bot.send_message(chat, agere)
            response = await response
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("unblock me (@telkomsel_official_bot) and try again")
            return
        if response.text.startswith("Untuk"):
            await event.edit("Please cek bot and complete your identity")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message) #FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
# response 2


@register(outgoing=True, pattern=r"^\.tlkmls")
async def _(event):
    if event.fwd_from:
        return
    chat = "@telkomsel_official_bot"
    now = "cek kuota"
    tart = "/start"
    await event.edit("Processing..")
    async with event.client.conversation(chat) as conv:
        try:
            await bot.send_message(chat, tart)
            sleep(3)
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=266446332))
            await bot.send_message(chat, now)
            response = await response
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("unblock me (@telkomsel_official_bot) and try again")
            return
        if response.text.startswith("Untuk"):
            await event.edit("Please cek bot and complete your identity")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message) #FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4

CMD_HELP.update({
    "telkomsel":
    ">`.tlkmsl `"
    "\nUsage: Cek kuota when you don't have session number."
    "\n`.tlkmls `"
    "\nUsage: Cek kuota when you already have session number"
})
