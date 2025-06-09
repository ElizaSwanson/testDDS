from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, filters, status, generics
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response

from .filters import MoneyFlowFilter
from .models import MoneyFlow, Status, FlowType, Category, SubCategory
from .serializers import (
    MoneyFlowSerializer,
    StatusSerializer,
    FlowTypeSerializer,
    CategorySerializer,
    SubCategorySerializer,
)
from django_filters.rest_framework import DjangoFilterBackend


class MoneyFlowView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moneyflow_list.html'
    filter_backends = [DjangoFilterBackend]
    filterset_class = MoneyFlowFilter

    def get(self, request):
        queryset = MoneyFlow.objects.all()
        filterset = MoneyFlowFilter(request.GET, queryset=queryset)
        return Response({'moneyflows': filterset.qs})


class MoneyFlowDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moneyflow_form.html'


    def get(self, request, pk):
        queryset = get_object_or_404(MoneyFlow, pk=pk)
        serializer = MoneyFlowSerializer(queryset)
        return Response({'serializer': serializer, 'obj': queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(MoneyFlow, pk=pk)
        serializer = MoneyFlowSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'obj': queryset})
        serializer.save()
        return redirect('moneyflow')

class MoneyFlowCreateAPIView(generics.ListCreateAPIView):
    queryset = MoneyFlow.objects.all()
    serializer_class = MoneyFlowSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moneyflow_create.html'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/moneyflows/')
        else:
            return Response({'serializer': serializer})

class MoneyFlowDestroyAPIView(generics.DestroyAPIView):
    queryset = MoneyFlow.objects.all()
    serializer_class = MoneyFlowSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moneyflow_delete.html'


    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({'obj': obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect('/moneyflows/')

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