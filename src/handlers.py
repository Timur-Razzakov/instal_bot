from src.bot import create_quick_replies, send_message

user_states = {}


def handle_message(sender_id, message_text):
    if sender_id not in user_states:
        send_language_choice(sender_id)
        user_states[sender_id] = 'choose_language'
    elif user_states[sender_id] == 'choose_language':
        if message_text == 'O‘zbek tili':
            send_uzbek_menu(sender_id)
            user_states[sender_id] = 'uzbek_menu'
        elif message_text == 'Русский язык':
            send_russian_menu(sender_id)
            user_states[sender_id] = 'russian_menu'
    elif user_states[sender_id] == 'russian_menu':
        handle_russian_menu(sender_id, message_text)
    elif user_states[sender_id] == 'uzbek_menu':
        handle_uzbek_menu(sender_id, message_text)


def send_language_choice(sender_id):
    message = "Assalomu alaykum! Tilni tanlang\nЗдравствуйте! Выберите язык"
    options = ["O‘zbek tili", "Русский язык"]
    quick_replies = create_quick_replies(options)
    send_message(sender_id, message, quick_replies)


def send_russian_menu(sender_id):
    message = "Привет, на связи Xalq! Что вы хотели бы узнать?"
    options = [
        "Стоимость доставки из Китая",
        "Сроки доставки",
        "Как сделать заказ?",
        "Минимальный вес заказа",
        "Шаг округления",
        "Позвонить",
        "Связаться с менеджером"
    ]
    quick_replies = create_quick_replies(options)
    send_message(sender_id, message, quick_replies)


def send_uzbek_menu(sender_id):
    message = "Salom, Xalq aloqada! Qanday ma'lumotni bilishni xohlaysiz?"
    options = [
        "Xitoydan yetkazib berish narxi",
        "Xitoydan yetkazib berish muddati",
        "Qanday qilib buyurtma berish kerak?",
        "Buyurtmaning minimal og‘irligi",
        "Yaxlitlash shartlari",
        "Qo‘ng‘iroq qilish",
        "Menejer bilan bog‘lanish"
    ]
    quick_replies = create_quick_replies(options)
    send_message(sender_id, message, quick_replies)


def handle_russian_menu(sender_id, message_text):
    if message_text == 'Стоимость доставки из Китая':
        send_message(sender_id,
                     "На данный момент стоимость доставки из Китая в Узбекистан составляет 5,5$ за кг.")
    elif message_text == 'Сроки доставки':
        send_message(sender_id,
                     "В среднем заказы по направлению Китай - Узбекистан доставляются от 15 до 20 дней.")
    elif message_text == 'Как сделать заказ?':
        send_message(sender_id,
                     "Для оформления заказа нужно перейти на наш сайт xalq.global. Сначала нужно "
                     "зарегистрироваться, а затем оформить заказ.")
    elif message_text == 'Минимальный вес заказа':
        send_message(sender_id,
                     "Минимальный вес заказа составляет 1кг. Например: если ваша посылка весит 700гр, "
                     "она будет рассчитываться по минимальному весу, как 1кг.")
    elif message_text == 'Шаг округления':
        send_message(sender_id,
                     "Шаг округления + 100гр. Например: если ваша посылка весит 1кг 290гр, "
                     "то рассчитываться она будет как 1кг 300гр.")
    elif message_text == 'Позвонить':
        send_message(sender_id, "Вы всегда можете позвонить нам по номеру: +998 78 113 85 55")


def handle_uzbek_menu(sender_id, message_text):
    if message_text == 'Xitoydan yetkazib berish narxi':
        send_message(sender_id,
                     "Ayni paytda Xitoydan O‘zbekistonga yetkazib berish narxi bir kg uchun 5,5 dollarni "
                     "tashkil etadi.")
    elif message_text == 'Xitoydan yetkazib berish muddati':
        send_message(sender_id,
                     "Xitoy-O‘zbekiston yo'nalishi bo'yicha buyurtmalar o‘rtacha 15 dan 20 kungacha "
                     "yetkazib beriladi.")
    elif message_text == 'Qanday qilib buyurtma berish kerak?':
        send_message(sender_id,
                     "Buyurtma berish uchun siz bizning xalq.global veb-saytimizga o‘tishingiz kerak. Avval "
                     "ro’yxatdan o‘tib, keyin buyurtma berishingiz kerak.")
    elif message_text == 'Buyurtmaning minimal og‘irligi':
        send_message(sender_id,
                     "Buyurtmaning minimal og‘irligi 1kg. Masalan: agar posilkangiz 700g bo'lsa, u minimal "
                     "og'irlik bo'yicha 1kg sifatida hisoblanadi.")
    elif message_text == 'Yaxlitlash shartlari':
        send_message(sender_id,
                     "Yaxlitlash shartlari + 100gr. Masalan: agar posilkangiz 1kg 290g bo'lsa, u 1kg 300g "
                     "sifatida hisoblanadi.")
    elif message_text == 'Qo‘ng‘iroq qilish':
        send_message(sender_id, "Istalgan vaqtda bizga qo‘ng‘iroq qilishingiz mumkin: +998 78 113 85 55")
