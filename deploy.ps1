python2 -m pip install --user --upgrade setuptools wheel
python2 setup.py sdist bdist_wheel
python2 -m pip install --user --upgrade twine
python2 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*