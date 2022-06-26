import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeflex/primeflex.css";
import "primeicons/primeicons.css";

import InputText from "primevue/inputtext";
import Button from "primevue/button";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);
app.component("InputText", InputText);
app.component("ButtonComponent", Button);
app.mount("#app");
