from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'A simple IP and port scanner tool.'
LONG_DESCRIPTION = 'PortIP is a Python package that allows you to ping websites and scan for open ports.'

# Setting up
setup(
    name="portip",
    version=VERSION,
    author="Pabitra Banerjee",
    author_email="<rockstarpabitra2204@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'port scanner', 'networking', 'IP', 'port'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points={
        'console_scripts': [
            'portip=portip.portip:main',
        ],
    },
    python_requires='>=3.6',
)
