from django.db import models

POSTS = (
    ('Dgsec' , 'Department General Secretary'),
    ('Gsec' , 'General Secretary (CSEA)'),
    ('pgrep' , 'PG Represntative')

)

class applicant(models.Model):
    name = models.CharField(max_length=30)
    post = models.CharField(max_length=5, choices=POSTS, default='Dgsec')
    image = models.ImageField(upload_to='photos')
    count = models.IntegerField(default=0)

   
