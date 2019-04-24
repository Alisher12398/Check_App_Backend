from django.db import models

class Qa(models.Model):
    id = models.IntegerField(),
    id_group = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=512)
    answer_1 = models.CharField(max_length=40)
    answer_2 = models.CharField(max_length=40)
    answer_3 = models.CharField(max_length=40)
    answer_4 = models.CharField(max_length=40)
    answer_right = models.IntegerField()

    def get_questions(self):
        return {
            'id': self.id,
            'id_group': self.id_group,
            'question': self.question,
            'answer_1': self.answer_1,
            'answer_2': self.answer_2,
            'answer_3': self.answer_3,
            'answer_4': self.answer_4,
            'answer_right': self.answer_right,
        }

class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40)
    id_prerequisite = models.IntegerField()

    def get_groups(self):
        return {
            'id': self.id,
            'title': self.title,
            'id_prerequisite': self.id_prerequisite,
        }

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    points = models.IntegerField()

class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    points = models.IntegerField()



# name = models.CharField(max_length=255)
# created_at = models.DateTimeField()
# due_on= models.DateTimeField(auto_now_add=True)
# status = models.CharField(max_length=255)
# task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
#
# def __str__(self):
#     return self.name
#
# def to_json_task(self):
#     return {
#         'id': self.id,
#         'name': self.name,
#         'status': self.status,
#     }
#
# def to_json_all(self):
#     return {
#         'id': self.id,
#         'name': self.name,
#         'created_at': self.created_at,
#         'due_on': self.due_on,
#         'status': self.status,
#         'task_list': self.task_list.to_json(),
#     }