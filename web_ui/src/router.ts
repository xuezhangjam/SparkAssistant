import { createRouter, createWebHashHistory } from 'vue-router'
import Dashboard from './components/Dashboard.vue'
import LogViewer from './components/LogViewer.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/logs', component: LogViewer }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
