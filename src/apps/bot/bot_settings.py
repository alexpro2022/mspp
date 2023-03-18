# EMOJI ======================================================
BABY_ANGEL = " \U0001F47C "
THUMBS_UP = " \U0001F44D "
CLAPPING_HANDS = " \U0001F44F "
GO_LEFT = " \U0001F448 "
GO_RIGHT = " \U0001F449 "
BABY = " \U0001F476 "
BOOK_EMOJI = " \U0001F4D6 "
BOY = " \U0001F466 "
GIRL = " \U0001F467 "
TEENS = " \U0001F467\U0001F466 "
GROWING_HEART = " \U0001F497 "
WRITING_HAND = " \U0000270D "
HANDSHAKE = " \U0001F91D "
SHRUGGING = " \U0001F937 "
RAINING_EMOJI = " \U000026C8 "
MOSCOW_EMOJI = " \U0001F4AA "
REGIIONS_EMOJI = " \U00002708 "
OUTSIDE_EMOJI = " \U0001F30D \U0001F30E \U0001F30F "
MOSCOW_REGION_EMOJI = " \U0001F6E3 "
KAZAHSTAN_EMOJI = " \U0001F40E "
DESERT_ISLAND_EMOJI = " \U0001F3DD "
MOUNTAIN_EMOJI = " \U0001F304 "
SNOWFLAKE_EMOJI = " \U00002744 "
CLOUDY_EMOJI = " \U0001F324 "
OTHER_REGIONS_EMOJI = CLOUDY_EMOJI + SNOWFLAKE_EMOJI
FINISH = " \U0001F3C1 "
SMILE = " \U0001F601 "
NUMB = " \U0001F607 "
SUNGLASSES = " \U0001F60E "

# TEXT CONSTANTS =========================================================
APPLICATION_FORM_TEXT = "{}, давай заполним анкету" + WRITING_HAND
APPLY_FORM_BUTTON_TEXT = "Готово" + FINISH

# CONVERSATION ===========================================================
USERNAME = "To be implemented"
MAIN_CONVERSATION = "Главная ветка беседы"
BOT_SPEAKING = BABY_ANGEL + "\n\n"
GREETING = (
    "{}, привет!\n\nЯ" + BABY_ANGEL + "бот проекта ЗНАЧИМ. Я помогу тебе встать на путь "
    "наставничества - стать настоящим другом для ребенка или подростка" + TEENS
    + ", которому нужна помощь.\n\nСначала я помогу тебе выбрать фонд, а затем заполнить "
    + WRITING_HAND + "небольшую анкету."
)
REFUSAL = (
    BOT_SPEAKING + "{}, спасибо, что ты уже стремишься помогать другим людям "
    + CLAPPING_HANDS + ", но стать наставником ты сможешь только, когда тебе "
    "исполнится 18. А пока, я уверен, ты сможешь найти себя в другом "
    "волонтерском проекте. Удачи!!!" + THUMBS_UP
)
WHAT_AGE = BOT_SPEAKING + "Сколько тебе лет, {}?"
WHAT_LOCATION = BOT_SPEAKING + "{}, в каком ты городе?"
PRESS_BUTTON_TO_FILL_FORM = BOT_SPEAKING + "Нажми на кнопку ниже, чтобы заполнить анкету"
START_PROJECT_REQUEST = (
    BOT_SPEAKING + "Спасибо! Я передал твою заявку. Поcтараемся запустить проект в "
    "твоем городе как можно скорее и обязательно свяжемся с тобой." + HANDSHAKE)
CHOOSE_COUNTRY = BOT_SPEAKING + "Выбери страну"
CHOOSE_REGION = BOT_SPEAKING + "Выбери регион"
CHOOSE_CITY = BOT_SPEAKING + "Выбери город"
CHOOSE_FUND = BOT_SPEAKING + "Фонды, доступные в твоем городе:"
NO_CITY = "Нет моего города"
NO_FUND_MESSAGE = (
    BOT_SPEAKING + "{}, к сожалению на данный момент проект не реализуется в твоем городе или стране, но "
    "мы планируем развиваться! Напиши нам если знаешь благотворительный "
    "фонд, который занимается помощью детям-сиротам и детям, оставшимся "
    "без попечения родителей, чтобы мы запустили проект в твоем городе."
)

# LOCATIONS ======================================================
LOCATION = "location"
COUNTRY = "country"
REGION = "region"
CITY = "city"
MSK = "Москва"
MSK_reg = "Московская область"
SPB = "Санкт-Петербург"
TWO_CAPITALS = (MSK, MSK_reg, SPB)
# TWO_CAPITALS = ("Москва", "Московская область", "Санкт-Петербург")
KAZAHSTAN = "Казахстан"
# FUNDS =======================================================
FUND = "fund"
NO_FUND = "no_fund"
NEW_FUND = "new_fund"
ARITHMETIC = (
    "Арифметка добра - помогает детям-сиротам стать личностью, "
    "поддерживает приемные семьи, содействует семейному устройству.")
OLD_BROTHERS = (
    "Старшие братья старшие сестры - подбирает наставников детям и "
    "подросткам, находящихся в трудной жизненной ситуации.")
IN_YOUR_HANDS = (
    "В твоих руках - помогает подросткам, оставшимся без поддержки "
    "родителей, подготовиться к самостоятельной жизни.")
VOLONTIERS = (
    "Волонтеры в помощь детям-сиротам - помогает детям сиротам в "
    "детских домах и больницах, ищет им приемных родителей и "
    "поддерживает семьи в трудной жизненной ситуации.")
