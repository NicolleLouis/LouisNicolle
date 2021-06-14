import collections.abc


class OptionService:
    @staticmethod
    def deep_update(option_1, option_2):
        for key, value in option_2.items():
            if isinstance(value, collections.abc.Mapping):
                option_1[key] = OptionService.deep_update(option_1.get(key, {}), value)
            else:
                option_1[key] = value
        return option_1
