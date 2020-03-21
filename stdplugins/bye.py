# For @UniBorg

"""use cmd `.leave` and kick yourself from the group chat"""



from telethon.tl.functions.channels import LeaveChannelRequest

from uniborg.util import admin_cmd

import time





@borg.on(admin_cmd("bye", outgoing=True))

async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("`I'm leaving this chat.....!` @admin `Goodbye aren't forever. It was a pleasant time with you guys..`")

        time.sleep(3)

        if '-' in str(e.chat_id):

            await borg(LeaveChannelRequest(e.chat_id))

        else:

            await e.edit('`Sir This is Not A Chat`')
