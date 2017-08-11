from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SudoPy',
    version='1.0',
    description='SudoPy. A Python based sudoku project. Generate, solve and rate Sudoku. ',
    long_description=readme,
    author='Tolis Chal, Pantelispanka, nikfot',
    author_email='burnyourpc@gmail.com',
    url='https://github.com/BurnYourPc',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
