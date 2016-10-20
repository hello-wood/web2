from django.db import models
from ..base.models import BaseModel
from ..user_manage.models import User
from ..tag_manage.models import Tag


class BlogInfo(BaseModel):
    title = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    comment_count = models.IntegerField(default=0)
    cover_img = models.CharField(max_length=255)
    favor_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)


class BlogComment(BaseModel):
    blog_info_id = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User)
    content = models.TextField()
    reply_comment_id = models.ForeignKey('self', on_delete=models.CASCADE)


class BlogTagRelation(BaseModel):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    blog_info_id = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)
