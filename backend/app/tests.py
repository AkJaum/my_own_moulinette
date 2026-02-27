from app.compiler import compile_c, run_program
import os

def test_ex00(base):
    try:
        file_path = os.path.join(base, "ex00/ft_putchar.c")
        compile_c(file_path)

        tests = [
            ("A", "A"),
            ("0", "0"),
            ("#", "#"),
            ("z", "z"),
            ("!", "!")
        ]

        for inp, expected in tests:
            output = run_program([inp])
            if output != expected:
                return False

        return True
    except:
        return False


def test_ex01(base):
    try:
        file_path = os.path.join(base, "ex01/ft_print_alphabet.c")
        compile_c(file_path)

        expected = "abcdefghijklmnopqrstuvwxyz"
        output = run_program()

        if output != expected:
            return False

        return True
    except:
        return False
