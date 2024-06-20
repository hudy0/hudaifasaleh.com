# import pytest

from django_blog.accounts.tests.factories import UserFactory


# @pytest.mark.django_db
class TestUser:
    def test_factory(self):
        """The factory produces a valid instance."""
        user = UserFactory()

        assert user is not None
