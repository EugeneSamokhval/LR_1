import Class


def integer_summ_negative_and_negative(first_binary, second_binary):
    result = [1]
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result_raw = Class.binary_addition(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    else:
        result_raw = Class.binary_addition(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    return result


def integer_summ_negative_and_positive(first_binary, second_binary):
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result = [1]
        raw_result = Class.binary_difference(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    else:
        result = [0]
        raw_result = Class.binary_difference(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    return result


def integer_summ_positive_and_negative(first_binary, second_binary):
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result = [0]
        raw_result = Class.binary_difference(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    else:
        result = [1]
        raw_result = Class.binary_difference(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    return result


def integer_summ_positive_and_positive(first_binary, second_binary):
    result = [0]
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result_raw = Class.binary_addition(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    else:
        result_raw = Class.binary_addition(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    return result


def integer_sub_negative_and_negative(first_binary, second_binary):
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result = [1]
        raw_result = Class.binary_difference(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    else:
        result = [0]
        raw_result = Class.binary_difference(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    return result


def integer_sub_positive_and_negative(first_binary, second_binary):
    result = [0]
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result_raw = Class.binary_addition(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    else:
        result_raw = Class.binary_addition(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    return result


def integer_sub_negative_and_positive(first_binary, second_binary):
    result = [1]
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result_raw = Class.binary_addition(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    else:
        result_raw = Class.binary_addition(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in result_raw:
            result.append(number)
    return result


def integer_sub_positive_and_positive(first_binary, second_binary):
    if Class.binary_compare_more(first_binary.get_straight_form(), second_binary.get_straight_form()):
        result = [0]
        raw_result = Class.binary_difference(first_binary.get_straight_form(), second_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    else:
        result = [1]
        raw_result = Class.binary_difference(second_binary.get_straight_form(), first_binary.get_straight_form())
        for number in raw_result:
            result.append(number)
    return result


def float_summ_first_bigger_than_second_logic(first_binary, second_binary,
                                              first_mantissa, second_mantissa, first_exponent):
    if first_binary.get_sign() == 1 and second_binary.get_sign() == 1:
        result = [first_binary.get_sign(), Class.binary_fixed_sum(first_mantissa, second_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    elif first_binary.get_sign() == 0 and second_binary.get_sign() == 1:
        result = [first_binary.get_sign(), Class.binary_fixed_sub(first_mantissa, second_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    elif first_binary.get_sign() == 1 and second_binary.get_sign() == 0:
        result = [first_binary.get_sign(), Class.binary_fixed_sub(first_mantissa, second_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    else:
        result = [first_binary.get_sign(), Class.binary_fixed_sum(first_mantissa, second_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    return result


def float_summ_second_bigger_than_first_logic(first_binary, second_binary,
                                              first_mantissa, second_mantissa, first_exponent):
    if first_binary.get_sign() == 1 and second_binary.get_sign() == 1:
        result = [second_binary.get_sign(), Class.binary_fixed_sum(second_mantissa, first_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    elif first_binary.get_sign() == 0 and second_binary.get_sign() == 1:
        result = [second_binary.get_sign(), Class.binary_fixed_sub(second_mantissa, first_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    elif first_binary.get_sign() == 1 and second_binary.get_sign() == 0:
        result = [second_binary.get_sign(), Class.binary_fixed_sub(second_mantissa, first_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    else:
        result = [second_binary.get_sign(), Class.binary_fixed_sum(second_mantissa, first_mantissa),
                  Class.binary_addition(first_exponent, [1])]
    return result


def first_mantissa_expansion(first_mantissa, second_exponent, first_exponent):
    comma_index = 1
    while not Class.binary_compare_equal(first_exponent, second_exponent):
        if len(first_mantissa) - 1 > comma_index:
            first_exponent = Class.binary_difference(first_exponent, [1])
            first_mantissa[comma_index] = first_mantissa[comma_index + 1]
            first_mantissa[comma_index + 1] = ","
            comma_index += 1
        else:
            first_mantissa.append(0)
    return first_mantissa, first_exponent


def second_mantissa_expansion(second_mantissa, second_exponent, first_exponent):
    comma_index = 1
    while not Class.binary_compare_equal(first_exponent, second_exponent):
        if len(second_mantissa) - 1 > comma_index:
            second_exponent = Class.binary_difference(second_exponent, [1])
            second_mantissa[comma_index] = second_mantissa[comma_index + 1]
            second_mantissa[comma_index + 1] = ","
            comma_index += 1
        else:
            second_mantissa.append(0)
    return second_mantissa, second_exponent
