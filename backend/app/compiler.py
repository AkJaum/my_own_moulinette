import subprocess
import os
import tempfile

# Store the directory where the program was compiled
_compiled_dir = None

def compile_c(file_path, main_code=None):
    """
    Compile a C file, optionally with a generated main function.
    
    Args:
        file_path: Path to the C file to compile
        main_code: Optional C code to append (usually a main function)
    """
    global _compiled_dir
    file_dir = os.path.dirname(file_path) or "."
    # Use absolute path for output
    output_path = os.path.join(os.path.abspath(file_dir), "a.out")
    _compiled_dir = os.path.abspath(file_dir)
    
    # If main_code is provided, create a temporary main file
    if main_code:
        # Create main file in a temp directory with write permissions
        main_file = os.path.join(tempfile.gettempdir(), "main_generated.c")
        with open(main_file, "w") as f:
            f.write(main_code)
        # Compile from file_dir so #include "ft_putchar.c" works
        compile_files = [main_file]
    else:
        compile_files = [file_path]
    
    subprocess.run(
        ["gcc", "-Wall", "-Wextra", "-Werror"] + compile_files + ["-o", output_path],
        check=True,
        cwd=_compiled_dir
    )

def run_program(args=None):
    """Run the compiled program from the directory where it was compiled."""
    global _compiled_dir
    
    if args:
        result = subprocess.run(
            ["./a.out"] + args,
            capture_output=True,
            text=True,
            cwd=_compiled_dir
        )
    else:
        result = subprocess.run(
            ["./a.out"],
            capture_output=True,
            text=True,
            cwd=_compiled_dir
        )

    return result.stdout
