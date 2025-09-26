# Readable Programming Language:

import turtle

name = "READABLE Programming Language"
version = "0.0.1"
exit_word = "Type 'close' to exit, 'stop' to stop when you are in forever mode. and 'help me:' to get explanation about the features.\n"

print(f"<-- {name} -->")
print(f"Version: {version}\n")
print(exit_word)

prints = {}
variables = {}
inputs = {}

def say(line):
    if line.startswith("say "):
        message = line[4:].strip()
        if not message:
            print("⚠️  Error: Please provide something to say.")
            return
        if not ((message.startswith("'") and message.endswith("'")) or (message.startswith('"') and message.endswith('"'))):
            print("⚠️  Error: Please, wrap your letter or word with the quotation marks!")
            return
        
        print(message[1:-1])

        while True:
            choice = input(">>> Do you want to name it? (Yes / No): ").strip().lower()
            if choice == "yes":
                name_of_print = input(">>> Enter a name: ").strip()
                if not name_of_print:
                    print("⚠️  Error: Please, enter a name!")
                    continue
                prints[name_of_print] = message[1:-1]
                break
            elif choice == "no":
                break
            else:
                print("⚠️  Error: Please, enter a valid choice!")

def show_print_value(line):
    if line.startswith("show print value of "):
        name_of_print = line[20:]
        if name_of_print in prints:
            print(prints[name_of_print])
    else:
        print("⚠️  Error: No name of any print value was found.")

def set_variable(line):
    if line.startswith("create a variable:"):
        var_name = input(">>> Enter the name of the variable: ")
        var_value = input(f">>> Enter the value of '{var_name}': ")
        if not var_name.strip() and not var_value.strip():
            print("⚠️  Error: Variable name or value cannot be empty.")
        else:
            variables[var_name] = var_value

        with open("variable_history.txt", "a") as history:
            (f"{history.write(var_name)} {history.write(" = ")} {history.write(var_value)}")
            history.write("\n")

def show_variable(line):
    if line.startswith("show variable "):
        var_name = line[14:]
        if var_name in variables:
            print(variables[var_name])
    else:
        print("⚠️  Error: No variable with that name was found. Did you forget the quotation marks?")

def calculate_variables():
    expr = input(">>> Enter an expression (e.g., x + y): ")

    for var in variables:
        if var in expr:
            expr = expr.replace(var, variables[var])
    try:
        
        result = eval(expr)
        
        print(f"The result is: {result}")
    except Exception as e:
        print("⚠️  Error: Couldn't evaluate that. Make sure your variables are numeric and are created.")


def add(line):
    try:
        if line.startswith("add:"):
            firstNumber = float(input(">>> Enter the first number: "))
            secondNumber = float(input(">>> Enter the second number: "))
            result = firstNumber + secondNumber
            print(f"The result is: {result}.")

        else:
            print("⚠️  Error: Please, enter a number!")

    except ValueError:
        print("⚠️  Error: The character should be a number, not a letter or empty.")

def subtract(line):
    try:
        if line.startswith("subtract:"):
            firstNumber = float(input(">>> Enter the first number: "))
            secondNumber = float(input(">>> Enter the second number: "))
            result = firstNumber - secondNumber
            print(f"The result is: {result}.")

        else:
            print("⚠️  Error: Please, enter a number!")

    except ValueError:
        print("⚠️  Error: The character should be a number, not a letter or empty.")

def multiply(line):
    try:
        if line.startswith("multiply:"):
            firstNumber = float(input(">>> Enter the first number: "))
            secondNumber = float(input(">>> Enter the second number: "))
            result = firstNumber * secondNumber
            print(f"The result is: {result}.")

        else:
            print("⚠️  Error: Please, enter a number!")

    except ValueError:
        print("⚠️  Error: The character should be a number, not a letter or empty.")

def divide(line):
    try:
        if line.startswith("divide:"):
            firstNumber = float(input(">>> Enter the first number: "))
            secondNumber = float(input(">>> Enter the second number: "))
            result = firstNumber / secondNumber
            print(f"The result is: {result}.")

        else:
            print("⚠️  Error: Please, enter a number!")

    except ValueError:
        print("⚠️  Error: The character should be a number, not a letter or empty.")

