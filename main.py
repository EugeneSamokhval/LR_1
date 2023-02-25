import Class
import copy


def better_visual(summ: list):
    exponent_decimal = Class.binary_to_int(summ[2])
    exponent_decimal -= 100
    dot_position = summ[1].index(",")
    while exponent_decimal != 0:
        if exponent_decimal>0:
            summ[1][dot_position] = summ[1][dot_position + 1]
            summ[1][dot_position + 1] = ","
            exponent_decimal -= 1
            dot_position += 1
        else:
            if dot_position > 0:
                summ[1][dot_position] = summ[1][dot_position - 1]
                summ[1][dot_position - 1] = ","
                exponent_decimal += 1
                dot_position -= 1
            else:
                summ[1].insert(dot_position+1, 0)
                exponent_decimal += 1
    iterator = 0
    integer_part_binary = []
    float_part_binary = []
    while summ[1][iterator] != ",":
        integer_part_binary.append(summ[1][iterator])
        iterator += 1
    iterator+=1
    while iterator < len(summ[1]):
        float_part_binary.append(summ[1][iterator])
        iterator += 1
    integer_part = Class.binary_to_int(integer_part_binary)
    float_part = Class.float_to_int(float_part_binary)
    print(integer_part_binary, ",", float_part_binary, "\n", integer_part + float_part, end="\n")


def binary_signed_to_int(binary: list)->int:
    print(binary)
    sign = binary[0]
    binary.pop(0)
    output = Class.binary_to_int(binary)
    if sign == 1:
        output = output*(-1)
    return output


def main():
    while True:
        print("Input type:int or float. To exit print exit\n")
        command = input()
        if command == "int":
            first_num = int(input("Input first number\n"))
            second_num = int(input("Input second number\n"))
            first_binary_pos = Class.BinaryInteger(first_num)
            second_binary_pos = Class.BinaryInteger(second_num)
            first_binary_neg = Class.BinaryInteger(-first_num)
            second_binary_neg = Class.BinaryInteger(-second_num)
            print(first_binary_pos.get_straight_form(), "\n", first_num, "\n", second_binary_pos.get_straight_form(),
                  "\n", second_num)
            operation = input("Input operation: sum, sub, mult, div\n")
            if operation == "sum":
                print(binary_signed_to_int(copy.deepcopy(first_binary_pos)+copy.deepcopy(second_binary_pos)))
                print(binary_signed_to_int(copy.deepcopy(first_binary_pos)+copy.deepcopy(second_binary_neg)))
                print(binary_signed_to_int(copy.deepcopy(first_binary_neg)+copy.deepcopy(second_binary_pos)))
                print(binary_signed_to_int(copy.deepcopy(first_binary_neg)+copy.deepcopy(second_binary_neg)))
            elif operation == "sub":
                print(binary_signed_to_int(copy.deepcopy(first_binary_pos)-copy.deepcopy(second_binary_pos)))
                print(binary_signed_to_int(copy.deepcopy(first_binary_neg)-copy.deepcopy(second_binary_pos)))
                print(binary_signed_to_int(copy.deepcopy(first_binary_pos)-copy.deepcopy(second_binary_neg)))
                print(binary_signed_to_int(copy.deepcopy(first_binary_neg)-copy.deepcopy(second_binary_neg)))
            elif operation == "mult":
                print(binary_signed_to_int(first_binary_pos*second_binary_pos))
            elif operation == "div":
                print(binary_signed_to_int(first_binary_pos/second_binary_pos))

        elif command == "float":
            first_number = float(input("Input first number\n"))
            second_number = float(input("Input second number\n"))
            first_binary_pos = Class.FloatingPoint(first_number)
            second_binary_pos = Class.FloatingPoint(second_number)
            print(first_binary_pos.get_sign(), first_binary_pos.get_exponent(), first_binary_pos.get_mantissa(), "\n",
                  second_binary_pos.get_sign(), second_binary_pos.get_exponent(), second_binary_pos.get_mantissa())
            operation = input("Input operation: sum, sub\n")
            if operation == "sum":
                pos_pos = first_binary_pos+second_binary_pos
                better_visual(pos_pos)
            elif operation == "sub":
                sub = first_binary_pos - second_binary_pos
                better_visual(sub)
        elif command == "exit":
            break


if __name__ == "__main__":
    main()
