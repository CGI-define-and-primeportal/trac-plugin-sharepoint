from setuptools import setup

setup(
    name = 'TracSharePointInteroperability',
    version = '0.0',
    author = 'Nick Piper',
    author_email = 'nick.piper@cgi.com',
    license = 'Modified BSD License',
    packages = ['tracsharepoint'],
    package_data={
        'tracsharepoint': [
            'templates/*.html',
            'htdocs/js/*.js',
            ]
        },
    install_requires = ['ContextMenuPlugin'],
    entry_points = {
        'trac.plugins': [
            'tracsharepoint = tracsharepoint',            
            'tracsharepoint.browser = tracsharepoint.browser',
        ],
    },
)
