import jax.numpy as np
from numba import int64, float64    # import the types
from numba.experimental import jitclass

spec = [
    ('_degree', int64),
    ('_knots', float64[:]),
    ('_coeffs', float64[:]),
]

@jitclass(spec)
class Spline:
    def __init__(self, degree : int, knots : 'float[:]', coeffs : 'float[:]'):
        self._degree = degree
        self._knots = knots
        self._coeffs = coeffs

    @property
    def degree(self):
        return self._degree

    def _basis_funcs(self, x: 'float', span: 'int', values: 'float[:]'):
        """ Compute non-zero basis functions at x following Algorithm A2.2
        from the NURBS book [1]. """
        left = np.empty(self.degree)
        right = np.empty(self.degree)

        values[0] = 1.0

        for j in range(0, self.degree):
            left[j] = x - self._knots[span-j]
            right[j] = self._knots[span+1+j] - x
            saved = 0.0

            for r in range(0, j+1):
                temp = values[r] / (right[r] + left[j-r])
                values[r] = saved + right[r] * temp
                saved = left[j-r] * temp

            values[j+1] = saved

    def eval(self, x : 'const float[:]', y : 'float[:]'):
        """ Evaluate spline at non-zero basis elements: sum_i N_i(x) * c_i.
        """
        basis = np.empty(self.degree+1)
        for i, xi in enumerate(x):
            span = self._find_span(xi)
            self._basis_funcs(xi, span, basis)

            # Evaluate the spline at xi
            y[i] = 0.0
            for j in range(self.degree+1):
                y[i] += self._coeffs[span-self.degree+j]*basis[j]

    def _find_span(self, x: float) -> int:
        # Knot index at left/right boundary
        low = self.degree
        high = len(self._knots)-1-self.degree

        # Check if point is exactly on left/right boundary, or outside domain
        if x <= self._knots[low]:
            returnVal = low
        elif x >= self._knots[high]:
            returnVal = high-1
        else:
            # Perform binary search
            span = (low+high)//2

            while x < self._knots[span] or x >= self._knots[span+1]:
                if x < self._knots[span]:
                    high = span
                else:
                    low = span
                span = (low+high)//2

            returnVal = span

        return returnVal

