import asynctest
from aiohttp.web_request import Request
from asynctest import mock

from aiohttp_ultrajson import get_json


class TestViews(asynctest.TestCase):

    async def test_get_json(self) -> None:
        cases = [
            (
                '{"data": "（）"}',
                {'data': '()'}
            ),
            (
                '{"data": "※＂＂　"}',
                {'data': '※\\\"\\\" '}
            ),
            (
                '{"data": "＼"}',
                {'data': '\\\\'}
            )
        ]

        for raw_text, expected_text in cases:
            mock_request: Request = mock.Mock(spec=Request)
            mock_request.text = asynctest.CoroutineMock(return_value=raw_text)

            result = await get_json(mock_request)

            self.assertEqual(result, expected_text)
