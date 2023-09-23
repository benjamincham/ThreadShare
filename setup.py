
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ThreadShare',
    version='0.2',
    packages=find_packages(),
    description='A Python library to maximise CPU usage by smartly sharing threads among multiple functions.',
    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/benjamincham/ThreadShare',

    author='Benjamin Cham',

    author_email='benjaminchamwb@gmail.com',

    lassifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Hardware',
        'Topic :: System :: Operating System Kernels :: Linux',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    
    install_requires=[
        'psutil',
    ],
)
    