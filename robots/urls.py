from django.urls import path
from robots import views as views_robots

urlpatterns = [

    path('robot/', views_robots.RobotView.as_view(), name='robot'),
    path('allrobots/', views_robots.ListRobotsView.as_view(), name='all_robots'),
    path('seriesrobot/', views_robots.ListSeriesRobotsView.as_view(), name='series_robot'),
    path('exportrobots/', views_robots.export_robots_xls, name='xls_robots'),
    path('detail/<int:pk>/', views_robots.DetailRobot.as_view(), name='robot-id'),



]