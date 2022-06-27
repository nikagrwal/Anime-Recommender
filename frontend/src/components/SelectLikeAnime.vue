<template>
  <div>
    <div class="name">
      <h4>Hello {{ user }}</h4>
      <div class="header">Please select 3 animes that you like:</div>

      <MultiSelect
        v-model="selectedAnime"
        :options="animes"
        :selectionLimit="3"
        optionLabel="Name"
        placeholder="Select Animes"
        :filter="true"
        class="multiselect-custom"
      >
        <template #value="slotProps">
          {{ slotProps.data }}
          <div
            class="anime-item anime-item-value"
            v-for="option of slotProps.value"
            :key="option.ID"
          >
            <div>{{ option.Name }}</div>
          </div>
          <template v-if="!slotProps.value || slotProps.value.length === 0">
            Select Animes
          </template>
        </template>
        <template #option="slotProps">
          <div class="anime-item">
            <div>{{ slotProps.option.Name }}</div>
          </div>
        </template>
      </MultiSelect>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import Anime from "@/interface/Anime";

export default defineComponent({
  setup() {
    const router = useRouter();
    const selectedAnime = ref();

    const animes = ref<Anime[]>([]);
    const animeOption = async () => {
      const url = `http://localhost:3000/anime`;

      try {
        const { data } = await axios.get(url);
        animes.value = data;
      } catch (error: any) {
        console.error(error.response);
      }
    };

    const user = router.currentRoute.value.params.user;
    animeOption();
    return {
      user,
      animes,
      animeOption,
      selectedAnime,
    };
  },
});
</script>

<style>
.p-multiselect {
  width: 18rem;
}
.p-multiselect-label-container {
  color: black;
}
::v-deep(.multiselect-custom) {
  .p-multiselect-label:not(.p-placeholder) {
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
  }

  .anime-item-value {
    padding: 0.25rem 0.5rem;
    border-radius: 3px;
    display: inline-flex;
    margin-right: 0.5rem;
    background-color: black;
    color: white;
  }
}
.header {
  padding: 10px;
}
</style>
