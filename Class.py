import copy
import ClassMethods


def addition_cases(first_object: list, second_object: list, in_mind: int, iterator: int, result):
    if in_mind == 0:
        if first_object[iterator] == 1 and second_object[iterator] == 0:
            result.insert(0, 1)
        elif first_object[iterator] == 0 and second_object[iterator] == 1:
            result.insert(0, 1)
        elif first_object[iterator] == 1 and second_object[iterator] == 1:
            result.insert(0, 0)
            in_mind += 1
        elif first_object[iterator] == 0 and second_object[iterator] == 0:
            result.insert(0, 0)
    else:
        if first_object[iterator] == 1 and second_object[iterator] == 0:
            result.insert(0, 0)
        elif first_object[iterator] == 0 and second_object[iterator] == 1:
            result.insert(0, 0)
        elif first_object[iterator] == 1 and second_object[iterator] == 1:
            result.insert(0, 1)
        elif first_object[iterator] == 0 and second_object[iterator] == 0:
            result.insert(0, 1)
            in_mind -= 1
    return result, in_mind


def subtraction_cases(first_object: list, second_object: list, iterator: int, result: list):
    if first_object[iterator] == 1 and second_object[iterator] == 1:
        result.insert(0, 0)
    elif first_object[iterator] == 1 and second_object[iterator] == 0:
        result.insert(0, 1)
    elif first_object[iterator] == 0 and second_object[iterator] == 1:
        second_iterator = copy.copy(iterator)
        while first_object[second_iterator] != 1:
            first_object[second_iterator] = 1
            second_iterator -= 1
        first_object[second_iterator] = 0
        result.insert(0, 1)
    elif first_object[iterator] == 0 and second_object[iterator] == 0:
        result.insert(0, 0)
    return result, iterator, first_object


def binary_addition(first_binary: list, second_binary: list)->list:
    result = []
    first_binary.insert(0, 0)
    in_mind = 0
    while len(first_binary) != len(second_binary):
        second_binary.insert(0, 0)
    iterator = len(first_binary) - 1
    while iterator >= 0:
        result, in_mind = addition_cases(first_binary, second_binary, in_mind, iterator, result)
        iterator-=1
    cleaner = 0
    while second_binary[cleaner] != 1 and len(second_binary)>1:
        second_binary.pop(0)
    while first_binary[cleaner] != 1 and len(first_binary)>1:
        first_binary.pop(0)
    while result[cleaner] != 1 and len(result)>1:
        result.pop(0)
    return result


def binary_difference(first_binary: list, second_binary: list):
    result = []
    first_binary.insert(0, 0)
    while len(second_binary) < len(first_binary):
        second_binary.insert(0, 0)
    iterator = len(first_binary) - 1
    while iterator >= 0:
        result, iterator, first_binary = subtraction_cases(first_binary, second_binary, iterator, result)
        iterator-=1
    while second_binary[0] != 1 and len(second_binary)>1:
        second_binary.pop(0)
    while first_binary[0] != 1 and len(first_binary)>1:
        first_binary.pop(0)
    while result[0] != 1 and len(result)>1:
        result.pop(0)
    return result


def binary_multiplication(first_binary, second_binary):
    list_for_summ = []
    iterator = len(second_binary) - 1
    while iterator >= 0:
        if second_binary[iterator] == 1:
            temp_binary = copy.copy(first_binary)
            for shift in range(0, len(second_binary)-iterator-1):
                temp_binary.append(0)
            list_for_summ.append(temp_binary)
        iterator-=1
    result = copy.copy(list_for_summ[len(list_for_summ)-1])
    iterator = len(list_for_summ) -2
    while iterator>=0:
        result=binary_addition(result, list_for_summ[iterator])
        iterator-=1
    return result


def binary_compare_more(first_binary, second_binary)->bool:
    if len(first_binary) > len(second_binary):
        return True
    elif len(first_binary) < len(second_binary):
        return False
    else:
        for iteration in range(0, len(first_binary)):
            if first_binary[iteration] == 1 and second_binary[iteration] == 0:
                return True
            elif first_binary[iteration] == 0 and second_binary[iteration] == 1:
                return False


def binary_compare_equal(first_binary, second_binary)->bool:
    if len(first_binary) == len(second_binary):
        for iterator in range(0, len(first_binary)):
            if first_binary[iterator] != second_binary[iterator]:
                return False
        return True
    else:
        return False
            

def binary_division(first_binary, second_binary):
    result = [0]
    first_binary: list
    assert second_binary != [0], "Zero division error"
    if binary_compare_more(first_binary, second_binary):
        while binary_compare_more(first_binary, second_binary) or binary_compare_equal(first_binary, second_binary):
            first_binary = binary_difference(first_binary, second_binary)
            result = binary_addition(result, [1])
    elif binary_compare_equal(first_binary, second_binary):
        result[0] = 1
    else:
        result = [0]
    return result


