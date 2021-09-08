import telebot, time
import conf
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from botapp.models import Users, Musics, TaskManager
import logging


ADMIN_ID = ""
logging.basicConfig(
            filename="logs.log",
            level=logging.INFO,
            format='%(asctime)s %(message)s ',
            datefmt='%Y-%m-%d-%H:%M:%S'
            )

TOKEN = "Your token here"
bot = telebot.TeleBot(
    token=TOKEN,
)   

ss = True

def check_user(id, name, message):
    some_id = Users.objects.filter(u_id=id,)
    if some_id.exists():
        
        IdOfUser = message.chat.id
        NameOfUser = message.chat.first_name

        IdOfNamedUser = list(some_id.values('u_id'))[0]['u_id']
        NameOfNamedUser = list(some_id.values('name'))[0]['name']

        if NameOfUser != NameOfNamedUser and int(IdOfNamedUser) == int(IdOfUser):
            Users.objects.filter(name=NameOfNamedUser, u_id=IdOfNamedUser).update(name=NameOfUser, u_id=IdOfUser)
            logging.info(f'{NameOfUser} updated to {NameOfUser}')
        else:
            pass
    else:
        Users.objects.create(name=message.chat.first_name, u_id=message.chat.id)
        logging.info(f'{message.chat.first_name} created')
            
@bot.message_handler(commands=['start'])
def start(message):
    check_user(message.chat.id, message.chat.first_name, message)
    bot.send_message(
        message.chat.id,
        text="Qo'shiqchi yoki qo'shiq nomini yozing va men siz uchun musiqalarni topib beraman!"
    )
@bot.message_handler(content_types=['audio'])
def welcome(message):

    try:
        music = Musics.music.filter(music_name=message.audio.title + f" {message.audio.performer}").exists()
        if music:
            bot.reply_to(message,
                     text=f"Musiqa qabul qilinmadi! \n\
                           Bir musiqani qayta qayta yuklab bo'lmaydi!")
        else:
            Musics.music.create(
                from_user=message.chat.first_name,
                music_name=message.audio.title + f" {message.audio.performer}",
                music_id=message.audio.file_id)
            bot.reply_to(
                message,
                text="Qo'shiq bazaga saqlandi!"
            )
    except Exception as e:
        pass
mes = []
mes1 = []

@bot.message_handler(content_types=['text'])
def search(message):
    global ss
    ss = Musics.music.filter(music_name__contains=message.text).values()
    if len(ss) != 0:
        mes.clear()
        mes1.clear()
        for i in ss[0:len(ss)]:
            mes.append([i['music_name'], i['id']])
        s, y=0, 9
        while True:
            if y<len(mes):
                mes1.append(list(mes[s:y+1]))
                s+=10
                y+=10
            else:
                mes1.append(list(mes[s:]))
                break
        
        
        main = InlineKeyboardMarkup()
        main.row_width = 5
        
        
        de = ""
        for j, i in enumerate(mes1[0], 1):
            main.add(InlineKeyboardButton(f'{j}',callback_data=f"{i[1]}"))

            de += f"{j}. {i[0]}\n"
            
        main.add(
        InlineKeyboardButton('⏮',callback_data=f"-1|1"),
        InlineKeyboardButton(text="❌", callback_data="del"),
        InlineKeyboardButton('⏭',callback_data=f"+1|1")
        )
        bot.send_message(
            message.chat.id,
            f"Natijalar {len(ss)} dan 1-10 \n\n{de}",
            reply_markup=main,
            
        )
    else:
        main1 = InlineKeyboardMarkup()
        main1.add(InlineKeyboardButton(text="❌", callback_data="del"),)
        bot.send_message(
            message.chat.id,
               "I can't found this music :(",
            reply_markup=main1
        )

markup_del = InlineKeyboardMarkup()
markup_del.add(InlineKeyboardButton(text="❌", callback_data="del_music"))

@bot.callback_query_handler(lambda call: True)
def send_music(call):
    if call.data == "del" or call.data == "del_music":
        bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
    elif call.data[0] == "-" or call.data[0] == "+":
        main = InlineKeyboardMarkup()
        main.row_width = 5
        full_data = call.data.split("|")
        num = int(full_data[1]) + int(full_data[0])
        if num > len(mes1):
            num = 1
        if num == 0:
            num = len(mes1)
        get_location = mes1[num-1]
        d = ''
        for i, j in enumerate(get_location, 1):
            main.add(InlineKeyboardButton(f'{i}',callback_data=f"{j[1]}"),)
            d += f"{i}. {j[0]}\n"
        main.add(InlineKeyboardButton(
            '⏮',callback_data=f"-1|{str(num)}"),
            InlineKeyboardButton(text="❌", callback_data="del"),
            InlineKeyboardButton('⏭',callback_data=f"+1|{str(num)}")
            )
        
        
        _from = 1
        _to = 10
        if num == 1:
            _from = 1
            _to = 10
        
        else:
            _from = (num-1) * 10
            _to = num * 10
        bot.edit_message_text(f'Natijalar {len(ss)} dan {_from}-{_to}\n\n{d}', 
        chat_id=call.message.chat.id, 
        message_id=call.message.message_id, 
        reply_markup=main, 
        disable_web_page_preview=True,)
    else:
        id = Musics.music.filter(id=call.data).first()
        bot.send_audio(
            call.message.chat.id,
            audio=id.music_id,
            reply_markup=markup_del
        )

bot.infinity_polling()
