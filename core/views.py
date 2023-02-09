# from django.shortcuts import render
# import pandas as pd
#
# # Create your views here.
import base64
import calendar
from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file into a pandas dataframe
from django.shortcuts import render

from core.models import PatientData


def home(request):
    return render(request, 'home.html')


def index(request):
    x = []
    y = []
    z = []

    df = pd.read_csv('Book1.1.csv')
    df.plot(x='name', figsize=(10, 5), grid=True)
    # plt.show()
    df = df.sort_values('months_of_treatment', ascending=False)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    # plt.show()
    return render(request, 'index.html', {'graphic': graphic})


def detail(request):
    return render(request, 'details.html')


def patient(request):
    df = pd.read_csv("Book1.csv")
    name = request.GET.get('search')

    # # # Filter the data based on some condition
    df_data = df[df['Name'] == name]

    month = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'July']
    eating_behaviour = []
    harm_behaviour = []
    mood_behaviour = []
    social_interactions = []
    for i in range(1, 7):
        eating_behaviour.append(df_data[calendar.month_abbr[i].lower() + "_eating_behaviour"])
        harm_behaviour.append(df_data[calendar.month_abbr[i].lower() + "_self_harm"])
        mood_behaviour.append(df_data[calendar.month_abbr[i].lower() + "_mood"])
        social_interactions.append(df_data[calendar.month_abbr[i].lower() + "_social_interactions"])

    plt.plot(month, eating_behaviour, label='Eating')
    plt.plot(month, harm_behaviour, label='Harm')
    plt.plot(month, mood_behaviour, label='mood')
    plt.plot(month, social_interactions, label='social')
    plt.legend()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image1_png = buffer.getvalue()
    buffer.close()

    graphic1 = base64.b64encode(image1_png)
    graphic1 = graphic1.decode('utf-8')
    plt.close()

    return render(request, 'details.html', {'graphic1': graphic1})


# def patient_detail(request):
#     df = pd.read_csv("Book1.csv")
#
#     # # # Filter the data based on some condition
#     df_data = df[df['Name'] == 'dannz']
#
#     month = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'July']
#     eating_behaviour = []
#     harm_behaviour = []
#     mood_behaviour = []
#     social_interactions = []
#     for i in range(1, 7):
#         eating_behaviour.append(df_data[calendar.month_abbr[i] + "-Eating-Behaviour"])
#         harm_behaviour.append(df_data[calendar.month_abbr[i] + "-Self-Harm"])
#         mood_behaviour.append(df_data[calendar.month_abbr[i] + "-Mood"])
#         social_interactions.append(df_data[calendar.month_abbr[i] + "-Social-Interactions"])
#
#     plt.plot(month, eating_behaviour, label='Eating')
#     plt.plot(month, harm_behaviour, label='Harm')
#     plt.plot(month, mood_behaviour, label='mood')
#     plt.plot(month, social_interactions, label='social')
#
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()
#
#     graphic = base64.b64encode(image_png)
#     graphic = graphic.decode('utf-8')
#
#     return render(request, 'user_detail.html', {'graphic': graphic})


def patient_detail(request):
    # df = pd.read_csv("Book1.csv")

    name = request.GET.get('search')
    data = PatientData.objects.filter(Name=name)

    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July']
    eating_behaviour = []
    harm_behaviour = []
    mood_behaviour = []
    social_interactions = []
    for data in data:
        eating_behaviour = [data.jan_eating_behaviour, data.feb_eating_behaviour, data.mar_eating_behaviour,
                            data.apr_eating_behaviour, data.may_eating_behaviour, data.jun_eating_behaviour,
                            data.jul_eating_behaviour]
        harm_behaviour = [data.jan_self_harm, data.feb_self_harm, data.mar_self_harm, data.apr_self_harm,
                          data.may_self_harm, data.jun_self_harm, data.jul_self_harm]

        mood_behaviour = [data.jan_mood, data.feb_mood, data.mar_mood, data.apr_mood, data.may_mood, data.jun_mood,
                          data.jul_mood]
        social_interactions = [data.jan_social_interactions, data.feb_social_interactions, data.mar_social_interactions,
                               data.apr_social_interactions, data.may_social_interactions, data.jun_social_Interactions,
                               data.jul_social_Interactions]
    plt.close()
    plt.plot(month, eating_behaviour, label='Eating')
    plt.plot(month, harm_behaviour, label='Harm')
    plt.plot(month, mood_behaviour, label='mood')
    plt.plot(month, social_interactions, label='social')
    plt.legend()
    buffer = BytesIO()
    plt.savefig(buffer, format='png')

    plt.close()
    buffer.seek(0)
    image1_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image1_png)

    graphic = graphic.decode('utf-8')
    plt.close()

    return render(request, 'details.html', {'graphic': graphic, 'data': data})
