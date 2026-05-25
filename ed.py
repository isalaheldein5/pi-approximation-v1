def findpi(stepCount):
    stepWith = 1/stepCount
    area = 0
    for i in range(stepCount):
        x = i*stepWith
        height = 1/(1+x**2)
        rectangleArea = height*stepWith
        area = area + rectangleArea
    return area * 4
user = int(input("enter stepcount: "))
ans = findpi(user)
print(ans)


