<template>
  <div class="grid-content ep-bg-purple-light" />
  <el-alert title="欢迎来到管理员页面，请进行登录！" type="success" />
  <el-row :gutter="10">
    <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8">
      <div class="grid-content ep-bg-purple-light" />
    </el-col>
    <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12">

      <br>
      <label>账号：</label>
      <el-input :required="true" v-model="user" style="width: 30%;" clearable></el-input>
      <br>
      <label>密码：</label>
      <el-input :required="true" type="password" v-model="password" style="width: 30%;" show-password
        clearable></el-input>

      <br>
      <br>
      {{ successful }}
    </el-col>
  </el-row>
  <el-row>
    <el-col :xs="10" :sm="10" :md="10" :lg="10" :xl="10">
      <div class="grid-content ep-bg-purple-light" />
    </el-col>
    <el-button @click="login" type="primary">登录</el-button>

  </el-row>
</template>

<script lang="ts" setup>

import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const user = ref('')
const password = ref('')
const successful = ref('')
const router = useRouter();

async function login() {
  let res = await axios.post("http://localhost:8888/login",
    {
      user: user.value,
      password: password.value
    }
  )
  if (res.status == 200) {
    successful.value = res.data
    if (successful.value == "登录成功") {

      router.push({ path: 'Adminstration', query: { user: user.value } })
    }
  }
}



</script>