def sign_logic(number: int, minus_sign, matrix):
    if number > 0:
        minus_sign = False
    else:
        number *= -1
    while number > 0:
        matrix.insert(0, number % 2)
        number = number // 2
    rev_ver = copy.copy(matrix)
    if minus_sign:
        for sign in rev_ver:
            if sign == 0:
                sign = 1
            else:
                sign = 0
    output = (minus_sign, matrix, rev_ver)
    return output


def int_to_bin(number: int):
    matrix = []
    minus_sign = True
    if number != 0:
        output = sign_logic(number, minus_sign, matrix)
    else:
        minus_sign = False
        matrix = [0]
        rev_ver = [0]
        output = (minus_sign, matrix, rev_ver)
    return output


def floating_to_bin(number: float)->list:
    temp_current = copy.copy(number)
    result = []
    if number != 0.0:
        for iteration in range(0, 20):
            check = temp_current * 2
            if check > 1:
                temp_current = check - 1
                result.append(1)
            elif check == 1:
                result.append(1)
                break
            else:
                temp_current = copy.copy(check)
                result.append(0)
    else:
        result = [0]
    return result


def normalise_positive(true_binary, exponent, counter: int):
    while true_binary[0][counter] != 1:
        counter += 1
    start = copy.copy(counter)
    while counter < len(true_binary[0]) - 1:
        exponent = exponent + 1
        counter += 1
    iterator = len(true_binary[0]) - 1
    while iterator != start:
        true_binary[1].insert(0, true_binary[0][iterator])
        iterator -= 1
    true_binary[0].clear()
    true_binary[0].append(1)
    result = [true_binary[0], true_binary[1], exponent]
    return result


def normalise_negative(true_binary, exponent, counter: int):
    while true_binary[1][counter] != 1:
        counter += 1
    end = copy.copy(counter)
    counter = 0
    while counter <= end:
        true_binary[0].append(true_binary[1][counter])
        counter += 1
        exponent = exponent - 1
    for iterator in range(0, end + 1):
        true_binary[1].pop(0)
        iterator += 1
    result = [true_binary[0], true_binary[1], exponent]
    return result


def normalise_true_binary(true_binary: tuple, exponent):
    counter = 0
    if true_binary[0] != [0]:
        return normalise_positive(true_binary, exponent, counter)
    else:
        return normalise_negative(true_binary, exponent, counter)


def fixed_sum_preparations(first_binary: list, second_binary: list):
    first_dot = 0
    second_dot = 0
    while second_binary[second_dot] != ",":
        second_dot += 1
    second_binary.pop(second_dot)
    first_size = len(first_binary)
    while first_binary[first_dot] != ",":
        first_dot += 1
    first_binary.pop(first_dot)
    first_binary.insert(0, 0)
    return first_binary, second_binary, first_size, first_dot, second_dot


def binary_fixed_sum(first_binary: list, second_binary: list):
    result = []
    first_binary, second_binary, first_size, first_dot, second_dot = fixed_sum_preparations(first_binary, second_binary)
    in_mind = 0
    while len(first_binary) != len(second_binary):
        second_binary.insert(0, 0)
    iterator = len(first_binary) - 1
    while iterator>=0:
        result, in_mind = addition_cases(first_binary, second_binary, in_mind, iterator, result)
        iterator-=1
    cleaner = 0
    while second_binary[cleaner] != 1 and len(second_binary)>1:
        second_binary.pop(0)
    while first_binary[cleaner] != 1 and len(first_binary)>1:
        first_binary.pop(0)
    while result[cleaner] != 1 and len(result)>1:
        result.pop(0)
    first_dot = first_dot + (len(result) - first_size)
    result.insert(first_dot, ",")
    return result


def binary_fixed_sub(first_binary, second_binary):
    first_dot = 0
    second_dot = 0
    while second_binary[second_dot] != ",":
        second_dot += 1
    second_binary.pop(second_dot)
    first_size = len(first_binary)
    while first_binary[first_dot] != ",":
        first_dot += 1
    first_binary.pop(first_dot)
    result = binary_difference(first_binary, second_binary)
    first_dot = first_dot - (first_size - len(result))
    result.insert(first_dot, ",")
    return result


def binary_to_int(binary)->int:
    result = 0
    iterator = len(binary)-1
    power = 0
    while iterator >= 0:
        if binary[iterator] == 1:
            result+=2**power
        power+=1
        iterator-=1
    return result


def float_to_int(binary)->float:
    result = 0.0
    iterator = 0
    while iterator <= len(binary)-1:
        if binary[iterator] == 1:
            result+=2**(-(iterator+1))
        iterator+=1
    return result


