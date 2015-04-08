from setuptools import setup

setup(
    name = 'TracSharePointInteroperability',
    version = '0.0',
    author = 'Nick Piper',
    author_email = 'nick.piper@cgi.com',
    license = 'Modified BSD License',
    packages = ['tracsharepoint'],
    entry_points = {
        'trac.plugins': [
            'tracsharepoint = tracsharepoint',            
            'tracsharepoint.browser = tracsharepoint.browser',
        ],
    },
)
