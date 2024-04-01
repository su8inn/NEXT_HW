from django.shortcuts import render
def count(request):
    return render(request,'count.html')

def result(request):
    text=request.POST["text"]
    total_len=len(text)
    
    words=text.split()
    wordsCount=len(words)
    
    return render(request,'result.html',{
        "text":text,
        "total_len":total_len,
        "wordsCount":wordsCount})

# Create your views here.