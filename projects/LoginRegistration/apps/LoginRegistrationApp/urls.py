from django.conf.urls import url
from . import views #(imports views.py of the current folder)

urlpatterns = [ 
    url(r'^$', views.index), 
    url(r'^register', views.register),
    url(r'login', views.login),
    url(r'success', views.success) 
    ]

    # @app.route('/register', methods=['POST'])
    # @app.route('/')
    # @app.route('/login', methods=['POST'])
    # @app.route('/msgs') 