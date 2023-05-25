from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('',views.log_in,name="login"),
    path('register',views.register,name="register"),
    path('Quora',views.index,name="home"),
    path('Quora/list', views.question_list, name='question_list'),
    path('Quora/create/', views.create_question, name='create_question'),
    path('question/<int:q_id>/answer', views.question_detail, name='question_detail'),
    # path('question/<int:q_id>/answer', views.question_details, name='question_details'),
    path('answer/<int:q_id>', views.answer_detail, name='answer_detail'),
    path('question/<int:q_id>', views.create_answer, name='create_answer'),
    path('logout',views.log_out,name='logout'),

 
]


