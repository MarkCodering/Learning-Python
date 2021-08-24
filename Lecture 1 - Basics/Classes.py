#This is a classes in Python

class sampleClass():
    def __init__(self):
        self.x = 5
        self.y = 6

    def feature1(self):
        print("Feature 1 is working")

class sampleClass2(sampleClass):
    def __init__(self):
        super().__init__()
        self.z = 7

    def feature2(self):
        print("Feature 2 is working")

def main():
    sample = sampleClass()
    sample.feature1()
    sample2 = sampleClass2()
    sample2.feature2()

main()