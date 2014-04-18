import os
from pip.req import parse_requirements

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

mainscript = 'server.py'

install_requirements = parse_requirements('./requirements.txt')
install_requirements = [str(ir.req) for ir in install_requirements]

setup(
	name = 'newsworm',
	version = 0.02,
	author = 'Tristan Fisher',
	author_email = 'code@tristanfisher.com',
	description = "scrape html and save links to a database for future consumption",
	long_description = open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'README.md'), 'r').read(),
	scripts = [],
	url = "http://github.com/tristanfisher/newsworm",
	license = open('LICENSE').read(),
	install_requires = install_requirements,
	setup_requires = []
)
