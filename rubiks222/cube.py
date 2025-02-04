from __future__ import annotations

class CubeFaceStringLengthError(BaseException):
    pass

class CubeStringLengthError(BaseException):
    pass

class CubePiece:
    '''
    The class for a piece of the cube face.
    '''
    def __init__(self: CubePiece, color: str) -> None:
        self.color = color

    def __str__(self: CubePiece) -> str:
        return f"CubePiece color '{self.color}'"

    def __repr__(self: CubePiece) -> str:
        return f"CubePiece(color='{self.color}')"

class CubeFace:
    '''
    The class for the cube face.
    '''
    def __init__(self: CubeFace, face_str: str) -> None:
        try:
            assert len(face_str) == 9
        except AssertionError:
            raise CubeFaceStringLengthError("The length of the cube face string must be 9.")
        
        self.pieces = []
        for idx in range(0, 9, 3):  # Parse the cube face string
            self.pieces.append([CubePiece(color) for color in face_str[idx:idx+3]])

    def __str__(self: CubeFace) -> str:
        return f"CubeFace: {self.pieces}"
    
    def __repr__(self: CubeFace) -> str:
        return f"CubeFace(pieces={repr(self.pieces)})"

class Cube:
    '''
    The class for the cubes.
    '''
    def __init__(self: Cube, cube_str: str) -> None:
        try:
            assert len(cube_str) == 54
        except AssertionError:
            raise CubeStringLengthError("The length of the cube string must be 54.")
        
        self.faces = {}
        faces = ("U", "D", "F", "B", "L", "R")
        for idx, face in enumerate(faces):  # Parse the cube string
            start = idx * 9
            end = (idx + 1) * 9
            self.faces[face] = CubeFace(cube_str[start:end])
    
    def __str__(self: Cube) -> str:
        return f"Cube: {self.faces}"
    
    def __repr__(self: Cube) -> str:
        return f"Cube(faces={repr(self.faces)})"
