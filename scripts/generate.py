import os
import subprocess
import sys

def main():
    # Run protoc compiler using current Python interpreter
    subprocess.run([
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        "-I./protos",
        "--python_out=./protos",
        "--grpc_python_out=./protos",
        "./protos/polynomial.proto"
    ])

if __name__ == "__main__":
    main() 