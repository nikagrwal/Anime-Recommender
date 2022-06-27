<template>
  <div class="h-screen flex align-items-center justify-content-center">
    <div
      class="surface-900 shadow-2 p-3 opacity-90 w-9 h-30rem border-round-2xl text-white text-2xl text-center"
    >
      <router-view></router-view>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {
    return;
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
</style>
