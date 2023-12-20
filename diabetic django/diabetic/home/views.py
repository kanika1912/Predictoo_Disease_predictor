from django.shortcuts import render,HttpResponse
import joblib
import numpy as np
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")

def heart(request):
    return render(request,"heart.html")
def heartresult(request):
    model=joblib.load('heart1.sav')
    lis = [
        float(request.GET.get('age', 0)),  # Providing a default value of 0 if 'age' is missing
        float(request.GET.get('sex', 0)),
        float(request.GET.get('cp', 0)),
        float(request.GET.get('trestbps', 0)),
        float(request.GET.get('chol', 0)),
        float(request.GET.get('fbs', 0)),
        float(request.GET.get('restecg', 0)),
        float(request.GET.get('thalach', 0)),
        float(request.GET.get('exang', 0)),
        float(request.GET.get('oldpeak', 0)),
        float(request.GET.get('slope', 0)),
        float(request.GET.get('ca', 0)),
        float(request.GET.get('thal', 0)),
    ]

    # Convert the input list to a NumPy array
    input_data = np.array(lis).reshape(1, -1)  # Assuming a single sample

    context=model.predict([lis])
    if context == 0:
        return render(request, "heartresult.html", {"context": "You Heart are not defected"})
    else:
        return render(request, "heartresult.html", {"context": "You Heart may be defected "})


def parkeson(request):
    return render(request,"parkeson.html")

def parkessonresult(request):
    model=joblib.load('parkeson.sav')
    lis = [
        float(request.GET.get('MDVP:Fo(Hz)', 0)),  # Providing a default value of 0 if 'age' is missing
        float(request.GET.get('MDVP:Fhi(Hz)', 0)),
        float(request.GET.get('MDVP:Flo(Hz)', 0)),
        float(request.GET.get('MDVP:Jitter(%)', 0)),
        float(request.GET.get('MDVP:Jitter(Abs)', 0)),
        float(request.GET.get('MDVP:RAP', 0)),
        float(request.GET.get('MDVP:PPQ', 0)),
        float(request.GET.get('Jitter:DDP', 0)),
        float(request.GET.get('MDVP:Shimmer', 0)),
        float(request.GET.get('MDVP:Shimmer(dB)', 0)),
        float(request.GET.get('Shimmer:APQ3', 0)),
        float(request.GET.get('Shimmer:APQ5', 0)),
        float(request.GET.get('MDVP:APQ', 0)),
        float(request.GET.get('Shimmer:DDA', 0)),
        float(request.GET.get('NHR', 0)),
        float(request.GET.get('HNR', 0)),
        
        float(request.GET.get('RPDE', 0)),
        float(request.GET.get('DFA', 0)),
        float(request.GET.get('spread1', 0)),
        float(request.GET.get('spread2', 0)),
        float(request.GET.get('D2', 0)),
        float(request.GET.get('PPE', 0)),
    ]

    # Convert the input list to a NumPy array
    input_data = np.array(lis).reshape(1, -1)  # Assuming a single sample

    context=model.predict([lis])
    if context == 0:
        return render(request, "parkessonresult.html", {"context": "You are not parkesson defected"})
    else:
        return render(request, "parkessonresult.html", {"context": "You may be parkesson defected"})