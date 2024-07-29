from todo.models import TodoModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from accounts.context_processors import profile_information
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

# generics-items
'''
class TodoView(ListAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
'''

# generics-item
'''
class TodoDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()
'''

# APIView-items
'''
class TodoView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer   # new

    def get(self, request):
        try:
            tasks_done = TodoModel.objects.filter(profile__user=request.user, is_done=True).order_by('-updated')
            tasks_active = TodoModel.objects.filter(profile__user=request.user, is_done=False).order_by('dead_end')
            tasks_done_serializer = self.serializer_class(tasks_done, many=True).data   # new
            tasks_active_serializer = self.serializer_class(tasks_active, many=True).data
        except TypeError:
            tasks_done_serializer = {'detail': '404 not found'}
            tasks_active_serializer = {'detail': '404 not found'}

        context = {
            'tasks_done': tasks_done_serializer,
            'tasks_active': tasks_active_serializer,
        }
        return Response(context)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        TodoModel.objects.create(
            profile_id=profile_information(request)['profile'].id,
            level=serializer_data['level'],
            job=serializer_data['job'],
            dead_end=serializer_data['dead_end']
        )
        return Response(serializer_data)
'''

# APIView-item
'''
class TodoDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer

    def get(self, request, id: int):
        task = get_object_or_404(TodoModel, id=id)
        task_serializer = self.serializer_class(task)
        return Response(task_serializer.data)

    def put(self, request, id: int):
        task = get_object_or_404(TodoModel, id=id)
        serializer = self.serializer_class(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id: int):
        task = get_object_or_404(TodoModel, id=id)
        if task.is_done:
            task.delete()
            return Response({'detail': 'task deleted'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'is_done should be true'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
'''

# ViewSet
'''
class TodoViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()

    def list(self, request):
        serializer = TodoSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        TodoModel.objects.create(
            profile_id=profile_information(request)['profile'].id,
            level=serializer_data['level'],
            job=serializer_data['job'],
            dead_end=serializer_data['dead_end']
        )
        return Response(serializer_data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
'''

# ModelViewSet
class TodoModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = TodoModel.objects.all()