from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")
kb.row(button, button2, button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.row(button3, button4)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product2', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product3', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product4', callback_data="product_buying")]
    ]
)
kb3.row()

class UserState(StatesGroup):
    start = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(text='Привет, я бот помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer('Информация о боте!')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    with open("1.jpg", "rb") as img:
        await message.answer_photo(img, f'Название: Витамин Fe, Описание: Витамин железо, Цена: {1 * 100}')
    with open("2.jpg", "rb") as img:
        await message.answer_photo(img, f'Название: Мультивитамины, Описание: Витаминный комплекс, Цена: {2 * 100}')
    with open("3.jpg", "rb") as img:
        await message.answer_photo(img, f'Название: Витамин B9, Описание: Фолиевая кислота, Цена: {3 * 100}')
    with open("4.jpg", "rb") as img:
        await message.answer_photo(img, f'Название: Витамин D, Описание: Рыбный жир, Цена: {4 * 100}')
    await message.answer("Выберите продукт для покупки:", reply_markup=kb3)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора для женщин: 10 x вес (кг) + 6,25 x рост (см) –\
     5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer("Введите свой возраст: ")
    await call.answer()
    await UserState.age.set()


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer("Введите свой рост: ")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer("Введите свой вес: ")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    norma = 10 * int(data['third']) + 6.25 * int(data['second']) - 5 * int(data['first']) - 161
    await message.answer(f"Ваша норма калорий {norma} ккал")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
