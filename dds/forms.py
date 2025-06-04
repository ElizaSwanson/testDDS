from django import forms
from .models import MoneyFlow

class MoneyFlowForm(forms.ModelForm):
    class Meta:
        model = MoneyFlow
        fields = [
            'date',
            'status',
            'flow_type',
            'category',
            'subcategory',
            'amount',
            'comment'
        ]
        widgets = {
            'date': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'placeholder': 'дд.мм.гггг',
                    'type': 'date'  # Можно оставить так для выбора через календарь в браузере
                }
            ),
            'status': forms.Select(),
            'flow_type': forms.Select(),
            'category': forms.Select(),
            'subcategory': forms.Select(),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'date': 'Дата операции',
            'status': 'Статус',
            'flow_type': 'Тип операции',
            'category': 'Категория',
            'subcategory': 'Подкатегория',
            'amount': 'Сумма (руб)',
            'comment': 'Комментарий'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)