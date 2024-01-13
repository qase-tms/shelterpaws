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

Если при попытке закоммитить изменения появляется эта ошибка, можно обойти проверку, используя флаг `--no-verify`:

```
git commit -m 'commit name' --no-verify
```

Перед тем, как запушить изменения, рекомендуется запустить проверку вручную и исправить ошибки, если они есть:

```
yarn stylelint
```
