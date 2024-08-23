from django.core.management.base import BaseCommand
from django.db import connections, transaction
from todo.models import Prospect

class Command(BaseCommand):
    help = 'Update MSSQL with new records from MySQL based on uuid'

    def handle(self, *args, **kwargs):
        # Get the latest `uuid` value from the MSSQL table
        last_uuid = Prospect.objects.order_by('-uuid').first().uuid

        # Fetch new records from MySQL that have a greater uuid
        with connections['mysql_db'].cursor() as cursor:
            cursor.execute("""
                SELECT
                  wpvo_fluentform_entry_details.id,
                  wpvo_fluentform_entry_details.form_id,
                  wpvo_fluentform_entry_details.submission_id,
                  wpvo_fluentform_entry_details.field_name,
                  wpvo_fluentform_entry_details.field_value,
                  CAST(wpvo_fluentform_submissions.created_at AS DATE)
                FROM wpvo_fluentform_submissions
                  INNER JOIN wpvo_fluentform_entry_details
                    ON wpvo_fluentform_submissions.form_id = wpvo_fluentform_entry_details.form_id
                    AND wpvo_fluentform_submissions.id = wpvo_fluentform_entry_details.submission_id
                WHERE wpvo_fluentform_entry_details.form_id = 4
                AND wpvo_fluentform_entry_details.id > %s
                ORDER BY wpvo_fluentform_entry_details.id
            """, [last_uuid])
            rows = cursor.fetchall()

        # Insert the new records into MSSQL
        with transaction.atomic():
            for row in rows:
                prospect = Prospect(
                    uuid=row[0],  # Using the new field name `uuid`
                    form_id=row[1],
                    submission_id=row[2],
                    field_name=row[3],
                    field_value=row[4],
                    created_at=row[5],
                )
                prospect.save()

        self.stdout.write(self.style.SUCCESS('New records successfully migrated'))
