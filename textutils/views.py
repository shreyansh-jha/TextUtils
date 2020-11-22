# I have craeted this file - Shreyansh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br>
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which check box is on
    if removepunc == 'on':
        punctutations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctutations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctutations',
                  'analyaze_text': analyzed}
        djtext = analyzed

    if(fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyaze_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char

        params = {'purpose': 'Removed NewLines', 'analyaze_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed += char

        params = {'purpose': 'Removed NewLines', 'analyaze_text': analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'Charcount', 'analyaze_text': analyzed}

    if (removepunc != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and fullcaps != 'on' and charcount != 'on'):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)
