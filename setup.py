from distutils.core import setup

setup(
    name='mkdocs-structurizr-diagram-export',
    version='0.1.0',
    author='Volodymyr Lytvynov',
    author_email='avoidroutine@gmail.com',
    packages=['src'],
    license='MIT license',
    description='Mkdocs plugin that exports structurizr diagrams.',
    install_requires=['mkdocs'],

    entry_points={
        'mkdocs.plugins': [
            'structurizr-diagram-export = src.plugin:NavTitleLoader',
        ]
    }
)