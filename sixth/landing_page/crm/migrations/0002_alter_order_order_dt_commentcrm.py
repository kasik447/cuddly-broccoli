# Generated by Django 5.0.1 on 2024-06-11 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_dt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст комментария')),
                ('comment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('comment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
