from django.shortcuts import render
from django.views import View


class TodoView(View):
    def get(self, request):
        context = {
            'calender_days_name': ['Su', 'Mo', 'Tu', 'We', 'Te', 'Fr', 'Sa'],
            'calender_days_number': range(1, 32),
            'calender_months': ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand'],
        }
        return render(request, 'todo/todo.html', context)
