from django import forms

from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'done', 'complete_before')
        labels = {
            'name': 'Nombre de la Tarea',
            'description': 'Descripción',
            'done': '¿Completada?',
            'complete_before': 'Fecha de Finalización',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre de la tarea'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Descripción'}
            ),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'complete_before': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                }
            ),
        }
