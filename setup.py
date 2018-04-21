from setuptools import setup, find_packages


def readfile(filename):
    with open(filename, 'r+') as f:
        return f.read()


setup(
    name="ntx",
    version='0.1',
    url="https://github.com/medubin/ntx",
    license='Apache License 2.0',
    install_requires=[
        'urwid>=2.0.1',
    ],
    author="Matt Dubin",
    author_email="medubin@gmail.com",
    description="A note taking app for the terminal",
    long_description=readfile('README.md'),
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ntx = ntx.ntx:main'
        ]
    },
)