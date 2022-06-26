<template>
  <div class="main">
    <div class="h-screen flex align-items-center justify-content-center">
      <div
        class="surface-900 shadow-2 p-3 opacity-90 w-9 h-30rem border-round-2xl text-white text-2xl text-center"
      >
        <h1>Please Enter Your Names:</h1>
        <div class="textinput">
          <div class="user">
            User 1:
            <InputText type="text" id="user1" v-model="formValues.user1" />
          </div>

          <div class="user">
            User 2:
            <InputText type="text" id="user1" v-model="formValues.user2" />
          </div>
        </div>
        <div>
          <ButtonComponent label="Continue"></ButtonComponent>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const router = useRouter();
    const user1 = ref();

    const formValues = {
      user1: "",
      user2: "",
    };

    return { formValues, user1 };
  },
});
</script>

<style>
body {
  background-image: url("@/assets/background.jpeg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}
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
  color: black;
}
</style>
