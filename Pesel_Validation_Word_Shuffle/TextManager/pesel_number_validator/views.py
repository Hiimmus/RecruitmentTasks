from django.shortcuts import render
from .forms import PeselForm
from .models import Pesel
from pesel_number_validator.scripts.utils import return_gender_from_pesel, return_birth_date_from_pesel, validate_number


def pesel_view(request):

    result = None
    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel_number = form.cleaned_data['number']

            if len(pesel_number) != 11:
                result = {'valid': False,
                          'error': 'Numer PESEL musi mieć dokładnie 11 cyfr.'}
            elif not pesel_number.isdigit():
                result = {'valid': False,
                          'error': 'Numer PESEL musi składać się tylko z cyfr.'}
            else:
                try:
                    pesel_number_int = int(pesel_number)
                    if validate_number(pesel_number_int):
                        gender = return_gender_from_pesel(pesel_number_int)
                        birth_date = return_birth_date_from_pesel(
                            pesel_number_int)
                        result = {
                            'valid': True,
                            'gender': gender,
                            'birth_date': birth_date,
                        }
                    else:
                        result = {'valid': False,
                                  'error': 'Numer PESEL jest niepoprawny.'}
                except ValueError:
                    result = {'valid': False,
                              'error': 'Numer PESEL zawiera niedozwolone znaki.'}
        else:
            result = {'valid': False, 'error': 'Wypełnij formularz poprawnie.'}
    else:
        form = PeselForm()

    form.fields['number'].widget.attrs.update({'class': 'form-control'})

    return render(request, 'pesel_form.html', {'form': form, 'result': result})
