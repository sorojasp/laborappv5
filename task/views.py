from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
#from django.contrib.auth.models import User
from user.models import  MyUser as User
from task import models
from task import serializer
from django.db.models import Avg, Max, Min
from django.db.models import Q

class TaskView(ModelViewSet):


    serializer_class = serializer.TaskSerializer
    queryset = models.Task.objects.all()


    def create(self, request, *args, **kwargs):
        try:
            dataTask: dict = request.data
            print(dataTask)
            print(f"*datos desde el servidor: {request.query_params.get('Authorization')}")
            obj_user: User = User.objects.get(email=request.query_params.get('Authorization'))
            obj_task: models.Task = models.Task.objects.create(description = dataTask['description'], fecha = dataTask['fecha'],
                                                               porcentajeCumplimiento=dataTask['porcentajeCumplimiento'], tiempo=dataTask['tiempo'], user=obj_user)
            obj_task.save()
            return Response({
            "resp": "ok",
            "id": obj_task.id
            })

        except Exception as error:

            return Response({
                "resp": "failed",
                "detail": error.__str__()
            })

    def list(self, request, *args, **kwargs):

        obj_user: User = User.objects.get(email=request.query_params.get('Authorization'))
        fecha_inicial = request.query_params.get('fecha_inicial')
        fecha_final = request.query_params.get('fecha_final')

        task_queryset=models.Task.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final)& Q(user=obj_user))

        for task in task_queryset:
            print(task)
        serializer = self.serializer_class(task_queryset, many=True)
        return Response({
            "resp": "ok",
            "data": serializer.data
        })



class SubTaskView(ModelViewSet):


    serializer_class = serializer.SubTaskSerializer
    queryset = models.SubTask.objects.all()


    def create(self, request, *args, **kwargs):
        try:
            description = request.data["description"]
            porcentajeCumplimiento=request.data["porcentajeCumplimiento"]
            id_task=request.data["id_task"]
            task_obj:models.Task=models.Task.objects.get(id=id_task)
            subtask_obj=models.SubTask.objects.create(description=description, porcentajeCumplimiento= porcentajeCumplimiento, task=task_obj)
            subtask_obj.save()
            return Response({
                "resp": "ok",
                "id":subtask_obj.id
            })

        except Exception as error:
            return Response({
                "resp": "failed",
                "detalle": error.__str__()
            })

    def list(self, request, *args, **kwargs):

        obj_user: User = User.objects.get(email=request.query_params.get('Authorization'))
        fecha_inicial = request.query_params.get('fecha_inicial')
        fecha_final = request.query_params.get('fecha_final')

        task_queryset = models.Task.objects.filter(Q(fecha__gte=fecha_inicial) & Q(fecha__lte=fecha_final) & Q(user = obj_user))

        tasks: list = []
        sumatoria_cumplimiento = 0

        for task in task_queryset:
            task_: dict = {}
            subTasks = models.SubTask.objects.filter(task=task)
            task_['task'] = serializer.TaskSerializer(task).data
            serializer_subtask = self.serializer_class(subTasks, many=True)
            task_['subtasks'] = serializer_subtask.data

            if len(subTasks) > 0:

                for subtask in subTasks:
                    sumatoria_cumplimiento = sumatoria_cumplimiento + subtask.porcentajeCumplimiento

                task_['promedioRendimiento']= sumatoria_cumplimiento / len(subTasks)
                print(sumatoria_cumplimiento / len(subTasks))

            else:
                task_['promedioRendimiento'] = task.porcentajeCumplimiento


            tasks.append(task_)



        return Response({
            "resp": "ok",
            "data": tasks
        })




# Create your views here.
