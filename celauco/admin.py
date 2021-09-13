from django.contrib import admin

from celauco.models.board import Board, BoardAdmin
from celauco.models.game_result import GameResult, GameResultAdmin

admin.site.register(Board, BoardAdmin)
admin.site.register(GameResult, GameResultAdmin)
