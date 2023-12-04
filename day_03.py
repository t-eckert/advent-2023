from lib import read, tee

digits = {"0","1","2","3","4","5","6","7","8","9"}

def part_1(engine_rows: list[str], symbols: set[str]) -> int:
    engine_dimensions = (len(engine_rows), len(engine_rows[0]))

    reading_number = False
    subject_buffer = set()
    number_buffer = ""

    total = 0

    for row, vals in enumerate(engine_rows):
        for col, char in enumerate(vals):
            if char in "0123456789":
                subject_buffer.add((row,col))
                number_buffer += char
                reading_number = True
            else:
                if reading_number:
                    if has_symbol(engine_rows, border(subject_buffer, engine_dimensions), symbols):
                        total += int(number_buffer)
                    subject_buffer.clear()
                    number_buffer = ""
                reading_number = False

    return total

def part_2(engine_rows: list[str]) -> int:
    """
    I want to find all of the "gears"
    When I find a gear, grab the border using the existing function.
    Pass the border through the "has_symbol" with numbers
    Pass the border with numbers through a group_contiguous function.
    If the length of the output is 2,
        Start a process to grab those numbers.
        glob_numbers?
    """


    engine_dimensions = (len(engine_rows), len(engine_rows[0]))

    gear_ratio_sums = 0
    for row, vals in enumerate(engine_rows):
        print(vals, end="\t")
        for col, char in enumerate(vals):
            if char == "*":
                bordering_cells = border({(row,col)}, engine_dimensions)
                numeric_bordering_cells = {cell for cell in bordering_cells if has_symbol(engine_rows, {cell}, {"0","1","2","3","4","5","6","7","8","9"})}
                grouped_rows = group_rows(numeric_bordering_cells)
                number_count = 0
                for r in grouped_rows:
                    if are_contiguous(r):
                        number_count += 1
                    else:
                        number_count += 2
                # print(numeric_bordering_cells, end=" : ")
                # print(number_count, end="\t")
                if number_count == 2:
                    ratio = get_ratio(engine_rows, grouped_rows)
                    gear_ratio_sums += ratio
        print(gear_ratio_sums, end="\t")
        print()


    return gear_ratio_sums


def get_ratio(engine_rows: list[str] ,rows: list[set[tuple[int,int]]]) -> int:
    ratio = 1
    print("( ", end="")
    for row in rows:
        if are_contiguous(row):
            ratio *= glob_number(engine_rows, row.pop())
        else:
            cells = [cell for cell in row]
            a, b = cells[0], cells[1]
            ratio *= glob_number(engine_rows, a)
            ratio *= glob_number(engine_rows, b)
    print(f")", end="\t")

    return ratio

def glob_number(engine_rows: list[str], cell: tuple[int,int]) -> int:
    row, col = cell[0], cell[1]
    number = engine_rows[row][col]

    # Back to start
    for c in range(col-1, 0, -1):
        val = engine_rows[row][c]
        if val not in digits:
            break
        number = val + number
    # To the end
    for c in range(col+1, len(engine_rows[row])):
        val = engine_rows[row][c]
        if val not in digits:
            break
        number += val
    print(number, end=" ")

    return int(number)

def group_rows(cells: set[tuple[int,int]]) -> list[set[tuple[int,int]]]:
    row_groups = {}
    for cell in cells:
        if cell[0] not in row_groups.keys():
            row_groups[cell[0]] = [cell]
        else:
            row_groups[cell[0]].append(cell)

    return [group for group in row_groups.values()]


def are_contiguous(cells: set[tuple[int,int]]) -> bool:
    # Numbers can only be contiguous within rows.
    cols = sorted([cell[1] for cell in cells])

    prev = None
    for col in cols:
        if prev and prev != col - 1:
            return False
        prev = col
    return True


def group_contiguous(cells: set[tuple[int,int]]) -> list[list[tuple[int,int]]]:
    row_groups = {}
    for cell in cells:
        if cell[0] not in row_groups.keys():
            row_groups[cell[0]] = [cell]
        else:
            row_groups[cell[0]].append(cell)

    print(row_groups)
    for _, group in row_groups.items():
        cols = []
        for cell in group:
            cols.append(cell[1])
        cols.sort()
        print(cols)

        grouped_cols = []
        prev = None



    return []


def has_symbol(engine_rows: list[str], locations: set[tuple[int,int]], symbols: set[str]) -> bool:
    for loc in locations:
        if engine_rows[loc[0]][loc[1]] in symbols:
            return True
    return False

def border(subject: set[tuple[int,int]], engine_dimensions: tuple[int,int]) -> set[tuple[int,int]]:
    height, width = engine_dimensions

    all_borders = set()

    cell_borders = set()
    for cell in subject:
        cell_borders.clear()

        row, col = cell[0], cell[1]

        # Iterate clockwise around the location
        if row > 0 and col > 0:
            cell_borders.add((row-1,col-1)) # above left
        if row > 0:
            cell_borders.add((row-1,col))   # above center
        if row > 0 and col < width - 1:
            cell_borders.add((row-1,col+1)) # above right
        if col < width - 1:
            cell_borders.add((row,col+1))   # center right
        if row < height - 1 and col < width - 1:
            cell_borders.add((row+1,col+1)) # below right
        if row < height - 1:
            cell_borders.add((row+1,col))   # below center
        if row < height - 1 and col > 0:
            cell_borders.add((row+1,col-1)) # below left
        if col > 0:
            cell_borders.add((row,col-1))   # center left

        all_borders.update(cell_borders)

    return all_borders-subject



def border_test():
    tests = [
        (
            {(0,0)},
            (4,4),
            {(1,0), (1,1), (0,1)}
        ),
        (
            {(1,1), (1,2), (1,3)},
            (4,4),
            {(0,0), (0,1), (0,2), (0,3), (1,0), (2,0), (2,1), (2,2), (2,3)}
        )
    ]

    for test in tests:
        assert test[2] == border(test[0], test[1])


if __name__ == "__main__":
    engine_rows = read("day_03.txt").strip().split("\n")

    symbols = set()
    for row in engine_rows:
        for c in row:
            if c not in "0123456789.":
                symbols.add(c)

    print("Part 1")
    print(part_1(engine_rows, symbols))
    print()


    print("Part 2")
    print(part_2(engine_rows))
    print()

