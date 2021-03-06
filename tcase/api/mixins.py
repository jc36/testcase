# from rest_framework.decorators import detail_route
# from rest_framework.response import Response
#
# from .. import services
# from .serializers import LikeSerializer
#
#
# class LikedMixin:
#
#     @detail_route(methods=['POST'])
#     def like(self, request, pk=None):
#         """like post"""
#         obj = self.get_object()
#         services.add_like(obj, request.user)
#         return Response()
#
#     @detail_route(methods=['POST'])
#     def unlike(self, request, pk=None):
#         """dislike"""
#         obj = self.get_object()
#         services.remove_like(obj, request.user)
#         return Response()
#
#     @detail_route(methods=['GET'])
#     def fans(self, request, pk=None):
#         """get likers"""
#         obj = self.get_object()
#         fans = services.get_fans(obj)
#         serializer = LikeSerializer(fans, many=True)
#         return Response(serializer.data)