def power(line):
    try:
        if line.startswith("power:"):
            firstNumber = float(input(">>> Enter the first number: "))
            secondNumber = float(input(">>> Enter the second number: "))
            result = firstNumber ** secondNumber
            print(f"The result is: {result}.")

        else:
            print("⚠️  Error: Please, enter a number!")

    except ValueError:
        print("⚠️  Error: The character should be a number, not a letter or empty.")

def percent(line):
    try:
        if line.startswith("percent:"):
            firstNumber = float(input(">>> Enter the first number: "))
            secondNumber = float(input(">>> Enter the second number: "))
            result = firstNumber % secondNumber
            print(f"The result is: {result}.")

        else:
            print("⚠️  Error: Please, enter a number!")

    except ValueError:
        print("⚠️  Error: The character should be a number, not a letter or empty.")

def repeat(line):
    if line.startswith("repeat:"):
        to_repeat = input(">>> Enter what do you want to repeat: ")
        try:
            times = int(input(">>> Enter how many times to repeat: "))
        except ValueError:
            print("⚠️  Error: Times to repeat should be a number, not a letter or word!")

        if (to_repeat.startswith("'") and to_repeat.endswith("'") or to_repeat.startswith('"') and to_repeat.endswith('"')):
            message = to_repeat[1:-1]
            for _ in range(times):
                print(message)

def repeat_variable(line):
    if line.startswith("repeat variable:"):
        try:
            try:
                var_name = input(">>> Enter the name of the variable you want to repeat: ")
            except ValueError:
                print("⚠️  Error: The inputs should have a existing variable and you should type a number in how many times to repeat the variable.")

            try:
                times_to_repeat = int(input(f">>> Enter how many times you want to repeat variable '{var_name}': "))
            except ValueError:
                print("⚠️  Error: The inputs should have a existing variable and you should type a number in how many times to repeat the variable.")

            try:
                for var in variables:
                    if var in var_name:
                        var_value = var_name.replace(var, variables[var])
                    for _ in range(times_to_repeat):
                        print(var_value)
            except ValueError:
                print("⚠️  Error: No variable was found to repeat with that name. Please, be sure that you made the variable with that name!")

        except ValueError:
            print("⚠️  Error: The inputs should not be empty and should not contain non existing variables!")
    else:
        print("⚠️  Error: No variable was found to repeat with that name. Please, be sure that you made the variable with that name!")

def text_box(line):
    if line.startswith("ask "):
        text = line[4:].strip()
        if (text.startswith("'") and text.endswith("'") or text.startswith('"') and text.endswith('"')):
            text = text[1:-1]
            text_input = input(text)
            print(f"'{text_input}'")

            choice = input(">>> Do you want to name it? (Yes / No): ").strip().lower()

            if choice == "yes":
                name_of_input = input(">>> Enter the name of the input so you can save what you typed: ").strip()
                inputs[name_of_input] = text_input
            
            elif choice == "no":
                pass
            if not choice:                   
                print("⚠️  Error: Please, enter a 'Yes' or 'No'")
                return
            if not name_of_input:
                print("⚠️  Error: Please, enter the name of the input!")
                return

def show_input_value(line):
    if line.startswith("show input "):
        name_of_input = line[11:]
        if name_of_input.isdigit():
            print("⚠️  Error: The name of the variable should be a letter or word, not a number!")
        if name_of_input in inputs:
            print(inputs[name_of_input])
    else:
        print("⚠️  Error: No variable with that name was found. Did you forget the quotation marks?")

def calculate_inputs():
    expr = input(">>> Enter an expression (e.g., x + y): ")

    for name_of_input in inputs:
        if name_of_input in expr:
            expr = expr.replace(name_of_input, inputs[name_of_input])
    try:
        
        result = eval(expr)
        
        print(f"The result is: {result}")
    except Exception as e:
        print("⚠️  Error: Couldn't evaluate that. Make sure your variables are numeric and are created.")

