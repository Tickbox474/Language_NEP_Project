from django.shortcuts import render
from .translations import translate

# Create your views here

def index(request):
    translated_text = ''
    if request.method == 'POST':
        source_text = request.POST.get('sourceText', '')
        source_language = request.POST.get('sourceLanguage', 'en')
        target_language = request.POST.get('targetLanguage', 'en')
        translated_text = translate(source_text, source_language, target_language)
        return render(request, 'index.html', {'sourceText': source_text, 'translatedText': translated_text})
    
    return render(request, 'index.html', {'sourceText': '', 'translatedText': ''})

    