from django.shortcuts import render
import joblib
import pandas as pd


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def result(request):
    cls = joblib.load('C:/Users/salwa/PycharmProjects/finalq/finalq/quality/static/quality/quality.pkl')

    value1 = request.GET['fixed_acidity']
    value2 = request.GET['volatile_acidity']
    value3 = request.GET['citric_acid']
    value4 = request.GET['residual_sugar']
    value5 = request.GET['chlorides']
    value6 = request.GET['free_sulphur_dioxide']
    value7 = request.GET['alcohol']
    value8 = request.GET['density']
    value9 = request.GET['sulphates']
    value10 = request.GET['pH']
    dict = {'fixed acidity': value1, 'volatile acidity': value2, 'citric acid': value3, 'residual sugar': value4,
            'chlorides': value5, 'free sulphur dioxide': value6, 'density': value8, 'pH': value10, 'sulphates': value9,
            'alcohol': value7}

    user_df = pd.DataFrame(data=dict, index=[0], columns=['fixed acidity', 'volatile acidity',
                                                          'citric acid', 'residual sugar',
                                                          'chlorides', 'free sulphur dioxide',
                                                          'density',
                                                          'pH', 'sulphates', 'alcohol'])

    ans = cls.predict(user_df)
    if ans == 0:
        return render(request, 'resultbad.html')
    elif ans == 1:
        return render(request, 'resultgood.html')
