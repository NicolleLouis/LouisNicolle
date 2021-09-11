from django.contrib import admin

from celauco.models.board import Board, BoardAdmin

admin.site.register(Board, BoardAdmin)
