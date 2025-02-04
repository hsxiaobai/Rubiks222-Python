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
along with this program.  If not, see <https://www.gnu.org/licenses/>
'''
from __future__ import annotations
from ._error import *

class Cube:
  '''
  The class for the cubes.
  '''
  def __init__(self : Cube, cube_str: str) -> None:
    try:
      assert len(cube_str) == 54
    except:
      raise CubeStringLengthError("The length of the cube string must be 54.")
