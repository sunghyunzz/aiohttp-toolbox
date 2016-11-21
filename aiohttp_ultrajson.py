import unicodedata
from typing import Any, Optional, Union

import ujson
from aiohttp.web import Response
from aiohttp.web_reqrep import Request


async def get_json(request: Request) -> Optional[Any]:
    raw_text = await request.text()
    unicode_normalized_text = unicodedata.normalize('NFKC', raw_text)

    return ujson.loads(unicode_normalized_text) \
        if unicode_normalized_text else None


def jsonify(
    data: Union[str, dict, list, set],
    status: int = 200,
    content_type: str = 'application/json'
) -> Response:
    return Response(
        text=ujson.dumps(data),
        status=status,
        content_type=content_type
    )
