current_result = 0
pending_operation = None
new_number_input = 0


def num_input(num):
    global new_number_input

    new_number_input = new_number_input * 10 + num


def perform_calculation(num1, op, num2):

    if op == "+":
        return num1 + num2

    elif op == "-":
        return num1 - num2

    elif op == "*":
        return num1 * num2

    elif op == "/":

        if num2 == 0:
            print("Cannot divide by zero")
            return num1

        return num1 / num2


def op_pressed(op):

    global current_result
    global pending_operation
    global new_number_input

    if pending_operation is None:

        current_result = new_number_input

    else:

        current_result = perform_calculation(
            current_result,
            pending_operation,
            new_number_input
        )

    pending_operation = op
    new_number_input = 0


def equals_pressed():

    global current_result
    global pending_operation
    global new_number_input

    if pending_operation is not None:

        current_result = perform_calculation(
            current_result,
            pending_operation,
            new_number_input
        )

        pending_operation = None
        new_number_input = 0

    return current_result


def clear_pressed():

    global current_result
    global pending_operation
    global new_number_input

    current_result = 0
    pending_operation = None
    new_number_input = 0