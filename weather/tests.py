from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from requests import Response


class MainPageTestCase(TestCase):
    def _check_response(
        self, page: str, equal: bool = True, query_params: dict = None
    ) -> Response:
        response = self.client.get(reverse(page), data=query_params)
        if equal:
            self.assertEqual(response.status_code, HTTPStatus.OK)
        else:
            self.assertNotEqual(response.status_code, HTTPStatus.OK)
        return response

    def test_main_page(self):
        response = self._check_response(page="main_page")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_weather_now_with_search(self):
        response = self._check_response(
            page="weather_now", query_params={"search": "Казань"}
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_weather_now_with_search_empty(self):
        response = self._check_response(
            page="weather_now", equal=False, query_params={"search": ""}
        )
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    def test_weather_forecast_with_search(self):
        response = self._check_response(
            page="weather_forecast", query_params={"search": "Kazan"}
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_weather_forecast_with_search_empty(self):
        response = self._check_response(
            page="weather_forecast", equal=False, query_params={"search": ""}
        )
        self.assertNotEqual(response.status_code, HTTPStatus.OK)
