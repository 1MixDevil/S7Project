import pandas as pd
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .colab_files.Preprocess import preprocess
from .colab_files.Model_help import model
from .forms import StartForm
from S7Project.settings import FIELDS_CONST, FLOAT_CHOICE_CONST
from .models import Yarik
from django.template.defaulttags import register


def index(request):
    data = {}
    data["info"] = [{"name": "Проблема",
    "info": "Несмотря на то, что воздушный вид транспорта на сегодняшний день является самым безопасным, чрезвычайные происшествия происходят и в авиации. Ключевым фактором является жизнеспособность и надежность систем в особенности двигательных. Не все проблемы можно решить, но четко оценивая состояние летных показателей возможно свести количество фатальных катастроф к минимуму. Наша команда предлагает упростить рассчетный фактор, сводя человеческую ошибку к минимуму используя компьютерные мощности и модели машинного обучения. В условиях, где проблема импортозамещения обострилась как никогда и приходится самостоятельно осваивать новейшие системы оценки и производства, данный проект можно назвать необходимым."
    }, {"name": "Наше решение",
    "info": "Наша команда представляет Engine Condition Monitoring. Мы разработали веб интерфейс, способный показать стандартные характеристики летательного аппарата на основе показаний базовых состояний. В основе веб-интерфейса лежит модель машинного обучения - CatBoostRegressor, а также алгоритм автоматизированного конструирования признаков IterativeImputer, алгоритм заполнения категориальных столбцов - OneHotEncoder, что делает проект понятным и удобным в использовании. Несмотря на то, что проект рассчитан на местное пользование, будучи встроенным прямо в операционную систему судна, воспользоваться им может каждый прямо сейчас. К приложению предоставлен пользовательский интерфейс для возможности проверки работы модели. От пользователя требуется предоставить входные данные (показания датчиков). Для этого в веб версии приложения предоствлена удобная форма ввода. Модель справляется даже с неполностью заполненными входными, поэтому получить информацию о состоянии систем можно даже в случае различных непредвиденных обстоятельств (серьезные неполадки аппарата, датчиков, человеческий фактор). Так же был разработан ряд моделей, которые онованы на типах двигателей самолёта, что позволило повысить точность предсказания по ряду таргетов."
    }]
    return render(request, "Graphs/main.html", data)


class GetData(CreateView):
    template_name = 'Graphs/getData.html'
    form_class = StartForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["constant"] = FIELDS_CONST
        return context

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def finish(request):
    a = request.POST
    keys = []
    values = []
    for i in a:
        if i in FIELDS_CONST:
            try:
                values.append(float(a[i]))
                keys.append(i)
            except:
                keys.append(i)
                values.append(a[i])
    all = preprocess(keys, values)
    new_data = model(all)
    label = new_data[0]
    res = new_data[1]
    data = {}
    for i in range(0, len(res)):
        data[label[i]] = min(res[i])
    id = {}
    for i in range(0, len(label)):
        id[label[i]] = i+1

    context = {"all": data, "constant": FIELDS_CONST, "labels": label, 'id': id}
    return render(request, 'Graphs/finish.html', context)