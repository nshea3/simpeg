import numpy as np
import unittest
from SimPEG import *
from TestUtils import checkDerivative
from scipy.sparse.linalg import dsolve


class ModelTests(unittest.TestCase):

    def setUp(self):

        a = np.array([1, 1, 1])
        b = np.array([1, 2])
        self.mesh2 = Mesh.TensorMesh([a, b], x0=np.array([3, 5]))
        self.mesh22 = Mesh.TensorMesh([b, a], x0=np.array([3, 5]))

    def test_modelTransforms(self):
        for M in dir(Model):
            try:
                model = getattr(Model, M)(self.mesh2)
                assert isinstance(model, Model.BaseModel)
            except Exception, e:
                continue
            self.assertTrue(model.test())

    def test_Mesh2MeshModel(self):
        model = Model.Mesh2Mesh([self.mesh22, self.mesh2])
        self.assertTrue(model.test())

    def test_comboModels(self):
        combos = [(Model.LogModel, Model.Vertical1DModel)]
        for combo in combos:
            model = Model.ComboModel(self.mesh2, combo)
            self.assertTrue(model.test())


if __name__ == '__main__':
    unittest.main()
