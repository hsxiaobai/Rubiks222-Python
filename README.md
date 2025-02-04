[跳转到中文介绍](./README-cn.md)

# Rubiks222-Python
A Python Package for controlling 2x2x2 Rubik's cube.

## Table of Contents
1. [Introduction](#Introduction)
2. [Overview](#Overview)<br>
 2.1. [Modules](#Modules)

## Introduction
It seems that there isn't any packages on **PyPI** which provides full methods controlling 2x2x2 Rubik's cube:
 1. Algorithms: Methods for reversing, simplifying and some other operations to the algorithms.
 2. Virtual cube: Methods for making, rotating faces and other operations to the virtual cube.
 3. Solving cube: Methods for solving cubes in many ways.
To use these features in one package easily, I created this package.
It will be a little hard to create a package for 3x3x3 Rubik's cube, so I just support methods for 2x2x2 Rubik's cube.

## Overview
### Modules
1. `cube.py`: Virtual cube.
2. `solver.py`: Solving cube.
3. `alg.py`: Simplify and do something else to the algorithm.
