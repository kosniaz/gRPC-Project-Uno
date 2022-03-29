import grpc
import helloworld.helloworld_pb2_grpc as pb2_grpc
import helloworld.helloworld_pb2 as pb2


class HelloWorldClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.HelloWorldStub(self.channel)

    def requestGreeting(self, time_of_day):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(time_of_day=time_of_day)
        print(f'{time_of_day}')
        return self.stub.requestGreeting(message)


if __name__ == '__main__':
    client = HelloWorldClient()
    result = client.requestGreeting(time_of_day="afternoon")
    print(f'{result}')
