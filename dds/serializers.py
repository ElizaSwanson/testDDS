from datetime import *

from django.utils import timezone
from rest_framework import serializers

from .models import Category, FlowType, MoneyFlow, Status, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    """сериализатор для подкатегории"""

    class Meta:
        model = SubCategory
        fields = ["id", "name", "category"]


class CategorySerializer(serializers.ModelSerializer):
    """сериализатор для категории"""

    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "flow_type",
        ]


class FlowTypeSerializer(serializers.ModelSerializer):
    """сериализатор для типа операций"""

    class Meta:
        model = FlowType
        fields = ["id", "name"]


class StatusSerializer(serializers.ModelSerializer):
    """сериализатор для статуса"""

    class Meta:
        model = Status
        fields = ["id", "name"]


class MoneyFlowSerializer(serializers.ModelSerializer):
    """сериализатор для класса движения ДС"""

    date = serializers.DateField(
        format="%d.%m.%Y", input_formats=["%d.%m.%Y", "%Y-%m-%d"]
    )

    class Meta:
        model = MoneyFlow
        fields = "__all__"

    def validate(self, data):
        # Валидация связей подкатегория - категория - тип

        if data["subcategory"].category != data["category"]:
            raise serializers.ValidationError(
                "Подкатегория не принадлежит выбранной категории."
            )
        if data["category"].flow_type != data["flow_type"]:
            raise serializers.ValidationError(
                "Категория не принадлежит выбранному типу операции."
            )
        if data["amount"] < 0:
            raise serializers.ValidationError("Сумма не может быть отрицательной.")
        if data["date"] > timezone.now().date():
            raise serializers.ValidationError("Дата не может быть больше текущей.")
        return data
