# shelterpaws
A system for animal shelters, providing an easy and free way for shelter owners to display their pets, help them find new homes, and fundraise.

- [board to work on](https://github.com/orgs/qase-tms/projects/5/views/1)
- [meta page](https://meta.shelterpaws.org)
- [website](https://shelterpaws.org)

## Режим разработки

Перед тем, как закоммитить изменения, необходимо установить зависимости:

```
yarn install
```

### Возможные проблемы

#### Found incompatible module.

Для успешной установки всех зависимостей желательно использовать **node >=18.12.0**. Для переключения между версиями node можно воспользоваться [nvm](https://github.com/nvm-sh/nvm).

#### fatal: cannot exec '.husky/pre-commit': No such file or directory

1. Скопировать содержимое файла `.husky/pre-commit`:

```
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

yarn precommit
```

2. Удалить файл `.husky/pre-commit`

3. Создать пустой `.husky/pre-commit` и вставить туда скопированный код.

4. Запустить команду `npx husky install`

5. Попробовать еще раз сделать коммит.

Если данная инструкция не решила проблему, можно обойти проверку, используя флаг `--no-verify`:

```
git commit -m 'commit name' --no-verify
```

Перед тем, как закоммитить изменения с флагом `--no-verify`, рекомендуется запустить проверки вручную и исправить ошибки, если они есть:

```
yarn stylelint
```
