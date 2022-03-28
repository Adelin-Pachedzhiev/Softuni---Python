# # 1
#
# class Storage:
#     def __init__(self, capacity):
#         self.storage = []
#         self.capacity = capacity
#
#
#     def add_product(self, product):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#
#
#     def get_products(self):
#         return self.storage
#
# storage = Storage(4)
# storage.add_product('apple')
# storage.add_product('banana')
# storage.add_product('potato')
# storage.add_product('tomato')
# storage.add_product('bread')
# print(storage.get_products())

# 2

# class Weapon:
#     def __init__(self, bullets):
#         self.bullets = bullets
#
#
#     def shoot(self):
#
#         if self.bullets > 0:
#             self.bullets -= 1
#             return 'shooting…'
#         return 'no bullets left'
#
#     def __repr__(self):
#         return f'Remaining bullets: {self.bullets}'
#
#
# weapon = Weapon(5)
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# print(weapon)

# 3

# class Catalogue:
#     def __init__(self, name):
#         self.products = []
#         self.name = name
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def get_by_letter(self, first_letter):
#         return [element for element in self.products if element[0] == first_letter]
#
#     def __repr__(self):
#         self.products.sort()
#         result = f'Items in the {self.name} catalogue:\n'
#         for product in self.products:
#             result += f'{product}\n'
#         return result


# catalogue = Catalogue('Furniture')
# catalogue.add_product('Sofa')
# catalogue.add_product('Mirror')
# catalogue.add_product('Desk')
# catalogue.add_product('Chair')
# catalogue.add_product('Carpet')
# print(catalogue.get_by_letter('C'))
# print(catalogue)

# 4.

# class Town:
#     def __init__(self, town_name):
#         self.name = town_name
#
#     def set_latitude(self, latitude):
#         self.latitude = latitude
#
#     def set_longitude(self, longitude):
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
#
# town = Town('Sofia')
# town.set_latitude('42° 41\' 51.04\' N')
# town.set_longitude('23° 19\' 26.94\' E')
# print(town)

# 5

# class Class:
#     __students_count = 22
#
#     def __init__(self, class_name):
#         self.name = class_name
#
#         self.students = []
#         self.grades = []
#
#     def add_student(self, name, grade):
#         if len(self.students) < self.__students_count:
#             self.students.append(name)
#             self.grades.append(grade)
#
#     def get_average_grade(self):
#         return sum(self.grades)/len(self.grades)
#
#     def __repr__(self):
#         return f'The students in {self.name}: {", ".join(self.students)}.Average grade: {self.get_average_grade():.2f}'
#
# a_class = Class('11B')
# a_class.add_student('Peter', 4.80)
# a_class.add_student('George', 6.00)
# a_class.add_student('Amy', 3.50)
# print(a_class)

# 6

# class Inventory:
#     def __init__(self, capacity):
#         self.__capacity = capacity
#         self.items = []
#
#     def add_item(self, item):
#         if len(self.items) < self.__capacity:
#             self.items.append(item)
#         else:
#             print("not enough room in the inventory")
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         return f'Items: {", ".join(self.items)}.\nCapacity left: {self.get_capacity() - len(self.items)}'

# inventory = Inventory(2)
# inventory.add_item('potion')
# inventory.add_item('sword')
# inventory.add_item('bottle')
# print(inventory.get_capacity())
# print(inventory)

# 7

# class Article:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author
#
#     def edit(self, new_content):
#         self.content = new_content
#
#     def change_author(self, new_author):
#         self.author = new_author
#
#     def rename(self, new_title):
#         self.title = new_title
#
#     def __repr__(self):
#         return f'{self.title} - {self.content}: {self.author}'

# article = Article( 'some title ', 'some content', 'some author')
# article.edit('new content')
# article.rename('new title')
# article.change_author('new author')
# print(article)

# 8

# class Movie:
#     __watched_movies = []
#     def __init__(self, movie_name, movie_director):
#         self.name = movie_name
#         self.director = movie_director
#         self.watched = False
#
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def change_director(self, new_director):
#         self.director = new_director
#
#     def watch(self):
#         if self.name not in self.__watched_movies:
#             self.watched = True
#             self.__watched_movies.append(self.name)
#
#     def __repr__(self):
#         return (
#             f'Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {len(self.__watched_movies)}'
#         )

# first_movie = Movie('Inception', 'Christopher Nolan')
# second_movie = Movie('TheMatrix', 'The Wachowskis')
# third_movie = Movie('The Predator', 'Shane Black')
# first_movie.change_director('Me')
# third_movie.change_name('My Movie')
# first_movie.watch()
# third_movie.watch()
# first_movie.watch()
# print(first_movie)
# print(second_movie)
# print(third_movie)

# 8

class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if money >= self.price and self.owner is None:
            self.owner = owner
            print(f'Successfully bought a {self.type}. Change: {money - self.price}')
            return f'Successfully bought a {self.type}. Change: {money - self.price}'

        if money < self.price:
            print('Sorry, not enough money')
            return 'Sorry, not enough money'

        if self.owner is None:
            print('Car already sold')
            return'Car already sold'

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            print('Vehicle has no owner')

    def __repr__(self):
        if self.owner is None:
            return f'{self.model} {self.type} is on sale: {self.price}'
        return f"{self.model} {self.type} is owned by: {self.owner}"


vehicle_type = 'car'
model = 'BMW'
price = 30000
vehicle = Vehicle(vehicle_type,model, price)
vehicle.buy(15000, 'Peter')
vehicle.buy(35000, 'George')
print(vehicle)
vehicle.sell()
print(vehicle)