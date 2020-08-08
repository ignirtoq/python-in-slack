import codecs
import os
import re
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError('Unable to find version string.')


NAME = 'pyslackapp'
VERSION = find_version(NAME, '__init__.py')
LICENSE = 'MIT'
AUTHOR = 'Jeffrey Bouas'
EMAIL = 'ignirtoq+pyslackapp@gmail.com'
PACKAGES = find_packages()
INSTALL_REQUIRES = [
    'aiohttp',
    'jupyter_client ~= 6.1',
]
TEST_SUITE = 'nose.collector'
TESTS_REQUIRE = ['nose']
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]
PYTHON_REQUIRES = '>=3.6'


setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    license=LICENSE,
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    classifiers=CLASSIFIERS,
    test_suite=TEST_SUITE,
    tests_require=TESTS_REQUIRE,
    python_requires=PYTHON_REQUIRES,
)
