class HomePage {
  constructor(page) {
    this.page = page;
    this.heading = page.getByRole('heading', { name: 'Secure Area', exact: true });
    this.logoutButton = page.getByRole('link', { name: 'Logout' });
  }

  async logout() {
    await this.logoutButton.click();
  }
}

module.exports = { HomePage };