input = [[1, 1, 2], [2, 2, 0.5], [-1, -3, 2], [5, 2, 1]]


class Circle():
    """A circle object"""

    def __init__(self, input_coord):
        self.x = input_coord[0]
        self.y = input_coord[1]
        self.r = input_coord[2]

    def left_xcoord(self):
        """Return leftmost coordinate"""
        return self.r - self.x

    def top_ycoord(self):
        """Return topmost coordinate"""
        return self.r - self.x

    def right_xcoord(self):
        """Return rightmost coordinate"""
        return self.r + self.x

    def bottom_ycoord(self):
        """Return bottommost coordinate"""
        return self.r - self.y


def convert_to_circle_object(input_list):
    """In: Array of (x,y,r) circle data. Out: Array of circle objects"""
    circle_list = []
    for coord in input_list:
        new_circle = Circle(coord)
        circle_list.append(new_circle)

    return circle_list


def find_leftmost(circle_list):
    """In: list of circle objects. Return xcoord (double) of leftmost circle"""
    x_min = 9999
    for circle in circle_list:
        if circle.x - circle.r < x_min:
            x_min = circle.x - circle.r

    return x_min


def find_topmost(circle_list):
    """In: list of circle objects."""
    y_max = -9999
    for circle in circle_list:
        if circle.y + circle.r > y_max:
            y_max = circle.y + circle.r

    return y_max


def find_rightmost(circle_list):
    """In: list of circle objects."""
    x_max = -9999
    for circle in circle_list:
        if circle.x + circle.r > x_max:
            x_max = circle.x + circle.r

    return x_max


def find_bottommost(circle_list):
    """In: list of circle objects."""
    y_min = 9999
    for circle in circle_list:
        if circle.y - circle.r < y_min:
            y_min = circle.y - circle.r

    return y_min


# Main Procedure
# 1) Convert input to an array of circle objects
# 2) Find leftmost, rightmost, etc x,y value of circles
# 3) Return as [(-x,-y),(-x,y),(x,y),(x,-y)] list
# 4) Output in correct format

circle_list = convert_to_circle_object(input)
edge_list = [find_leftmost(circle_list), find_topmost(circle_list),
             find_rightmost(circle_list), find_bottommost(circle_list)]
output_list = [[edge_list[0], edge_list[3]], [edge_list[0], edge_list[1]],
               [edge_list[2], edge_list[1]], [edge_list[2], edge_list[3]]]

# Output in required format
print("({0:.3f}, {1:.3f}), ({2:.3f}, {3:.3f}), ({4:.3f}, {5:.3f}), ({6:.3f}, {7:.3f})"
      .format(output_list[0][0], output_list[0][1],
              output_list[1][0], output_list[1][1],
              output_list[2][0], output_list[2][1],
              output_list[3][0], output_list[3][1]))
