from setuptools import setup, find_packages

setup(
    name='mypackages',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Anna/mypackages',
    author='Anna',
    author_email='mofokenganna21@gmail.com'
)
