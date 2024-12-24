import grpc
import logging
from protos.polynomial_pb2 import Point, InterpolateRequest
from protos.polynomial_pb2_grpc import PolynomialServiceStub

def run():
    logging.info("Starting client...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = PolynomialServiceStub(channel)
        
        # Create test points
        points = [
            Point(x=1.0, y=1.0),
            Point(x=2.0, y=4.0),
            Point(x=3.0, y=9.0),
        ]
        
        logging.info(f"Sending points: {points}")
        # Make request
        request = InterpolateRequest(points=points)
        try:
            response = stub.Interpolate(request)
            logging.info(f"Received coefficients: {response.coefficients}")
        except grpc.RpcError as e:
            logging.error(f"RPC failed: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    run() 