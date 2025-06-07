from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, filters, status
from rest_framework.renderers import TemplateHTMLRenderer
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

#class MoneyFlowViewSet(viewsets.ModelViewSet):
    #queryset = MoneyFlow.objects.all().order_by('-date')
    #serializer_class = MoneyFlowSerializer
    #filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    #filterset_fields = ['date', 'status', 'flow_type', 'category', 'subcategory']

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

class MoneyFlowCreateAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'moneyflow_create.html'

    def post(self, request):
        if request.method == 'POST':
            serializer = MoneyFlowSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return redirect('moneyflow_list.html')
        else:
            serializer = MoneyFlowSerializer()

        return render(request, 'moneyflow_create.html', {'serializer': serializer})

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