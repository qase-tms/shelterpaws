---
title: "Contributors How-To"
---

# Why Contribute

1. If you are a beginner programmer, participating in an open-source project is an excellent way to gain real-world development experience, not just academic knowledge. You not only learn to write code that goes into production but also acquire essential teamwork skills and experience with Git and GitHub. Open-source experience is a valuable addition to your resume.

2. By participating in this specific project, you are helping real animals and the people who care for them. It's hard work. Typically, animals enter shelters in difficult conditions—sick, hungry, having experienced cruelty and mistreatment. They need food, medication, care, and new homes. Your participation will help make their lives better and the world kinder.

# How to Contribute

Work on the project is carried out solely based on issues. Before starting to write code, you need to:

- Familiarize yourself with the [list of issues](https://github.com/qase-tms/shelterpaws/issues) in this repository, choose one (!) task, and assign yourself as the executor. Tasks suitable for beginners are labeled as `goodfirstissue`.
- In the comments of the issue, briefly describe the proposed solution and obtain confirmation.
- Fork the repository.
- Clone the repository: `git clone https://github.com/qase-tms/shelterpaws/`

Please note that we use [Trunk-Based Development (TBD)](https://trunkbaseddevelopment.com), so all work on the Shelterpaws system is done in the `main` branch.

- Changes to the project are made in the form of separate branches, following the principle of "one change - one branch - one task."
- Branch names follow the template:

  ```plaintext
  feat/what-was-done/issue-number
  ```

For example:

```plaintext
feat/nav-menu/#12
```

- Commit rules: We follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) and use the following types: `feat:`, `fix:`, `chore:`, `style:`, `refactor:`, `perf:`.

  - `feat:` - adding new functionality
  - `fix:` - fixing a bug
  - `style:` - changes in code formatting that do not affect its implementation (e.g., variable renaming)
  - `refactor:` - changes in code implementation
  - `perf:` - changes that improve code performance (e.g., optimizing algorithm performance)
  - `chore:` - changes not falling into the categories listed above

  For example:

```plaintext
git commit -m "feat: add navigation menu"
```

**See also:**

- [How to Write Better Git Commit Messages – A Step-By-Step Guide](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/)
- [How to Write a Git Commit Message](https://cbea.ms/git-commit/)

- Commit and [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

# Code Style

The code style agreement is enforced using a linter. It is necessary to address not only errors but also warnings.
