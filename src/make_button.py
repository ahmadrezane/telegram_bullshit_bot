from types import SimpleNamespace

import emoji
from telebot import types


def make_btn(*keys, row_width=1, resize_keyboard=True):
    markup = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    btn = map(types.KeyboardButton, keys)
    markup.add(*btn)
    return markup

keys = SimpleNamespace(
    hello='hi',
    goodbye='bye',
    ok='ok',
    back='Back:BACK_arrow:',
    very_good = 'Very good:smiling_face:',
    good = 'Good:smiling_face_with_smiling_eyes:',
    bad = 'Bad:face_with_head-bandage:'
)

keyboard = SimpleNamespace(
    main=make_btn(keys.hello, keys.goodbye, keys.ok),
    second=make_btn(emoji.emojize(keys.back)),
    first=make_btn(
        emoji.emojize(keys.very_good),
         emoji.emojize(keys.good),
          emoji.emojize(keys.bad)
    )

)
