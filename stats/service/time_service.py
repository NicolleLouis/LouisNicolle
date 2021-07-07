from datetime import datetime, timezone


class TimeService:
    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60

    @staticmethod
    def year_to_seconds(years):
        return years * \
               TimeService.days_in_year * \
               TimeService.hours_in_day * \
               TimeService.minutes_in_hour * \
               TimeService.seconds_in_minute

    @staticmethod
    def seconds_to_higher_timelapse(seconds):
        return {
            "seconds": round(
                seconds
            ),
            "minutes": round(
                seconds / TimeService.seconds_in_minute
            ),
            "hours": round(
                seconds / (TimeService.seconds_in_minute * TimeService.minutes_in_hour))
            ,
            "days": round(
                seconds / (
                        TimeService.seconds_in_minute *
                        TimeService.minutes_in_hour *
                        TimeService.hours_in_day)
            ),
            "years": round(
                seconds / (
                        TimeService.seconds_in_minute *
                        TimeService.minutes_in_hour *
                        TimeService.hours_in_day *
                        TimeService.days_in_year)
            ),
        }

    @staticmethod
    def seconds_from_now(date):
        current_date = datetime.now(timezone.utc)
        return (current_date - date).seconds
