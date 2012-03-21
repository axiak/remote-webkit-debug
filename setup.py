from setuptools import setup


setup(
    name="remote-webkit-debug",
    version="0.0.1",
    author="Michael Axiak",
    install_requires=['websocket-client', 'httplib2'],
    author_email='mike@axiak.net',
    keywords='webkit chrome development',
    url='https://github.com/axiak/remote-webkit-debug',
    packages=['remote_webkit_debug'],
    long_description='Remote webkit debugging with python.',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
)
