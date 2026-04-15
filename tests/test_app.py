import unittest

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_homepage_renders_updated_greeting(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("Hello<span>.</span>World", body)
        self.assertIn("Flask application up and running", body)

    def test_health_endpoint(self):
        response = self.client.get("/api/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"status": "healthy", "message": "Service is running"},
        )

    def test_info_endpoint(self):
        response = self.client.get("/api/info")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {
                "name": "ayoung-test",
                "version": "1.0.0",
                "description": "A Flask application",
            },
        )


if __name__ == "__main__":
    unittest.main()
