<template>
  <el-container class="layout-container">
    <el-aside width="200px" class="aside">
      <div class="logo">火花助手</div>
      <el-menu
        router
        :default-active="$route.path"
        background-color="#1e1e2d"
        text-color="#a2a3b7"
        active-text-color="#ffffff"
      >
        <el-menu-item index="/">
          <el-icon><Monitor /></el-icon>
          <span>客户管理</span>
        </el-menu-item>
        <el-menu-item index="/logs">
          <el-icon><Document /></el-icon>
          <span>运行日志</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    
    <el-container>
      <el-header class="header">
        <div class="header-content">
          <span>抖音自动续火花 - Web 控制台</span>
        </div>
      </el-header>
      <el-main class="main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<style>
body {
  margin: 0;
  font-family: 'Inter', sans-serif;
  background-color: #f5f8fa;
}

.layout-container {
  height: 100vh;
}

.aside {
  background-color: #1e1e2d;
  box-shadow: 2px 0 8px rgba(0,0,0,0.1);
}

.logo {
  height: 60px;
  line-height: 60px;
  text-align: center;
  color: #fff;
  font-size: 20px;
  font-weight: bold;
  background-color: #1a1a27;
  letter-spacing: 2px;
}

.header {
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  display: flex;
  align-items: center;
  padding: 0 20px;
}

.header-content {
  font-size: 18px;
  font-weight: 500;
  color: #3f4254;
}

.main {
  padding: 24px;
  background-color: #f5f8fa;
}

/* 覆盖 el-menu 边框 */
.el-menu {
  border-right: none !important;
}

.el-menu-item.is-active {
  background-color: #1b1b29 !important;
  border-left: 4px solid #3699ff;
}
</style>
