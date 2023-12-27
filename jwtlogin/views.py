from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenVerifyView, TokenViewBase
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode, InvalidTokenError
import config.settings

class CustomUserCreate(APIView):
    permission_classes = [ AllowAny ]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data) # 시리얼라이저의 create가 실행이됨.
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # class CustomTokenViewBase(TokenViewBase):
# #     def post(self, request: Request, *args, **kwargs) -> Response:
# #         print("call")
# #         print(request.data)
# #         serializer = self.get_serializer(data=request.data)
        
# #         try:
# #             serializer.is_valid(raise_exception=True)
# #         except TokenError as e:
# #             raise InvalidToken(e.args[0])
        
# #         print(serializer)
# #         print("val : ", serializer.validated_data)

# #         if serializer.validated_data:
# #             return Response(serializer.validated_data, status=status.HTTP_200_OK)
# #         else:
# #             try:
# #                 # 토큰 디코드
# #                 print(request.get('token', None))
# #                 decoded_token = decode(request.get('token', None), config.settings.SECRET_KEY, algorithms=['HS256'])

# #                 # 클레임에 접근
# #                 student_id = decoded_token.get('student_id')

# #                 print(f"Decoded Token: {decoded_token}")
# #                 print(f"Student ID: {student_id}")

# #                 return Response({"student_id" : student_id}, status=status.HTTP_200_OK)
# #             except InvalidTokenError as e:
# #                 print(f"Invalid Token: {e}")
# #                 return Response(status=status.HTTP_401_UNAUTHORIZED)
            
# # class TokenVerifyView(CustomTokenViewBase):
# #     pass

    
# class CustomTokenVerifyView(TokenVerifyView):
# #     authentication_classes = [JWTAuthentication]
# #     permission_classes = [IsAuthenticated]

# #     # def post(self, request, *args, **kwargs):
# #     #     # 기본 TokenVerifyView의 post 메서드를 호출하여 유효성을 검증
# #     #     response = super().post(request, *args, **kwargs)

# #     #     # 유효한 경우, 추가적인 정보를 payload에 추가
# #     #     if response.status_code == 200:
# #     #         print("call")
# #     #         validated_token = response.data
# #     #         user = self.request.user  # 현재 로그인한 사용자
# #     #         # 사용자의 student_id를 payload에 추가
# #     #         print(validated_token, user)
# #     #         validated_token['student_id'] = user.student_id

# #     #     return Response(validated_token)
#     pass