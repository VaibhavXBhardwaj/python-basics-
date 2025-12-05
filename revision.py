name = input("whats ur name? ")

match name:
    case "harry" | "ron" | "hermione":
        print("gryffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who're you? ")
        