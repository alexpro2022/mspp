from . import emoji

BOT_SPEAKING = emoji.BABY_ANGEL + "\n\n"
GREETING = (
    BOT_SPEAKING + "{}, привет!\n\nЯ бот проекта ЗНАЧИМ. Я помогу тебе "
    "встать на путь наставничества - стать настоящим другом для ребенка "
    "или подростка" + emoji.KIDS + ", которому нужна помощь.\n\nСначала "
    "я помогу тебе выбрать фонд, а затем ты "
    "заполнишь " + emoji.WRITING_HAND + " небольшую анкету.")

WHAT_AGE = BOT_SPEAKING + "Сколько тебе лет, {}?"
REFUSAL = (
    BOT_SPEAKING + "{}, спасибо, что ты уже стремишься помогать другим "
    "людям " + emoji.CLAPPING_HANDS + ", но стать наставником ты сможешь "
    "только, когда тебе исполнится 18.\nА пока, я уверен, ты сможешь найти "
    "себя в другом волонтерском проекте. Удачи!!!" + emoji.OK)
WHAT_LOCATION = BOT_SPEAKING + "{}, в каком ты городе?"
CHOOSE_COUNTRY = BOT_SPEAKING + "{}, выбери страну"
CHOOSE_REGION = BOT_SPEAKING + "{}, выбери регион в стране: "
CHOOSE_CITY = BOT_SPEAKING + "{}, выбери город в твоем регионе: "
CHOOSE_FUND = BOT_SPEAKING + "{}, выбери фонд в твоем городе: "
CHOOSE_FUND_OR_CITY = BOT_SPEAKING + "{}, ты можешь выбрать региональный фонд или город в твоем регионе: "
PRESS_BUTTON_TO_FILL_FORM = (
    BOT_SPEAKING + "{}, нажми на кнопку ниже, чтобы заполнить "
    "анкету " + emoji.PRESS_BUTTON)
NO_FUND_MESSAGE = (
    BOT_SPEAKING + "{}, к сожалению на данный момент проект не реализуется "
    "в твоем городе или стране, но мы планируем развиваться! Напиши нам если "
    "знаешь благотворительный фонд, который занимается помощью детям-сиротам "
    "и детям, оставшимся без попечения родителей, чтобы мы запустили проект "
    "в твоем городе.")
NEW_FUND_REQUEST = (
    BOT_SPEAKING + "Спасибо! Я передал твою заявку. Поcтараемся запустить "
    "проект в твоем городе как можно скорее и обязательно свяжемся "
    "с тобой." + emoji.HANDSHAKE)

WARNING_NO_GOOGLE = (
    "\n\nПРЕДУПРЕЖДЕНИЕ: введенные данные не {will} отправлены, "
    "так как не установлены переменные окружения:\n\n{empty_env_vars}\n{conclusion}"
)
CONTINUE_FILLING_FORM = "Вы можете продолжить, чтобы проверить как работает заполнение формы."

CONFIRMATION_MESSAGE = BOT_SPEAKING + "{}, твои данные будут отправлены:\n\n"

FORMS_FILLING_FINISH = (
    BOT_SPEAKING + "{} cпасибо! Я передал твою заявку. Фонд свяжется с "
    "тобой, чтобы уточнить детали.")
