"""
pi=3.1415
calculate the area of circle upto 2 decimal point.
"""
def circleArea(r):
    pi=3.1415
    return round(r*r*pi,2)
r=int(input())
print(circleArea(r))