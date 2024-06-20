import factory


class UserFactory(factory.django.DjangoModelFactory):
    """
    The factory produce a valid instance.
    """

    class Meta:
        model = "accounts.User"
