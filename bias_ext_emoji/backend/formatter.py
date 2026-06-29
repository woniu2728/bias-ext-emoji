import re


EMOJI_PATTERN = re.compile(r"(?<![\w/])(:\)|:D|:P|:\(|:\||;\)|:'\(|:O|>:\()")
EMOJI_MAP = {
    ":)": "\U0001f642",
    ":D": "\U0001f603",
    ":P": "\U0001f61b",
    ":(": "\U0001f641",
    ":|": "\U0001f610",
    ";)": "\U0001f609",
    ":'(": "\U0001f622",
    ":O": "\U0001f62e",
    ">:(": "\U0001f621",
}


def parse_emoticons(text: str) -> str:
    return EMOJI_PATTERN.sub(lambda match: EMOJI_MAP.get(match.group(1), match.group(1)), text or "")
