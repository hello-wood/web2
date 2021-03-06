from django.db import models
from ..base.models import BaseModel
from ..user_manage.models import User
from ..tag_manage.models import Tag


class BlogInfo(BaseModel):
    title = models.CharField(max_length=255, default='')
    author = models.CharField(max_length=50, default='')
    abstract = models.CharField(max_length=500, default='')
    file_path = models.CharField(max_length=255, default='')
    comment_count = models.IntegerField(default=0)
    cover_img = models.CharField(max_length=255, default='default.png')
    favor_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0, db_index=True)


class BlogComment(BaseModel):
    blog_info = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User)
    content = models.TextField(default='')
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE)


class BlogTagRelation(BaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    blog_info = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("tag", "blog_info")  # 这是重点
