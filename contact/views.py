from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContactForm, QuoteForm, QuoteFormNew
# Create your views here.


class ContactView(View):
    template_name = 'contact/contact.html'

    def get(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Thanks you for Message! we reply to you very Soon.')
            # return redirect('contact:contact_index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            # messages.success(request, 'Thanks you for Message! we reply to you very Soon.')
            # return redirect('contact:contact_index')
        else:
            print("form Not Valid")
            # messages.success(request, 'Form Generic  View: Form Not valid')
            # return redirect('contact:contact_index')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def contact_form_view(request):
    template_name = 'contact/contact.html'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # messages.success(request, 'Thanks you for Message! we reply to you very Soon.')
        # return redirect('contact:contact_index')
    # else:
    #     print("form Not Valid")
    #     messages.success(request, 'Form Not valid')

    context = {
        'form': form
    }
    return render(request, template_name, context)


def quote_submit(request):
    print(request.POST)
    form = QuoteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(form.cleaned_data)
        print(request.POST.get('service'))
        return redirect('home:index')
    else:
        # print(form.errors)
        print(request.POST.get('service'))
        return redirect('home:index')


def quote_view(request):
    template_name = 'contact/quote.html'
    form = QuoteFormNew(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('contact:quote')
    context = {
        'form': form
    }
    return render(request, template_name, context)

