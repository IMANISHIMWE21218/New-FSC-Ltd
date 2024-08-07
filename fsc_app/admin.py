from django.contrib import admin
from .models import CompanyInfo, TestimonialInfo, OurProjects, Partner, TeamMember, Tag, Blog

# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(TestimonialInfo)
admin.site.register(OurProjects)
admin.site.register(Partner)
admin.site.register(TeamMember)
admin.site.register(Tag)
admin.site.register(Blog)