from rest_framework import viewsets, filters
from .models import MoneyFlow, Status, FlowType, Category, SubCategory
from .serializers import (
    MoneyFlowSerializer,
    StatusSerializer,
    FlowTypeSerializer,
    CategorySerializer,
    SubCategorySerializer,
)
from django_filters.rest_framework import DjangoFilterBackend

class MoneyFlowViewSet(viewsets.ModelViewSet):
    queryset = MoneyFlow.objects.all().order_by('-date')
    serializer_class = MoneyFlowSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date', 'status', 'flow_type', 'category', 'subcategory']

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class FlowTypeViewSet(viewsets.ModelViewSet):
    queryset = FlowType.objects.all()
    serializer_class = FlowTypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer