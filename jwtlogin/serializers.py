from rest_framework import serializers
from .models import NewUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('student_id', 'password')
        extra_kwargs = {'password': {'write_only': True}} # 클라이언트한테 요청은 받되, 응답에는 포함되지 않음.

    def create(self, validated_data):
        #validated_data = 사용자한테 받은 데이터
        password = validated_data.pop('password', None) # 패스워드를 가져옴과 동시에, 딕셔너리에서 삭제함
        instance = self.Meta.model(**validated_data) # 사용자 데이터를 이용해 모델 인스턴스 생성
        if password is not None: # 패스워드 존재시
            instance.set_password(password) # 인스턴스에 패스워드 바인딩
        instance.save() # 저장
        return instance