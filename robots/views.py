from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.db.models import F, Sum, Max, Min, Count, Avg
from django.forms import model_to_dict
from .models import Robot, Customer

import xlwt
import json

# Create your views here.

dc_bar = [

    {'title': 'API', 'url_name': 'robot'},
    {'title': 'Все роботы', 'url_name': 'all_robots'},
    {'title': 'Скачать файл Exel', 'url_name': 'series_robot'},

]


@method_decorator(csrf_exempt, name='dispatch')
class RobotView(View):

    def get(self, request):
        robot_count = Robot.objects.count()
        robots = Robot.objects.all()
        robot_serializer_data = serialize('python', robots, fields=['serial', 'model', 'version'])
        actual_fields = [i['fields'] for i in robot_serializer_data]
        # for robot in robots:
        #     robot_serializer_data.append({
        #         'serial': robot.serial,
        #         'model': robot.model,
        #         'version': robot.version
        #     })
        data = {
            'robot': actual_fields,
            'robot_count': robot_count,
        }
        return JsonResponse(data)

    def post(self, request):
        post_body = json.loads(request.body.decode('utf-8'))
        robot_serial = post_body.get('serial')
        robot_model = post_body.get('model')
        robot_version = post_body.get('version')

        robot_data = {
            'serial': robot_serial,
            'model': robot_model,
            'version': robot_version
        }
        robot_obj = Robot.objects.create(**robot_data)
        data = json.loads(serialize('json', [robot_obj]))
        return JsonResponse(data, safe=False)


class ListRobotsView(ListView):

    model = Robot
    template_name = 'robots/index_robot.html'
    context_object_name = 'all_robots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dc_bar'] = dc_bar
        return context


class ListSeriesRobotsView(ListView):

    model = Robot
    template_name = 'robots/all_serial_robots.html'
    context_object_name = 'serial_robots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dc_bar'] = dc_bar
        context['rob_count'] = Robot.objects.all().aggregate(Count('model'))
        return context

    def get_queryset(self):
        return Robot.objects.all()


class DetailRobot(DetailView):
    model = Robot
    template_name = 'robots/detail_robot.html'
    context_object_name = 'one_robot'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'dc_bar': dc_bar,
            'cust': Customer.objects.all()
        })
        return context


def export_robots_xls(request):

    response = HttpResponse(content_type='application/ms-exel')
    response['Content-Disposition'] = 'attachment;filename="robots.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Robot')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Модель', 'Версия', 'Количество']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Robot.objects.all().values_list('model', 'version', 'stock')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
