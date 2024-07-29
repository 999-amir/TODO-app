from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

# APIView & generics urls
'''
urlpatterns = [
    path('', views.TodoView.as_view(), name='main_page'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name='detail')
]
'''

# ViewSet & ModelViewSet urls
'''
urlpatterns = [
    path('', views.TodoViewSet.as_view({'get':'list', 'post':'create'}), name='main_page'),
    path('<int:pk>/', views.TodoViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='detail')
]
'''

# router
router = DefaultRouter()
router.register('', views.TodoModelViewSet, basename='todo')
urlpatterns = router.urls
