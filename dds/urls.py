from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MoneyFlowViewSet,
    StatusViewSet,
    FlowTypeViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
)

app_name = "dds"

router = DefaultRouter()
router.register(r'moneyflows', MoneyFlowViewSet, 'moneyflow')
router.register(r'statuses', StatusViewSet)
router.register(r'flowtypes', FlowTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]