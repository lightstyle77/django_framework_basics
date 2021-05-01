from django.shortcuts import render

def main(request):
    context = {
        'slogan': 'Супер УДОБНЫЕ СТУЛЬЯ',
        'topic': 'Тренды'
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')
