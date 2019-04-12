class SomeClass:
    def __init__(self):
        self.name = "LiLei"


@property
def speak(self):
    return "chinese"


SomeClass.speak = speak
someone = SomeClass()
print(someone.speak)

