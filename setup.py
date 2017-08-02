from setuptools import setup, find_packages

setup(
    name='LSB Download App',
    version='1.0',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask>=0.12', 'Flask-Script', 'flask-bootstrap'],
    packages=find_packages(),
    scripts=['bin/download_app.py']
)
