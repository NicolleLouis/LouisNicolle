from django.contrib import admin

from aeon.models.card import Card
from aeon.models.card_admin import CardAdmin
from aeon.models.extension import Extension, ExtensionAdmin
from aeon.models.game import Game
from aeon.models.game_admin import GameAdmin
from aeon.models.mage import Mage
from aeon.models.mage_admin import MageAdmin
from aeon.models.nemesis import Nemesis
from aeon.models.nemesis_admin import NemesisAdmin

admin.site.register(Card, CardAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Mage, MageAdmin)
admin.site.register(Nemesis, NemesisAdmin)

admin.site.disable_action('delete_selected')
