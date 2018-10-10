from __future__ import print_function
from ortools.constraint_solver import pywrapcp


def main():
    # Creates the solver.
    solver = pywrapcp.Solver("simple_example")

    # Creates the variables.
    num_vals = 3

    x = solver.IntVar(0, num_vals - 1, "x")
    y = solver.IntVar(0, num_vals - 1, "y")
    z = solver.IntVar(0, num_vals - 1, "z")

    # Create the constraints.
    solver.Add(x != y)
    solver.Add(y != z)
    solver.Add(x != z)
    # Create the decision builder.

    db = solver.Phase([x, y, z], solver.CHOOSE_MIN_SIZE, solver.ASSIGN_MIN_VALUE)
    solver.Solve(db)
    count = 0

    while solver.NextSolution():
        count += 1
        print("Solution", count, '\n')
        print("x = ", x.Value())
        print("y = ", y.Value())
        print("z = ", z.Value())
        print()
    print("Number of solutions:", count)


if __name__ == "__main__":
    main()
