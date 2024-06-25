from django.urls import reverse


class TestIndex:
    def test_unauthenticated(self, client):
        """An unauthenticated user gets a valid response."""
        response = client.get(reverse("index"))
        assert response.status_code == 200


class TestTerms:
    def test_terms(self, client):
        """Test, The terms of service page of the application."""
        response = client.get(reverse("terms"))
        assert response.status_code == 200


class TestPrivacy:
    def test_privacy(self, client):
        """Test, The privacy of service page of the application."""
        response = client.get(reverse("privacy"))
        assert response.status_code == 200
