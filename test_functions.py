import numpy as np

class Paraboloid:
    # Objective function
    def objective(x):
        return x[0]**2 + x[1]**2

    # Hessian of the objective function
    def hessian(x):
        return np.array([
            [2, 0],
            [0, 2]])

    # Jacobian of the objective function
    def jacobian(x):
        return np.array([2 * x[0], 2 * x[1]])
    
import numpy as np

class Rosenbrock:
    # Objective function
    def objective(x):
        return (1-x[0])**2 + 100*(x[1] - x[0]**2)**2

    # Hessian of the objective function
    def hessian(x):
        return np.array([
        [2 + 800*x[0]**2 - 400*(x[1]-x[0]**2), -400*x[0]],
        [-400*x[0], 200]])

    # Jacobian of the objective function
    def jacobian(x):
        return np.array([
        -2*(1-x[0])-400*x[0]*(x[1]-x[0]**2),
        200*(x[1]-x[0]**2)
        ])

class Himmelblau:
    # Objective function
    def objective(x):
        return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

    # Hessian of the objective function
    def hessian(x):
        d2f_dx2 = 4 * (3 * x[0]**2 + x[1] - 11) + 2
        d2f_dy2 = 4 * (x[0] + 3 * x[1]**2 - 7) + 2
        d2f_dxdy = 4 * (1 - 3 * x[0]) * x[1]
        return np.array([[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]])

    # Jacobian of the objective function
    def jacobian(x):
        df_dx = 2 * (2 * x[0] * (x[0]**2 + x[1] - 11) + x[0] + x[1]**2 - 7)
        df_dy = 2 * (x[0]**2 + 2 * x[1] * (x[0] + x[1]**2 - 7) + x[1] - 11)
        return np.array([df_dx, df_dy])
    
    