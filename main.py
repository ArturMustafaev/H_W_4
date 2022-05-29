from aiogram.utils import executor
from config import dp
from hendlers import admin, client, callback, extra, fsm_anketa, fsmadminmenu, inline
import logging
from database import bot_db, menu


async def on_startup(_):
    bot_db.sql_create()
    menu.sql_create()


client.register_handler_client(dp)
admin.register_handlers_admin(dp)
callback.register_habdler_callback(dp)
inline.register_handler_inline(dp)
fsmadminmenu.register_hendler_fsmadminmenu(dp)
fsm_anketa.register_hendler_fsmanketa(dp)
extra.register_hendler_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
