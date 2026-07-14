<template>
  <v-card elevation="2" rounded="xl" class="border log-viewer-card" color="surface">
    <v-card-title class="d-flex align-center py-4 px-6 font-weight-bold">
      <span>实时运行日志</span>
      <v-spacer></v-spacer>
      <v-btn
        prepend-icon="mdi-refresh"
        variant="tonal"
        color="primary"
        rounded="pill"
        size="small"
        @click="fetchLogs"
      >
        刷新日志
      </v-btn>
    </v-card-title>
    
    <v-divider></v-divider>

    <v-card-text class="pa-0">
      <div class="log-content bg-black text-green-accent-3 pa-4 font-weight-medium" ref="logContainer">
        <pre>{{ logs }}</pre>
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

const logs = ref('')
const logContainer = ref<HTMLElement | null>(null)
let timer: any = null

const fetchLogs = async () => {
  try {
    const res = await axios.get('/api/logs')
    logs.value = res.data.logs || '暂无日志输出...'
    setTimeout(() => {
      if (logContainer.value) {
        logContainer.value.scrollTop = logContainer.value.scrollHeight
      }
    }, 100)
  } catch (e) {
    logs.value = '无法获取日志文件，请检查后端服务。'
  }
}

onMounted(() => {
  fetchLogs()
  timer = setInterval(fetchLogs, 3000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})
</script>

<style scoped>
.log-content {
  height: 60vh;
  overflow-y: auto;
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 14px;
  line-height: 1.6;
}
pre {
  margin: 0;
  white-space: pre-wrap;
}
</style>
