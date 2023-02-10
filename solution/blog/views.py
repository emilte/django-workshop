# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated

# from django.contrib.auth import login, logout
# from django.middleware.csrf import get_token
# from django.utils.decorators import method_decorator
# from django.contrib.auth.models import Group
# from django.views.decorators.csrf import csrf_protect

# from .utils import (
#     user_to_dataclass,
#     users_to_dataclass,
#     groups_to_dataclass,
# )

# from .models import (
#     User,
# )
# from .serializers import (
#     LoginSerializer,
# )

# @method_decorator(csrf_protect, 'dispatch')
# class LoginView(APIView):
#     # This view should be accessible also for unauthenticated users.
#     permission_classes = [AllowAny]

#     def post(self, request: Request) -> Response:
#         serializer = LoginSerializer(data=self.request.data, context={'request': self.request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request=request, user=user)
#         new_csrf_token = get_token(request=request)

#         return Response(
#             status=status.HTTP_202_ACCEPTED,
#             data=new_csrf_token,
#             headers={XCSRFTOKEN: new_csrf_token},
#         )

# @method_decorator(csrf_protect, 'dispatch')
# class LogoutView(APIView):
#     # This view should be accessible also for unauthenticated users.
#     permission_classes = [IsAuthenticated]

#     def post(self, request: Request) -> Response:
#         if not request.user.is_authenticated:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#         logout(request)
#         return Response(status=status.HTTP_200_OK)

# class UserView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request: Request) -> Response:
#         user = user_to_dataclass(user=request.user)
#         return Response(data=user.to_dict())  # type: ignore[attr-defined]

# class AllUsersView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request: Request) -> Response:
#         users = users_to_dataclass(users=User.objects.all())
#         users_objs = [user.to_dict() for user in users]  # type: ignore[attr-defined]
#         return Response(data=users_objs)

# class AllGroupsView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request: Request) -> Response:
#         all_groups = groups_to_dataclass(groups=Group.objects.all())
#         all_groups_objs = [group.to_dict() for group in all_groups]  # type: ignore[attr-defined]
#         return Response(data=all_groups_objs)
