<script setup>
import { ref, computed } from 'vue'
const awesome = ref(true)
</script>

<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <!-- <el-text class="mx-1" type="primary" size="large">欢迎使用Lolita图书馆!</el-text> -->
       

        <el-menu :router="true" mode="horizontal" ellipsis="false">
          
          <el-image src="../public/images-list/lolita.jpg" style="width: 20%; height: 100%;"></el-image>
          <div style="width: 60%;"></div>
          <el-menu-item index="/Search">
            <span>查询</span>
          </el-menu-item>
          <el-menu-item index="/login">
            <span>管理</span>
          </el-menu-item>
          <el-menu-item index="/user_login">
            <span>用户界面</span>
          </el-menu-item>
        </el-menu>
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
