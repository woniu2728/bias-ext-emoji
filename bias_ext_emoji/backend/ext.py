from bias_ext_emoji.backend.extenders import (
    formatting_extenders,
    frontend_extenders,
    lifecycle_extenders,
    settings_extenders,
)


def extend():
    return [
        *frontend_extenders(),
        *settings_extenders(),
        *formatting_extenders(),
        *lifecycle_extenders(),
    ]
