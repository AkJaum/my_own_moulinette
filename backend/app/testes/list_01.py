from app.compiler import compile_c, run_program
import os

PASSING_EXERCISE = "ex06"

def test_ex00(base):
    file_path = os.path.join(base, "ex00/ft_ft.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"

int main(void)
{{
    int a = 0;
    int b = 100;
    int c = -5;

    ft_ft(&a);
    ft_ft(&b);
    ft_ft(&c);

    printf("%d %d %d", a, b, c);
    return (0);
}}
"""
    compile_c(file_path, main_code)

    return run_program() == "42 42 42"


def test_ex01(base):
    file_path = os.path.join(base, "ex01/ft_ultimate_ft.c")
    abs_file_path = os.path.abspath(file_path)

    main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"

int main(void)
{{
    int x = 0;
    int *p1 = &x;
    int **p2 = &p1;
    int ***p3 = &p2;
    int ****p4 = &p3;
    int *****p5 = &p4;
    int ******p6 = &p5;
    int *******p7 = &p6;
    int ********p8 = &p7;
    int *********p9 = &p8;

    ft_ultimate_ft(p9);
    printf("%d", x);
    return (0);
}}
"""
    compile_c(file_path, main_code)

    return run_program() == "42"


def test_ex02(base):
    file_path = os.path.join(base, "ex02/ft_swap.c")
    abs_file_path = os.path.abspath(file_path)

    tests = [
        (2, 5, "5 2"),
        (-1, 10, "10 -1"),
        (0, 0, "0 0"),
        (42, -42, "-42 42"),
        (1, 2, "2 1"),
    ]

    for a, b, expected in tests:
        main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"
int main(void)
{{
    int a = {a};
    int b = {b};
    ft_swap(&a, &b);
    printf("%d %d", a, b);
    return (0);
}}
"""
        compile_c(file_path, main_code)
        if run_program() != expected:
            return False

    return True


def test_ex03(base):
    file_path = os.path.join(base, "ex03/ft_div_mod.c")
    abs_file_path = os.path.abspath(file_path)

    tests = [
        (10, 3, "3 1"),
        (9, 3, "3 0"),
        (-10, 3, "-3 -1"),
        (10, -3, "-3 1"),
        (-10, -3, "3 -1"),
    ]

    for a, b, expected in tests:
        main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"
int main(void)
{{
    int div;
    int mod;
    ft_div_mod({a}, {b}, &div, &mod);
    printf("%d %d", div, mod);
    return (0);
}}
"""
        compile_c(file_path, main_code)
        if run_program() != expected:
            return False

    return True


def test_ex04(base):
    file_path = os.path.join(base, "ex04/ft_ultimate_div_mod.c")
    abs_file_path = os.path.abspath(file_path)

    tests = [
        (10, 3, "3 1"),
        (9, 3, "3 0"),
        (100, 10, "10 0"),
        (7, 2, "3 1"),
        (1, 1, "1 0"),
    ]

    for a, b, expected in tests:
        main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"
int main(void)
{{
    int a = {a};
    int b = {b};
    ft_ultimate_div_mod(&a, &b);
    printf("%d %d", a, b);
    return (0);
}}
"""
        compile_c(file_path, main_code)
        if run_program() != expected:
            return False

    return True


def test_ex06(base):
    file_path = os.path.join(base, "ex06/ft_strlen.c")
    abs_file_path = os.path.abspath(file_path)

    tests = [
        ("", "0"),
        ("a", "1"),
        ("abc", "3"),
        ("abcdef", "6"),
        ("1234567890", "10"),
    ]

    for s, expected in tests:
        main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"
int main(void)
{{
    printf("%d", ft_strlen("{s}"));
    return (0);
}}
"""
        compile_c(file_path, main_code)
        if run_program() != expected:
            return False

    return True


def test_ex07(base):
    file_path = os.path.join(base, "ex07/ft_rev_int_tab.c")
    abs_file_path = os.path.abspath(file_path)

    tests = [
        ([1,2,3,4,5], "54321"),
        ([1,2,3,4], "4321"),
        ([1], "1"),
        ([1,2], "21"),
        ([9,8,7], "789"),
    ]

    for arr, expected in tests:
        array_values = ",".join(str(x) for x in arr)
        size = len(arr)

        main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"
int main(void)
{{
    int tab[{size}] = {{{array_values}}};
    ft_rev_int_tab(tab, {size});
    for(int i = 0; i < {size}; i++)
        printf("%d", tab[i]);
    return (0);
}}
"""
        compile_c(file_path, main_code)
        if run_program() != expected:
            return False

    return True


def test_ex08(base):
    file_path = os.path.join(base, "ex08/ft_sort_int_tab.c")
    abs_file_path = os.path.abspath(file_path)

    tests = [
        ([5,2,4,1,3], "12345"),
        ([1,2,3,4,5], "12345"),
        ([5,4,3,2,1], "12345"),
        ([-1,3,-2,5,0], "-2-1035"),
        ([1], "1"),
    ]

    for arr, expected in tests:
        array_values = ",".join(str(x) for x in arr)
        size = len(arr)

        main_code = f"""
#include <stdio.h>
#include "{abs_file_path}"
int main(void)
{{
    int tab[{size}] = {{{array_values}}};
    ft_sort_int_tab(tab, {size});
    for(int i = 0; i < {size}; i++)
        printf("%d", tab[i]);
    return (0);
}}
"""
        compile_c(file_path, main_code)
        if run_program() != expected:
            return False

    return True
