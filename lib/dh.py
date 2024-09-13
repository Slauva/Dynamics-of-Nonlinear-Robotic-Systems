import numpy as np
import sympy as sp

class Transformation:
    
    @staticmethod
    def rotate_x(angle: int | float | sp.Symbol) -> sp.Matrix:
        rot = sp.eye(4, 4)
        rot[1:3, 1:3] = sp.Matrix([
            [sp.cos(angle), -sp.sin(angle)],
            [sp.sin(angle), sp.cos(angle)]
        ])
        return rot
    
    @staticmethod
    def rotate_z(angle: int | float | sp.Symbol) -> sp.Matrix:
        rot = sp.eye(4, 4)
        rot[0:2, 0:2] = sp.Matrix([
            [sp.cos(angle), -sp.sin(angle)],
            [sp.sin(angle), sp.cos(angle)]
        ])
        return rot
    
    @staticmethod
    def rotate_y(angle: int | float | sp.Symbol) -> sp.Matrix:
        rot = sp.eye(4, 4)
        rot[0, 0:3] = sp.Matrix([sp.cos(angle), 0, sp.sin(angle)]).T
        rot[2, 0:3] = sp.Matrix([-sp.sin(angle), 0, sp.cos(angle)]).T
        return rot
    
    @staticmethod
    def translate(pos: sp.Matrix | np.ndarray | list) -> sp.Matrix:
        rot = sp.eye(4, 4)
        rot[0:3, 3] = pos
        return rot
    
    
    def link(self, angle_z: int | float | sp.Symbol, dist_z: int | float | sp.Symbol, angle_x: int | float | sp.Symbol, dist_x: int | float | sp.Symbol) -> sp.Matrix:
        return self.rotate_z(angle_z) @ self.translate([0, 0, dist_z]) @ self.rotate_x(angle_x) @ self.translate([dist_x, 0, 0])