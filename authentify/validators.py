from django.core.validators import RegexValidator

username_validator = [
    RegexValidator(
        regex=r"^[a-zA-Z0-9_]{4,30}$",
        message="Username must be 4-30 characters long and contain only letters, numbers and underscores.",
    )
]
