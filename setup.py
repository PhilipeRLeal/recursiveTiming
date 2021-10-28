import yaml
import os
from setuptools import setup, find_packages
from version_file_seeker import find_version
import pathlib
import unittest


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


here = pathlib.Path(__file__).parent

with open('README.md') as readme_file:
    readme = readme_file.read()


try:
    with open('HISTORY.rst') as history_file:

        history = history_file.read()
except BaseException:
    history = None


try:
    with open('docs/description.txt') as description_file:
        description = description_file.read()

except BaseException:
    description = None


try:
    def dict_to_values(dependencies):
        values = []
        for k in dependencies:
            if isinstance(k, str):
                values.append(k)
            elif isinstance(k, dict):
                for key, value in k.items():
                    if isinstance(value, str):
                        values.append(value)
                    elif isinstance(value, list):
                        values = values + value
        return values

    with open('environment.yml') as f:
        my_dict = yaml.safe_load(f)
        requirements = dict_to_values(my_dict['dependencies'])
        del my_dict

except BaseException:
    requirements = None


Version = find_version('', 'version.py')


setup_requirements = ['pytest-runner', 'flake8']

test_requirements = ['pytest', ]


setup(name='recursiveTiming',
      author="Philipe Riskalla Leal",
      author_email='leal.philipe@gmail.com',

      maintainer="Philipe Riskalla leal: developer",
      maintainer_email='leal.philipe@gmail.com',

      classifiers=[
          'Topic :: Education',  # this line follows the options given by: [1]
          "Topic :: Scientific/Engineering",
          # this line follows the options given by: [1]
          'Intended Audience :: Education',
          "Intended Audience :: Science/Research",
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],

      keywords="timeit",

      description='This is a python package for timing operation processes.',

      long_description=description,

      license="MIT license",

      version=Version,

      # Requirements

      install_requires=requirements,
      setup_requires=setup_requirements,

      python_requires='>=2.7',  # Your supported Python ranges

      packages=find_packages(include='recursiveTiming'),
      # package_dir = {'': ''},

      # Testers:
      test_suite='nose.collector',
      tests_require=['nose'],
      url='https://github.com/PhilipeRLeal/recursiveTiming',

      zip_safe=False
      )