def if_statement(line):
    try:
        if line.startswith("if:"):
            type = input(">>> What do you want to type (variable): ")
            if not type.strip():
                print("⚠️  Error: Please, enter a valid choice!")
                return
            if type == "variable":
                var_name = input(">>> Type the name of an existing variable: ")
                if not var_name.strip():
                    print("⚠️  Error: Please, enter a valid choice!")
                    return
                for var in variables:
                    if var in var_name:
                        var_value = variables[var_name]
                    if var not in var_name:
                        print("⚠️  Error: No variable was found with that name. Please make a variable with that name or type the correct name of an existing variable.")
                        return
                    
                what_to_type = input(">>> Type one of these choices (<, =, >, is): ")
                    
                if not what_to_type.strip():
                    print("⚠️  Error: Please, enter a valid choice!")
                    return
                    
                to_compare = input(">>> Type a value to compare: ")
                    
                if not to_compare:
                    print("⚠️  Error: Please, enter a valid choice!")
                    return
                    
                condition = input(">>> Type a condition if it's true: ")
                                        
                if what_to_type == "=":  
                    if not condition.strip():
                        print("⚠️  Error: Please, enter a valid choice!")
                    if var_value.isdigit():
                        var_value = int(var_value)
                        to_compare = int(to_compare)
                        
                    if not var_value:
                        print("⚠️  Error: Please, enter a valid choice!")
                        
                    if not to_compare:
                        print("⚠️  Error: Please, enter a valid choice!")
                        
                    if var_value == to_compare:
                        if condition.startswith("say "):
                            print("It's True!")
                            say(condition)
                    else:
                        print("It's False!")
                        
                if what_to_type == "<":                
                    if not condition.strip():
                        print("⚠️  Error: Please, enter a valid choice!")
                    if var_value.isdigit():
                        var_value = int(var_value)
                        to_compare = int(to_compare)
                        
                    if not var_value:
                        print("⚠️  Error: Please, enter a valid choice!")
                        
                    if not to_compare:
                        print("⚠️  Error: Please, enter a valid choice!")
                    
                    if var_value < to_compare:
                        if condition.startswith("say "):
                            print("It's True!")
                            say(condition)
                    else:
                        print("It's False!")
                    
                if what_to_type == ">":                
                    if not condition.strip():
                        print("⚠️  Error: Please, enter a valid choice!")
                    if var_value.isdigit():
                        var_value = int(var_value)
                        to_compare = int(to_compare)

                    if not var_value:
                        print("⚠️  Error: Please, enter a valid choice!")
                        
                    if not to_compare:
                        print("⚠️  Error: Please, enter a valid choice!")
                    
                    if var_value > to_compare:
                        if condition.startswith("say "):
                            print("It's True!")
                            say(condition)
                    else:
                        print("It's False!")
                
                if what_to_type == "is":
                    boolean = input(">>> Type a boolean (True or False): ")
                    if not boolean.strip():
                        print("⚠️  Error: Please, enter a valid choice!")
                        
                    condition = input(">>> Type the condition if it's true or false: ")      
                    if not condition.strip():                    
                        print("⚠️  Error: Please, enter a valid choice!")
                    
                    for var in variables:
                        if var in var_name and boolean == "True":
                            if condition.startswith("say "):
                                print("It's True!")
                                say(condition)
                        if not var in var_name and boolean == "False":
                            print("It's False!")
                            
                        if var in var_name and boolean == "False":
                            if condition.startswith("say "):
                                print("It's True!")
                                say(condition)
                                
                        if not var in var_name and boolean == "True":
                            print("It's False!")
    
    except Exception as e:
        print(f"⚠️  Error: Unexpected or unknown error: {e}")
                

def write_new_file(line):
    if line.startswith("create a new file:"):
        file_name = input(">>> Enter the name of the file you want to create: ")
        
        if not file_name.strip():
            print("⚠️  Error: Please, enter the name of the file!")
            return write_new_file(line)

        file_type = input(">>> Enter the type of the file you want to create: ")
        
        if not file_type.strip():
            print("⚠️  Error: Please, enter the type of the file!")
            return write_new_file(line)

        file_content = input(">>> Enter what should your file contain: ")

        if not file_content.strip():
            print("⚠️  Error: Please, enter the content of the file!")
            return write_new_file(line)

        with open(f"{file_name}.{file_type}", "a") as file:
            file.write(f"{file_content}\n")
        
