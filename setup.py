import distutils.core

try:
	import setuptools
except ImportError:
	pass

packages=[]

distutils.core.setup(
	name='study',
	version = '0.4.2',
	packages=['test_module'],
	author='Innovaser',
	author_email='rancavil@innovaser.cl',
	install_requires=packages
)

