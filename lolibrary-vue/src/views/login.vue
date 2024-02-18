<template>
    <label>欢迎来到管理页面，请进行登录！</label>
    <br>
    <label>账号：</label>
    <el-input :required="true" v-model="user" style="width: 30%;" clearable></el-input>
    <br>
    <label>密码：</label>
    <el-input :required="true"  type="password" v-model="password" style="width: 30%;" show-password clearable></el-input>
    <br>
    <button @click="login">登录</button>
    <br>
    {{ successful }}
</template>

<script lang="ts" setup>

import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const user=ref('')
const password=ref('')
const successful=ref('')
const router = useRouter();

async function login(){
  let res = await axios.post("http://localhost:8888/login",
    {
      user:user.value,
      password:password.value
    }
  )
  if (res.status == 200) {
    successful.value = res.data
    if(successful.value=="登录成功"){
      
    router.push('/Adminstration/'+user.value)
}
  }
}



</script>
