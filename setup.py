import io
import re
from setuptools import setup


setup(
    name='bl',
    version='1.0',
    include_package_data=True,
    license='GPLv3',
    author='Carlo De Pieri',
    description='An utility to manage my bluetooth headsets and quickly fix them when they do not connect',
    scripts=["bl"],
    install_requires=[
        "appdirs>=1.4.4",
        "pexpect>=4.8.0"
    ],
    extras_require={}
)
