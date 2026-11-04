from django.core.exceptions import ValidationError
def validate_name(value):
    if len(value) < 5:
        raise ValidationError(f"{value}s must be more than 5 symbols")


class NameValidator:
    message = "must be more than 5 symbols"
    def __call__(self, value):
        if len(value) < 5:
            raise ValidationError(value + self.message)