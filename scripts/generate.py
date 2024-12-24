import os
import subprocess

def main():
    # Ensure generated directory exists
    os.makedirs("generated", exist_ok=True)
    
    # Run protoc compiler
    subprocess.run([
        "python", "-m", "grpc_tools.protoc",
        "-I./protos",
        "--python_out=./generated",
        "--grpc_python_out=./generated",
        "./protos/polynomial.proto"
    ])

if __name__ == "__main__":
    main() 