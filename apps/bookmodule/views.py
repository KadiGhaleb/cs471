from django.shortcuts import render, redirect

def index(request):
    return render(request, 'bookmodule/index.html') #it will be in template folder

def books(request):
    u = request.user #the requesting user's info
    #return redirect('/') #here is redirection to the root "it will go back to urls and to the index"
    return render(request, 'bookmodule/booklist.html') #(request, template)

def book(request, bId):
    book1 = {'id':12344321, 'title': 'Continuous Delivery', 'author': 'by J. Humble and D. Farley'}
    book2 = {'id':56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author':'by E. Eilam'}

    targetBook = None

    if book1['id'] == bId: targetBook = book1
    if book2['id'] == bId: targetBook = book2
    
    if targetBook == None:
        return redirect('/books')
    
    context = {'book':targetBook} #book is the variable name accessible by template
    return render(request, 'bookmodule/book.html', context)