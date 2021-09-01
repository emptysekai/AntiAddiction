from typing import Union

from mcdreforged.api.types import CommandSource
from mcdreforged.api.rtext import RTextBase


def plug_in_fox(msg: Union[str, RTextBase]):
    def broadcast_msg(src: CommandSource):
        src.reply(msg)
    return broadcast_msg
