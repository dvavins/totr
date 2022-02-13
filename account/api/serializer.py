from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email')



class AccountViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


# class AccountUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = ('username', 'email', 'first_name', 'last_name', 'password', 'date_joined')
#         read_only_fields = ('username',)


class CreateAccountSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        } 

    
    def save(self):
        account = Account(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
        )
        password = self.validated_data['password1']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'Password must match'})
        account.set_password(password)
        account.is_active=True
        account.save()
        return account






