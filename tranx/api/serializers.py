from rest_framework import serializers

from tranx.models import Transactions


class TranxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ('id', 'user', 'title')



class TranxViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transactions
        fields = '__all__'


class TranxCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = '__all__'

    def save(self):
        tranx = Transactions(
            user = self.validated_data['user'],
            title = self.validated_data['title'],
            desc = self.validated_data['desc'],
            amount = self.validated_data['amount'],
            paid_on = self.validated_data['paid_on']
        )
        tranx.save()
        return tranx


        