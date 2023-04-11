# from django.shortcuts import render
# from .models import Student, Teacher
# from django.db import connection
# from django.db.models import Q

# # Part 2
# #################################################################

# ################
# # Simple OR
# ################

# def student_list_(request):

#     posts = Student.objects.all()

#     print(posts)
#     print(posts.query)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})


# # Part 3
# #################################################################

# ################
# # Simple AND
# ################

# def student_list_(request):
#     posts = Student.objects.filter(classroom=1) & Student.objects.filter(age=20)

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# def student_list_(request):
#     posts = Student.objects.filter(Q(surname__startswith='baldwin')&Q(firstname__startswith='lakisha'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# # Part 4
# #################################################################

# ################
# # Simple UNION
# ################

# def student_list_(request):

#     posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))

#     print(posts)
#     print(connection.queries)
#     return render(request,'output.html',{'posts': posts})

# # Part 5
# #################################################################

# ################
# # Simple EXCLUDE
# ################

# def student_list_(request):

#     posts = Student.objects.exclude(age__gt=19)

#     # gt
#     # gte
#     # lt
#     # lte

#     print(posts)
#     print(connection.queries)
#     return render(request,'output.html',{'posts': posts})

# def student_list_(request):

#     posts = Student.objects.filter(~Q(age__gt=20)&~Q(surname__startswith='baldwin'))

#     print(posts)
#     print(connection.queries)
#     return render(request,'output.html',{'posts': posts})

# # Part 6
# #################################################################

# ################
# # SELECT & OUTPUT INDIVIDUAL FILEDS
# ################

# def student_list_(request):

#     posts = Student.objects.filter(classroom=1).only('firstname','age')

#     print(posts)
#     print(connection.queries)
#     return render(request,'output.html',{'data': posts})


# from django.shortcuts import render

# # Create your views here.
# # this is not related to the project just when i was learning sql in django
# from django.db import connection

# # when you use raw sql it dose not returns the data in dic format witch we use in 
# # python django so this fct formats the returned data for us
# def dictfetchall(cursor):
#     desc = cursor.description
#     return [
#         dict(zip([col[0] for col in desc], raw))
#         for raw in cursor.fetchall()
#     ]

# def student_list_(request):
# 	cr = connection.cursor()
# 	cr.execute('SELECT count(*) FROM accounts_student')
# 	result = dictfetchall(cr)
# 	print(result)
# 	print(connection.queries)
# 	return render(request, 'output.html')

