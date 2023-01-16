class ClassTest():
    def instance_method(self):
        print(f'Called instance_method of {self}')



    @classmethod
    def class_method(cls):
        """When class_method get called classtest will automatically pass to it"""
        print(f'called class_method of {cls}')



    @staticmethod
    def static_method():
        """static methods don't get anything when call them"""
        print("called static_method")
    




test = ClassTest()
"""Instance means object"""
ClassTest.instance_method(test)
ClassTest.class_method()