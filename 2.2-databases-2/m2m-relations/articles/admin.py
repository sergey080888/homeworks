from django.contrib import admin
from .models import Article, Scope, Tag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count > 1:
            raise ValidationError('Только один основной')
        elif count == 0:
            raise ValidationError('Необходимо выбрать хотя бы один основной раздел')
        else:
            return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # inlines = [ScopeInline]
    pass
