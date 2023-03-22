import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

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
  .use(router)
  .mount("#app");
