# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class HelloWorldStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.requestGreeting = channel.unary_unary(
                '/helloworld.HelloWorld/requestGreeting',
                request_serializer=helloworld__pb2.HelloWorldRequest.SerializeToString,
                response_deserializer=helloworld__pb2.HelloWorldResponse.FromString,
                )


class HelloWorldServicer(object):
    """Missing associated documentation comment in .proto file."""

    def requestGreeting(self, request, context):
        """hello world example, super simple
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloWorldServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'requestGreeting': grpc.unary_unary_rpc_method_handler(
                    servicer.requestGreeting,
                    request_deserializer=helloworld__pb2.HelloWorldRequest.FromString,
                    response_serializer=helloworld__pb2.HelloWorldResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.HelloWorld', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloWorld(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def requestGreeting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.HelloWorld/requestGreeting',
            helloworld__pb2.HelloWorldRequest.SerializeToString,
            helloworld__pb2.HelloWorldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
