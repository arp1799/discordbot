

import random
import json
import os

from settings import *


async def dm_user(member,message):
    if member is not None:
        channel=member.dm_channel
        if channel is None:
            channel=await member.create_dm()
        await channel.send(message)


############################ get momma jokes######################


async def get_momma_jokes():
    # print(os.path.join(DATA_DIR,"jokes.json"))
    with open(os.path.join(DATA_DIR,"jokes.json"),encoding='utf-8') as joke_file:
        jokes=json.load(joke_file)
        random_cat=random.choice(list(jokes.keys()))
        insult=random.choice(list(jokes[random_cat]))
        return insult



##################### text-to-owo #####################


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))

    return text