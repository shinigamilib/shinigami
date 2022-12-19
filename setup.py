"""
    Owner: Shinigamilib (https://github.com/shinigamilib)
    Project: Shinigami (Python)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "shinigami",
    version = "0.1.10",
    author = "Hifumi1337",
    description = "Shinigami is an open source Python library allowing the user to generate and build Dockerfiles during runtime",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shinigamilib/shinigami-py",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    packages = [
        "shinigami"
    ],
    python_requires = ">=3.6"
)