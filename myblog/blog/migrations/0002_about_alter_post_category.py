# Generated by Django 4.0.3 on 2022-03-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(help_text='글의 분류를 설정하세요.(Ctrl키를 누른 상태로 클릭하여, 여러 개의 카테고리를 설정 가능합니다.)', to='blog.category'),
        ),
    ]
