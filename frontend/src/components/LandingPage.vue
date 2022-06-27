<template>
  <div class="main">
    <h1>Please Enter Your Names:</h1>
    <div class="textinput">
      <div class="user">
        User 1:
        <InputText type="text" id="user1" v-model="formValues.user1" />
      </div>

      <div class="user">
        User 2:
        <InputText type="text" id="user2" v-model="formValues.user2" />
      </div>
    </div>
    <div>
      <ButtonComponent
        label="Continue"
        @click="step2(formValues)"
      ></ButtonComponent>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useCookies } from "@vueuse/integrations/useCookies";

export default defineComponent({
  setup() {
    const router = useRouter();
    const cookies = useCookies(["locale"]);

    const formValues = {
      user1: "",
      user2: "",
    };

    const step2 = async (formValues: any) => {
      cookies.set("user1", formValues.user1);
      cookies.set("user2", formValues.user2);
      console.log(cookies.getAll());

      router.push({
        name: "SelectContainer",
        params: { user: formValues.user1 },
      });
    };

    return { formValues, step2 };
  },
});
</script>

<style>
.p-inputtext {
  padding: 0.5rem;
}
.user {
  padding: 5px;
}
.textinput {
  padding: 30px;
}
.p-button {
  background-color: black;
  border: black;
  width: 25%;
}
.p-button:hover {
  background-color: black;
}
</style>
