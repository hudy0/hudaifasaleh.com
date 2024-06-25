from django.urls import reverse


class TestIndex:
    def test_unauthenticated(self, client):
        """An unauthenticated user gets a valid response."""
        response = client.get(reverse("core:index"))
        assert response.status_code == 200


class TestTerms:
    def test_terms_of_service(self, client):
        """Test, The terms of service page of the application."""
        response = client.get(reverse("core:terms"))
        assert response.status_code == 200


class TestPrivacy:
    def test_terms_of_service(self, client):
        """Test, The privacy of service page of the application."""
        response = client.get(reverse("core:privacy"))
        assert response.status_code == 200
