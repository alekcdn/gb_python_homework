from aiogram import Bot, Dispatcher, executor, types
"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import csv

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5601609648:AAFPb916orpiq9AiT0hOe_wF-hsnz5fpVMo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# @dp.message_handler(regexp='(^cat[s]?$|puss)')
# async def cats(message: types.Message):
#     with open('data/cats.jpg', 'rb') as photo:
#         '''
#         # Old fashioned way:
#         await bot.send_photo(
#             message.chat.id,
#             photo,
#             caption='Cats are here 😺',
#             reply_to_message_id=message.message_id,
#         )
#         '''

#         await message.reply_photo(photo, caption='Cats are here 😺')
        
@dp.message_handler(commands=['calc'])
async def calc(message: types.Message):
    # await message.reply(f'Result')
    data = []
    bookreader = csv.reader([message.text], delimiter=' ', quotechar='"')

    for row in bookreader:
        data.append([row[0], row[1]])

    del data[0][0]
    # eval(data[0])
    await message.reply(f'Result =  {eval(data[0][0])}')
    
    # with open('data/cats.jpg', 'rb') as photo:
    #     '''
    #     # Old fashioned way:
    #     await bot.send_photo(
    #         message.chat.id,
    #         photo,
    #         caption='Cats are here 😺',
    #         reply_to_message_id=message.message_id,
    #     )
    #     '''

    #     await message.reply_photo(photo, caption='Cats are here 😺')
        
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)