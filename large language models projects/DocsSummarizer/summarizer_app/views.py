from django.shortcuts import render
import tempfile
from .llm import doc_words_join, summarize


def home(request):
    if request.method == 'POST':
        form_file = request.FILES.get('formFileMultiple')
        if form_file:
            # Save the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                for chunk in form_file.chunks():
                    temp_file.write(chunk)

            
            # Pass the temporary file path to PyPDFLoader
            join_string = doc_words_join(temp_file.name)

            model_output=summarize(join_string)
            model_summary=model_output['output_text']

            # Delete the temporary file after use
            temp_file.close()
            context = {'summary': model_summary}
            return render(request, "home.html", context)

    return render(request, "home.html")
