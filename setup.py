"""pypi package setup."""
import codecs
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with codecs.open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()
import sys

requirements = ['scikit-hep']
if sys.version_info < (3,6):
    sys.exit('Sorry, Python < 3.6 is not supported')
if sys.version_info < (3,7):
    requirements.append('dataclasses')

setup(
    name='lhereader',
    version='1.0',
    description='',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='',
    url='',
    author='',
    author_email='',
    classifiers=[
    ],
    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    zip_safe=False,
    install_requires=requirements,
    setup_requires=[],
    tests_require=[],
    project_urls={
    }, )