from django.urls import path
from . import views

urlpatterns = [
	
	
	path('', views.home, name = 'home'),
	path('second', views.second, name = 'second'),
	path('modal', views.modal, name = 'modal'),
	path('modalsec', views.modalsec, name = 'modalsec'),
	path('third', views.third, name = 'third'),
	path('forth', views.forth, name = 'forth'),
	path('fifth', views.fifth, name = 'fifth'),
	path('test', views.test, name = 'test'),
	path('delete', views.delete, name = 'delete'),
	path('deleter', views.deleter, name = 'deleter'),
	path('backtest', views.backtest, name = 'backtest'),
	path('secondback', views.secondback, name = 'secondback'),
	path('thirdback', views.thirdback, name = 'thirdback'),
	path('static', views.static, name = 'static'),
	path('exit', views.exit, name = 'exit'),
	
	]