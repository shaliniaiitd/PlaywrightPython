from playwright.async_api import expect
from playwright.sync_api import sync_playwright, Route, Page


#
#
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#
#     # Start tracing
#     context.tracing.start(
#         screenshots=True,
#         snapshots=True,
#         sources=True
#     )
#
#     page = context.new_page()
#
#     # Mock API route
#     def handle_route(route):
#         print("Intercepted:", route.request.url)
#         route.fulfill(
#             status=200,
#             content_type="application/json",
#             body='{"message": "Mocked response from Playwright!"}'
#         )
#
#     page.route("**/api/data", handle_route)
#
#     # # Go to a simple page that triggers the call
#     # page.goto("https://httpbin.org/html")
#     # # Trigger the mocked API call manually
#     # page.evaluate("fetch('/api/data').then(r => r.json()).then(console.log)")
#
#     page.goto("https://httpbin.org/html")
#     page.evaluate("fetch('https://example.com/api/data')")
#
#     # Stop tracing and save file
#     context.tracing.stop(path="trace1.zip")
#
#     browser.close()
def test_mock_the_fruit_api(page: Page):
    def handle(route: Route):
        json = [{"name": "Strawberry", "id": 21}]
        # fulfill the route with the mock data
        route.fulfill(json=json)

    # Intercept the route to the fruit API
    page.route("*/**/api/v1/fruits", handle)

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    # Assert that the Strawberry fruit is visible
    expect(page.get_by_text("Strawberry")).to_be_visible()