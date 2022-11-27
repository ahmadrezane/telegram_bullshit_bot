from telebot import types
from types import SimpleNamespace
import emoji

def make_btn(*keys, row_width=1, resize_keyboard=True):
    markup = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    btn = map(types.KeyboardButton, keys)
    markup.add(*btn)
    return markup

keys = SimpleNamespace(
    hello='hi',
    goodbye='bye',
    ok='ok',
    back='back',
    very_good = 'Very good',
    good = 'Good',
    bad = 'Bad'
)

keyboard = SimpleNamespace(
    main=make_btn(keys.hello, keys.goodbye, keys.ok),
    second=make_btn(keys.back),
    first=make_btn(keys.very_good, keys.good, keys.bad)

)
