# aiohttp-UltraJSON

[![PyPI version](https://badge.fury.io/py/aiohttp-ultrajson.svg)](https://badge.fury.io/py/aiohttp-ultrajson) [![PyPI](https://img.shields.io/pypi/status/aiohttp-ultrajson.svg)](https://badge.fury.io/py/aiohttp-ultrajson) [![PyPI](https://img.shields.io/pypi/pyversions/aiohttp-ultrajson.svg)](https://badge.fury.io/py/aiohttp-ultrajson) [![PyPI](https://img.shields.io/pypi/l/aiohttp-ultrajson.svg)](https://badge.fury.io/py/aiohttp-ultrajson)

Integrates [UltraJSON](https://github.com/esnme/ultrajson) with your [aiohttp](https://github.com/KeepSafe/aiohttp) application.

## Installation

```bash
pip install aiohttp-ultrajson
```

## Usage

```python
from aiohttp_ultrajson import get_json, jsonify


async def handle(request):
    data = await get_json(request)
    return jsonify({'data': data})
```
