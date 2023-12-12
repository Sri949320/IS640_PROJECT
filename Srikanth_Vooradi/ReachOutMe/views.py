from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.utils import timezone

# This function displays the list of contacts.
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_time')
    current_year = timezone.now().year
    return render(request, 'contact_list.html', {'contacts': contacts, 'current_year': current_year})

# This function handles the creation of a new contact.
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.created_time = timezone.now()  # Set the created time here
            new_contact.save()  # Save the new contact to the database
            return redirect('contact_list')  # Redirect to the contact list view
    else:
        form = ContactForm()
    return render(request, 'contact_create.html', {'form': form})

# This function displays the detail of a contact.
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

# This function updates an existing contact.
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

# This function deletes a contact.
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_delete.html', {'contact': contact})
