<script setup>
import { ref, computed } from 'vue'
const awesome = ref(true)
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-row :gutter="10">
          <el-col :xs="4" :sm="4" :md="4" :lg="3" :xl="11">
            <el-image src="../public/images-list/lolita.jpg"></el-image>
          </el-col>
          <el-col :xs="10" :sm="14" :md="15" :lg="15" :xl="11">
            <div class="grid-content ep-bg-purple-light" />
          </el-col>
          <el-col :xs="10" :sm="6" :md="5" :lg="5" :xl="11">
            <div class="grid-content ep-bg-purple" />
            <el-menu :router="true" mode="horizontal" ellipsis="false" style="menu">
              <el-menu-item index="/Search">
                <span>查询</span>
              </el-menu-item>
              <el-menu-item index="/user_login">
                <span>用户</span>
              </el-menu-item>
              <el-menu-item index="/login">
                <span>管理</span>
              </el-menu-item>
            </el-menu>
          </el-col>

        </el-row>
      </el-header>

      <el-container>

        <!-- <router-link to="/Search"><button>点击查询</button></router-link>
          <router-link to="/Adminstration">管理</router-link>
          <router-view />
          <router-link to="/detail">detail</router-link>-->

        <el-main>

          <router-view></router-view>

        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
<style type="images">

</style>
<style>
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.el-image {
  width: 100%;
  height: 100%;
}
</style>
