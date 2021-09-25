import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Decorator function for function level logging'
LONG_DESCRIPTION = 'Logging decorator for both sync and async functions. Logging is carried out at logging levels ' \
                   'DEBUG and INFO. ' \
                   'INFO logs Module name, Method name, Variables, Returns, Elapsed time ' \
                   'DEBUG logs Module name, Method name, Variables, Returns, Elapsed time, Synchronous or ' \
                   'Asynchronous function type, Working directory, Start time, End time All times recorded in UTC ' \
                   'Exceptions are logged if the exception is not handled in code or the exception is handled and ' \
                   'raised. If the exception is handled in code and not raised it is not logged by this decorator '

# Setting up
setup(
    name="ecgai-logging",
    version=VERSION,
    author="Rob Clapham",
    author_email="<rob.clapham@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pytest', 'freezegun', 'colorlog'],
    keywords=['python', 'ecgai', 'logging', 'log', 'decorator', 'decorators', 'log decorator', 'logging decorator'],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
