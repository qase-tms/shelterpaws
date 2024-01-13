# shelterpaws
A system for animal shelters, providing an easy and free way for shelter owners to display their pets, help them find new homes, and fundraise.

- [board to work on](https://github.com/orgs/qase-tms/projects/5/views/1)
- [meta page](https://meta.shelterpaws.org)
- [website](https://shelterpaws.org)

## Preparing the dev mode

Before committing changes, it is necessary to install dependencies:

```
npx husky-init && yarn install
```

### Possible Issues

#### Found incompatible module.

We support **node >=18.12.0**. To switch between node versions, use [nvm](https://github.com/nvm-sh/nvm).

#### fatal: cannot exec '.husky/pre-commit': No such file or directory

1. Remove `.husky/pre-commit` file

2. Create empty `.husky/pre-commit` and paste the following code into the file:

```
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

yarn precommit
```

3. Run `npx husky install`

5. Try committing once again.

If this instruction did not solve the problem, you can bypass the check using the `--no-verify` flag:

```
git commit -m 'commit name' --no-verify
```

Before committing changes with the `--no-verify` flag, it is recommended to run checks manually and fix errors if there are any:"

```
yarn stylelint
```
