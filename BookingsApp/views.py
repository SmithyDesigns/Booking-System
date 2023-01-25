from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Rental
from django import template
from .forms import RentalCreateForm, ReservationCreateForm


def home(request):
    """
        home function is a view function that renders the index.html template.
        it takes request as an argument and returns the rendered template.
        """
    return render(request, "index.html")


def reservation_list(request):
    """
        reservation_list function is a view function that renders the reservation_list.html template.
        it takes request as an argument, gets all the reservations, creates a context dictionary and
        appends reservations and their previous reservation to it. it returns the rendered template.
        """
    reservations = Reservation.objects.all()
    context = {
        'reservations': [],
    }

    for reservation in reservations:
        try:
            prev_obj = prev_reservation(reservation.rental.id)

            context['reservations'].append((reservation, prev_obj))

        except Reservation.DoesNotExist:
            reservation.prev_reservation_id = None

    return render(request, 'reservation_list.html', context)


def rental_create(request):
    """
        rental_create function is a view function that creates a new rental.
        it takes request as an argument, checks if it's a post request, creates a new rental from the form data
        and saves it in the database. it returns a redirect to the home page.
        """
    if request.method == 'POST':
        form = RentalCreateForm(request.POST)
        if form.is_valid():
            rental_name = request.POST['name']
            new_rental = Rental(name=rental_name)
            new_rental.save()
            return redirect('BookingsApp:Home')
    else:
        form = RentalCreateForm()
    return render(request, 'rental_create.html', {'form': form})


def reservation_edit(request, pk):
    """
        reservation_edit function is a view function that allows editing of a reservation.
        it takes request and pk as arguments, gets the reservation with the given pk, checks if it's a post request,
        edits the reservation with the form data, saves it in the database and returns a redirect to the reservation_list page.
        """
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReservationCreateForm(request.POST)
        if form.is_valid():
            reservation.checkin = form.cleaned_data['checkin']
            reservation.checkout = form.cleaned_data['checkout']
            reservation.rental = form.cleaned_data['rental']
            reservation.save()
            return redirect('BookingsApp:reservation_list')
    else:
        data = {'checkin': reservation.checkin, 'checkout': reservation.checkout, 'rental': reservation.rental}
        form = ReservationCreateForm(initial=data)
    return render(request, 'reservation_edit.html', {'form': form, 'reservation': reservation})


def reservation_delete(request, pk):
    """
        reservation_delete function is a view function that deletes a reservation.
        it takes request and pk as arguments, gets the reservation with the given pk, deletes it and returns a redirect to the reservation_list page.
        """
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('BookingsApp:reservation_list')


def reservation_create(request):
    """
        reservation_create function is a view function that creates a new reservation.
        it takes request as an argument, checks if it's a post request, creates a new reservation from the form data
        and saves it in the database. it returns a redirect to the reservation_list page.
        """
    if request.method == 'POST':
        form = ReservationCreateForm(request.POST)
        if form.is_valid():
            rental_pk = request.POST['rental']
            rental_object = get_object_or_404(Rental, pk=rental_pk)
            checkin = request.POST['checkin']
            checkout = request.POST['checkout']
            new_reservation = Reservation(rental=rental_object, checkin=checkin, checkout=checkout)
            new_reservation.save()
        return redirect('BookingsApp:reservation_list')

    form = ReservationCreateForm()
    return render(request, 'reservation_create.html', {'form': form})


register = template.Library()


@register.filter
def prev_reservation(pk):
    """
        prev_reservation is a filter function that returns the previous reservation of a rental.
        it takes pk as an argument and returns the previous reservation of a rental with the given pk.
        """
    try:
        prev_reserve = Reservation.objects.all().filter(rental_id=pk).values().first()
        return prev_reserve
    except Reservation.DoesNotExist:
        return None
