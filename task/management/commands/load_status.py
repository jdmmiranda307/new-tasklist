# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from task.models import Status

def load_objects(objects, model_name):
    for obj in objects:
        try:
            current = obj
            current.save()
        except Exception as e:
            db.session.rollback()

    print('{} objects loaded.'.format(model_name))

def load_status():
    load_objects([
        Status(description="To do"),
        Status(description="Doing"),
        Status(description="Done"),
    ], "Status")

class Command(BaseCommand):
    """ Loads data into newly created database """

    def handle(self, *args, **options):
        load_status()
