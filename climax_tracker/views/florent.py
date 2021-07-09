from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from climax_tracker.repository.profile_repository import ProfileRepository
from stats.service.time_service import TimeService


class FlorentView(APIView):
    florent_id = 3
    florent_life_expectancy_year = 53
    florent_weight = 70
    climax_weight = 0.032
    repository = ProfileRepository

    def get(self, request, *args, **kwargs):
        data = {}
        profile_florent = self.repository.get_by_id(self.florent_id)
        total_climax_eaten = profile_florent.climax_eaten
        data["total_climax_eaten"] = total_climax_eaten

        total_debt = round(self.florent_weight / self.climax_weight)
        data["total_debt"] = total_debt

        remaining_climax = total_debt - total_climax_eaten
        data["remaining_climax"] = remaining_climax

        remaining_percentage = 100 * round(remaining_climax / total_debt, 2)
        data["remaining_percentage"] = remaining_percentage

        florent_life_expectancy_seconds = TimeService.year_to_seconds(self.florent_life_expectancy_year)
        climax_per_second = round(florent_life_expectancy_seconds/total_debt)
        climax_frequency = TimeService.seconds_to_higher_timelapse(
            climax_per_second
        )
        data["climax_frequency"] = climax_frequency

        florent_start_of_debt = profile_florent.created_at
        debt_time = TimeService.seconds_from_now(florent_start_of_debt)
        theoretical_number_of_climax_eaten = round(debt_time * total_debt / florent_life_expectancy_seconds)
        data["theoretical_number_of_climax_eaten"] = theoretical_number_of_climax_eaten

        return Response(data, status=status.HTTP_200_OK)
