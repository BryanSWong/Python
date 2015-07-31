try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Bryan Wong',
    'url': 'https://github.com/BryanSWong',
    'download_url': 'https://github.com/BryanSWong',
    'author_email': 'bwong727@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex49'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
