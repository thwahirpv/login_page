from django.shortcuts import render

# Create your views here.

def list_view(requast):
    movies_list = {
        'movies' : [
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
            {
                'title': 'Leo',
                'year': '2023',
                'rate': '10/10'
            },
            {
                'title': 'King of Kotha',
                'year': '2023',
                'rate': '6/10'
            },
            {
                'title': 'veeran',
                'year': '2023',
                'rate': '7/10'
            },
            {
                'title': 'avengers',
                'year': '2021',
                'rate': '10/10'
            },
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
            {
                'title': 'RDX',
                'year': '2023',
                'rate': '9/10'
            },
        ]
    }
    return render(requast, 'list.html', movies_list)


def card(requast):
    return render(requast, 'card.html')
