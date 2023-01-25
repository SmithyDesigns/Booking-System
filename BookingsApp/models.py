from django.db import models


class Rental(models.Model):
    """
        Rental is a Django model representing a rental property.
        It has a name field, which is a CharField of maximum length 255.
        """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Reservation(models.Model):
    """
        Reservation is a Django model representing a reservation for a rental property.
        It has a ForeignKey field for the associated rental, check-in date and check-out date.
        When a Rental object is deleted, all of its associated Reservation objects will also be deleted.
        """
    # when a Rental object is deleted, all of its associated Reservation objects will also be deleted.
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()