class BinaryInteger:
    def __init__(self, number: int):
        binary_conversion = int_to_bin(number)
        self.__decimal_number = number
        self.__binary_straight = binary_conversion[1]
        if binary_conversion[0]:
            self.__binary_reversed = copy.copy(binary_conversion[2])
        else:
            self.__binary_reversed = copy.copy(self.__binary_straight)
        if not binary_conversion[0]:
            self.__binary_add = self.__binary_straight
        else:
            operating = copy.copy(binary_conversion[2])
            operating: list
            self.__binary_add = binary_addition(operating, [1])
        self.__sign = binary_conversion[0]

    def get_straight_form(self)->list:
        return self.__binary_straight

    def get_sign(self)->bool:
        return self.__sign

    def __add__(self, other):
        self: BinaryInteger
        other: BinaryInteger
        result = []
        if self.get_sign() and other.get_sign():
            result = ClassMethods.integer_summ_negative_and_negative(self, other)
        elif self.get_sign() and not other.get_sign():
            result = ClassMethods.integer_summ_negative_and_positive(self, other)
        elif not self.get_sign() and other.get_sign():
            result = ClassMethods.integer_summ_positive_and_negative(self, other)
        elif not self.get_sign() and not other.get_sign():
            result = ClassMethods.integer_summ_positive_and_positive(self, other)
        return result

    def __sub__(self, other):
        self: BinaryInteger
        other: BinaryInteger
        result = []
        if self.get_sign() and other.get_sign():
            result = ClassMethods.integer_sub_negative_and_negative(self, other)
        elif not self.get_sign() and other.get_sign():
            result = ClassMethods.integer_sub_positive_and_negative(self, other)
        elif self.get_sign() and not other.get_sign():
            result = ClassMethods.integer_sub_negative_and_positive(self, other)
        elif not self.get_sign() and not other.get_sign():
            result = ClassMethods.integer_sub_positive_and_positive(self, other)
        return result

    def __mul__(self, other):
        self: BinaryInteger
        other: BinaryInteger
        if self.get_sign() == other.get_sign():
            result = [0]
        else:
            result = [1]
        raw_result = binary_multiplication(self.get_straight_form(), other.get_straight_form())
        for number in raw_result:
            result.append(number)
        return result

    def __truediv__(self, other):
        self: BinaryInteger
        other: BinaryInteger
        if self.get_sign() == other.get_sign():
            result = [0]
        else:
            result = [1]
        raw_result = binary_division(self.get_straight_form(), other.get_straight_form())
        for number in raw_result:
            result.append(number)
        return result


class FloatingPoint:
    def __init__(self, number: float):
        if number >= 0:
            self.__sign = 0
        else:
            self.__sign = 1
        less_than_one = number - int(number)
        exponent = 0
        true_binary = (int_to_bin(int(number))[1], floating_to_bin(less_than_one))
        normalised_true_binary= normalise_true_binary(true_binary, exponent)
        biased_exponent = int_to_bin(normalised_true_binary[2]+100)[1]
        self.__mantissa = normalised_true_binary[1]
        self.__exponent = biased_exponent

    def get_mantissa(self):
        return self.__mantissa

    def get_exponent(self):
        return self.__exponent

    def get_sign(self):
        return self.__sign

    def __add__(self, other):
        other: FloatingPoint
        first_mantissa = copy.copy(self.__mantissa)
        first_mantissa: list
        first_exponent = copy.copy(self.__exponent)
        second_exponent = copy.copy(other.get_exponent())
        second_mantissa = copy.copy(other.get_mantissa())
        second_mantissa: list
        first_mantissa.insert(0, 1)
        second_mantissa.insert(0, 1)
        first_mantissa.insert(1, ",")
        second_mantissa.insert(1, ",")
        while True:
            if binary_compare_equal(first_exponent, second_exponent):
                if binary_compare_more(first_mantissa, second_mantissa) or binary_compare_equal(first_mantissa,
                                                                                                second_mantissa):
                    result = ClassMethods.float_summ_first_bigger_than_second_logic(self, other, first_mantissa,
                                                                                    second_mantissa, first_exponent)
                else:
                    result = ClassMethods.float_summ_second_bigger_than_first_logic(self, other, first_mantissa,
                                                                                    second_mantissa, first_exponent)
                return result
            elif binary_compare_more(first_exponent, second_exponent):
                first_mantissa, first_exponent = ClassMethods.first_mantissa_expansion(first_mantissa, second_exponent,
                                                                                       first_exponent)
            else:
                second_mantissa, second_exponent = ClassMethods.second_mantissa_expansion(second_mantissa,
                                                                                          second_exponent,
                                                                                          first_exponent)
