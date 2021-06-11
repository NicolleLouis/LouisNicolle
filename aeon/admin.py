from django.contrib import admin

from aeon.models.card import Card, CardAdmin
from aeon.models.extension import Extension, ExtensionAdmin
from aeon.models.game import Game, GameAdmin
from aeon.models.mage import Mage, MageAdmin
from aeon.models.nemesis import Nemesis, NemesisAdmin

admin.site.register(Card, CardAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Mage, MageAdmin)
admin.site.register(Nemesis, NemesisAdmin)
