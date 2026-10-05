const { test, expect } = require('../fixtures/test.fixture');
const { validUser } = require('../test-data/users');

test('user can log out after successful login', async ({ loginPage, homePage, page }) => {
  await loginPage.open();
  await loginPage.login(validUser.username, validUser.password);
  await expect(homePage.heading).toBeVisible();

  await homePage.logout();

  await expect(page).toHaveURL(/\/login$/);
  await expect(loginPage.flashMessage).toContainText('You logged out of the secure area!');
});