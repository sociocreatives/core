from django.contrib import admin
from .models import Faq, Partners, About, AboutHeader, Terms

class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'author')

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class AboutHeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class TermsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Faq, FaqAdmin)
admin.site.register(Partners, PartnersAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(AboutHeader, AboutHeaderAdmin)
admin.site.register(Terms, TermsAdmin)

