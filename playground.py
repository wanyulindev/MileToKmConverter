def add(*args):
    result = 0
    # print(args[2])
    for n in args:
        result += n
    return result


# print(add(3, 4, 5, 68, 8, 9, 12))


def calculate(n, **kwargs):
    # print(kwargs)
    # print((type(kwargs)))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
#     print(n)
#


# calculate(3, add=5, multiply=6)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)



