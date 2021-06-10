class ModelService:
    @staticmethod
    def get_model_field_names(model):
        all_fields = model._meta.get_fields()
        all_field_name = list(
            map(
                lambda field: field.name,
                all_fields
            )
        )
        return all_field_name

    @staticmethod
    def get_model_app_name(model):
        return model._meta.app_label
