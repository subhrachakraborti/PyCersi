# setup.py
from setuptools import setup, find_packages

setup(
    name="Sub Py Library",
    version="0.1.0",
    description="A great Python library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/subhrachakraborti/sub-py-library",
    author="Subhra Chakraborti",
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
