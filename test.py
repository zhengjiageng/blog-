import hashlib

#md5加密
"""
Str = '123456'+'abcdef'

m = hashlib.md5()
m.update(Str.encode('utf-8'))
print(m.hexdigest())

"""

class A:
    __name = '张三'
    __age = 0

    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self,age):
    #     self.__age = age

    def get_age(self):
        print(self.__dict__['__age'])
        print(self.__age) #_A__age




a = A()
print(A._A__age)
# a.age = 'abc'
# a.set_age(10)
# print(a.get_age())

# print(a.age)

# a.__age = 100
# a.get_age()
# print(a.__age)
# print(a.__dict__)
# print(A.__dict__)