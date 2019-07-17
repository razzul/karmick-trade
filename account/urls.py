from django.urls import path
from account import views

urlpatterns = [
    # path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
    path('build-risk-pro/', views.build_risk_pro, name='build_risk_pro'),
    path('pick-product/', views.pick_product, name='pick_product'),
    path('review/', views.review, name='review'),
    path('run/', views.run, name='run'),
]