from setuptools import setup, find_packages
from platform import python_version_tuple


def requirements():

    with open('requirements.txt', 'r') as fileobj:
        requirements = [line.strip() for line in fileobj]
        return requirements


def long_description():
    with open('README.rst', 'r', encoding='utf-8') as fileobj:
        return fileobj.read()


setup(
    name='cos-py3-sdk-v5',
    version='1.0.0',
    url='',
    license='MIT',
    author='heli',
    author_email='mmm@qq.com',
    description='cos-py3-sdk-v5',
    long_description=long_description(),
    packages=find_packages(),
    install_requires=requirements()
)
