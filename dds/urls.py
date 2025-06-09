from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryCreateAPIView, CategoryDestroyAPIView,
                    CategoryDetailView, CategoryView, FlowtypeCreateAPIView,
                    FlowtypeDestroyAPIView, FlowtypeDetailView, FlowtypeView,
                    MoneyFlowCreateAPIView, MoneyFlowDestroyAPIView,
                    MoneyFlowDetailView, MoneyFlowView, StatusCreateAPIView,
                    StatusDestroyAPIView, StatusDetailView, StatusView,
                    SubcategoryCreateAPIView, SubcategoryDestroyAPIView,
                    SubcategoryDetailView, SubcategoryView)

app_name = "dds"

router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    # ддс
    path("moneyflows/", MoneyFlowView.as_view(), name="moneyflow"),
    path(
        "moneyflows/<int:pk>/", MoneyFlowDetailView.as_view(), name="moneyflow-detail"
    ),
    path(
        "moneyflows/create/", MoneyFlowCreateAPIView.as_view(), name="moneyflow-create"
    ),
    path(
        "moneyflows/<int:pk>/delete/",
        MoneyFlowDestroyAPIView.as_view(),
        name="moneyflow-delete",
    ),
    # статусы
    path("status/", StatusView.as_view(), name="status"),
    path("status/<int:pk>/", StatusDetailView.as_view(), name="status-detail"),
    path(
        "status/<int:pk>/delete/", StatusDestroyAPIView.as_view(), name="status-delete"
    ),
    path("status/create/", StatusCreateAPIView.as_view(), name="status-create"),
    # категории
    path("category/", CategoryView.as_view(), name="category"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path(
        "category/<int:pk>/delete/",
        CategoryDestroyAPIView.as_view(),
        name="category-delete",
    ),
    path("category/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    # типы категорий
    path("flowtype/", FlowtypeView.as_view(), name="flowtype"),
    path("flowtype/<int:pk>/", FlowtypeDetailView.as_view(), name="flowtype-detail"),
    path(
        "flowtype/<int:pk>/delete/",
        FlowtypeDestroyAPIView.as_view(),
        name="flowtype-delete",
    ),
    path("flowtype/create/", FlowtypeCreateAPIView.as_view(), name="flowtype-create"),
    # подкатегории
    path("subcategory/", SubcategoryView.as_view(), name="subcategory"),
    path(
        "subcategory/<int:pk>/",
        SubcategoryDetailView.as_view(),
        name="subcategory-detail",
    ),
    path(
        "subcategory/<int:pk>/delete/",
        SubcategoryDestroyAPIView.as_view(),
        name="subcategory-delete",
    ),
    path(
        "subcategory/create/",
        SubcategoryCreateAPIView.as_view(),
        name="subcategory-create",
    ),
]
