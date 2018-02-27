from setuptools import setup, find_packages

setup(
    name='measure-me-jenkins',
    packages=find_packages(),
    version='0.1',
    description='A set of scripts to extract build health from Jenkins',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    keywords=['dev3l', 'python', 'selenium', 'jenkins', ],
    install_requires=[
        'selenium',
        # build / test
        'bandit',
        'coveralls',
        'pytest',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
