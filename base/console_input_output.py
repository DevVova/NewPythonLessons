def input_output():
    print("Hello", end="! ")
    print("I'm Vova", "And you?", sep="\t")
    print("Good!", "Enter your name: ",sep=" ", end="")
    name = input()
    print(f"Hello {name}", "!", sep="")