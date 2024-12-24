import subprocess
import sys

def main():
    # Run protoc compiler using current Python interpreter
    subprocess.run([
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        "-I./server/protos",
        "--python_out=./server/protos",
        "--grpc_python_out=./server/protos",
        "./server/protos/polynomial.proto"
    ])

if __name__ == "__main__":
    main() 