from rest_framework import serializers

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    # создается скрытое поле и в нем прописыаается текущий юзер
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = '__all__'
