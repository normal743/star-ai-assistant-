import sys
import io
import traceback
from contextlib import redirect_stdout, redirect_stderr

class PythonExecutor:
    def __init__(self, timeout=30):
        self.timeout = timeout

    def execute_code(self, code):
        # Capture stdout and stderr
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        # Prepare the result dictionary
        result = {
            "output": "",
            "error": None,
            "returned_value": None
        }

        try:
            # Redirect stdout and stderr
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # Execute the code
                exec_globals = {}
                exec(code, exec_globals)
                
                # Check if there's a returned value (last expression)
                if 'last_expression' in exec_globals:
                    result["returned_value"] = str(exec_globals['last_expression'])

        except Exception as e:
            result["error"] = {
                "type": type(e).__name__,
                "message": str(e),
                "traceback": traceback.format_exc()
            }

        # Get captured stdout and stderr
        result["output"] = stdout_capture.getvalue()
        if stderr_capture.getvalue():
            result["error"] = result["error"] or {}
            result["error"]["stderr"] = stderr_capture.getvalue()

        return result

# Usage example:
# executor = PythonExecutor()
# code = """
# def greet(name):
#     return f"Hello, {name}!"
# 
# result = greet("World")
# print(result)
# last_expression = result
# """
# result = executor.execute_code(code)
# print(result)
