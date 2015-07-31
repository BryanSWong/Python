try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Python the hard way chapter 48',
    'author': 'Bryan Wong',
    'url': 'https://github.com/BryanSWong',
    'download_url': 'https://github.com/BryanSWong',
    'author_email': 'bwong727@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
