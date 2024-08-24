# setup.py
from setuptools import setup, find_packages

setup(
    name="SubPyNum",
    version="1.0.1",
    description="A Python Library by Subhra Chakraborti",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/subhrachakraborti/Sub-Py-Library",
    author="SUBHRA CHAKRABORTI",
    author_email="mail@subhrachakraborti.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
