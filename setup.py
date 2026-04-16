# setup.py
from pathlib import Path
from setuptools import setup, find_packages


def read_requirements() -> list[str]:
    requirements_path = Path(__file__).with_name("requirements.txt")
    return [line.strip() for line in requirements_path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]

setup(
    name="pycersi",
    version="7.0.5",
    description="PyCersi is a lightweight Python library for number-related utilities. It offers mathematical functions, checkers, and stack operations, simplifying common tasks. Easy to install via pip , it's designed for efficient integration into various Python projects.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/subhrachakraborti/PyCersi",
    author="Subhra Chakraborti",
    author_email="mail@subhrachakraborti.com, subhra@linuxmail.org",
    license="MIT",
    keywords="PyCersi",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">3.10",
)

