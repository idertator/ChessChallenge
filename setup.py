from distutils.core import setup

setup(
    name='ChessChallenge',
    version='0.0.1',
    packages=['chess'],
    url='https://github.com/idertator/ChessChallenge',
    license='MIT',
    author='Roberto Antonio Becerra García',
    author_email='idertator@gmail.com',
    description='A variation of the N-Queen problem with different chess pieces',
    scripts=['bin/chess_challenge.py'],
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    requires=[
        'numpy',
    ]
)
