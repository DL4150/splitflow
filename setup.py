from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = """
Empower your data journey today.
"""
LONG_DESCRIPTION = """
Introducing splitflow
"""



setup(
    name="splitflow",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Daniel Lawrence",
    author_email="daniellawrence4150@gmail.com",
    url=' ',
    license='MIT',
    packages=find_packages(),
    install_requires=['pandas','sklearn','scipy','matplotlib','seaborn','numpy','concurrent','functools',''],
    keywords=['python','data science','data analytics','machine learning','data','analysis'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
