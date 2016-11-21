# aiohttp-UltraJSON

[![PyPI version](https://badge.fury.io/py/aiohttp-ultrajson.svg)](https://badge.fury.io/py/aiohttp-ultrajson) [![python3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/)

Integrates [UltraJSON](https://github.com/esnme/ultrajson) with your [aiohttp](https://github.com/KeepSafe/aiohttp) application.

## Installation

```sh
pip install aiohttp-ultrajson
```

## Usage

```python
from aiohttp_ultrajson import get_json, jsonify


async def index(request):
    data = await get_json(request)
    return jsonify({
        'data': data
    })
```
