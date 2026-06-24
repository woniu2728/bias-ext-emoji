from django.apps import AppConfig

class EmojiExtensionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bias_ext_emoji.backend"
    label = "emoji"
