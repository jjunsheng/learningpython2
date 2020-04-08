# 1
def subtract_two_numbers(n1, n2):
    if n1 > n2:
        n3 = n1 - n2
    else:
        n3 = n2 - n1
    return n3


print(subtract_two_numbers(4320, 2234))
print()

# 2
def multiply_two_numbers(n1, n2):
    n3 = n2 * n1
    return n3


print(multiply_two_numbers(4320, 2234))
print()


# 3
def handlebars(word1, word2):
    str_word1 = str(word1)
    str_word2 = str(word2)
    return print("--{}--{}--".format(str_word1, str_word2))


print(handlebars('me', 'you'))
print()


# 4
def area_circle(c_radius):
    radius_float = float(c_radius)
    c_area = 3.142 * radius_float ** 2
    return c_area


def area_triangle(t_base, t_height):
    base_float = float(t_base)
    height_float = float(t_height)
    t_area = base_float * height_float / 2
    return t_area


a = area_circle(6)
b = area_triangle(10, 5)
c = area_triangle(3, 2)
d = a + a + b - c
print(d)

big_t_b = input("Key in big triangle base: ")
big_t_h = input("Key in big triangle height: ")
big_t = area_triangle(big_t_b, big_t_h)

small_t_b = input("Key in small triangle base: ")
small_t_h = input("Key in small triangle height: ")
small_t = area_triangle(small_t_b, small_t_h)

circle_r = input("Key in circle radius: ")
circle_a = area_circle(circle_r)

float_shaded_region = float(big_t - small_t + 2 * circle_a)
shaded_region = str(float_shaded_region)
print("Total area of shaded region is {0}".format(shaded_region))
print()

