from rest_framework import serializers


class MinLengthValidator:

    def __init__(self, minimum):
        self.minimum = minimum

    def __call__(self, value):
        if len(value) < self.minimum:
            raise serializers.ValidationError(
                f'Value should be greater or equal to {self.minimum}'
            )
