class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Merhaba, benim adım {self.name}!"

# Sınıfı kullanma örneği
if __name__ == "__main__":
    obj = MyClass("Ahmet")
    print(obj.greet())
