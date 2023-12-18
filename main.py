import numpy as np
from custom_dogleg import custom_dogleg
from test_functions import Paraboloid, Rosenbrock, Himmelblau
from visualize import visualize

# Callback function
def callback(state):
    print("Current position", state)

# Initial guess
initial_guess = np.array([-3.0, 1.0])

fun = Paraboloid

if __name__ == "__main__":
    res, points = custom_dogleg(
        function=fun,
        x0=initial_guess,
        args=(),
        # callback=callback,
        options={
            'initial_trust_radius': 1,
            # 'max_trust_radius': 10,
            'disp': True, 
            'maxiter': 15
            },
        )


    visualize(fun, points[0], points[1], save_file=True, gif=True, fps=1)

