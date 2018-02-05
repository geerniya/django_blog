from django.contrib import admin

from myblog.models import Blog, Category, Tag, Comment, Counts


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'click_nums', 'category', 'create_time', 'modify_time']

    def save_model(self, request, obj, form, change):
        obj.save()
        #统计博客数目
        blog_nums = Blog.objects.count()
        count_nums = Counts.objects.get(id=1)
        count_nums.blog_nums = blog_nums
        count_nums.save()
        #博客分类数目统计
        obj_category = obj.category
        category_number = obj_category.blog_set.count()
        obj_category.number = category_number
        obj_category.save()
        #博客标签数目统计
        obj_tag_list = obj.tag.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number
            obj_tag.save()

    def delete_model(self, request, obj):
        # 统计博客数目
        blog_nums = Blog.objects.count()
        count_nums = Counts.objects.get(id=1)
        count_nums.blog_nums = blog_nums - 1
        count_nums.save()
        # 博客分类数目统计
        obj_category = obj.category
        category_number = obj_category.blog_set.count()
        obj_category.number = category_number - 1
        obj_category.save()
        # 博客标签数目统计
        obj_tag_list = obj.tag.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number - 1
            obj_tag.save()
        obj.delete()



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']

    def save_model(self, request, obj, form, change):
        obj.save()
        category_nums = Category.objects.count()
        count_nums = Counts.objects.get(id=1)
        count_nums.category_nums = category_nums
        count_nums.save()

    def delete_model(self, request, obj):
        obj.delete()
        category_nums = Category.objects.count()
        count_nums = Counts.objects.get(id=1)
        count_nums.category_nums = category_nums
        count_nums.save()


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']

    def save_model(self, request, obj, form, change):
        obj.save()
        tag_nums = Tag.objects.count()
        count_nums = Counts.objects.get(id=1)
        count_nums.tag_nums = tag_nums
        count_nums.save()

    def delete_model(self, request, obj):
        obj.delete()
        tag_nums = Tag.objects.count()
        count_nums = Counts.objects.get(id=1)
        count_nums.tag_nums = tag_nums
        count_nums.save()


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'blog', 'content', 'create_time']


class CountsAdmin(admin.ModelAdmin):
    list_display = ['blog_nums', 'category_nums', 'tag_nums', 'visit_nums']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Counts, CountsAdmin)