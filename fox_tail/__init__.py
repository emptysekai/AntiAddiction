from mcdreforged.api.types import PluginServerInterface
from mcdreforged.api.command import Literal
from mcdreforged.api.rtext import RText, RTextList, RColor, RAction

from fox_tail.plug import plug_in_fox


def on_load(server: PluginServerInterface, old):
    server.register_help_message('!!fox', server.tr('help_msg'))
    server.register_command(Literal('!!fox').runs(plug_in_fox(RTextList(
        '\\',
        RText(server.tr('fox'), RColor.gold)
        .h('Fallen_Breath')
        .c(RAction.open_url, 'https://github.com/Fallen-Breath'),
        server.tr('tail'), '/'
    ))))
