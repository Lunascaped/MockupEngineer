from setuptools import setup, find_packages


setup(
    name='MockupEngineer',
    version='2022.03.24.1',
    packages=find_packages(),
    url='https://github.com/ulbwazhine/MockupEngineer',
    license='MIT',
    author='Ulbwazhine',
    author_email='ulbwa@icloud.com',
    description='A simple library for creating beautiful screenshots.',
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    include_package_data=True
)
