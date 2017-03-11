def check_triangle_existence(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


print(check_triangle_existence(28, 14, 37))