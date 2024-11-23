from aiogram.dispatcher.filters.state import StatesGroup,State


class KinoAddState(StatesGroup):
    kino_add=State()
    kino_kod=State()


class KinoDeleteState(StatesGroup):
    kino_kod=State()
    is_confirm=State()

class EditCap(StatesGroup):
    ID=State()
    caption=State()

class SearchName(StatesGroup):
    waiting=State()
class Search(StatesGroup):
    waiting=State()

class SorovSearch(StatesGroup):
    nomi=State()
    janr=State()
    yil=State()
    davlat=State()
    kinopoisk=State()

