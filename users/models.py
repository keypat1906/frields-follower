
from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,blank=False,null=False)

    class Meta(object):
        db_table = 'Users'

class Relations(models.Model):
    follower_id = models.ForeignKey('Users', on_delete=models.CASCADE,related_name='from_user')
    following_id = models.ForeignKey('Users', on_delete=models.CASCADE,related_name='to_user')
    
    class Meta(object):
        db_table = 'Relations'
        unique_together = ('follower_id','following_id',)
