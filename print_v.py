
from project import motor
from project import variables

# My Blocks
from lower_pen import lower_pen
from lift_pen import lift_pen


def print_v(size):
    seg4 = variables['Seg4']
    lower_pen()
    motor['A+B'].on_for_degrees(10, -20, seg4)
    motor['A+B'].on_for_degrees(10, 20, seg4)
    lift_pen()
