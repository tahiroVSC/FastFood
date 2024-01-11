from django.contrib import admin
from django.contrib.auth.models import User,Group

admin.site.unregister(User)
admin.site.unregister(Group)


from apps.base.models import Settings
from apps.secondary.models import Begin, About, Category,Products,Offer,Reviews,Blog,Slide,About_page,Reviews_2,Blogs,Shops
from apps.menu import models
from apps.contact.models import Contact

admin.site.register(Settings)
admin.site.register(Begin)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Offer)
admin.site.register(Reviews)
admin.site.register(Blog)
admin.site.register(Slide)
admin.site.register(About_page)
admin.site.register(Reviews_2)

admin.site.register(models.SetFamily)
admin.site.register(models.SetCouple)
admin.site.register(models.SetIndivudal)
admin.site.register(models.FootBurger)
admin.site.register(models.FootPasta)
admin.site.register(models.FootPizza)
admin.site.register(models.DessertCake)
admin.site.register(models.DessertIceCream)
admin.site.register(models.DessertSnake)
admin.site.register(models.JuiceCoffee)
admin.site.register(models.JuiceFruitJuice)
admin.site.register(Blogs)
admin.site.register(Shops)
admin.site.register(Contact)

