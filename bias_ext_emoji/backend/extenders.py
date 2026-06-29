from pathlib import Path

from bias_core.extensions import FormatterExtender, FrontendExtender, LifecycleExtender, LocalesExtender, SettingsExtender, setting_field

from bias_ext_emoji.backend.formatter import parse_emoticons


def _extension_root() -> Path:
    return Path(__file__).resolve().parents[2]


def frontend_extenders():
    return (
        FrontendExtender(
            forum_entry="extensions/emoji/frontend/forum/index.js",
        ),
        LocalesExtender(paths=(str(_extension_root() / "locale"),)),
    )


def settings_extenders():
    return (
        SettingsExtender(fields=(
            setting_field({
                "key": "cdn_url",
                "label": "Twemoji CDN",
                "type": "text",
                "default": "",
                "placeholder": "留空时使用默认 Twemoji CDN",
                "help_text": "用于覆盖表情图片资源地址。",
                "order": 10,
            }),
        ), expose_to_forum=("cdn_url",))
        .default("cdn_url", "https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/")
        .reset_when("cdn_url", lambda value: not str(value or "").strip())
        .reset_frontend_cache_for("cdn_url")
        .theme_variable("bias-emoji-cdn", "cdn_url"),
    )


def formatting_extenders():
    return (
        FormatterExtender().parse(parse_emoticons),
    )


def lifecycle_extenders():
    return (LifecycleExtender(),)
