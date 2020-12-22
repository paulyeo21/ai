from utils import *

def grid_values(grid, default=default_box_value):
    """
    Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    output = {}
    for i in range(len(grid)):
        val = (default if grid[i] == "." else grid[i])
        output[boxes[i]] = val
    return output

def eliminate(values):
    """
    Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after eliminating values.
    """
    for box, val in values.items():
        if len(val) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(val, '')

def only_choice(values):
    """
    Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in "123456789":
            boxes = [box for box in unit if digit in values[box]]
            if len(boxes) == 1:
                values[boxes[0]] = digit

def reduce_puzzle(values):
    """
    Using constraint propogation reduce the puzzle possible solution sets. 1) [Eliminate] Using solved boxes
    eliminate those from peers' possiblities. 2) [Only choice] Boxes that have the only possible value in from 
    their peer means that that value must be the solution. Find those and set those. Repeat steps 1 and 2, since
    a change from one could impact more improvements for the other. Stop when there are no more improvements
    to be made.

    Input: Sudoku in dictionary form
    Output: None
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        eliminate(values)

        # Your code here: Use the Only Choice Strategy
        only_choice(values)

        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])

        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after

def invalid(values):
    """
    Determine if a puzzle is invalid

    Input: Sudoku in dictionary form
    Output: Boolean
    """
    # for box in values.keys():
    #     if len(values[box]) == 0:
    #         return True
    # return False
    return len([box for box in values.keys() if len(values[box]) == 0]) != 0

def solved(values):
    """
    Determine if a puzzle is solved

    Input: Sudoku in dictionary form
    Output: Boolean
    """
    # for box in values.keys():
    #     if len(values[box]) != 1:
    #         return False
    # return True
    return len([box for box in values.keys() if len(values[box]) != 1]) == 0

def search(values):
    reduce_puzzle(values)

    if invalid(values):
        return None

    if solved(values):
        return values ## Solved!

    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    for value in values[s]:
        tmp = values.copy()
        tmp[s] = value
        tmp = search(tmp)
        if tmp:
            return tmp

s1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
print("grid1")
print()
display(grid_values(s1, default='.'))
print()
values = grid_values(s1)
values = search(values)
display(values)
print()

grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid2)
print("grid2")
print()
display(grid_values(grid2, default='.'))
print()
values = grid_values(grid2)
values = search(values)
display(values)

grid2 = '2..6.9.........67.......8923.1.2.4.78..1.3...529478.61.56...9.843...6715.1.3572..'
values = grid_values(grid2)
print("grid2")
print()
display(grid_values(grid2, default='.'))
print()
values = grid_values(grid2)
values = search(values)
display(values)
