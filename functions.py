def print_empl_data(name, age):  # paraméter nevek==változók
    print("alkalmazott név", name)
    print("alkalmazott kora", age)
    # változók csak addig élnek, amíg a függvény. Végén paraméterek törlődnek. Lokális és nem globális


print_empl_data("John", 10)  # függvény hívás, paraméter értékek
print_empl_data("Jane", 20)
print("end")


def sum_A_B(a, b):  #
    print(a + b)


sum_A_B(6, 8)
