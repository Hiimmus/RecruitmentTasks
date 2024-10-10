from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Wybierz plik tekstowy', help_text='Maksymalny rozmiar pliku: 100 KB')
    
