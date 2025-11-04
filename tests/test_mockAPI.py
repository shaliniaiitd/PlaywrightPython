from playwright.sync_api import sync_playwright


def test_mock_and_trace():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Start tracing
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        # Mock API route
        def handle_route(route):
            print("Intercepted:", route.request.url)
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"message": "Mocked response from Playwright!"}'
            )

        page.route("**/api/data", handle_route)

        # Go to a simple page that triggers the call
        page.goto("https://httpbin.org/html")
        # Trigger the mocked API call manually
        page.evaluate("fetch('/api/data').then(r => r.json()).then(console.log)")

        # Stop tracing and save file
        context.tracing.stop(path="trace.zip")

        browser.close()
