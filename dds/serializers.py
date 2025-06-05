from rest_framework import serializers
from .models import MoneyFlow, Status, FlowType, Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    """сериализатор для подкатегории"""

    class Meta:
        model = SubCategory
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    """сериализатор для категории"""

    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'flow_type', 'subcategories']


class FlowTypeSerializer(serializers.ModelSerializer):
    """сериализатор для типа операций"""

    class Meta:
        model = FlowType
        fields = ['id', 'name']


class StatusSerializer(serializers.ModelSerializer):
    """сериализатор для статуса"""

    class Meta:
        model = Status
        fields = ['id', 'name']


class MoneyFlowSerializer(serializers.ModelSerializer):
    """сериализатор для класса движения ДС"""

    date = serializers.DateField(format='%d-%m-%Y', input_formats=['%d-%m-%Y'])

    class Meta:
        model = MoneyFlow
        fields = '__all__'

    def validate(self, data):
        # Валидация связей подкатегория - категория - тип

        if data['subcategory'].category != data['category']:
            raise serializers.ValidationError("Подкатегория не принадлежит выбранной категории.")
        if data['category'].flow_type != data['flow_type']:
            raise serializers.ValidationError("Категория не принадлежит выбранному типу операции.")
        return data