def draw(line):    
    try:
        if line.startswith("draw "):
            shape = line[5:].strip()
        
            t = turtle.Turtle()
        
            if shape == "rectangle":
                for _ in range(2):
                    t.forward(100)
                    t.right(90)
                    t.forward(50)
                    t.right(90)
                
            elif shape == "circle":
                t.circle(50)

            elif shape == "triangle":
                for _ in range(3):
                    t.forward(100)
                    t.left(120)
            
            else:
                print("⚠️  Error: Unknown or unsupported shape!")

    except turtle.Terminator:
        print("⚠️  Error: Please, type the name of a supported shape, like rectangle, circle or triangle!")
    except Exception as e:
        print(f"⚠️  Unexpected or unknown error: {e}")

def comment(line):
    if line.startswith("#"):
        pass

def help(line):
    if line.startswith("help me:"):
        print("<-- READABLE Programming Language Help Center (RPLHC) -->\n")
        print(" -- Printing and Displaying:")
        print("say 'Hello, World!'- Prints a value and then asks you if you want to name it or not. For example: 'say 'Hello, World!''.")
        print("show print value of (name of print value) - Prints the value of the print you have saved. For example: 'show print value of greeting' and let's say it prints 'Hello!'.")
        print("show variable (name of the variable) - Prints the value of the variable. For example: 'show variable a' and let's say it prints 'Hey!'.\n")
        print(" -- Math and Calculations:")
        print("calculate variables: - Calculates the value of the existing variables. You will be asked to write two variables and in between them, you need to write an operation. For example: 'a + b'.")
        print("calculate inputs: - Calculates the value of the existing inputs. You will be asked to write two inputs and in between them, you need to write an operation. For example: 'a + b'.")
        print("add: - Adds two numbers. You will be asked to write the first number and the second number.")
        print("subtract: - Subtracts two numbers. You will be asked to write the first number and the second number.")
        print("multiply: - Multiplies two numbers. You will be asked to write the first number and the second number.")
        print("divide: - Divides two numbers. You will be asked to write the first number and the second number.")
        print("power: - You will be asked to write the first number and the second number. Something like this: first number in the power of second number that you have written.\n")
        print(" -- Control Flow:")
        print("forever: - It creates a forever loop. To exit, you can type 'stop'. For example: in the forever loop, when you write 'say 'Hello!'', it will print 'Hello!' forever, until you close the program.")
        print("repeat: - It repeats a letter or word how many times you want. You will be asked what kind of string to repeat and how many times to repeat.")
        print("repeat variable: - It repeats an existing variable how many times you want. You will be asked to type the name of the variable and how many times to print that variable.")
        print("if: - It creates a if statement. You will be asked to type a variable, an expression, a value and the condition where you can type a line of code. If the condition is True, it will execute the code, but if it's false, it will not execute the code.\n")
        print(" -- Functionality:")
        print("create a variable: - Creates a new variable. You will be asked about the name of the variable and its value.")
        print("create a function: - It creates a new function and you will be asked to type the name of the function. Then you can type some code inside that function forever, until you type 'end the function'. To run the function, you type: 'run (name of the function)'.")
        print("create a new file: - Creates a new file and you will be asked to write the name of the file, the type of the file and the content of the file.")
        print("run (name of the file): - It runs a supported file that RPL (READABLE Programming Language) can run. It should contain code that can be run by RPL.\n")
        print(" -- User interactions:")
        print("ask 'Say something: '- It will create a input where you can type a text and then it will ask you if you want to save it or not. For example: input 'Say something: ', it will display 'Say something: ' and you'll be able to type anything you want.")
        print("show input (name of input) - Prints the saved input.")
        print("draw rectangle: / triangle: / circle: - Draws the figures that you type. For example: 'draw rectangle:' draws a rectangle.\n")
        print(" -- REM:")
        print("# - Makes a comment. Comments are ignored by the program.\n")
        print(" -- Explanation and Helping:")
        print("help me: - This brings you here in the READABLE Programming Language Help Center (RPLHC).\n")

