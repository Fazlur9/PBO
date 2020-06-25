#1 method overloading dan overriding
#Dalam Python, Anda dapat mendefinisikan metode sedemikian rupa sehingga ada beberapa cara untuk menyebutnya.

#Diberikan metode atau fungsi tunggal, kita dapat menentukan jumlah parameter sendiri.

#Bergantung pada definisi fungsi, dapat dipanggil dengan parameter nol, satu, dua atau lebih.

#Ini dikenal sebagai metode overloading. Tidak semua bahasa pemrograman mendukung metode overloading, tetapi Python dapat melakukannya.
# Contoh
class Human:

    def sayHello(self, name=None):
    
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
        print("======================")

# Create instance
obj = Human()
    
# Call the method
#obj.sayHello()
    
# Call the method with a parameter
obj.sayHello('Guido')


#Overriding adalah properti dari kelas untuk mengubah implementasi metode yang disediakan oleh salah satu kelas dasarnya.
#Dalam metode Python overriding terjadi hanya dengan mendefinisikan di kelas anak metode dengan nama metode yang sama di kelas induk. 
#Ketika Anda mendefinisikan metode dalam objek Anda membuat yang terakhir ini mampu memenuhi panggilan metode itu, sehingga implementasi dari leluhurnya tidak ikut berperan.
# Contoh
# Defining parent class 
class Parent(): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
          
    # Parent's show method 
    def show(self): 
        print(self.value) 
          
# Defining child class 
class Child(Parent): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"
          
    # Child's show method 
    def show(self): 
        print(self.value) 
        print("======================")  
          
# Driver's code 
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show() 

# 2. Studi kasus
from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self._length = length

    def area(self):
        return self._length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self._radius = radius

    def area(self):
        return pi*self._radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())