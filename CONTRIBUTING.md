# Team Moon-glE Contributing Guidelines

Please follow these guidelines when you are trying to contribute to **My Community** software.

## Language

We **_prefer English and Korean_** due to all of our team member is Korean, we prefer Korean. So it is strongly recommended to use Korean. But it needs to conversate in globally, we also prefer the English.

## Code Formatting

Keep your codes clean and consistent using code formatters and linters. Most of the time formatting and linting would already have been set by default in each repository. And sometimes you should use the specific code editor to match the configuration.

## Git commit messages

Generally there are two acceptable styles of commit message.

### commit type: what you did in present-tense, imperative-style

Refer to [here](http://karma-runner.github.io/0.10/dev/git-commit-msg.html) and [here](https://seesparkbox.com/foundry/semantic_commit_messages) for more information.

**Available types**

- chore (updating grunt tasks etc; no production code change)
- docs (changes to documentation)
- feat (new feature)
- fix (bug fix)
- refactor (refactoring production code)
- test (adding missing tests, refactoring tests; no production code change)

**Examples**

- `chore: Add Oyster build script`
- `docs: Explain hat wobble`
- `feat: Add beta sequence`
- `fix: Remove broken confirmation message`
- `refactor: Share logic between 4d3d3d3 and flarhgunnstow`
- `test: Ensure Tayne retains clothing`

> You can also use other types like `misc:`, `design:`, `types:`, `deps:` or whatever that fit well with your works.

### Start with a present-tense verb in imperative-style with a first character in uppercase

**Examples**

- `chore : Update README.md`
- `feat: Add assets`

## Pull Requests
- There are 2 types of _PULL_REQUEST_TEMPLATE_, **feature-template** and **bug-template**
- Follow our _Pull request template_ **STRICTLY** when you hang out the pull request
- **feature-template**
- `Function description`
- `Code description`
- **bug-template**
- `Bug description`
- `Root cause`
- `Solution description`
- After release, this _guide_ and _PULL_REQUEST_TEMPLATE_ will be editted for release version

## Versioning

We are following the [SemVer](https://semver.org/) but in a much simpler and restricted way.

### Backwards Compatible

It means that your code written on a new version should run on the previous backwards compatible versions without any modification.

### x.y.Z (Patch version)

- Fix backwards compatible bugs

### x.Y.z (Minor version)

- Introduce new backwards compatible functionality
- Deprecate functionality

### X.y.z (Major version)

- Introduce any backwards incompatible changes

### Pre-release version

In a form of `x.y.z-keyword.n`

**Examples**

- `1.0.0-alpha.1`
- `2.0.0-beta.3`
