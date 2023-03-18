from django.shortcuts import render

from myapp1.models import Worker


# Create your views here.
def index_page(request):
    workers = Worker.objects.all()
    print((workers))

    return render(request, 'index.html', context={'data': workers})

    # create new worker
    # new_Worker = Worker(name = 'Ivan', second_name = 'Ohlobystin', salary = 85000)
    # new_Worker.save()
    # Worker.objects.create(name = 'Kilian', second_name = 'Mpappe', salary = 1000)

    # change worker
    change_worker = Worker.objects.get(id=4)
    change_worker.second_name = 'Urgant'
    change_worker.save()


    # delete worker
    # Worker.objects.get(id=5).delete()


    filter_workers = Worker.objects.filter(salary = 60000)
    print((filter_workers))

    # for i in workers:
    #     print(f'Surname: {i.second_name}, Name: {i.name}, Salary: {i.salary}, ID: {i.id}')




