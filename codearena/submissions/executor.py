import subprocess
import tempfile
import os

def execute_code(language, code, input_data=""):
    """
    Executes user code inside Docker container based on language.
    Returns output and success status.
    """

    with tempfile.TemporaryDirectory() as temp_dir:
        # Decide file name and image based on language
        if language == "python":
            filename = "code.py"
            image = "python-runner"

        elif language == "cpp":
            filename = "code.cpp"
            image = "cpp-runner"

        elif language == "java":
            filename = "Main.java"
            image = "java-runner"

        else:
            return "Unsupported language", False

        file_path = os.path.join(temp_dir, filename)

        # Write user code to file
        with open(file_path, "w") as f:
            f.write(code)

        # Build docker command
        command = [
            "docker", "run", "--rm",
            "-v", f"{temp_dir}:/app",
            image
        ]

        try:
            result = subprocess.run(
                command,
                input=input_data,
                capture_output=True,
                text=True,
                timeout=5
            )

            output = result.stdout if result.stdout else result.stderr

            return output, True

        except subprocess.TimeoutExpired:
            return "Time Limit Exceeded", False
