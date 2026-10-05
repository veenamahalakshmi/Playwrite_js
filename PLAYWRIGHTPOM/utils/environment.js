const DEFAULT_BASE_URL = 'https://the-internet.herokuapp.com';

function getBaseUrl() {
  const baseUrl = process.env.BASE_URL || DEFAULT_BASE_URL;

  try {
    return new URL(baseUrl).toString().replace(/\/$/, '');
  } catch {
    throw new Error(`BASE_URL must be an absolute URL. Received: ${baseUrl}`);
  }
}

module.exports = { getBaseUrl };