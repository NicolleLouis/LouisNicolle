from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from aeon.repository.mage_repository import MageRepository

from graph.views.pie_chart_view import PieChartView
from stats.service.utils import Utils


class MagePopularityData(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        graph = MagePopularityGraph()
        return Response(graph.generate_chart(), status=status.HTTP_200_OK)


class MagePopularityGraph(PieChartView):
    def __init__(self):
        super().__init__()
        mage, popularity = self.split_database_data(
            self.get_database_data()
        )
        self.mage = mage
        self.popularity = popularity
        self.mage_popularity_datasource = "Mage Popularity"

    def get_x_labels(self):
        return self.mage

    def get_data(self):
        return {
            self.mage_popularity_datasource: self.popularity,
        }

    @staticmethod
    def get_database_data():
        mage_popularity = []
        other_popularity = 0
        mages = MageRepository.get_queryset()
        total_game_number = sum(
            map(
                lambda mage: mage.game_number,
                mages
            )
        )
        if total_game_number == 0:
            raise SystemError("Total game number is 0")
        for mage in mages:
            popularity = Utils.ratio_to_percentage(mage.game_number / total_game_number)
            if popularity < 2:
                other_popularity += popularity
            else:
                mage_popularity.append({
                    "mage": mage.name,
                    "popularity": popularity,
                })
        if other_popularity > 0:
            mage_popularity.append({
                "mage": "Others",
                "popularity": other_popularity,
            })
        mage_popularity.sort(
            key=lambda mage: mage["popularity"],
            reverse=True
        )
        return mage_popularity

    @staticmethod
    def split_database_data(database_data):
        mage = list(
            map(
                lambda nemesis_data: nemesis_data["mage"],
                database_data
            )
        )
        popularity = list(
            map(
                lambda nemesis_data: nemesis_data["popularity"],
                database_data
            )
        )
        return mage, popularity
