from distutils.core import setup

setup(
	name = 'jellylanguage',
	version = '0.1.5',
	packages = [
		'jelly'
	],
	scripts = [
		'scripts/jelly'
	],
	requires = [
		'sympy'
	]
)
