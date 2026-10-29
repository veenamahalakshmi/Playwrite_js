const { test, expect } = require('@playwright/test');

const baseUrl = 'https://www.urbanladder.com';
const email = process.env.URBAN_LADDER_EMAIL;
const password = process.env.URBAN_LADDER_PASSWORD;

test.describe('Assignment 5 - Urban Ladder purchase flow', () => {
  test('opens the real sign-in flow from the profile menu', async ({ page }) => {
    await page.goto(baseUrl, { waitUntil: 'domcontentloaded' });

    await page.locator('[data-testid="header-profile-icon"]').filter({ visible: true }).click();
    await page.getByRole('button', { name: 'SIGN IN' }).click();

    await expect(page).toHaveURL(/\/auth\/login/);
    await expect(page.getByRole('heading', { name: /Login \/ Sign Up/i })).toBeVisible();
    await expect(page.getByPlaceholder('Enter 10-digit Mobile Number')).toBeVisible();
  });

  test('logs in, sorts coffee tables by price, views a product, adds it to cart, and logs out', async ({ page }) => {
    test.skip(
      !email || !password,
      'Set URBAN_LADDER_EMAIL and URBAN_LADDER_PASSWORD to run this account-dependent journey.'
    );

    await page.goto(`${baseUrl}/auth/login`, { waitUntil: 'domcontentloaded' });
    await page.getByRole('button', { name: 'Login with Password' }).click();

    const emailInput = page.getByPlaceholder(/email/i).or(page.getByLabel(/email/i));
    const passwordInput = page.getByPlaceholder(/password/i).or(page.getByLabel(/password/i));
    await emailInput.fill(email);
    await passwordInput.fill(password);
    await page.getByRole('button', { name: /log in|sign in|continue/i }).click();

    await expect(page.locator('[data-testid="header-profile-icon"]')).toBeVisible();

    await page.goto(`${baseUrl}/collection/coffee-table`, { waitUntil: 'domcontentloaded' });
    await expect(page.getByRole('heading', { name: 'Coffee Table', exact: true })).toBeVisible();

    const sortControl = page.locator('[aria-label="Sort By filter"]').filter({ visible: true });
    await sortControl.click();
    await page.getByText(/Price\s*:?\s*High to Low/i).click();

    const firstProduct = page.getByTestId('plp-product-card').first();
    await expect(firstProduct).toBeVisible();
    const productName = firstProduct.locator('h2, h3').first();
    const expectedProductName = (await productName.innerText()).trim();
    await firstProduct.locator('a').first().click();

    await expect(page.getByRole('heading', { name: expectedProductName })).toBeVisible();
    await page.getByRole('button', { name: /add to cart|add to bag/i }).click();

    await page.locator('[data-testid="header-cart-icon"]').click();
    await expect(page.getByText(expectedProductName, { exact: false })).toBeVisible();

    await page.locator('[data-testid="header-profile-icon"]').filter({ visible: true }).click();
    await page.getByRole('button', { name: /log out|logout/i }).click();
    await expect(page).toHaveURL(/\/auth\/login|\/$/);
  });
});
