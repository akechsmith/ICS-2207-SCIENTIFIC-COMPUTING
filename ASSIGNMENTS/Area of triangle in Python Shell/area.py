def area_triangle(base, height):
    return 0.5 * float(base) * float(height)

base = input("Enter the base: ")
height = input("Enter the height: ")

area = area_triangle(base, height)

print("The area of the triangle is:", area)
