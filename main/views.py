from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'category' : 'jersey',
        'name' : 'Jersey Custom',
        'price' : 150000,
        'description' : 'Jersey Custom Nama dan Nomor Punggung. Terbuat dari bahan berkualitas tinggi dengan teknologi dry-fit untuk kenyamanan maksimal.',
        'thumbnail' : 'https://5.imimg.com/data5/SELLER/Default/2024/3/404714376/NM/AG/BO/14081053/football-uniforms.jpg',
        'is_featured' : True,
    }
    return render(request, 'main.html', context)