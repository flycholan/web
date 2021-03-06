# Generated by Django 2.2.4 on 2020-11-21 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0029_quest_reward_tip'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='force_visible',
            field=models.BooleanField(default=False, help_text='override such that the re_rank_quests mgmt command does not make the quest invisible due to low feedback.'),
        ),
    ]
