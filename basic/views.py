from django.http.request import HttpRequest
from django.shortcuts import render
from .models import Product

# Create your views here.
def wellcome_page(request:HttpRequest):
    #Burada bir takim işler yapılıyor:
    harfler = ['A','B','C']

    calisanlar = []
    turkay = Calisan("Türkay Ürkmez",41)    
    calisanlar.append(turkay)
    calisanlar.append(Calisan("Oğuzhan Paçal",34))
    calisanlar.append(Calisan("Caner Uçal",29))
    calisanlar.append(Calisan('Furkan Er',28))

    products = Product.objects.all()
    



    return render(request,'index.html',{'harfler':harfler,
                                        'personel':calisanlar,
                                        'products':products})

def product_detail(request:HttpRequest):
    requested_id = request.GET.get('id')
    product : Product = Product.objects.get(id=requested_id)
    
    return render(request,'urundetay.html',{'urun':product})







class Calisan():
    def __init__(self, name:str,age:int):
        self.ad = name
        self.yas = age
    
