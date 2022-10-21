# Encapsulation Example:n
from abc import ABC, abstractmethod
class Employee_Id(ABC):
    @abstractmethod
    def details(self):
        pass
class Information(Employee_Id):
    def details(self):
        print("Employee name is John")
d = Information()
d.details()

