from setuptools import setup

setup(name="package",
version="1.0",
description= "simple module which recommends you beer", 
author= "Ashmin",
packages=['packages'],
install_requires = ['requests', 'json'])