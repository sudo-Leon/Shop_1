"""
URL configuration for Online_Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Online_Shop.mainapp import views
"""
1:25:42
"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
# urlpatterns в Django - это список путей (URL-шаблонов),
# которые определяют, как обрабатываются запросы от клиента. В данном коде присутствует
# один элемент в списке urlpatterns, определяющий путь 'admin/' и указывающий,
# что для этого пути должен быть использован обработчик, предоставляемый Django для
# административного интерфейса. Это означает, что когда клиент делает запрос на URL,
# который начинается с 'admin/', Django будет использовать соответствующий обработчик,
# чтобы обработать этот запрос и предоставить административный интерфейс.

path('',views )
