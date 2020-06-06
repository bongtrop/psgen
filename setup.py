#/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages
import psgen
import os

datadir = os.path.join('payload')
datafiles = [(d, [os.path.join(d,f) for f in files])
    for d, folders, files in os.walk(datadir)]


setup(name=psgen.__name__,
      version=psgen.__version__,
      author='Pongsakorn Sommalai',
      author_email='bongtrop@gmail.com',
      license='MIT',

      url='https://github.com/bongtrop/psgen',
      description='A powershell payload generator tool for hacking',
      long_description=open("README.md").read(),
      packages=['psgen'],
      include_package_data = True,
      install_requires=[

      ],
      entry_points="""
        [console_scripts]
        psgen=psgen:main
      """,
      keywords=['powershell', 'tool', 'hack'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Other Audience',
          'License :: OSI Approved :: MIT License',
          'Topic :: Utilities',
          'Programming Language :: Python :: 3']
    )
