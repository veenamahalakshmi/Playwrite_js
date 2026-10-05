const base = require('@playwright/test');
const { HomePage } = require('../pages/home.page');
const { LoginPage } = require('../pages/login.page');

const test = base.test.extend({
  homePage: async ({ page }, use) => {
    await use(new HomePage(page));
  },
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page));
  },
});

module.exports = {
  test,
  expect: base.expect,
};