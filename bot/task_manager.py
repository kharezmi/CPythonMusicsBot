import telebot, time, traceback, conf

from telebot import types
from botapp.models import Users, TaskManager

def main():
    bot = telebot.TeleBot(
        "Your token here",

        parse_mode='HTML',
        num_threads=2,
    )
    

    while True:
        if (task := TaskManager.unfulfilled.last()) is None:
            time.sleep(5)
            continue

        try:
            if task.txt == TaskManager.Type.SEND_MESSAGE:
                for i in Users.objects.all():
                    bot.send_message(i.u_id, TaskManager.task.all().values()[0]['info'])
            elif task.txt == TaskManager.Type.SEND_PHOTO:
                for i in Users.objects.all():
                    img = open("../"+TaskManager.task.all().values()[0]['photo'], 'rb')

                    bot.send_photo(i.u_id, img, caption=TaskManager.task.all().values()[0]['info'])
                
            task.done = True
        except Exception:
            print(traceback.format_exc())
        finally:
            task.save()
            time.sleep(5)


if __name__ == '__main__':
    main()