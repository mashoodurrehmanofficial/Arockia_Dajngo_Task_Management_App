from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid,os
from django.db.models.signals import post_save, post_delete,post_save,pre_save
from django.dispatch.dispatcher import receiver
from datetime import datetime

 



class Chore_Table(models.Model):
    chore_name         = models.CharField(max_length=1000,blank=True,default='')
    chore_code         = models.CharField(max_length=1000,blank=True,default='')
    cre_on              = models.DateTimeField(blank=True,null=True,default=datetime.now())
    last_updt_on        = models.DateTimeField(blank=True,null=True,default=datetime.now())
    cre_by              = models.CharField(max_length=1000,blank=True,default='System')
    last_updt_by        = models.CharField(max_length=1000,blank=True,default='System')
    category            = models.IntegerField(blank=True,default=0)
    rank                = models.IntegerField(blank=True,default=10000)
    points              = models.IntegerField(blank=True,default=100)
    background_color    = models.CharField(max_length=1000,blank=True,default='')
    icon                = models.FileField(upload_to="chore_icons/",blank=True,null=True)
    def __str__(self):
        return self.chore_name


@receiver([post_save,post_delete], sender=Chore_Table)
def delete_profile(sender, instance, *args, **kwargs):
    root_dir            = os.path.join(os.getcwd(),'Media','chore_icons')
    stored_images       = os.listdir(root_dir)
    required_images     = Chore_Table.objects.all().values('icon')
    required_images     = [str(x['icon']).replace('chore_icons/','') for x in required_images]
    extra_images        = [x for x in stored_images if x not  in required_images]
    extra_images        = [os.path.join(root_dir,x) for x in extra_images]
    # print("Extra images -> ", stored_images)
    # print("Extra images -> ", required_images)
    [os.remove(x) for x in extra_images if os.path.isfile(x)]



class Transaction_Table(models.Model):
    date            = models.DateTimeField(blank=True,null=True,default=datetime.now())
    duration        = models.IntegerField(blank=True,default=None,null=True)
    chore           = models.ForeignKey(Chore_Table,on_delete=models.CASCADE,blank=True,null=True)
    user            = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    cre_on          = models.DateTimeField(blank=True,null=True,default=datetime.now())
    last_updt_on    = models.DateTimeField(blank=True,null=True,default=datetime.now())
    cre_by          = models.CharField(max_length=1000,blank=True,default='System')
    last_updt_by    = models.CharField(max_length=1000,blank=True,default='System')