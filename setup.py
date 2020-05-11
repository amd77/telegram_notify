import os
from setuptools import find_packages, setup

os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name="telegram_notify",
    version='2020.01.01',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3 (GPLv3)',
    description='logger for sending django errors to telegram channel via bot',
    long_description=open('README.md').read(),
    url='https://github.com/amd77/telegram_notify',
    author='Alberto Morales',
    author_email='contacto9273@amd77.es',
    install_requires=[
        "Django>1",
        "requests",
        "python-decouple",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
