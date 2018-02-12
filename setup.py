import io

from setuptools import setup

with io.open('requirements.txt', 'r') as f:
        required = f.read().splitlines()

setup(
    name='petrarch3',
    install_requires=required,
    entry_points={
        'console_scripts': ['petrarch3 = petrarch3.petrarch3:main']},
    version='1.1.0',
    author='Philip Schrodt, John Beieler, Clayton Norris',
    author_email='openeventdata@gmail.com',
    packages=['petrarch3'],
    package_dir={'petrarch3': 'petrarch3'},
    package_data={'petrarch3': ['data/dictionaries/*', 'data/text/*',
                               'data/config/*']},
    url='openeventdata.org',
    license='LICENSE.txt',
    description='PETRARCH 3 parser for event data.',
    long_description=io.open('README.md', encoding="utf-8").read())
