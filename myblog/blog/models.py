from django.db import models
from django.urls import reverse

# Create your models here.
#글의 분류(게임 출시, 공략, 정보)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text = "블로그 글의 분류를 입력하십시오.")

    def __str__(self):
        return self.name

#블로그 글(제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.(Ctrl키를 누른 상태로 클릭하여, 여러 개의 카테고리를 설정 가능합니다.)")
    #하나의 글이 여러 분류에 적용 가능

    def __str__(self):
        return self.title
    
    #1번 글이면 post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def get_content(self):
        if len(self.content) > 96:
            return self.content[:96]
        else:
            return self.content

