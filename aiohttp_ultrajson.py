import re
import unicodedata
from functools import partial
from typing import Optional, Union

import ujson
from aiohttp.web import json_response
from aiohttp.web_request import Request

FULL_WIDTH_HANDLING_MAP = {
    '＂': r'\\\"',
    '＼': r'\\\\'
}
FULL_WIDTH_HANDLING_REGEX = re.compile('[＂＼]')
JSONCompatible = Union[str, dict, list, set]


def _escape_text(text: str) -> str:
    return FULL_WIDTH_HANDLING_REGEX.sub(
        lambda match: FULL_WIDTH_HANDLING_MAP[match.group()],
        text
    )


async def get_json(
    request: Request,
    unicode_normalizing_form: Optional[str]='NFKC'
) -> Optional[JSONCompatible]:
    raw_text = await request.text()

    if unicode_normalizing_form:
        raw_text = unicodedata.normalize(
            unicode_normalizing_form,
            _escape_text(raw_text)
        )

    return ujson.loads(raw_text) if raw_text else None


jsonify = partial(json_response, dumps=ujson.dumps)
