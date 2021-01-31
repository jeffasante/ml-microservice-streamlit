from setuptools import setup
import os

BASEPATH = os.path.dirname(os.path.abspath(__file__))

setup(name='app',
      py_modules=['app'],
      install_requires=[
          'streamlit'
      ],
)