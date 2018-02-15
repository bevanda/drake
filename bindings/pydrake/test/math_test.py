from __future__ import absolute_import, division, print_function

import unittest
from pydrake._math import BarycentricMesh
import numpy as np


class TestBarycentricMesh(unittest.TestCase):
    def test_spelling(self):
        mesh = BarycentricMesh([{0, 1}, {0, 1}])
        values = np.array([[0, 1, 2, 3]])

        mesh.get_input_grid()
        self.assertEquals(mesh.get_input_size(), 2)
        self.assertEquals(mesh.get_num_mesh_points(), 4)
        self.assertEquals(mesh.get_num_interpolants(), 3)
        self.assertTrue((mesh.get_mesh_point(0) == [0., 0.]).all())
        self.assertEquals(mesh.Eval(values, (0, 0))[0], 0)
        self.assertEquals(mesh.Eval(values, (1, 0))[0], 1)
        self.assertEquals(mesh.Eval(values, (0, 1))[0], 2)
        self.assertEquals(mesh.Eval(values, (1, 1))[0], 3)

    def test_mesh_values_from(self):
        mesh = BarycentricMesh([{0, 1}, {0, 1}])

        def mynorm(x):
            return [x.dot(x)]

        values = mesh.MeshValuesFrom(mynorm)
        self.assertEquals(values.size, 4)

    def test_surf(self):
        mesh = BarycentricMesh([{0, 1}, {0, 1}])
        values = np.array([[0, 1, 2, 3]])

        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X, Y = np.meshgrid(list(mesh.get_input_grid()[0]),
                           list(mesh.get_input_grid()[1]))
        Z = np.reshape(values, X.shape)

        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('x')
        ax.set_ylabel('y')


if __name__ == '__main__':
    unittest.main()
