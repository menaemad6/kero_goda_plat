from django.contrib import admin


from core.models import Assignment , AssignmentOpen , Question , AssignmentSubmit  , Answer

# Register your models here.


admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(AssignmentOpen)
admin.site.register(AssignmentSubmit)
admin.site.register(Answer)

