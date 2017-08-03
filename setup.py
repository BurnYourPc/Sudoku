from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Sudoku',
    version='0.1.0',
    description='Sudoku solver and generator',
    long_description=readme,
    author='Tolis Chal, Pantelispanka',
    author_email='burnyourpc@gmail.com',
    url='https://github.com/BurnYourPc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
