import os

import setuptools

PACKAGE_DIR = os.path.dirname(os.path.realpath(__file__))
REQUIREMENTS_FILENAME = os.path.join(PACKAGE_DIR, "requirements.txt")
README_FILENAME = os.path.join(PACKAGE_DIR, "readme.md")
REQUIREMENTS = [l.strip() for l in open(REQUIREMENTS_FILENAME).readlines()]
LONG_DESCRIPTION = open(REQUIREMENTS_FILENAME).read().strip()

setuptools.setup(
    name="repeaters",
    version="0.0.1",
    author="Salim Fadhley",
    author_email="salimfadhley@gmail.com",
    description="Repeater list compiler",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=["test_repeaters", "repeaters"],
    package_dir={"": "src"},
    install_requires=REQUIREMENTS,
    entry_points={
        "console_scripts": ["nl_prod_forecast=eunrg_gamo_control.nl_prod_forecast:main"]
    },
)
