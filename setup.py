# coding: utf-8

"""
    Channel API

    Front is a customer operations platform that enables support, sales, and account management teams to deliver exceptional service at scale. Front streamlines customer communication by combining the efficiency of a help desk and the familiarity of email, with automated workflows and real-time collaboration behind the scenes.  With Front, teams can centralize messages across channels, route them to the right person, and unlock visibility and insights across all of their customer operations. More than 8000 businesses use Front to drive operational efficiency that prevents churn, improves retention, and propels customer growth.

    The version of the OpenAPI document: 1.0.0
    Created by: https://community.front.com
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "front-channel-python-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

REQUIRES = [
    "certifi >= 2023.7.22",
    "python-dateutil ~= 2.8.2",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.18",
    "cryptography ~= 42.0.5",
    "frozendict ~= 2.3.4",
    "aiohttp ~= 3.9.2",
    "pydantic ~= 2.4.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Channel API",
    author="Front Platform",
    author_email="engineering@konfigthis.com",
    url="https://github.com/konfig-sdks/front-channel-python-sdk/tree/main/python",
    keywords=["Konfig", "Channel API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
