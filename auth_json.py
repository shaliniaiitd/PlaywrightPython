#https://playwright.dev/python/docs/codegen
import pytest
import re
from playwright.sync_api import Page, expect

#loads auth details from auth.json.



def test_example(page: Page) -> None:
    page.goto("https://github.com/microsoft/playwright")
