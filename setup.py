#!/usr/bin/env python3

import os
import re
import sys

from setuptools import find_packages, setup


if sys.hexversion < 0x3050000:
  print("Python version %s is unsupported, >= 3.5.0 is needed" % (".".join(map(str, sys.version_info[:3]))))
  exit(1)

with open(os.path.join("sacad", "__init__.py"), "rt") as f:
  version = re.search("__version__ = \"([^\"]+)\"", f.read()).group(1)

with open("requirements.txt", "rt") as f:
  requirements = f.read().splitlines()
if sys.platform == "win32":
  requirements.append("idna==2.6")

with open("test-requirements.txt", "rt") as f:
  test_requirements = f.read().splitlines()

with open("README.md", "rt") as f:
  readme = f.read()

setup(name="sacad",
      version=version,
      author="desbma",
      packages=find_packages(exclude=("tests",)),
      entry_points={"console_scripts": ["sacad = sacad:cl_main",
                                        "sacad_r = sacad.recurse:cl_main"]},
      test_suite="tests",
      install_requires=requirements,
      tests_require=test_requirements,
      description="Search and download music album covers",
      long_description=readme,
      long_description_content_type="text/markdown",
      url="https://github.com/desbma/sacad",
      download_url="https://github.com/desbma/sacad/archive/%s.tar.gz" % (version),
      keywords=["download", "album", "cover", "art", "albumart", "music"],
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Environment :: Console",
                   "Intended Audience :: End Users/Desktop",
                   "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3 :: Only",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Topic :: Internet :: WWW/HTTP",
                   "Topic :: Multimedia :: Graphics",
                   "Topic :: Utilities"])
