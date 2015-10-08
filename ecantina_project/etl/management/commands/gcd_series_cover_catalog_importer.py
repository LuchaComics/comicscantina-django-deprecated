import os
import sys
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from api.models.gcd.issue import GCDIssue


LARGE_ZOOM = 4
MEDIUM_ZOOM = 2
SMALL_ZOOM = 1
PRIMARY_IMAGE = 1
ALTERNATIVE_IMAGE = 2


class GCDIssueCoverCatalogImporter:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def begin_import(self):
        for event, elem in ET.iterparse(self.file_path):
            if elem.tag == "row":
                self.import_row(elem)
                elem.clear()

    def import_row(self, row):
        id = int(row.findtext('id'))
        image_type = int(row.findtext('type'))
        zoom = int(row.findtext('zoom'))
        url = row.findtext('url')

        print("GCDIssueCoverCatalogImporter: Updating: " + str(id))
        try:
            issue = GCDIssue.objects.get(issue_id=id)
        except GCDIssue.DoesNotExist:
            print("Error: Issue "+str(id)+" does not exist.")
            return

        if image_type is PRIMARY_IMAGE:
            if zoom is SMALL_ZOOM:
                issue.small_url = url
            if zoom is MEDIUM_ZOOM:
                issue.medium_url = url
            if zoom is LARGE_ZOOM:
                issue.large_url = url
        elif image_type is ALTERNATIVE_IMAGE:
            issue.has_alternative = True
            if zoom is SMALL_ZOOM:
                issue.alt_small_url = url
            if zoom is MEDIUM_ZOOM:
                issue.alt_medium_url = url
            if zoom is LARGE_ZOOM:
                issue.alt_large_url = url
        else:
            print("Error: Unknown Image Type: " + str(image_type))
            return
        issue.save()

class Command(BaseCommand):
    """
        ----------------------
        import_gcd_covers
        ----------------------
        ETL will load up the catalog.xml file for the Issue Cover assets and
        update the associated Issue in the database to reference the imported
        covers.
        
        Run in your console:
        $ python manage.py import_gcd_issue_covers /Users/bartlomiejmika/Developer/comicscantina/py-comicscantina/scripts/cover/issue_catalog.xml
        
        (Where that file path is the path to where the GCD XML files are located)
    """
    help = 'ETL loads up the GCD database into our applicaton using the provided xml files.'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+')
    
    def handle(self, *args, **options):
        os.system('clear;')  # Clear the console text.
        for file_path in options['file_path']:
            importer = GCDIssueCoverCatalogImporter(full_file_path)
            importer.begin_import()
            print(file_path)