def function(line):
    if line.startswith("create a function:"):
        try:
            function_name = input(">>> Enter the name of the function you want to create: ")
            if not function_name.strip():
                print("⚠️  Error: Please, enter the name of the variable!")
                return main()
            print(f"function {function_name}:")
            while True:            
                function_code = input("...    ")
                if function_code == "end the function":
                    return main()
            
                with open(function_name, "a") as function:
                    function.write(function_code)
                    function.write("\n")
        except FileNotFoundError:
            if not function_name.endswith(".txt") and not function_name.endswith(".rpl"):
                print(f"⚠️  Error: '{function_name}' is not a valid file. Did you mean to run a command instead?")
            return print(f"⚠️  Error: Function {function_name} not found! Be sure that the function exists or it's typed correctly!")
        except Exception as e:
            print(f"⚠️  Unexpected or unknown error: {e}")

    if line.startswith("run "):
        name_of_function = line[4:]
        if name_of_function == function_name:
            try:
                with open(f"{function_name}.rpl", "r") as function:
                    lines = function.readlines()
                    for line in lines:
                        line = line.strip()          
                            
                        if line.startswith("say "):
                            say(line)

                        elif line.startswith("show print value of "):
                            show_print_value(line)

                        elif line.startswith("create a variable"):
                            set_variable(line)
                                    
                        elif line.startswith("show variable "):
                            show_variable(line)
                                
                        elif line.startswith("calculate variables:"):
                            calculate_variables()
                                
                        elif line.startswith("add:"):
                            add(line)

                        elif line.startswith("subtract:"):
                            subtract(line)

                        elif line.startswith("multiply:"):
                            multiply(line)

                        elif line.startswith("divide:"):
                            divide(line)

                        elif line.startswith("power:"):
                            power(line)

                        elif line.startswith("percent:"):
                            percent(line)

                        elif line.startswith("forever:"):
                            forever(line)

                        elif line.startswith("repeat:"):
                            repeat(line)

                        elif line.startswith("repeat variable:"):
                            repeat_variable(line)

                        elif line.startswith("ask "):
                            text_box(line)

                        elif line.startswith("show input "):
                            show_input_value(line)

                        elif line.startswith("calculate inputs:"):
                            calculate_inputs()

                        elif line.startswith("if:"):
                            if_statement(line)
                        
                        elif line.startswith("create a new file:"):
                            write_new_file(line)

                        elif line.startswith("draw "):
                            draw(line)

                        elif line.startswith("#"):
                            comment(line)

            except FileNotFoundError:
                print(f"⚠️  Error: No function was found with that name in '{line}'. Make sure you made the function with that name or you typed its name correctly.")

            except Exception as e:
                print(f"⚠️  Unexpected or unknown error: {e}")
    
        else:
            print(f"⚠️  Error: Function {function_name} not found. Be sure that the function exists or it's typed correctly!")        

def forever(line):
    print("🔁 Forever mode activated. Type 'stop' to exit.")
    while True:
        forever_line = input("...    ")

        if forever_line.lower() == "stop":
            return main()

        while True:
            if forever_line.startswith("say "):
                say(forever_line)

            elif forever_line.startswith("show print value of "):
                show_print_value(forever_line)

            elif forever_line.startswith("create a variable:"):
                set_variable(forever_line)

            elif forever_line.startswith("show variable "):
                show_variable(forever_line)

            elif forever_line.startswith("calculate variables:"):
                calculate_variables()

            elif forever_line.startswith("add:"):
                add(forever_line)

            elif forever_line.startswith("subtract:"):
                subtract(forever_line)

            elif forever_line.startswith("multiply:"):
                multiply(forever_line)

            elif forever_line.startswith("divide:"):
                divide(forever_line)

            elif forever_line.startswith("power:"):
                power(forever_line)

            elif forever_line.startswith("percent:"):
                percent(forever_line)

            elif forever_line.startswith("repeat:"):
                repeat(forever_line)

            elif forever_line.startswith("repeat variable:"):
                repeat_variable(forever_line)

            elif forever_line.startswith("ask "):
                text_box(forever_line)
            
            elif forever_line.startswith("show input "):
                show_input_value(forever_line)
            
            elif forever_line.startswith("calculate inputs:"):
                calculate_inputs()

            if forever_line.startswith("if:"):
                if_statement(forever_line)
                
            elif forever_line.startswith("create a function:"):
                function(forever_line)

            elif forever_line.startswith("create a new file:"):
                write_new_file(forever_line)

            elif forever_line.startswith("draw "):
                draw(forever_line)
            
            elif forever_line.startswith("#"):
                comment(forever_line)

            elif forever_line.startswith("help me:"):
                help(forever_line)

            else:
                print("⚠️  Error: Unknown or incomplete function.")

