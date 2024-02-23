import asyncio

from aiogram import Router, Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
import json
from aiohttp import ClientSession

router = Router()
router.message.filter(F.chat.type.in_(["supergroup", "group"]))


@router.message(F.text)
async def echo(message: Message) -> None:
    async with ClientSession() as session:
        await session.post(f"{open('link.txt').read()}/get-messages", json=json.dumps({"message": html.quote(message.text), "name": html.quote(message.from_user.first_name)}))


async def main() -> None:
    bot = Bot(open("token.txt").read().strip(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())