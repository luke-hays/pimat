# Create new virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate

# Install package in editable mode
pip install -e .

# Generate gRPC files
python -m scripts.generate

# Run server
python -m server.server

# Run client
python -m server.client
