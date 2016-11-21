"""
aiohttp-ultrajson
-----------------

Integrates UltraJSON with your aiohttp application.
"""
from setuptools import setup

setup(
    name='aiohttp-ultrajson',
    version='0.0.1',
    url='https://github.com/sunghyunzz/aiohttp-ultrajson',
    license='MIT',
    author='sunghyunzz',
    author_email='me@sunghyunzz.com',
    description='Integrates UltraJSON with your aiohttp application.',
    long_description=__doc__,
    py_modules=['aiohttp_ultrajson'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'aiohttp',
        'ujson>=1.34'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)
