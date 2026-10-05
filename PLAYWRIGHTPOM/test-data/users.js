const validUser = {
  username: process.env.TEST_USERNAME || 'tomsmith',
  password: process.env.TEST_PASSWORD || 'SuperSecretPassword!',
};

const invalidUsername = 'not-a-user';

module.exports = {
  validUser,
  invalidUsername,
};