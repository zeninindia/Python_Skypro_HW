class Smartphone:
    def __init__(self, phone_name, model_name, number):
        self.phone_name = phone_name
        self.model_name = model_name
        self.number = number


    def print_smartphone(self):
      print(f"{self.phone_name} - {self.model_name}. {self.number}")


