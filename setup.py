from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='json_datetime_converter',
    version='0.1a4',
    author='Hunter M. Allen',
    author_email='allenhm@gmail.com',
    license='MIT',
    packages=['json_datetime_converter'],
    install_requires=['python-dateutil>=2.7.3'],
    description='Convert datetime objects to iso-format while reading from and writing to json files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hmallen/json_datetime_converter',
    keywords=['json', 'datetime'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
