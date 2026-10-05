# Playwright POM Framework

JavaScript end-to-end tests built with Playwright Test and the Page Object Model. Chromium is the default browser project.

## Requirements

- Node.js 20 or newer
- npm

## Setup

```powershell
npm ci
npx playwright install chromium
```

## Run Tests

```powershell
npm test
npm run test:chromium
npm run test:headed
npm run test:ui
npm run test:debug
```

The default target is `https://the-internet.herokuapp.com`. Override the target and demo credentials with environment variables when running against another environment:

```powershell
$env:BASE_URL = 'https://your-test-host.example'
$env:TEST_USERNAME = 'test-user'
$env:TEST_PASSWORD = 'test-password'
npm test
```

Use your CI secret store for credentials outside this public demo application. Do not commit real credentials or `.env` files.

## Reports and Artifacts

Playwright writes HTML reports to `playwright-report/` and failure diagnostics to `test-results/`. View the latest HTML report with:

```powershell
npm run test:report
```

Screenshots and videos are retained for failed tests. Traces are recorded on the first retry in CI.

## Structure

```text
PLAYWRIGHTPOM/
├── .github/workflows/       # CI workflow
├── fixtures/                # Shared Playwright test fixtures
├── pages/                   # Page Object Model classes
├── test-data/               # Non-secret test data and env overrides
├── tests/                   # Test specs
├── utils/                   # Shared environment/configuration helpers
├── playwright.config.js     # Runner, browser, timeout, and reporter config
└── package.json              # Scripts and dependencies
```

## Conventions

- Use role, label, or test-id locators where available; keep selectors and page interactions in page objects.
- Keep assertions in tests so each test states the behavior it verifies.
- Use the shared fixtures from `fixtures/test.fixture.js` when a test needs a page object.
- Keep tests independent and avoid depending on execution order or shared browser state.
- CI sets `CI=true`, rejects focused tests, enables retries, and emits GitHub annotations plus an HTML report.