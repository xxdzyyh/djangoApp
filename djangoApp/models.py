from django.conf import settings

def upload_to(instance, filename):
	return '/'.join([settings.MEDIA_ROOT, time.strftime('%Y'),time.strftime('%m'), time.strftime('%d'),str(instance.project_id), filename])