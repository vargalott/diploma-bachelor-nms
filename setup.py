"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="diploma_bachelor_nms",
    author="vargalott",
    url="https://github.com/vargalott/diploma-bachelor-nms",
    description="simple web server for diploma-bachelor module:network",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "setuptools>=45.0",
        "falcon>=3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "diploma-bachelor-nms=diploma-bachelor-nms.__main__:main",
        ]
    },
)
