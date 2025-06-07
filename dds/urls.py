from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MoneyFlowView,
    StatusViewSet,
    FlowTypeViewSet,
    CategoryViewSet,
    SubCategoryViewSet, MoneyFlowDetailView, MoneyFlowCreateAPIView,
)

app_name = "dds"

router = DefaultRouter()
#router.register(r'moneyflows', MoneyFlowView, 'moneyflow')
router.register(r'statuses', StatusViewSet)
router.register(r'flowtypes', FlowTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('moneyflows/', MoneyFlowView.as_view(), name='moneyflow'),
    path('moneyflows/<int:pk>/', MoneyFlowDetailView.as_view(), name='moneyflow-detail'),
    path('moneyflows/create/', MoneyFlowCreateAPIView.as_view(), name='moneyflow-create')
]