class Staff:
    def __init__(self, name=None, age=None, sid=None, pay=0.0):
        self.name = name
        self.age = age
        self.__sid = sid
        self.__pay = pay

    def get_sid(self): 
        return self.__sid

    def set_sid(self, sid): 
        self.__sid = sid

    def get_pay(self): 
        return self.__pay

    def set_pay(self, pay): 
        if pay >= 0:
            self.__pay = pay
        else:
            print("Pay cannot be negative.")

    def display(self):
        print(f"\n[Staff Info]")
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.__sid}, Pay: Rs{self.__pay}")

    def __str__(self): 
        return f"Staff({self.name}, {self.age}, {self.__sid}, Rs{self.__pay})"

    def __eq__(self, other): return self.__pay == other.__pay
    def __lt__(self, other): return self.__pay < other.__pay
    def __gt__(self, other): return self.__pay > other.__pay

    def __del__(self): 
        print(f"Removed {self.name}")


class Supervisor(Staff):
    def __init__(self, name, age, sid, pay, division):
        super().__init__(name, age, sid, pay)
        self.division = division

    def display(self):
        super().display()
        print(f"Division: {self.division}")

    def __str__(self): 
        return f"Supervisor({self.name}, {self.age}, {self.get_sid()}, Rs{self.get_pay()}, Division={self.division})"


class Engineer(Staff):
    def __init__(self, name, age, sid, pay, skill):
        super().__init__(name, age, sid, pay)
        self.skill = skill

    def display(self):
        super().display()
        print(f"Skill: {self.skill}")

    def __str__(self): 
        return f"Engineer({self.name}, {self.age}, {self.get_sid()}, Rs{self.get_pay()}, Skill={self.skill})"


# Store staff members
team = {}

def system_menu():
    print("\nWelcome to Staff Center")
    print("Instructions:")
    print("- Add at least one staff, supervisor, or engineer before using Show or Compare.")
    print("- Use unique IDs for each staff member.")
    print("- Pay must be a positive number.\n")

    print("Class Hierarchy Check:")
    print("Supervisor subclass of Staff?", issubclass(Supervisor, Staff))
    print("Engineer subclass of Staff?", issubclass(Engineer, Staff))

    while True:
        print("\nMain Menu:")
        print("1. Add Staff")
        print("2. Add Supervisor")
        print("3. Add Engineer")
        print("4. Show Details (Need at least one staff)")
        print("5. Compare Pay (Need at least two staff members)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            sid = input("ID: ")
            pay = float(input("Pay: "))
            s = Staff(name, age, sid, pay)
            team[sid] = s
            print(f"Added: {s}")

        elif choice == "2":
            name = input("Name: ")
            age = int(input("Age: "))
            sid = input("ID: ")
            pay = float(input("Pay: "))
            division = input("Division: ")
            sup = Supervisor(name, age, sid, pay, division)
            team[sid] = sup
            print(f"Added: {sup}")

        elif choice == "3":
            name = input("Name: ")
            age = int(input("Age: "))
            sid = input("ID: ")
            pay = float(input("Pay: "))
            skill = input("Skill: ")
            eng = Engineer(name, age, sid, pay, skill)
            team[sid] = eng
            print(f"Added: {eng}")

        elif choice == "4":
            if not team:
                print("No staff members found. Please add someone first.")
            else:
                sid = input("Enter ID: ")
                if sid in team:
                    team[sid].display()
                else:
                    print("Staff not found.")

        elif choice == "5":
            if len(team) < 2:
                print("Need at least two staff members to compare pay. Please add more.")
            else:
                id1 = input("First ID: ")
                id2 = input("Second ID: ")
                if id1 in team and id2 in team:
                    s1, s2 = team[id1], team[id2]
                    print("\nPay Comparison:")
                    if s1 > s2:
                        print(f"{s1.name} ({id1}) earns more than {s2.name} ({id2})")
                    elif s1 < s2:
                        print(f"{s1.name} ({id1}) earns less than {s2.name} ({id2})")
                    else:
                        print(f"{s1.name} ({id1}) and {s2.name} ({id2}) earn the same")
                else:
                    print("Invalid IDs entered.")

        elif choice == "6":
            print("Exiting Staff Center. Goodbye.")
            break
        else:
            print("Invalid choice. Please select from 1–6.")

system_menu()
