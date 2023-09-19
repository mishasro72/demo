class person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def hello(self):
        print(f"Hello {self.name} {self.last_name}")

class Tester(person):

    def __init__(self, name, last_name, framework, age):
        super().__init__(name, last_name)
        self.framework = framework
        self.__age = age

    def test(self):
        return f'I like testing'
    
    def framew(self):
        return f'My framework is {self.framework}'

person_1 = person('Alex', 'Smith')

QA = Tester('Mike', ' Biker', 'pytester', 30)

#print(QA.age())
print(QA.__dict__)


#print(f"Hello, {person_1.name} {person_1.last_name}")
# person_1.hello()
