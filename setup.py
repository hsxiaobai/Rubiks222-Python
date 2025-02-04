'''
Copyright (c) 2025 hsxiaobai

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from setuptools import setup, find_packages

setup(
  name="rubiks222",
  version="0.0.1inital",
  packages=find_packages(),
  python_require=">=3.8"
  author="hsxiaobai",
  description="A Python Package for 2x2x2 Rubik's cube.",
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/hsxiaobai/Rubiks222-Python"
)
