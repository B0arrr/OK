from z3 import *

x, y, z = Ints('x y z')

solver = Solver()

solver.add(x > 0, y > 0, z > 0)
solver.add(x != 3, y != 6, z != 15)
solver.add(x < y, y < z)
solver.add(x * x + y * y + z * z == x * y * z)

if solver.check() == sat:
    model = solver.model()
    result_x = model[x].as_long()
    result_y = model[y].as_long()
    result_z = model[z].as_long()

    print(f"x = {result_x}, y = {result_y}, z = {result_z}")
else:
    print("Brak rozwiązania dla podanych warunków.")
