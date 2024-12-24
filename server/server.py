import grpc
from concurrent import futures
import logging
from protos.polynomial_pb2 import InterpolateResponse
from protos.polynomial_pb2_grpc import PolynomialServiceServicer, add_PolynomialServiceServicer_to_server

class PolynomialService(PolynomialServiceServicer):
    def Interpolate(self, request, context):
        """Simple test implementation that returns dummy coefficients"""
        logging.info("Received interpolation request")
        return InterpolateResponse(coefficients=[1.0, 2.0, 3.0])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PolynomialServiceServicer_to_server(
        PolynomialService(), 
        server
    )
    
    port = 50051
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    
    logging.info(f"Server started on port {port}")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()