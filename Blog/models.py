from django.db import models
from django.contrib.auth.models import User

# Create your models here.
upload_dir = ''
filename = ''
class BlogType(models.Model):
    type_name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'blogtype'

    def __str__(self):
        return self.type_name  # 显示标题类型


class Blog(models.Model):
    title = models.CharField(max_length=50) # 标题
    # 删除关联类型报错:ProtectedError
    blog_type = models.ForeignKey(BlogType,on_delete=models.PROTECT) # 标题类型
    author = models.ForeignKey(User,on_delete=models.PROTECT) # 作者
    content = models.TextField(blank=True) # 文章内容
    created_time = models.DateTimeField(auto_now_add=True) # 创建时间
    last_updated_time = models.DateTimeField(auto_now_add=True) # 上一次更新时间

    class Meta:
        db_table = 'blog'


    def __str__(self):
        return "<Blog: %s>" % self.title # 显示标题


class BlogImage(models.Model):
    '''存储图片'''
    def get_dir(filename):
        return upload_dir + filename
    image = models.ImageField(upload_to=get_dir(filename))


    class Meta:
        db_table = 'blogimage'
