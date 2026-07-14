<template>
  <v-app>
    <!-- 侧边栏 Navigation Drawer -->
    <v-navigation-drawer v-model="drawer" :rail="rail" permanent @click="rail = false" color="surface">
      <v-list-item
        prepend-icon="mdi-flare"
        title="火花助手"
        nav
      >
        <template v-slot:append>
          <v-btn
            icon="mdi-chevron-left"
            variant="text"
            @click.stop="rail = !rail"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item prepend-icon="mdi-account-group" title="客户管理" value="dashboard" to="/" color="primary" rounded="pill"></v-list-item>
        <v-list-item prepend-icon="mdi-text-box-search-outline" title="运行日志" value="logs" to="/logs" color="primary" rounded="pill"></v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- 顶栏 App Bar -->
    <v-app-bar color="background" elevation="0">
      <template v-slot:prepend>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" v-if="!$vuetify.display.mdAndUp"></v-app-bar-nav-icon>
      </template>
      <v-app-bar-title class="font-weight-medium">抖音自动续火花 - Web 控制台</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn icon="mdi-theme-light-dark" @click="toggleTheme" variant="text"></v-btn>
    </v-app-bar>

    <!-- 主内容区 Main -->
    <v-main class="bg-background">
      <v-container fluid class="pa-6">
        <v-fade-transition mode="out-in">
          <router-view />
        </v-fade-transition>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useTheme } from 'vuetify'

const drawer = ref(true)
const rail = ref(false)

const theme = useTheme()
const toggleTheme = () => {
  theme.global.name.value = theme.global.current.value.dark ? 'light' : 'dark'
}
</script>

<style>
body {
  margin: 0;
  font-family: 'Inter', sans-serif;
}
</style>
