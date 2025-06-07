from django.core.exceptions import ValidationError
from django.db import models


class Status(models.Model):
    """Модель для хранения статусов (Бизнес, Личное, Налог) с возможностью расширения"""

    name = models.CharField(max_length=100, unique=True, verbose_name="Название статуса")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class FlowType(models.Model):
    """Модель для хранения типов операций (Пополнение, Списание) с возможностью расширения"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Тип операции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"


class Category(models.Model):
    """Модель категорий с привязкой к типу операции"""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    flow_type = models.ForeignKey(FlowType, on_delete=models.CASCADE, verbose_name="Тип операции")

    def __str__(self):
        return f"{self.name} ({self.flow_type})"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ('name', 'flow_type')  # Чтобы названия не повторялись для одного типа


class SubCategory(models.Model):
    """Модель подкатегорий с привязкой к категории"""
    name = models.CharField(max_length=100, verbose_name="Название подкатегории")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ('name', 'category')


class MoneyFlow(models.Model):
    """Модель для хранения записей о движении денежных средств"""
    date = models.DateField(auto_now_add=True, verbose_name="Дата операции")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")
    flow_type = models.ForeignKey(FlowType, on_delete=models.PROTECT, verbose_name="Тип операции", null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория", null=False, blank=False)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name="Подкатегория", null=False, blank=False)
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма (руб)",
        null=False, blank=False
    )
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.date} | {self.amount} руб. | {self.status}"

    def clean(self):
        super().clean()

        # Проверка, что подкатегория связана с выбранной категорией
        if self.subcategory.category != self.category:
            raise ValidationError({
                'subcategory': 'Подкатегория не связана с выбранной категорией.'
            })

        # Проверка, что категория соответствует типу операции
        if self.category.flow_type != self.flow_type:
            raise ValidationError({
                'category': 'Категория не соответствует выбранному типу операции.'
            })

    class Meta:
        verbose_name = "Движение денежных средств"
        verbose_name_plural = "Движения денежных средств"
        ordering = ['-date']