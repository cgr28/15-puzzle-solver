from setuptools import setup

setup(
    name="slide-puzzle",
    version='1.0',
    py_modules=['slide-puzzle'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        slide-puzzle=game:cli
    ''',
)