# Frontend

[Design layout](https://www.figma.com/file/vPsA8xRIe0BgYkYPDIt8gw/Shelterpaws?type=design&node-id=0-1&mode=design)

### Preparing the dev mode

Change the directory to /frontend/ and install dependencies:

```
$ cd frontent/
$ yarn install
```

Run the build:
```
$ gulp
```
Live server will automatically start serving `http://localhost:3000/`.
Base live server directory is `testing`, your files will be there: `http://localhost:3000/index/index.html`

### Requirements:

- Use [BEM](https://getbem.com/naming/) class naming
- Class modifiers follow `.block--modifier` convention

### Possible issues:

#### command not found: gulp

Gulp must be installed globally:

```
yarn add global gulp
```

### Useful links:

- [nunjucks docs](https://mozilla.github.io/nunjucks/templating.html) - the templating engine we use , который используется в сборке
- for VS Code syntax highlighting in `.njk` we use [this extension](https://marketplace.visualstudio.com/items?itemName=ronnidc.nunjucks)
