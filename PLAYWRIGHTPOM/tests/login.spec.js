const { test, expect } = require('../fixtures/test.fixture');
const { validUser, invalidUsername } = require('../test-data/users');

test.describe('Login', () => {
  test('valid username and valid password', async ({ page, loginPage, homePage }) => {
    await loginPage.open();
    await loginPage.login(validUser.username, validUser.password);

    await expect(homePage.heading).toBeVisible();
    await expect(loginPage.flashMessage).toContainText('You logged into a secure area!');
    await expect(page).toHaveURL(/\/secure$/);
  });

  test('invalid username and valid password', async ({ loginPage }) => {
    await loginPage.open();
    await loginPage.login(invalidUsername, validUser.password);

    await expect(loginPage.flashMessage).toContainText('Your username is invalid!');
  });

  test('valid username and invalid password', async ({ loginPage }) => {
    await loginPage.open();
    await loginPage.login(validUser.username, 'wrong-password');

    await expect(loginPage.flashMessage).toContainText('Your password is invalid!');
  });

  test('empty username', async ({ loginPage }) => {
    await loginPage.open();
    await loginPage.login('', validUser.password);

    await expect(loginPage.flashMessage).toContainText('Your username is invalid!');
  });

  test('empty password', async ({ loginPage }) => {
    await loginPage.open();
    await loginPage.login(validUser.username, '');

    await expect(loginPage.flashMessage).toContainText('Your password is invalid!');
  });
});