def save_user_input(line):
    with open("readable_history.txt", "a") as history:
        history.write(line)
        history.write("\n")

def load_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()

                if line.startswith("say "):
                    say(line)

                elif line.startswith("show print value of "):
                    show_print_value(line)

                elif line.startswith("create a variable"):
                    set_variable(line)

                elif line.startswith("show variable "):
                    show_variable(line)

                elif line.startswith("calculate variables:"):
                    calculate_variables()

                elif line.startswith("add:"):
                    add(line)

                elif line.startswith("subtract:"):
                    subtract(line)

                elif line.startswith("multiply:"):
                    multiply(line)

                elif line.startswith("divide:"):
                    divide(line)

                elif line.startswith("power:"):
                    power(line)

                elif line.startswith("percent:"):
                    percent(line)

                elif line.startswith("forever:"):
                    forever(line)

                elif line.startswith("repeat:"):
                    repeat(line)

                elif line.startswith("repeat variable:"):
                    repeat_variable(line)

                elif line.startswith("ask "):
                    text_box(line)
                
                elif line.startswith("show input "):
                    show_input_value(line)

                elif line.startswith("calculate inputs:"):
                    calculate_inputs()

                elif line.startswith("if:"):
                    if_statement(line)
                    
                elif line.startswith("create a function:"):
                    function(line)
                
                elif line.startswith("create a new file:"):
                    write_new_file(line)

                elif line.startswith("draw "):
                    draw(line)

                elif line.startswith("#"):
                    comment(line)

                elif line.startswith("help me:"):
                    help(line)

                else:
                    print(f"⚠️  Error: Unknown or incomplete function in line '{line}'.")

    except FileNotFoundError:
        print("⚠️  Error: File not found or not supported!")

    except Exception as e:
        print(f"⚠️  Unexpected or unknown error: {e}")

def main():
    while True:
        line = input(">>> ")

        if line.lower() == "close":
            quit()

        elif line.startswith("say "):
            say(line)

        elif line.startswith("show print value of "):
            show_print_value(line)

        elif line.startswith("create a variable:"):
            set_variable(line)

        elif line.startswith("show variable "):
            show_variable(line)

        elif line.startswith("calculate variables:"):
            calculate_variables()

        elif line.startswith("add:"):
            add(line)

        elif line.startswith("subtract:"):
            subtract(line)

        elif line.startswith("multiply:"):
            multiply(line)

        elif line.startswith("divide:"):
            divide(line)

        elif line.startswith("power:"):
            power(line)

        elif line.startswith("percent:"):
            percent(line)

        elif line.startswith("forever:"):
            forever(line)

        elif line.startswith("repeat:"):
            repeat(line)

        elif line.startswith("repeat variable:"):
            repeat_variable(line)

        elif line.startswith("ask "):
            text_box(line)
        
        elif line.startswith("show input "):
            show_input_value(line)

        elif line.startswith("calculate inputs:"):
            calculate_inputs()

        elif line.startswith("if:"):
            if_statement(line)
            
        elif line.startswith("create a function:"):
            function(line)
        
        elif line.startswith("create a new file:"):
            write_new_file(line)

        elif line.startswith("draw "):
            draw(line)

        elif line.startswith("#"):
            comment(line)

        elif line.startswith("help me:"):
            help(line)
        
        elif line.startswith("run "):
            filename = line[4:].strip()
            load_file(filename)            
                    
        else:
            print(f"⚠️  Error: Line '{line}'. Unknown function, incomplete function or not found. Please type existing functions or complete functions, or type 'help me:' for explanation!")

        save_user_input(line)

if __name__ == "__main__":
    main()