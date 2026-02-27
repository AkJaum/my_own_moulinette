from app.compiler import compile_c, run_program
import os

# Nota de corte: precisa passar até ex05 para ser aprovado
PASSING_EXERCISE = "ex04"


def test_ex00(base):
    file_path = os.path.join(base, "ex00/ft_putchar.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"

int main(int argc, char **argv)
{{
    if (argc != 2)
        return (1);
    ft_putchar(argv[1][0]);
    return (0);
}}
"""
    compile_c(file_path, main_code)

    tests = [
        ("A", "A"),
        ("z", "z"),
        ("0", "0"),
        ("#", "#"),
        ("!", "!")
    ]

    for inp, expected in tests:
        if run_program([inp]) != expected:
            return False

    return True


def test_ex01(base):
    file_path = os.path.join(base, "ex01/ft_print_alphabet.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"
int main(void)
{{
    ft_print_alphabet();
    return (0);
}}
"""
    compile_c(file_path, main_code)

    expected = "abcdefghijklmnopqrstuvwxyz"

    for _ in range(5):
        if run_program() != expected:
            return False

    return True


def test_ex02(base):
    file_path = os.path.join(base, "ex02/ft_print_reverse_alphabet.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"
int main(void)
{{
    ft_print_reverse_alphabet();
    return (0);
}}
"""
    compile_c(file_path, main_code)

    expected = "zyxwvutsrqponmlkjihgfedcba"

    for _ in range(5):
        if run_program() != expected:
            return False

    return True


def test_ex03(base):
    file_path = os.path.join(base, "ex03/ft_print_numbers.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"
int main(void)
{{
    ft_print_numbers();
    return (0);
}}
"""
    compile_c(file_path, main_code)

    expected = "0123456789"

    for _ in range(5):
        if run_program() != expected:
            return False

    return True


def test_ex04(base):
    file_path = os.path.join(base, "ex04/ft_is_negative.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include <stdlib.h>
#include "{abs_file_path}"

int main(int argc, char **argv)
{{
    if (argc != 2)
        return (1);
    ft_is_negative(atoi(argv[1]));
    return (0);
}}
"""
    compile_c(file_path, main_code)

    tests = [
        ("-1", "N"),
        ("-42", "N"),
        ("0", "P"),
        ("1", "P"),
        ("999", "P"),
    ]

    for inp, expected in tests:
        if run_program([inp]) != expected:
            return False

    return True


def test_ex05(base):
    file_path = os.path.join(base, "ex05/ft_print_comb.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"
int main(void)
{{
    ft_print_comb();
    return (0);
}}
"""
    compile_c(file_path, main_code)

    output = run_program()

    # Testes estruturais
    if not output.startswith("012"):
        return False
    if not output.endswith("789"):
        return False
    if "321" in output:
        return False
    if len(output) < 100:
        return False
    if ",," in output:
        return False

    return True


def test_ex06(base):
    file_path = os.path.join(base, "ex06/ft_print_comb2.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"
int main(void)
{{
    ft_print_comb2();
    return (0);
}}
"""
    compile_c(file_path, main_code)

    output = run_program()

    if not output.startswith("00 01"):
        return False
    if "01 00" in output:
        return False
    if not output.endswith("98 99"):
        return False
    if len(output) < 1000:
        return False
    if ",," in output:
        return False

    return True


def test_ex07(base):
    file_path = os.path.join(base, "ex07/ft_putnbr.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"

int main(int argc, char **argv)
{{
    if (argc != 2)
        return (1);
    ft_putnbr(atoi(argv[1]));
    return (0);
}}
"""
    compile_c(file_path, main_code)

    tests = [
        ("0", "0"),
        ("42", "42"),
        ("-42", "-42"),
        ("2147483647", "2147483647"),
        ("-2147483648", "-2147483648"),
    ]

    for inp, expected in tests:
        if run_program([inp]) != expected:
            return False

    return True


def test_ex08(base):
    file_path = os.path.join(base, "ex08/ft_print_combn.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include "{abs_file_path}"

int main(int argc, char **argv)
{{
    if (argc != 2)
        return (1);
    ft_print_combn(atoi(argv[1]));
    return (0);
}}
"""
    compile_c(file_path, main_code)

    tests = [
        ("1", "0"),
        ("2", "01"),
        ("3", "012"),
        ("1", "9"),
        ("2", "89"),
    ]

    for inp, expected_start in tests:
        output = run_program([inp])
        if not output.startswith(expected_start):
            return False

    return True
