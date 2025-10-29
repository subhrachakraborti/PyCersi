# setup.py
from setuptools import setup, find_packages

setup(
    name="pycersi",
    version="6.1.5",
    description="PyCersi is a lightweight Python library for number-related utilities. It offers mathematical functions, checkers, and stack operations, simplifying common tasks. Easy to install via pip , it's designed for efficient integration into various Python projects.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/subhrachakraborti/PyCersi",
    author="Subhra Chakraborti",
    author_email="mail@subhrachakraborti.com",
    license="MIT",
    keywords="PyCersi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.30.5",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">3.10",
)

