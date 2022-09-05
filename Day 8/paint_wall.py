import math

def paint_calc(height, width, cover):
    num_of_cans = (height * width) / cover
    print(num_of_cans)
    total_cans = math.ceil(num_of_cans)
    print("After rounding: ", total_cans)

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)