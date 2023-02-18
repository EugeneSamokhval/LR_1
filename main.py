import math
import copy


def binary_addition(first_binary: list, second_binary: list)->list:
    result = []
    first_binary.insert(0, 0)
    in_mind = 0
    while len(second_binary) != len(second_binary):
        second_binary.insert(0, 0)
    for iterator in range(len(first_binary) - 1, 0):
        if in_mind == 0:
            if first_binary[iterator] == 1 and second_binary[iterator] ==0:
                result.insert(0, 1)
            elif first_binary[iterator] == 0 and second_binary[iterator] ==1:
                result.insert(0, 1)
            elif first_binary[iterator] == 1 and second_binary[iterator] ==1:
                result.insert(0, 0)
                in_mind += 1
            elif first_binary[iterator] == 0 and second_binary[iterator] ==0:
                result.insert(0, 0)
        else:
            if first_binary[iterator] == 1 and second_binary[iterator] == 0:
                result.insert(0, 0)
            elif first_binary[iterator] == 0 and second_binary[iterator] == 1:
                result.insert(0, 0)
            elif first_binary[iterator] == 1 and second_binary[iterator] == 1:
                result.insert(0, 1)
            elif first_binary[iterator] == 0 and second_binary[iterator] == 0:
                result.insert(0, 1)
                in_mind -=1
    return result


def binary_difference(first_binary: list, second_binary: list):
    result = []
    in_mind =0
    while len(second_binary) != len(first_binary):
        second_binary.insert(0, 0)
    for iterator in range(len(first_binary)-1, 0):
        if iterator != 0:
            if in_mind != 0:
                if first_binary[iterator] == 1 and second_binary[iterator] == 1:
                    result.insert(0, 0)
                elif first_binary[iterator] == 0 and second_binary[iterator] == 0:
                    result.insert(0, 0)
                elif first_binary[iterator] == 0 and second_binary[iterator] == 1:
                    result.insert(0, 0)
                    in_mind += 1
                elif first_binary[iterator] == 1 and second_binary[iterator] == 0:
                    result.insert(0, 0)
                    in_mind -= 1
            else:
                if first_binary[iterator] == 1 and second_binary[iterator] == 1:
                    result.insert(0, 0)
                elif first_binary[iterator] == 1 and second_binary[iterator] == 0:
                    result.insert(0, 1)
                elif first_binary[iterator] == 0 and second_binary[iterator] == 1:
                    result.insert(0, 1)
                    in_mind +=1
                elif first_binary[iterator] == 0 and second_binary[iterator] == 0:
                    result.insert(0, 0)
        else:
            if in_mind == 0:
                break
            else:
                for dec in range(0, in_mind):
                    result.pop(dec)
        return result


def binary_multiplication(first_binary, second_binary):
    list_for_summ = []
    for rev_iterator in range(len(second_binary)-1, 0):
        if second_binary[rev_iterator] == 1:
            temp_binary = copy.copy(first_binary)
            for shift in range(0, len(second_binary)-1-rev_iterator):
                temp_binary.append(0)
            list_for_summ.append(temp_binary)
    result = copy.copy(list_for_summ[len(list_for_summ)-1])
    for iterator in range(len(list_for_summ)-2, 0):
        result=binary_addition(result, list_for_summ[iterator])
    return result


def binary_compare_more(first_binary, second_binary)->bool:
    if len(first_binary) > len(second_binary):
        return True
    elif len(first_binary) < len(second_binary):
        return False
    else:
        for iteration in range(0, len(first_binary)-1):
            if first_binary[iteration] == 1 and second_binary[iteration] == 0:
                return True
            elif first_binary[iteration] == 0 and second_binary[iteration] == 1:
                return False


def binary_division(first_binary, second_binary):
    result = []
    first_binary: list
    temp_subst = []
    signs_after_dot = 0
    while signs_after_dot < 5:
        if binary_compare_more(temp_subst, second_binary):
            first_binary.remove(temp_subst)
            temp_subst = binary_difference(temp_subst, second_binary)
            result.append(1)
        elif len(second_binary) >= len(first_binary):
            while len(second_binary) >= len(first_binary):
                first_binary.append(0)
                if result.count(",") == 0:
                    result.append(",")
                signs_after_dot += 1
        else:
            count = 0
            while not binary_compare_more(temp_subst, second_binary):
                temp_subst.append(first_binary[count])
                count+=1
    return result


def int_to_bin(number: int):
    matrix = []
    minus_sign = True
    if number > 0:
        minus_sign = False
    else:
        number+=-1
    while number > 0:
        matrix.append(number % 2)
        number = number/2
    rev_ver = copy.copy(matrix)
    if minus_sign:
        for sign in rev_ver:
            if sign == 0:
                sign = 1
            else:
                sign = 0
    output = (minus_sign, matrix, rev_ver)
    return output


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
        if self.get_sign() and other.get_sign:
            result = [1]
            if binary_compare_more(self.get_straight_form(), other.get_straight_form()):
                result_raw = binary_addition(self.get_straight_form(), other.get_straight_form())
                for number in result_raw:
                    result.append(number)
            else:
                result_raw = binary_addition(other.get_straight_form(), self.get_straight_form())
                for number in result_raw:
                    result.append(number)
        elif self.get_sign() and not other.get_sign:
            if binary_compare_more(self.get_straight_form(), other.get_straight_form()):
                result = [1]
                raw_result = binary_difference(self.get_straight_form(), other.get_straight_form())
                for number in raw_result:
                    result.append(number)





