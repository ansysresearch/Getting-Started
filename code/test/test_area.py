import os
import trimesh
import unittest
import numpy as np
from src import *


class MeshTest(unittest.TestCase):
    @staticmethod
    def read_mesh(mesh_file):
        mesh = trimesh.load(os.path.join('test', mesh_file))
        return mesh

    def test_compute_triangle_area(self):
        vertices = np.array([[0., 0., 0.],
                             [1., 0., 0.],
                             [0., 1., 0.]])
        self.assertAlmostEqual(compute_triangle_area(vertices), 0.5)

    def test_compute_mesh_area(self):
        simple_mesh = self.read_mesh("simple_mesh.obj")
        self.assertAlmostEqual(compute_mesh_area(simple_mesh), simple_mesh.area)

        # complex_mesh = self.read_mesh("complex_mesh.obj")
        # self.assertAlmostEqual(compute_mesh_area(complex_mesh), complex_mesh.area)

    def test_compute_mesh_area_parallel(self):
        simple_mesh = self.read_mesh("simple_mesh.obj")
        self.assertAlmostEqual(compute_mesh_area_parallel(simple_mesh, n_jobs=4), simple_mesh.area)

    #     complex_mesh = self.read_mesh("complex_mesh.obj")
    #     self.assertAlmostEqual(compute_mesh_area_parallel(complex_mesh, n_jobs=4), complex_mesh.area)


if __name__ == '__main__':
    unittest.main()