from __future__ import absolute_import, print_function, division
import numpy as np
from numba import vectorize
from numba import unittest_support as unittest
from numba.ocl.testing import OCLTestCase


class TestVectorizeComplex(OCLTestCase):
    def test_vectorize_complex(self):
        @vectorize(['complex128(complex128)'], target='ocl')
        def vcomp(a):
            return a * a + 1.

        A = np.arange(5, dtype=np.complex128)
        B = vcomp(A)
        self.assertTrue(np.allclose(A * A + 1., B))


if __name__ == '__main__':
    unittest.main()
