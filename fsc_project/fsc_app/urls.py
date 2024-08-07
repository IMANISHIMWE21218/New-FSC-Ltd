from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from fsc_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('agroforestry/', views.agroforestry, name='agroforestry'),
    path('biogasGeneration', views.biogasGeneration, name='biogasGeneration'),
    path('blog/', views.blog, name='blog'),
    path('blogsingle/<int:pk>/', views.blogsingle, name='blogsingle'),
    path('career', views.career, name='career'),
    path('OrganicManureProduction', views.OrganicManureProduction, name='OrganicManureProduction'),
    path('projectsingle/<int:id>/', views.projectsingle, name='projectsingle'),
    path('RainwaterHarvesting', views.RainwaterHarvesting, name='RainwaterHarvesting'),
    path('RuralDevelopmentSolutions', views.RuralDevelopmentSolutions, name='RuralDevelopmentSolutions'),
    path('WasteManagement', views.WasteManagement, name='WasteManagement'),
    path('services', views.services, name='services'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
