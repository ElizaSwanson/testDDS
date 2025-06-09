from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MoneyFlowView,
    FlowTypeViewSet, CategoryView, CategoryCreateAPIView, CategoryDestroyAPIView, CategoryDetailView,
    SubCategoryViewSet, MoneyFlowDetailView, MoneyFlowCreateAPIView, MoneyFlowDestroyAPIView, StatusView,
    StatusDetailView, StatusDestroyAPIView, StatusCreateAPIView,
)

app_name = "dds"

router = DefaultRouter()
router.register(r'flowtypes', FlowTypeViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #ддс
    path('moneyflows/', MoneyFlowView.as_view(), name='moneyflow'),
    path('moneyflows/<int:pk>/', MoneyFlowDetailView.as_view(), name='moneyflow-detail'),
    path('moneyflows/create/', MoneyFlowCreateAPIView.as_view(), name='moneyflow-create'),
    path('moneyflows/<int:pk>/delete/', MoneyFlowDestroyAPIView.as_view(), name='moneyflow-delete'),
    #статусы
    path('status/', StatusView.as_view(), name='status'),
    path('status/<int:pk>/', StatusDetailView.as_view(), name="status-detail"),
    path('status/<int:pk>/delete/', StatusDestroyAPIView.as_view(), name='status-delete'),
    path('status/create/', StatusCreateAPIView.as_view(), name='status-create'),
    #категории
    path('category/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name="category-detail"),
    path('category/<int:pk>/delete/',CategoryDestroyAPIView.as_view(), name='category-delete'),
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
]