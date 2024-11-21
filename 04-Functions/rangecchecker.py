def check_range(x, lower_boundary, higher_boundary):
    c = False
    if lower_boundary > higher_boundary:
        v = lower_boundary
        lower_boundary = higher_boundary
        higher_boundary = v
    for i in range(lower_boundary + 1, higher_boundary):
        if x == i and not c:
            c = True
    return c