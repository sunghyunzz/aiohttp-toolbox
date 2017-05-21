import unicodedata
from functools import partial
from typing import Optional, Union

import ujson
from aiohttp.web import json_response
from aiohttp.web_request import Request


JSONCompatible = Union[str, dict, list, set]


async def get_json(
    request: Request,
    unicode_normalizing_form: Optional[str]='NFKC'
) -> Optional[JSONCompatible]:
    raw_text = await request.text()

    if unicode_normalizing_form:
        raw_text = unicodedata.normalize(unicode_normalizing_form, raw_text)

    return ujson.loads(raw_text) if raw_text else None


jsonify = partial(json_response, dumps=ujson.dumps)
