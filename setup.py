from setuptools import setup, find_packages

setup(
    name='helloworldprint',
    packages=find_packages(),
    version='0.4',
    description='A simple lib that prints out hello world',
    author='Mayank Jashnani',
    author_email='mayankjashnani69@gmail.com',
    url='https://github.com/mkjashnani/helloworldprint',
    download_url='https://github.com/mkjashnani/helloworldprint/tarball/0.4',
    keywords=['helloworldprint', 'helloworld', 'pypi', 'mayank'],  # arbitrary keywords
    install_requires=[
        'pytest==2.9.2'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'hello_world = helloworldprint.hello_world:print_hello_world'
        ]},
)
