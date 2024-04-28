# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from saturn_bot.protocol.v1 import saturnbot_pb2 as saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2


class PluginServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExecuteActions = channel.unary_unary(
                '/protocol.v1.PluginService/ExecuteActions',
                request_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteActionsRequest.SerializeToString,
                response_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteActionsResponse.FromString,
                )
        self.ExecuteFilters = channel.unary_unary(
                '/protocol.v1.PluginService/ExecuteFilters',
                request_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteFiltersRequest.SerializeToString,
                response_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteFiltersResponse.FromString,
                )
        self.GetPlugin = channel.unary_unary(
                '/protocol.v1.PluginService/GetPlugin',
                request_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.GetPluginRequest.SerializeToString,
                response_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.GetPluginResponse.FromString,
                )
        self.OnPrClosed = channel.unary_unary(
                '/protocol.v1.PluginService/OnPrClosed',
                request_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrClosedRequest.SerializeToString,
                response_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrClosedResponse.FromString,
                )
        self.OnPrCreated = channel.unary_unary(
                '/protocol.v1.PluginService/OnPrCreated',
                request_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrCreatedRequest.SerializeToString,
                response_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrCreatedResponse.FromString,
                )
        self.OnPrMerged = channel.unary_unary(
                '/protocol.v1.PluginService/OnPrMerged',
                request_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrMergedRequest.SerializeToString,
                response_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrMergedResponse.FromString,
                )


class PluginServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ExecuteActions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteFilters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlugin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnPrClosed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnPrCreated(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OnPrMerged(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PluginServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExecuteActions': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteActions,
                    request_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteActionsRequest.FromString,
                    response_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteActionsResponse.SerializeToString,
            ),
            'ExecuteFilters': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteFilters,
                    request_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteFiltersRequest.FromString,
                    response_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteFiltersResponse.SerializeToString,
            ),
            'GetPlugin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlugin,
                    request_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.GetPluginRequest.FromString,
                    response_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.GetPluginResponse.SerializeToString,
            ),
            'OnPrClosed': grpc.unary_unary_rpc_method_handler(
                    servicer.OnPrClosed,
                    request_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrClosedRequest.FromString,
                    response_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrClosedResponse.SerializeToString,
            ),
            'OnPrCreated': grpc.unary_unary_rpc_method_handler(
                    servicer.OnPrCreated,
                    request_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrCreatedRequest.FromString,
                    response_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrCreatedResponse.SerializeToString,
            ),
            'OnPrMerged': grpc.unary_unary_rpc_method_handler(
                    servicer.OnPrMerged,
                    request_deserializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrMergedRequest.FromString,
                    response_serializer=saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrMergedResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protocol.v1.PluginService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PluginService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ExecuteActions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.v1.PluginService/ExecuteActions',
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteActionsRequest.SerializeToString,
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteActionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteFilters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.v1.PluginService/ExecuteFilters',
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteFiltersRequest.SerializeToString,
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.ExecuteFiltersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPlugin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.v1.PluginService/GetPlugin',
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.GetPluginRequest.SerializeToString,
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.GetPluginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnPrClosed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.v1.PluginService/OnPrClosed',
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrClosedRequest.SerializeToString,
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrClosedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnPrCreated(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.v1.PluginService/OnPrCreated',
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrCreatedRequest.SerializeToString,
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrCreatedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OnPrMerged(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.v1.PluginService/OnPrMerged',
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrMergedRequest.SerializeToString,
            saturn__bot_dot_protocol_dot_v1_dot_saturnbot__pb2.OnPrMergedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)