# Playwright JavaScript Assignment

This project contains the JavaScript Playwright tests for the assignment tasks in the screenshots.

## Run tests

```bash
npm install
npx playwright install chromium
npm test
npm run test:chromium
npm run test:headed
npm run test:ui
```

The Assignment 5 sign-in smoke test can run without an account. The complete
purchase journey needs an Urban Ladder account and is skipped unless
`URBAN_LADDER_EMAIL` and `URBAN_LADDER_PASSWORD` are set in the environment.
Do not commit account credentials to this project.

## Included specs

- `tests/example.spec.js` — assignment 1 example smoke test
- `tests/assignment-2.spec.js` — successful login flow
- `tests/assignment-5.spec.js` — end-to-end Urban Ladder product purchase flow
