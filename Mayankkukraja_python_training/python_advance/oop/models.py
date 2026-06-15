# Q40, Q41, Q42, Q43, Q44 - Object Oriented Programming

#Q40- basic class

class Student:
    """Represent a student with basic details."""

    def __init__(
        self,
        name: str,
        roll_no: int,
        branch: str,
        marks: int
    ) -> None:
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks


    def display(self) -> None:
        """Display student details."""

        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")

#Q41- constructors
class Car:
    """Represent a car."""

    def __init__(
        self,
        company: str,
        model: str,
        year: int
    ) -> None:
        self.company = company
        self.model = model
        self.year = year

    def display(self) -> None:
        """Display car details."""

        print(f"Car: {self.year} {self.company} {self.model}")

    def start(self) -> None:
        """Start the car."""

        print(f"{self.company} {self.model} started")


class Person:
    """Represent a person."""

    def __init__(
        self,
        name: str,
        age: int
    ) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> None:
        """Introduce the person."""

        print(f"Hi, I am {self.name} and I am {self.age} years old.")

#Q 42 - Inheritance part
class Employee(Person):
    """Represent an employee."""

    def __init__(
        self,
        name: str,
        age: int,
        company: str,
        salary: int
    ) -> None:
        super().__init__(name, age)

        self.company = company
        self.salary = salary

    def introduce(self) -> None:
        """Display employee details."""

        super().introduce()
        print(f"I work at {self.company} and earn Rs.{self.salary}")

#Q 43 - Encapsulation
class BankAccount:
    """Represent a bank account."""

    def __init__(
        self,
        holder: str,
        balance: int
    ) -> None:
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount: int) -> None:
        """Deposit money into account."""

        if amount > 0:
            self.__balance += amount
            print(
                f"Deposited Rs.{amount}. "
                f"Balance: Rs.{self.__balance}"
            )

    def withdraw(self, amount: int) -> None:
        """Withdraw money from account."""

        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount

            print(
                f"Withdrew Rs.{amount}. "
                f"Balance: Rs.{self.__balance}"
            )

    def get_balance(self) -> int:
        """Return current balance."""

        return self.__balance


#Q 44 - polymorphism
class Dog:
    """Represent a dog."""

    def speak(self) -> None:
        print("Dog says: Woof!")


class Cat:
    """Represent a cat."""

    def speak(self) -> None:
        print("Cat says: Meow!")


class Cow:
    """Represent a cow."""

    def speak(self) -> None:
        print("Cow says: Moo!")


def make_animal_speak(animal) -> None:
    """Demonstrate polymorphism."""

    animal.speak()


if __name__ == "__main__":

    print("--- Q40: Student ---")

    student = Student(
        "Mayank",
        121,
        "CSE",
        89
    )

    student.display()

    print("\n--- Q41: Car ---")

    car = Car(
        "Hyundai",
        "i20",
        2023
    )

    car.display()
    car.start()

    print("\n--- Q42: Inheritance ---")

    employee = Employee(
        "Rohit",
        27,
        "NucleusTeq",
        85000
    )

    employee.introduce()

    print("\n--- Q43: Encapsulation ---")

    account = BankAccount(
        "Mayank",
        10000
    )

    account.deposit(5000)
    account.withdraw(3000)

    print(
        f"Current Balance: "
        f"Rs.{account.get_balance()}"
    )

    print("\n--- Q44: Polymorphism ---")

    animal_list = [
        Dog(),
        Cat(),
        Cow()
    ]

    for animal in animal_list:
        make_animal_speak(animal)