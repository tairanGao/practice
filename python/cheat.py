from collections import defaultdict

def find_overlap(column1, column2, column_size):
    c1brs = column1 & ~(1 << column_size)  # Column 1 bottom right side
    c1urs = column1 >> 1  # Column 1 upper right side
    c2brs = column2 & ~(1 << column_size)  # Column 2 bottom right side
    c2urs = column2 >> 1  # Column 2 upper right side

    return (c1brs & ~c2brs & ~c1urs & ~c2urs) | (~c1brs & c2brs & ~c1urs & ~c2urs) | (~c1brs & ~c2brs & c1urs & ~c2urs) | (~c1brs & ~c2brs & ~c1urs & c2urs)


def get_binary_number_from_row(row):
    return sum([(1 << key) * value for key, value in enumerate(row)])


def answer(g):
    if len(g[0]) > len(g):
        g = list(zip(*g))  # Make sure we always have shorter column

    column_count = len(g[0])

    columns_as_binary_numbers = [get_binary_number_from_row(row) for row in g]
    columns_as_binary_numbers_set = set(columns_as_binary_numbers)

    previous_column_states = {previous_state: 1 for previous_state in range(1 << (column_count+1))}

    overlapping_column_states_cache = defaultdict(set)

    for previous_state in range(1 << (column_count + 1)):
        for next_state in range(1 << (column_count + 1)):
            overlap = find_overlap(previous_state, next_state, column_count)

            if overlap in columns_as_binary_numbers_set:
                overlapping_column_states_cache[(overlap, previous_state)].add(next_state)

    for column_value in columns_as_binary_numbers:
        next_column = defaultdict(int)
        for previous_column_state in previous_column_states:
            for overlapping_column_state in overlapping_column_states_cache[(column_value, previous_column_state)]:
                next_column[overlapping_column_state] += previous_column_states[previous_column_state]

        previous_column_states = next_column

    return sum(previous_column_states.values())