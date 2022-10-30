from django import forms
from .models import Cars,CarSearchHistory,Review

class Search(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['name','brand']

class DispReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class SearchHist(forms.ModelForm):
    class Meta:
        model = CarSearchHistory
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['carName'].queryset = Cars.objects.none()

        if 'brandName' in self.data:
            cardId = self.data.get('brandName')
            self.fields['carName'].queryset = Cars.objects.filter(brand=cardId)