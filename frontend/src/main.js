import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

// Add markdown as global
import { marked } from "marked";
import * as DOMPurify from "dompurify";

marked.setOptions({
  breaks: true,
});

// Can be accessed anywhere in the components as `this.markdown`, `this.sanitizeHtml`.
const markedMixin = {
  methods: {
    markdown: function (input) {
      // Return marked down & sanitized input as raw HTML
      return DOMPurify.sanitize(marked(input));
    },
    sanitizeHtml: function (input) {
      // Return sanitized input
      return DOMPurify.sanitize(input);
    },
  },
};

axios.defaults.baseURL = "http://127.0.0.1:8000";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* add some free icons */
import { faVuejs } from "@fortawesome/free-brands-svg-icons";
import { faCartShopping } from "@fortawesome/free-solid-svg-icons";

/* add icons to the library */
library.add(faVuejs, faCartShopping);

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(store)
  .use(router, axios)
  .mixin(markedMixin)
  .mount("#app");
