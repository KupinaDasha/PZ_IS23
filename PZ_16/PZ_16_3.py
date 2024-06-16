# Для задачи из блока 1 создать две функции, save_def и load _def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

from PZ_16.PZ_16_1 import Car


def save_def(filename, objects):
    with open(filename, 'wb') as file:
        pickle.dump(objects, file)


def load_def(filename):
    with open(filename, 'rb') as file:
        objects = pickle.load(file)
    return objects


car1 = Car("Toyota", "Corolla", 2015)
car2 = Car("Honda", "Civic", 2018)
car3 = Car("Ford", "Mustang", 2020)

objects = [car1, car2, car3]
save_def("cars.pkl", objects)

loaded_objects = load_def("cars.pkl")

for car in loaded_objects:
    car.display_info()
