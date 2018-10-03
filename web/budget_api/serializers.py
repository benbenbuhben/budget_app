from django.contrib.auth.models import User
from rest_framework import serializers


# NOTE: Tutorial user HyperlinkedModelSerializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user


# class BudgetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='user.username')
#     user = serializers.HyperLinkedRelaredField(view_name='user_detail', read_only=True)

#     class Meta:
#         model = Budget
#         fields = ('name', 'total_budget')


# class TransactionSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='user.username')
#     user = serializers.HyperLinkedRelaredField(view_name='user_detail', read_only=True)

#     class Meta:
#         model = Transaction
#         fields = ('budget', 'description', 'amount')
