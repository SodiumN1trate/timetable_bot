import discord
import asyncio
import datetime
from datetime import datetime
from timetable_parser import alert_time, get_subjects
from bot_token import TOKEN

client = discord.Client()


def current_time():
    time_object = datetime.now()
    return f"{time_object.time().hour}:{time_object.time().minute}"


async def timer():
    await client.wait_until_ready()
    channel = client.get_channel(id=852897067399381041)
    while True:
        if datetime.today().isoweekday() == 1:
            dp2_1_timetable = get_subjects(open("DP2_1_timetable.html", "r", encoding="utf8"), "420")
            dp2_3_timetable = get_subjects(open("DP2_3_timetable.html", "r", encoding="utf8"), "420")

            while datetime.today().isoweekday() != 2:
                if current_time() in alert_time:
                    await channel.send("OTRĀI PUSGRUPAI STUNDAS NERĀDĀS! PATS SKATIES!")
                    await channel.send("=============================")
                    await channel.send("DP2-1 {1}: {0}".format(dp2_1_timetable[alert_time.index(current_time())], "<@!310439855689695232>"))
                    await channel.send("=============================")
                    await channel.send("DP2-3 {1}: {0}".format(dp2_3_timetable[alert_time.index(current_time())], "<@!482612040708390913>"))
                await asyncio.sleep(60)

        elif datetime.today().isoweekday() == 2:
            dp2_1_timetable = get_subjects(open("DP2_1_timetable.html", "r", encoding="utf8"), "726")
            dp2_3_timetable = get_subjects(open("DP2_3_timetable.html", "r", encoding="utf8"), "726")

            while datetime.today().isoweekday() != 3:
                print(current_time())
                if current_time() in alert_time:
                    await channel.send("OTRĀI PUSGRUPAI STUNDAS NERĀDĀS! PATS SKATIES!")
                    await channel.send("=============================")
                    await channel.send("DP2-1 {1}: {0}".format(dp2_1_timetable[alert_time.index(current_time())], "<@!310439855689695232>"))
                    await channel.send("=============================")
                    await channel.send("DP2-3 {1}: {0}".format(dp2_3_timetable[alert_time.index(current_time())], "<@!482612040708390913>"))
                await asyncio.sleep(60)

        elif datetime.today().isoweekday() == 3:
            dp2_1_timetable = get_subjects(open("DP2_1_timetable.html", "r", encoding="utf8"), "1032")
            dp2_3_timetable = get_subjects(open("DP2_3_timetable.html", "r", encoding="utf8"), "1032")

            while datetime.today().isoweekday() != 4:
                if current_time() in alert_time:
                    await channel.send("OTRĀI PUSGRUPAI STUNDAS NERĀDĀS! PATS SKATIES!")
                    await channel.send("=============================")
                    await channel.send("DP2-1 {1}: {0}".format(dp2_1_timetable[alert_time.index(current_time())], "<@!310439855689695232>"))
                    await channel.send("=============================")
                    await channel.send("DP2-3 {1}: {0}".format(dp2_3_timetable[alert_time.index(current_time())], "<@!482612040708390913>"))
                await asyncio.sleep(60)

        elif datetime.today().isoweekday() == 4:
            dp2_1_timetable = get_subjects(open("DP2_1_timetable.html", "r", encoding="utf8"), "1338")
            dp2_3_timetable = get_subjects(open("DP2_3_timetable.html", "r", encoding="utf8"), "1338")

            while datetime.today().isoweekday() != 5:
                if current_time() in alert_time:
                    await channel.send("OTRĀI PUSGRUPAI STUNDAS NERĀDĀS! PATS SKATIES!")
                    await channel.send("=============================")
                    await channel.send("DP2-1 {1}: {0}".format(dp2_1_timetable[alert_time.index(current_time())], "<@!310439855689695232>"))
                    await channel.send("=============================")
                    await channel.send("DP2-3 {1}: {0}".format(dp2_3_timetable[alert_time.index(current_time())], "<@!482612040708390913>"))
                await asyncio.sleep(60)
        elif datetime.today().isoweekday() == 5:
            dp2_1_timetable = get_subjects(open("DP2_1_timetable.html", "r", encoding="utf8"), "1644")
            dp2_3_timetable = get_subjects(open("DP2_3_timetable.html", "r", encoding="utf8"), "1644")

            while datetime.today().isoweekday() != 6:
                if current_time() in alert_time:
                    await channel.send("OTRĀI PUSGRUPAI STUNDAS NERĀDĀS! PATS SKATIES!")
                    await channel.send("=============================")
                    await channel.send("DP2-1 {1}: {0}".format(dp2_1_timetable[alert_time.index(current_time())], "<@!310439855689695232>"))
                    await channel.send("=============================")
                    await channel.send("DP2-3 {1}: {0}".format(dp2_3_timetable[alert_time.index(current_time())], "<@!482612040708390913>"))
                await asyncio.sleep(60)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.loop.create_task(timer())


client.run(TOKEN)
