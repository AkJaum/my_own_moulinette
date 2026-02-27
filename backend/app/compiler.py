import subprocess

def compile_c(file_path):
    subprocess.run(
        ["gcc", "-Wall", "-Wextra", "-Werror", file_path],
        check=True
    )

def run_program(args=None):
    if args:
        result = subprocess.run(
            ["./a.out"] + args,
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(
            ["./a.out"],
            capture_output=True,
            text=True
        )

    return result.stdout
