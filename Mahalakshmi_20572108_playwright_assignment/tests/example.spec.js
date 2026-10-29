const { test, expect } = require('@playwright/test');

test.describe('Assignment 1 - Example Playwright test', () => {
  test('opens the practice login page and shows the login form', async ({ page }) => {
    await page.goto('https://practicetestautomation.com/practice-test-login/');

    await expect(page).toHaveTitle(/Practice Test Automation/);
    await expect(page.getByRole('textbox', { name: 'Username' })).toBeVisible();
    await expect(page.getByRole('textbox', { name: 'Password' })).toBeVisible();
    await expect(page.getByRole('button', { name: 'Submit' })).toBeVisible();
  });
});
