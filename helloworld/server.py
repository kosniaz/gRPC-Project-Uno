import grpc
from concurrent import futures
import time
import helloworld_pb2_grpc as pb2_grpc
import helloworld_pb2 as pb2


class HelloWorldService(pb2_grpc.HelloWorldServicer):

    def __init__(self, *args, **kwargs):
        pass

    def echoMessage(self, request, context):

        # get the string from the incoming request
        time_of_day= request.time_of_day
        result = f'Enjoy is a fine {time_of_day}!'
        result = {'greeting': result}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
