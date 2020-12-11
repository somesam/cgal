from setuptools import setup

from os import path
from pathlib import Path
headers = []
for ext in ('*.h', '*.hpp'):
    for file in Path('.').rglob(ext):
        fullpath = file.__str__()
        split = fullpath.split('/include/')
        if len(split) == 2:
            head, tail = path.split(split[1])
            install_dir = path.join('include', head)
            headers += [(install_dir, [fullpath])]

setup(
    name="CGAL",
    version="5.0.3",
    author="The CGAL Project",
    author_email="cgal-discuss@inria.fr",
    maintainer="Samuel Burbulla",
    maintainer_email="samuel.burbulla@ians.uni-stuttgart.de",
    description="The Computational Geometry Algorithms Library",
    long_description="CGAL (Computational Geometry Algorithms Library) makes the most important of the solutions and methods developed in computational geometry available to users in industry and academia in a C++ library. The goal is to provide easy access to useful, reliable geometric algorithms. This package includes only header files.",
    url="https://www.cgal.org",
    data_files = headers
)
