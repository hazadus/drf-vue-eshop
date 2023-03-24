# Django Rest API Framework + Vue 3 Eshop Project

Tutorial project to learn how to combine DRF API, Vue.js 3, Nginx and Node.

## What I have lerned from this tutorial

- Tried out Bulma.
- DRF can serialize output from `@property` or regular model methods as well as from model fields.
- How to use [Vue Router](https://router.vuejs.org/).
- How to use [Vuex](https://vuex.vuejs.org/guide/).
- How to use `bulma-toast`.

## References

### Videos

- [E-commerce Website With Django and Vue Tutorial (Django Rest Framework)](https://www.youtube.com/watch?v=Yg5zkd9nm6w)
- Code for video above: [Backend](https://github.com/SteinOveHelset/djackets_django) / [Frontend](https://github.com/SteinOveHelset/djackets_vue).
- [Vue Router 4 for Everyone](https://vueschool.io/lessons/introduction-to-vue-router-4)

### Articles

- [ESLint and Prettier with Vite and Vue.js 3](https://vueschool.io/articles/vuejs-tutorials/eslint-and-prettier-with-vite-and-vue-js-3/)
- [How To Enable Linting on Save with Visual Studio Code and ESLint](https://www.digitalocean.com/community/tutorials/workflow-auto-eslinting)

## Tech stack used

- [Django](https://www.djangoproject.com/)
  - [Django REST Framework](https://www.django-rest-framework.org/)
  - [djoser](https://djoser.readthedocs.io/en/latest/introduction.html): REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation.
- [Vue.js 3](https://vuejs.org/)
  - [Axios](https://www.npmjs.com/package/axios): Promise based HTTP client for the browser and node.js
  - [Bulma](https://www.npmjs.com/package/bulma): [Bulma](https://bulma.io/) is a modern CSS framework based on Flexbox.
    - [bulma-toast](https://www.npmjs.com/package/bulma-toast): Bulma's pure JavaScript extension to display toasts. Basically a Bulma's notification implemented as a toast plugin.
  - [Marked.js](https://marked.js.org/): a low-level markdown compiler for parsing markdown without caching or blocking for long periods of time.
  - [DOMPurify](https://github.com/cure53/DOMPurify): a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG.
  - [Font Awesome](https://fontawesome.com/docs/web/use-with/vue/add-icons): Cool free [icons library](https://fontawesome.com/icons).

## Dev Tools used

- Python
  - [black](https://pypi.org/project/black/): Black is the uncompromising Python code formatter.
  - [flake8](https://pypi.org/project/flake8/): Python code linter.
  - [isort](https://pycqa.github.io/isort/): isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
  - [interrogate](https://interrogate.readthedocs.io/en/latest/): `interrogate` checks your code base for missing docstrings.
- JavaScript
  - [ESlint](https://eslint.org/): ESLint statically analyzes your code to quickly find problems.
  - [Prettier](https://prettier.io/) [VSCode plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Your code is formatted on save. Prettier is an opinionated code formatter. It enforces a consistent style by parsing your code and re-printing it with its own rules that take the maximum line length into account, wrapping code when necessary.