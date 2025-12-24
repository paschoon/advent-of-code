
def parse(y:str):
    direction = y[:1]
    distance = y[1:]
    if direction == "L":
        distance = "-" + distance
    # elif direction == "R":
    #     distance = "+" + distance
    return direction, int(distance)

def a_solve(solve_list: list[str]) -> int:
    start_at = 50
    pwd = 0
    current_loc = start_at

    for rotation_instruct in solve_list:
        current_loc = a_solve_core(rotation_instruct, current_loc)
        if current_loc == 0:
            pwd += 1

    return pwd


def a_solve_core(rotate_instruction: str, current_location: int) -> int:
    direction, distance = parse(rotate_instruction)
    number_line_loc = current_location + distance
    dial_size: int = 100
    dial_location = number_line_loc % dial_size
    return dial_location


def b_solve_core(rotate_instruction: str, current_location: int):
    direction, distance = parse(rotate_instruction)
    number_line_loc: int = current_location + distance

    dial_size: int = 100
    times_past_zero: int = abs(int(number_line_loc / dial_size))
    if current_location > 0 and number_line_loc <= 0:
        times_past_zero += 1

    dial_location = number_line_loc % dial_size
    return dial_location, times_past_zero


def b_solve(solve_list: list[str]) -> int:
    start_at = 50
    pwd = 0
    current_loc = start_at

    for rotation_instruct in solve_list:
        current_loc, times_past_zero = b_solve_core(rotation_instruct, current_loc)
        # print(current_loc)
        # print(times_past_zero)
        pwd += times_past_zero

    return pwd