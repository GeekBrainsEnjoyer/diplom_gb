from django import forms


from .models import Recipe

INPUT_CLASSES = 'w-full py-2 px-7 rounded-xl border border-gray-300'


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('category', 'name', 'description', 'steps',
                  'cooking_time', 'image')
        widgets = {
            'category':  forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'placeholder': "Как называется блюдо?",
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'placeholder': "Опишите рецепт.",
                'class': INPUT_CLASSES
            }),
            'steps': forms.Textarea(attrs={
                'placeholder': "Опишите шаги приготовления.",
                'class': INPUT_CLASSES
            }),
            'cooking_time': forms.TextInput(attrs={
                'placeholder': "Напишите примерное время приговления.",
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
