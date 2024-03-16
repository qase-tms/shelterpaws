# Frontend

[Макет дизайна](https://www.figma.com/file/vPsA8xRIe0BgYkYPDIt8gw/Shelterpaws?type=design&node-id=0-1&mode=design)

## Режим разработки

Перейти в директорию /frontend/ и установить зависимости:
```
$ cd frontent/
$ yarn install
```
Запустить сборку:
```
$ gulp
```
Live server автоматически запустится по адресу `http://localhost:3000/`.
Базовая директория live server: `testing`. Путь к нужному файлу строим от неё.
Пример: `http://localhost:3000/index/index.html`

### Пути к изображениям

- Для scss используется переменная `$img-path`. Например: `background-image: url('#{$img-path}/test.webp')`
- Путь к изображению из `.njk` шаблона: `/img/**/*.png`; Например: `<img src="/img/test.webp" />` или `<img src="/upload/test.webp" />`

### Требования:

- Именования классов согласно БЭМ
- Классы модификаторы имеют вид `.block--modifier`
- Адаптив от 320px
- Все изображения оптимизировать с помощью [tinypng](https://tinypng.com/)
- В директорию `/src/static/img/` помещать декоративные изображения, относящиеся к дизайну сайта
- В директорию `/src/static/upload/` помещать изображения, являющиеся контентом (фото животных, фото приютов и т.д.)

### Возможные проблемы

#### command not found: gulp

Gulp должен быть установлен глобально:

```
yarn add global gulp
```

### Полезные ссылки:

- [Документация nunjucks](https://mozilla.github.io/nunjucks/templating.html) - шаблонизатор, который используется в сборке
- Для подсветки кода в `.njk` шаблонах можно использовать [расширение для vscode](https://marketplace.visualstudio.com/items?itemName=ronnidc.nunjucks)
