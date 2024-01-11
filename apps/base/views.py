from django.shortcuts import render
from apps.base.models import Settings
from apps.secondary.models import Begin,About,Category,Products, Offer,Reviews,Blog,Slide,About_page,Reviews_2,Blogs,Shops
from apps.menu import models
from apps.contact.models import Contact
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    return render(request, 'base/index-5.html', locals())

def about(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    about_page = About_page.objects.latest('id')
    reviews_2 = Reviews_2.objects.all()
    return render(request, 'about.html', locals())

def menu(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()

    # all products
    set_menu1 = models.SetFamily.objects.all()
    set_menu2 = models.SetCouple.objects.all()
    set_menu3 = models.SetIndivudal.objects.all()
    all_menu_products = list(set_menu1) + list(set_menu2) + list(set_menu3)
    # Fast Foot
    fast_food1 = models.FootPizza.objects.all()
    fast_food2 = models.FootBurger.objects.all()
    fast_food3 = models.FootPasta.objects.all()
    all_fast_food = list(fast_food1) + list(fast_food2) + list(fast_food3)
    # desert
    desert1 = models.DessertCake.objects.all()
    desert2 = models.DessertIceCream.objects.all()
    desert3 = models.DessertSnake.objects.all()
    all_deserts =  list(desert1) + list(desert2) + list(desert3)
    # Juise
    juice1 = models.JuiceCoffee.objects.all()
    juice2 = models.JuiceFruitJuice.objects.all()
    all_juice =  list(juice1) + list(juice2)
    return render(request, 'menu.html', locals())

def blogs(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    blogs2 = Blogs.objects.all()
    return render(request, 'blogs.html', locals())

def Shop(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    shop = Shops.objects.all()
    return render(request, 'shop.html', locals())

def Cart(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    return render(request, 'cart.html', locals())

def blog_details(request, id):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    blog2 = Blog.objects.get(id=id)
    return render(request, 'blog-details.html', locals())

def contact(request):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
        get_text(f"""
отправлен запрос на обратную связь 
                 
Имя {name}
Email {email}
Обьект {subject}
Сщщбщиение {message}
""")
    return render(request, 'contact.html', locals())

def shop_detail(request, id):
    setting = Settings.objects.latest('id')
    begin = Begin.objects.latest('id')
    about = About.objects.latest('id')
    categorys = Category.objects.all()
    products = Products.objects.all()
    offers = Offer.objects.all()
    reviews = Reviews.objects.all()
    blogs = Blog.objects.all()
    slides = Slide.objects.all()
    shop = Shops.objects.get(id=id)
    
    return render(request, 'blog-details.html', locals())