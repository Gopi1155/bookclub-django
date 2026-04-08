"""
Management command to export and import test data
Usage: python manage.py dumpdata books users > backup.json
       python manage.py loaddata backup.json
"""

# This file can be used for data backup and restoration

# Example backup command:
# python manage.py dumpdata books users auth > data_backup.json

# Example restore command:
# python manage.py loaddata data_backup.json

# Complete backup (including admin):
# python manage.py dumpdata > complete_backup.json

# Restore from backup:
# python manage.py loaddata complete_backup.json

print("""
Data Backup & Restore Guide
=============================

BACKUP COMMANDS:
1. Backup only books and users:
   $ python manage.py dumpdata books users auth > data_backup.json

2. Complete backup (all data):
   $ python manage.py dumpdata > complete_backup.json

3. Backup specific model:
   $ python manage.py dumpdata books.Book > books_backup.json

RESTORE COMMANDS:
1. Restore from backup:
   $ python manage.py loaddata data_backup.json

2. Clear and restore:
   $ python manage.py flush
   $ python manage.py loaddata complete_backup.json

USEFUL OPTIONS:
--format json   # Default JSON format
--format yaml   # YAML format
--indent 2      # Pretty print with indentation
--exclude auth.permission  # Exclude specific models
--natural-foreign  # Use natural keys

EXAMPLE:
$ python manage.py dumpdata books users --indent 2 > backup.json
$ python manage.py loaddata backup.json
""")
