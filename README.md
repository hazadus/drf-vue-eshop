# Django Rest API Framework + Vue 3 Eshop Project

Tutorial project to learn how to combine DRF API, Vue.js 3, Nginx and Node.

## Features

- User authentication - sign up, log in, log out.
- Product cart with checkout page (no real payment processing code, though, but it can be easily included).
- Markdown support in product descriptions.
- Powerful Django Admin panel can be used to easily create and modify products, categories, users, etc.
- You can easily get this app up and running on your own using step by step instructions below.

### ToDos

The project is in development right now, you can check which features I am planning to implement
in projects [Issues](https://github.com/hazadus/drf-vue-eshop/issues) section on GitHub. Any questions
or ideas are welcome!

## What I have learned while building this project

- Tried out Bulma.
- DRF can serialize output from `@property` or regular model methods as well as from model fields.
- Practised using [Vue Router](https://router.vuejs.org/):
  - [Watch and handle](https://router.vuejs.org/guide/essentials/dynamic-matching.html#reacting-to-params-changes) route changed when the route view is reused (e.g. in `CategoryDetailView`).
  - Using [Named routes](https://router.vuejs.org/guide/essentials/named-routes.html#named-routes) (e.g. `<router-link :to="{ name: 'AboutView' }" class="is-link">` instead of hardcoding link to the view).
  - [Lazy loading routes](https://router.vuejs.org/guide/advanced/lazy-loading.html) (e.g. `component: () => import(/* webpackChunkName: "SignUpView" */ "../views/SignUpView.vue"),` ).
  - Marking routes as `requireLogin` using [Route Meta Fields](https://router.vuejs.org/guide/advanced/meta.html#route-meta-fields).
- How to use `bulma-toast`.
- How to properly set page titles for Vue views.
- Learned the difference between [Named import and Default import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#description) in JavaScript.
- How to authenticate via REST API using Djoser and Axios.
- Practiced using [Vuex](https://vuex.vuejs.org/guide/):
  - Using storage data in templates (e.g. `v-if="!$store.state.isAuthenticated"`).
  - "Watching" objects in store to reactively reflect changes in UI (see `cart` computed property in `App.vue`). Read more in [Vuex Docs](https://vuex.vuejs.org/guide/getters.html#the-mapgetters-helper) and [this answer](https://stackoverflow.com/a/43294294) on SO.
- How to solve regular problem when [PyCharm not recognizing Django project imports: from my_app.models import thing](https://stackoverflow.com/a/40934430).
- How to properly serialize `Order` with multiple `OrderItems` to correctly and **easily** process data from frontend on backend.
- How to configure Djoser to [use custom serializers](https://djoser.readthedocs.io/en/latest/settings.html?highlight=users%2Fme#serializers) for `/users/me/` endpoint. Unfortunately, I have failed to make this endpoint work with token auth, so decided to create my own endpoint `/user/details/`.
- [Properly setting dafaults](https://eslint.vuejs.org/rules/require-default-prop.html) for component props. Especially, for [Objects](https://eslint.vuejs.org/rules/require-valid-default-prop.html).


## References

### Videos

- [E-commerce Website With Django and Vue Tutorial (Django Rest Framework)](https://www.youtube.com/watch?v=Yg5zkd9nm6w)
  - Code for video above: [Backend](https://github.com/SteinOveHelset/djackets_django) / [Frontend](https://github.com/SteinOveHelset/djackets_vue).
- [Vue Router 4 for Everyone](https://vueschool.io/lessons/introduction-to-vue-router-4)

### Articles

- [ESLint and Prettier with Vite and Vue.js 3](https://vueschool.io/articles/vuejs-tutorials/eslint-and-prettier-with-vite-and-vue-js-3/)
- [How To Enable Linting on Save with Visual Studio Code and ESLint](https://www.digitalocean.com/community/tutorials/workflow-auto-eslinting)

## Tech stack used

### Frameworks and libraries

- Backend: [Django](https://www.djangoproject.com/)
  - [Django REST Framework](https://www.django-rest-framework.org/): REST API on the backend was built using this battle-tested framework. It's powerful, well-documented and easy to use.
  - [djoser](https://djoser.readthedocs.io/en/latest/introduction.html): REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation.
- Frontend: [Vue.js 3](https://vuejs.org/)
  - [Axios](https://www.npmjs.com/package/axios): Promise based HTTP client for the browser and node.js
  - [Bulma](https://www.npmjs.com/package/bulma): [Bulma](https://bulma.io/) is a modern CSS framework based on Flexbox.
    - [bulma-toast](https://www.npmjs.com/package/bulma-toast): Bulma's pure JavaScript extension to display toasts. Basically a Bulma's notification implemented as a toast plugin.
  - [Marked.js](https://marked.js.org/): a low-level markdown compiler for parsing markdown without caching or blocking for long periods of time.
  - [DOMPurify](https://github.com/cure53/DOMPurify): a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG.
  - [Font Awesome](https://fontawesome.com/docs/web/use-with/vue/add-icons): Cool free [icons library](https://fontawesome.com/icons).

### Dev Tools used

- Python
  - [black](https://pypi.org/project/black/): Black is the uncompromising Python code formatter.
  - [flake8](https://pypi.org/project/flake8/): Python code linter.
  - [isort](https://pycqa.github.io/isort/): isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
  - [interrogate](https://interrogate.readthedocs.io/en/latest/): `interrogate` checks your code base for missing docstrings.
- JavaScript
  - [ESlint](https://eslint.org/): ESLint statically analyzes your code to quickly find problems.
    - [eslint-plugin-vue](https://eslint.vuejs.org): Official ESLint plugin for Vue.js.
  - [Prettier](https://prettier.io/) [VSCode plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Your code is formatted on save. Prettier is an opinionated code formatter. It enforces a consistent style by parsing your code and re-printing it with its own rules that take the maximum line length into account, wrapping code when necessary.

## How to start the project

The project consists of two parts - backend and frontend, and you need to run them simultaneously.

First of all you have to clone the repository to your local directory:

```bash
git clone https://github.com/hazadus/drf-vue-eshop
```

### Start in Development mode

In first shell window, create Python virtual environment for backend and install project dependencies:

```bash
cd ./drf-vue-eshop/backend/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then, create `.env` file using `touch ./.env` shell command, say `nano ./.env` and fill inn the necessary
environment variables:

| Variable     | Description                                                              |
|--------------|--------------------------------------------------------------------------|
| SECRET_KEY   | Standard Django secret key string. See below how to easily generate one. |
| DEBUG        | `True` since we are in development mode.                                 |
| FRONTEND_URL | `http://127.0.0.1:8080` by default.                                      |
| BACKEND_URL  | `http://127.0.0.1:8000` by default.                                      |

To create random `SECRET_KEY`, open Django `shell` with following commands and then execute the code below:

```bash
source .venv/bin/activate
python -m manage shell
```
```python
# Inside the shell:
import secrets
print(secrets.token_urlsafe())
# It will print something like:
# U9d7Aqac7Feo8dUyy-I4A1ppAGbwj4PUmrd8_uPSu9g
# Copy it and use as your SECRET_KEY.
```

Now we are ready to migrate the database, create admin user account, and start the server:

```bash
python -m manage migrate
python -m manage createsuperuser
python -m manage runserver
```

In second shell window, run the frontend development server:

```bash
cd ../frontend
npm run serve
```

Visit `http://127.0.0.1:8080` in your browser to see the working project.
Django admin panel is available at `http://127.0.0.1:8000/admin/`.
