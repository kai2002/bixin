# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

install_requires = ["cppjieba-py"]

setup(
    name='bixin',
    version='0.0.2',
    packages=find_packages(exclude=['bin', 'tests']),
    include_package_data=True,
    package_data={
        'bixin.data': ['*.pkl']
    },
    extras_require={
        'dev': ['prefixtree>=0.2.5', 'chardet>=3.0.4','opencc-python-reimplemented>=0.1.3']
    },
    install_requires=install_requires
    # prefixtree need at least 0.2.5 if not in pypi install if from github
)
