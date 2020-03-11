from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.project_description }}',
    author='{{ cookiecutter.full_name }}',
    license='{{ cookiecutter.license}}',
)
