from StrangeBrew.SNB.models import Category,Entry,UserProfile,Competition,Judging
from django.contrib.auth.admin import UserAdmin,User
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
    fields = ['category','name','description','type']
    list_filter = ['user','category','name','type']
    search_fields = ['description']


    def formattedUserName(self,object):
        return object.user.first_name


    def save_model(self,request,obj,form,change):
        if getattr(obj, 'user',None) is None:
            obj.user = request.user
        #if getattr(obj, 'project',None) is None:
        #    obj.project = Project.objects.filter(project__contains='N/A')[0]
        obj.last_modified_by = request.user
        obj.save()
    def queryset(self,request):
        qs = super(EntryAdmin,self).queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(user=request.user)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class SNBUserAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

admin.site.register(Entry,EntryAdmin)
admin.site.register(Category)
admin.site.register(Competition)
admin.site.register(Judging)
admin.site.unregister(User)
admin.site.register(User,SNBUserAdmin)
