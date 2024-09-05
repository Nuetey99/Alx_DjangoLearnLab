from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.permissions import IsAuthenticated
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Create a test book
        self.book = Book.objects.create(title='Test Book', publication_year=2024, author='Test Author')

        # Define the URLs for CRUD operations
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.book_update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.book_delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_create_book(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'New Book', 'publication_year': 2024, 'author': 'New Author'}
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Book'}
        response = self.client.put(self.book_update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should return one book

    def test_filter_books(self):
        response = self.client.get(f'{self.book_list_url}?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(f'{self.book_list_url}?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        response = self.client.get(f'{self.book_list_url}?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['title'] == 'Test Book')

    def test_permissions(self):
        # Test anonymous access
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test authenticated access for update and delete
        self.client.login(username='testuser', password='testpassword')
        response = self.client.put(self.book_update_url, {'title': 'Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Test unauthorized access
        self.client.logout()
        response = self.client.put(self.book_update_url, {'title': 'Unauthorized Update'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
