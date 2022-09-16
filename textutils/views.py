from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    res_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    char_count = request.POST.get('char_count', 'off')

    
    if removepunc == 'on':
        analyzed = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for c in res_text:
            if c not in punctuations:
                analyzed += c
        
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        res_text = analyzed
        
    
    if fullcaps == 'on':
        analyzed = res_text.upper()
        params = {'purpose':'To UpperCase', 'analyzed_text':analyzed}
        res_text = analyzed
        

    if newlineremover == 'on':
        analyzed = ''
        for c in res_text:
            if c != '\n' and c != '\r':
                analyzed += c
        
        params = {'purpose':'New Line Removed', 'analyzed_text':analyzed}
        res_text = analyzed
        
    
    if extraspaceremover == 'on':
        analyzed = ""
        for idx, char in enumerate(res_text):
            if not (res_text[idx] == " "  and res_text[idx + 1] == " "):
                analyzed += char
        
        params = {'purpose':'Extra Space Removed', 'analyzed_text':analyzed}
        res_text = analyzed
        
    
    if char_count == 'on':
        analyzed = dict()
        for c in res_text:
            if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
                analyzed[c] = analyzed.get(c, 0) + 1
        
        params = {'purpose':'Character Count', 'analyzed_text':analyzed}
        

    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and char_count != 'on'):
        return HttpResponse("<h1>Error 404</h1>")
    return render(request, 'analyze.html', params)

