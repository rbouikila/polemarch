# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-09 07:50
from __future__ import unicode_literals
import six
from django.db import migrations, models
import django.db.models.deletion
import polemarch.main.models.base
from polemarch.main.utils import AnsibleModules


def sync_modules(apps, schema_editor):
    Module = apps.get_registered_model('main', 'Module')
    modules = AnsibleModules(detailed=False)
    modules_list = modules.all()
    modules_list.sort()
    Module.objects.bulk_create([
        Module(path=module, project=None) for module in modules_list
    ])


def set_inventories_to_project(apps, schema_editor):
    PeriodicTask = apps.get_registered_model('main', 'PeriodicTask')
    Template = apps.get_registered_model('main', 'Template')
    for ptask in PeriodicTask.objects.exclude(_inventory=None):
        try:
            ptask.project.inventories.add(ptask._inventory)
        except:
            pass

    for templ in Template.objects.all():
        try:
            inv = templ.inventory_object
            if not isinstance(inv, (six.string_types, six.text_type)):
                templ.project.inventories.add(inv)
        except:
            pass


def remove_templates_without_project(apps, schema_editor):
    Template = apps.get_registered_model('main', 'Template')
    Template.objects.filter(project=None).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_v2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('hidden', models.BooleanField(default=False)),
                ('path', models.CharField(max_length=1024)),
                ('_data', models.CharField(default='{}', max_length=4096)),
                ('project', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', related_query_name='modules', to='main.Project')),
            ],
            options={
                'default_related_name': 'modules',
            },
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='_inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodic_task', related_query_name='periodic_task', to='main.Inventory'),
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='acl',
            field=models.ManyToManyField(blank=True, null=True, related_name='periodic_task', to='main.ACLPermission'),
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodic_task', related_query_name='periodic_task', to='main.Project'),
        ),
        migrations.AlterField(
            model_name='periodictask',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='periodic_task', related_query_name='periodic_task', to='main.Template'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playbook', related_query_name='playbook', to='main.Project'),
        ),
        migrations.AlterField(
            model_name='template',
            name='acl',
            field=models.ManyToManyField(blank=True, null=True, related_name='template', to='main.ACLPermission'),
        ),
        migrations.AlterField(
            model_name='template',
            name='project',
            field=polemarch.main.models.base.ForeignKeyACL(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='template', to='main.Project'),
        ),
        migrations.RunPython(
            code=sync_modules,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            code=set_inventories_to_project,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            code=remove_templates_without_project,
            reverse_code=migrations.RunPython.noop
        ),
    ]
