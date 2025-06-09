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

#вью для движения денежных средств

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


#вью для статусов
class StatusView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'status_list.html'

    def get(self, request):
        queryset = Status.objects.all()
        return Response({'statuses': queryset})

class StatusDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'status_detail.html'


    def get(self, request, pk):
        queryset = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(queryset)
        return Response({'serializer': serializer, 'obj': queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(Status, pk=pk)
        serializer = StatusSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'obj': queryset})
        serializer.save()
        return redirect('/status/')

class StatusDestroyAPIView(generics.DestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'status_delete.html'


    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({'obj': obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect('/status/')


class StatusCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'status_create.html'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/status/')
        else:
            return Response({'serializer': serializer})


#вью для категорий

class CategoryView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category_list.html'

    def get(self, request):
        queryset = Category.objects.all()
        return Response({'categories': queryset})

class CategoryDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category_detail.html'


    def get(self, request, pk):
        queryset = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(queryset)
        return Response({'serializer': serializer, 'obj': queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'obj': queryset})
        serializer.save()
        return redirect('/category/')

class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category_delete.html'


    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({'obj': obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect('/category/')


class CategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category_create.html'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/category/')
        else:
            return Response({'serializer': serializer})

#тип операций (flowtype)

class FlowtypeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'flowtype_list.html'

    def get(self, request):
        queryset = FlowType.objects.all()
        return Response({'flowtypes': queryset})

class FlowtypeDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'flowtype_detail.html'


    def get(self, request, pk):
        queryset = get_object_or_404(FlowType, pk=pk)
        serializer = FlowTypeSerializer(queryset)
        return Response({'serializer': serializer, 'obj': queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(FlowType, pk=pk)
        serializer = FlowTypeSerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'obj': queryset})
        serializer.save()
        return redirect('/flowtype/')

class FlowtypeDestroyAPIView(generics.DestroyAPIView):
    queryset = FlowType.objects.all()
    serializer_class = FlowTypeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'flowtype_delete.html'


    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({'obj': obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect('/flowtype/')


class FlowtypeCreateAPIView(generics.ListCreateAPIView):
    queryset = FlowType.objects.all()
    serializer_class = FlowTypeSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'flowtype_create.html'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/flowtype/')
        else:
            return Response({'serializer': serializer})


#подкатегории
class SubcategoryView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subcategory_list.html'

    def get(self, request):
        queryset = SubCategory.objects.all()
        return Response({'subcategories': queryset})

class SubcategoryDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subcategory_detail.html'


    def get(self, request, pk):
        queryset = get_object_or_404(SubCategory, pk=pk)
        serializer = SubCategorySerializer(queryset)
        return Response({'serializer': serializer, 'obj': queryset})

    def post(self, request, pk):
        queryset = get_object_or_404(SubCategory, pk=pk)
        serializer = SubCategorySerializer(queryset, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'obj': queryset})
        serializer.save()
        return redirect('/subcategory/')

class SubcategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subcategory_delete.html'


    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return Response({'obj': obj})

    def post(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return redirect('/subcategory/')


class SubcategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'subcategory_create.html'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response({'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/subcategory/')
        else:
            return Response({'serializer': serializer})