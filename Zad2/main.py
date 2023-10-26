from ortools.linear_solver import pywraplp


def main():
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return

    x = solver.IntVar(0, solver.infinity(), "x")
    y = solver.IntVar(0, solver.infinity(), "y")

    print("Number of variables =", solver.NumVariables())

    ct1 = solver.Constraint(0, 120, "ct1")
    ct1.SetCoefficient(x, 0.5)
    ct1.SetCoefficient(y, 0.25)

    ct2 = solver.Constraint(0, 160, "ct2")
    ct2.SetCoefficient(x, 0.5)
    ct2.SetCoefficient(y, 0.75)

    print("Number of constraints =", solver.NumConstraints())

    objective = solver.Objective()
    objective.SetCoefficient(x, 2.2)
    objective.SetCoefficient(y, 3)
    objective.SetMaximization()

    solver.Solve()
    print("Solution:")
    print("Objective value =", objective.Value())
    print("x =", x.solution_value())
    print("y =", y.solution_value())


if __name__ == '__main__':
    main()
