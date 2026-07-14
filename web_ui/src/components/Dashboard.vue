<template>
  <div class="dashboard">
    <div class="action-bar">
      <el-button type="primary" @click="runAll">
        <el-icon><VideoPlay /></el-icon> 批量自动续火花
      </el-button>
      <el-button type="success" @click="addClient">
        <el-icon><Plus /></el-icon> 添加新客户
      </el-button>
    </div>

    <el-card shadow="hover" class="client-card">
      <el-table :data="clients" style="width: 100%">
        <el-table-column prop="id" label="客户编号" width="120" />
        <el-table-column prop="name" label="备注名称" />
        <el-table-column prop="friends_count" label="火花数量" width="120" />
        <el-table-column label="操作" width="200" align="center">
          <template #default="scope">
            <el-button size="small" type="primary" plain @click="runSingle(scope.row)">运行</el-button>
            <el-button size="small" type="danger" plain @click="deleteClient(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'

const clients = ref<any[]>([])

const fetchClients = async () => {
  try {
    const res = await axios.get('/api/clients')
    clients.value = Object.keys(res.data).map(key => ({
      id: key,
      ...res.data[key]
    }))
  } catch (e) {
    ElMessage.error('无法获取客户数据')
  }
}

const addClient = () => {
  ElMessageBox.prompt('请输入客户编号(纯数字)', '添加客户', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
  }).then(async ({ value }) => {
    if (!value) return
    const current: any = {}
    clients.value.forEach(c => { current[c.id] = { name: c.name, friends_count: c.friends_count } })
    current[value] = { name: "新客户", friends_count: 5 }
    await axios.post('/api/clients', current)
    ElMessage.success('添加成功')
    fetchClients()
  })
}

const deleteClient = (row: any) => {
  ElMessageBox.confirm('确定要删除这个客户吗？', '警告', {
    type: 'warning'
  }).then(async () => {
    const current: any = {}
    clients.value.forEach(c => { 
      if (c.id !== row.id) current[c.id] = { name: c.name, friends_count: c.friends_count }
    })
    await axios.post('/api/clients', current)
    ElMessage.success('删除成功')
    fetchClients()
  })
}

const runAll = async () => {
  try {
    await axios.post('/api/run', {})
    ElMessage.success('任务已在后台启动！')
  } catch (e) {
    ElMessage.error('启动失败')
  }
}

const runSingle = async (row: any) => {
  try {
    await axios.post('/api/run', { cid: row.id })
    ElMessage.success(`开始处理客户: ${row.id}`)
  } catch (e) {
    ElMessage.error('启动失败')
  }
}

onMounted(() => {
  fetchClients()
})
</script>

<style scoped>
.action-bar {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}
.client-card {
  border-radius: 8px;
}
</style>
