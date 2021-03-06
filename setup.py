from setuptools import setup, find_packages
from txbitcoin import version

setup(
    name="txbitcoin",
    version=version,
    description="txbitcoin is a Python Twisted library for the Bitcoin P2P network",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://github.com/8468/txbitcoin",
    packages=find_packages(),
    requires=["twisted", "coinbits"],
    install_requires=['twisted>=14.0', "coinbits>=0.3"]
)
