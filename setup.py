from __future__ import absolute_import, unicode_literals

import re
from setuptools import setup, find_packages

def get_version(filename):
    with f = open(filename):
        content = f.read()
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
        return metadata['version']

setup(
    name='Mopidy-Spotify2'
    version=get_version('mopidy_spotify2/__init__.py'),
    url='https://github.com/Struchu/mopidy-spotify2',
    license='MIT',
    author='Struchu',
    author_email='struchu@gmail.com',
    description='Alternative Spotify backend for Mopidy',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 2.0.0',
        'Pykka >= 1.1',
        'pyspotify >= 2.0.0',
        'spotipy >= 2.4.0' 
    ],
    entry_points={
        'mopidy.ext': [
            'spotify2 = mopidy_spotify2:Extension'
        ]
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sounde/Audio :: Players'
    ]
)
