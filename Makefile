init:
	pandoc -o README.rst README.md
	python setup.py sdist upload

