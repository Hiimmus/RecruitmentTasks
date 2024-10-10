from django.shortcuts import render
from text_shuffle.scripts.utils import shuffle_words_with_punctuation
from django.core.files.uploadedfile import UploadedFile
from .forms import UploadFileForm


def text_shuffle(request):
    SHUFFLE_URL = 'text_shuffle/text_shuffle.html'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file: UploadedFile = form.cleaned_data['file']

            if uploaded_file.size == 0:
                error_message = "Przesłany plik jest pusty"
                return render(request, SHUFFLE_URL, {'form': form, 'error_message': error_message})

            if uploaded_file.content_type == 'text/plain':
                try:
                    # Max text length (100 KB)
                    max_text_length = 100000
                    text = uploaded_file.read().decode('utf-8')

                    if len(text) > max_text_length:
                        error_message = f"Tekst jest za długi. Maksymalna długość to {max_text_length} znaków."
                        return render(request, SHUFFLE_URL, {'form': form, 'error_message': error_message})

                    modified_text = shuffle_words_with_punctuation(text)
                    return render(request, SHUFFLE_URL, {'form': form, 'text': text, 'modified_text': modified_text})

                except UnicodeDecodeError:
                    error_message = "Nie udało się odczytać pliku"
                    return render(request, SHUFFLE_URL, {'form': form, 'error_message': error_message})
            else:
                error_message = "Proszę przesłać plik tekstowy (.txt)."
                return render(request, SHUFFLE_URL, {'form': form, 'error_message': error_message})
    else:
        form = UploadFileForm()

    return render(request, SHUFFLE_URL, {'form': form})
