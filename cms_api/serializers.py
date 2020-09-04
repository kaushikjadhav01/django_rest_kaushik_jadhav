from rest_framework import serializers
from .models import UserModel, ContentModel

# Serializer for User model objects
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id','email','name','password','phone','pincode','address','state','city','country']
        extra_kwargs = {'password': {'write_only': True}}

    # Create and return a new user
    def create(self, validated_data):
        user = UserModel(
            email=validated_data['email'],
            name=validated_data['name'],
            phone=validated_data['phone'],
            pincode=validated_data['pincode'],
            address=validated_data['address'],
            state=validated_data['state'],
            city=validated_data['city'],
            country=validated_data['country']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ContentSerializer(serializers.ModelSerializer):

    # We need to serialize categories as MultipleChoiceField since it is a Multi Select Dropdown
    choices = (('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Education', 'Education'),('Arts', 'Arts'))
    categories = serializers.MultipleChoiceField(choices, allow_blank=True)

    class Meta:
        model = ContentModel
        fields = ('id', 'author', 'title', 'body','summary','pdf','categories')
        extra_kwargs = {'author': {'read_only': True}}