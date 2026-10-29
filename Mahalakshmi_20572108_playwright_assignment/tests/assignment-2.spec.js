const { test, expect } = require('@playwright/test');

test.describe('Assignment 2 - Successful login', () => {
  test('logs in with valid credentials and lands on the success page', async ({ page }) => {
    const username = 'student';
    const password = 'Password123';

    await page.goto('https://practicetestautomation.com/practice-test-login/');
    await page.locator('#username').fill(username);
    await page.locator('#password').fill(password);
    await page.getByRole('button', { name: 'Submit' }).click();

    await expect(page).toHaveURL(/logged-in-successfully/);
    await expect(page.getByText('Congratulations student. You successfully logged in!')).toBeVisible();
    await expect(page.getByRole('link', { name: 'Log out' })).toBeVisible();
  });
});
