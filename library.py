class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def do_meau(self):
        print(f"{self.name}: МЯУ!")

    def grow_up(self):
        self.age+=1

cat1=Cat("Борис", 3)
cat2=Cat("Игорь", 1)

print(cat1.name, cat1.age)
print(cat2.name, cat2.age)

cat1.do_meau()
cat2.grow_up()

print(cat1.name, cat1.age)
print(cat2.name, cat2.age)