import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeflex/primeflex.css";
import "primeicons/primeicons.css";
import PrimeVue from "primevue/config";

import InputText from "primevue/inputtext";
import Button from "primevue/button";
import MultiSelect from "primevue/multiselect";
import Rating from "primevue/rating";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);
app.use(PrimeVue);
app.component("InputText", InputText);
app.component("ButtonComponent", Button);
app.component("MultiSelect", MultiSelect);
app.component("RatingComponent", Rating);
app.mount("#app");
