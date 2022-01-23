#! /usr/bin/python
from setuptools  import setup
import os
import sys
import platform
import configparser

from io import open
# to install type:
# python setup.py install --root=/
LONG_DESCRIPTION=open('README.md','r',encoding='utf8').read()        
        
if sys.version_info[0] < 3:
    raise Exception(
        'You are tying to install hlpl_arabic_words on Python version {}.\n'
        'Please install hlpl_arabic_words in Python 3 instead.'.format(
            platform.python_version()
        )
    )
    
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'hlpl_arabic_words/setup.cfg')
config.read(config_file_path)

VERSION = config['hlpl_arabic_words']['version']
AUTHOR = config['hlpl_arabic_words']['author']
AUTHOR_EMAIL = config['hlpl_arabic_words']['email']
URL = config['hlpl_arabic_words']['url']


projects_urls={}
for i in range(4,len(list(config['hlpl_arabic_words'].keys()))):
    x=list(config['hlpl_arabic_words'].keys())[i]
    y=x
    if i>3:
       y=y[0:len(y)-4]
    projects_urls[y]=config['hlpl_arabic_words'][x]
    

setup (name='hlpl_arabic_words', version=VERSION,
      description='hlpl_arabic_words lists nouns, verbs, articles, nouns prefix, nouns suffix, verbs prefix, and verbs suffix in a readable database file',
      long_description_content_type='text/markdown',  
      long_description = LONG_DESCRIPTION,       
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=URL+'/download/',
      project_urls=projects_urls,      
      python_requires='>=3, <3.8',
      license='MIT',
      platform="OS independent",
      keywords=['hlpl_arabic_words', 'hlpl arabic words', 'arabic words', 'hlpl arabic words', 'hlpl'],
      package_dir={'hlpl_arabic_words': 'hlpl_arabic_words',},
      packages=['hlpl_arabic_words',],
      install_requires=[],         
      include_package_data=True,
      entry_points ={
        'console_scripts': [
                'hlpl_arabic_words = hlpl_arabic_words.__main__:main',
            ]},   
      classifiers=[
          'Natural Language :: Arabic',
          ],
                  
    );
