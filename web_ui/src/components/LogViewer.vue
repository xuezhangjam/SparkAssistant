<template>
  <div class="log-viewer">
    <el-card shadow="hover" class="log-card">
      <template #header>
        <div class="card-header">
          <span>实时运行日志</span>
          <el-button size="small" type="primary" @click="fetchLogs" :icon="Refresh">刷新日志</el-button>
        </div>
      </template>
      <div class="log-content" ref="logContainer">
        <pre>{{ logs }}</pre>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'
import { Refresh } from '@element-plus/icons-vue'

const logs = ref('')
const logContainer = ref<HTMLElement | null>(null)
let timer: any = null

const fetchLogs = async () => {
  try {
    const res = await axios.get('/api/logs')
    logs.value = res.data.logs || '暂无日志输出...'
    // scroll to bottom
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
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.log-content {
  background-color: #1e1e1e;
  color: #00ff00;
  padding: 15px;
  border-radius: 4px;
  height: 60vh;
  overflow-y: auto;
  font-family: monospace;
  font-size: 13px;
  line-height: 1.5;
}
pre {
  margin: 0;
  white-space: pre-wrap;
}
</style>
