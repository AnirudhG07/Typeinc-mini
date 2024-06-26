import os
from setuptools import setup, find_packages
import shutil, gzip
import platform 

def install_man_page():
    source_path = os.path.join("docs", "man", "typeinc.1")
    dest_path = os.path.join("/usr/local/", "share", "man", "man1", "typeinc-mini.1.gz")

    # Compress the man page
    with open(source_path, 'rb') as src, gzip.open(dest_path, 'wb') as dst:
        shutil.copyfileobj(src, dst)

description="""
# Typeinc-mini

Tyepinc-mini, a miniature version of Typeinc, an ncurses based tool, is your goto terminal tool to play around with your typing speed with various difficulty levels.
You get an amazing UI for typing keyboard giving you a feel of both typewriters and keyboards.
Get your Tyepinc score and boast to your pals of your speed. Dream to achieve a Granddtypaa!

# Features

- Typing Speed Test where you can test your typing speed.
- Set your own difficulty level and test the abilities of your typing skills.
- Get your grade and Tyepinc score and boast to your pals of your speed.
- A user-friendly interface to make your typing experience more fun and interactive.
- View top 5 highscores(local) for each difficulty level.

# Installation
To install Typeinc-mini, please fulfill the dependicies and run the following command:
```bash
pip install typeinc-mini
```
To run the command, run the following command:
```bash
typeinc-mini
```
And you are good to go!

## Dependencies
- Python 3.11 or higher
- ncurses library
- Other python libraries which will be installed automatically

Visit the Github Repository for more details: https://github.com/AnirudhG07/Typeinc-mini

# Version
1.0.0

# Note:
1) The tool is developed using Python and ncurses library.
2) This tools is crossplatform for MacOS, Linux, Windows, etc.

"""

install_requires=[]

if platform.system() == 'Windows':
    install_requires.append('windows-curses')
install_requires+=['setuptools', 'wheel', 'twine']

setup(
    name='typeinc-mini',
    version='1.0.0',
    description='Typeinc-mini, a miniature version of Typeinc, an ncurses based tool, is your goto terminal tool to play around with your typing speed with various difficulty levels.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/AnirudhG07/Typeinc-mini',
    author='Anirudh Gupta',
    packages=find_packages(),
    install_requires=install_requires,
    keywords=['terminal', 'typing speed test', 'typing', 'CLI'],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'typeinc-mini=typeinc_mini.main:main',
        ],
    },
    package_data={
        'typeinc_mini': ['configurations/*', 'scores/*', 'wordlist.txt'],
    },
    include_package_data=True,
    classifiers=[   
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows"
    ],
)