KIDS_PLUS = (
    "Дети+ - оказывает поддержку детям, подросткам и молодым людям с "
    "ВИЧ, семьям, в которых живут дети с ВИЧ.")
OUR_KIDS = (
    "Дети наши - помогает в социальной адаптации воспитанников "
    "детских домов, поддерживает кризисные семьи.")
SUN_CITY = (
    "Солнечный город - помогает детям и семьям, которые оказались "
    "в трудной жизненной ситуации.")
FUNDS_TEXT = (
    BOT_SPEAKING + ARITHMETIC,
    OLD_BROTHERS,
    IN_YOUR_HANDS,
    VOLONTIERS,
    KIDS_PLUS,
    OUR_KIDS,
    SUN_CITY,)
FUNDS_INFO_SEPARATOR = "\n{} {} {}\n".format(GROWING_HEART, GROWING_HEART, GROWING_HEART)
FUNDS_DESCRIPTION = FUNDS_INFO_SEPARATOR.join(FUNDS_TEXT)

NEW_FUND_CONFIRM_MESSAGE = "Да, давай" + THUMBS_UP
NEW_FUND_FORM = "new_fund_form"

# BUTTONS ==========================================================
OK = "Понятно" + THUMBS_UP
FILL_FORM_BUTTON_TEXT = "Заполнить анкету"

# MISC =============================================================
AGE_LIMIT = 18
AGE = "age"
NAME = "name"
URL = "URL"


class CallbackQueries:
    STACK = "STACK"
    GO_BACK = "go_back"
    SHORT_BACK_BUTTON = (GO_LEFT, GO_BACK)
    LONG_BACK_BUTTON = (GO_LEFT + "Назад", GO_BACK)
# --------------------------------------------------
    GET_AGE = "get_age"
    CHECK_AGE = "check_age"
# --------------------------------------------------
    GET_LOCATION = "get_location"
# --------------------------------------------------
    OTHER_COUNTRY_TEXT = "Я не в России" + OUTSIDE_EMOJI
    OTHER_COUNTRY = "Другая страна" + DESERT_ISLAND_EMOJI
    GET_COUNTRY = "get_country"
    CHECK_COUNTRY = "check_country"
    BUTTON_OTHER_COUNTRY = (OTHER_COUNTRY_TEXT, GET_COUNTRY)
    # BUTTON_OTHER_COUNTRY_NO_FUND = (OTHER_COUNTRY, NO_FUND + OTHER_COUNTRY)
# --------------------------------------------------
    NO_MY_REGION_TEXT = "Нет моего региона" + SHRUGGING
    OTHER_REGION = "Выбрать другой регион" + OTHER_REGIONS_EMOJI
    GET_REGION = "get_region"
    CHECK_REGION = "check_region"
    BUTTON_OTHER_REGION = (OTHER_REGION, GET_REGION)
# --------------------------------------------------
    NO_MY_CITY_TEXT = "Нет моего города" + SHRUGGING
    OTHER_CITY = GO_LEFT + "Выбрать другой город"
    GET_CITY = "get_city"
    CHECK_CITY = "check_city"
    BUTTON_OTHER_CITY = (OTHER_CITY, GET_LOCATION)
# --------------------------------------------------
    OTHER_FUND = "Выбрать другой фонд"
    GET_FUND = "get_fund"
    CHECK_FUND = "check_fund"
    GET_FUNDS_INFO = "funds_info"
    GET_APPLICATION_FORM = "get_application_form"
    FUNDS_INFO_TEXT = "Про фонды" + BOOK_EMOJI
    BUTTON_OTHER_FUND = (OTHER_FUND, GET_FUND)
    NO_FUND = "no_fund"
    SEND_SPREADSHEET = "send_spreadsheet"
# --------------------------------------------------


TEST_DATA = (
    ("TEST", "TEST"),
    ("TEST", "TEST"),
    ("TEST", "TEST"),
    ("TEST", "TEST"),
    ("TEST", "TEST"),
)


'''
    {
        "age_limit": {"from_age": 18, "to_age": null},
        "coverage_area": ["Екатеринбург", "Зеленоградск", "Калининград", "Москва", "Московская область", "Санкт-Петербург"],
        "description": "Старшие братья старшие сестры - подбирает наставников детям и подросткам, находящихся в трудной жизненной ситуации.",
        "name": "Старшие братья старшие сестры"
    }


    "Арифметка добра - помогает детям-сиротам стать личностью, "
    "поддерживает приемные семьи, содействует семейному устройству.",

    "Старшие братья старшие сестры - подбирает наставников детям и "
    "подросткам, находящихся в трудной жизненной ситуации.",

    "В твоих руках - помогает подросткам, оставшимся без поддержки "
    "родителей, подготовиться к самостоятельной жизни.",

    "Волонтеры в помощь детям-сиротам - помогает детям сиротам в "
    "детских домах и больницах, ищет им приемных родителей и "
    "поддерживает семьи в трудной жизненной ситуации.",

    "Дети+ - оказывает поддержку детям, подросткам и молодым людям с "
    "ВИЧ, семьям, в которых живут дети с ВИЧ.",

    "Дети наши - помогает в социальной адаптации воспитанников "
    "детских домов, поддерживает кризисные семьи.",

    "Солнечный город - помогает детям и семьям, которые оказались в трудной жизненной ситуации.",
)

'''
