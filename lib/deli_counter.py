katz_deli = []


def line(katz_deli):
    if katz_deli:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f" {i+1}. {katz_deli[i]}"
        print(message)
    else:
        print("The line is currently empty.")


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")


def now_serving(katz_deli):
    if katz_deli:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.remove(katz_deli[0])
    else:
        print("There is nobody waiting to be served!")
