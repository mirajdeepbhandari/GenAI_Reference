from django.shortcuts import render
from .llm_titan import askChief

def display(request):
    userques = request.POST.get('userask')

    if userques:
        request.session['ai_recepie_que'] = userques
        modelans = askChief(userques)
        request.session['ai_recepie'] = modelans
    else:
        modelans = request.session.get('ai_recepie', "")
        userques = request.session.get('ai_recepie_que', "")

    return render(request, 'home.html', {'modelans': modelans, 'userques': userques})
