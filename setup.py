import os

from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='discord-api-wrapper',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple wrapper for the Discord API with async support.',
    url='https://www.github.com/jwestern1337/discord-api-wrapper',
    author='jwestern1337',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
        'requests'
    ]
)
