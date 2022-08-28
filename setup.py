from setuptools import setup

setup(
    name="15-puzzle",
    version='1.0',
    py_modules=['15-puzzle'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        15-puzzle=game:cli
    ''',
)