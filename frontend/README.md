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
Результат компиляции располагается в папке /testing/.
Базовая директория live server: `testing`. Путь к нужному файлу строим от неё.
Пример: `http://localhost:3000/index/index.html`

Требования:

- Именования классов согласно БЭМ
- Классы модификаторы имеют вид `.block--modifier`

Полезные ссылки:

- [Документация nunjucks](https://mozilla.github.io/nunjucks/templating.html) - шаблонизатор, который используется в сборке
- Для подсветки кода в `.njk` шаблонах можно использовать [расширение для vscode](https://marketplace.visualstudio.com/items?itemName=ronnidc.nunjucks)

Примечания:
- Для успешной установки всех зависимостей желательно использовать **node >=18.12.0**. Для переключения между версиями node можно воспользоваться [nvm](https://github.com/nvm-sh/nvm).
