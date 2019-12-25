from setuptools import setup

setup(
    name='whispers',
    version='0.1',
    py_modules=['whispers'],
    install_requires=[
        'Click',
        'profanity-check',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        whispers=whispers:cli
    ''',
)