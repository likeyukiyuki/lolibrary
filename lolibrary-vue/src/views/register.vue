<template>
  <label>欢迎来到注册页面，请进行注册！</label>
    <br>
    <label>账号：</label>
    <el-input :required="true" v-model="user" style="width: 30%;" clearable></el-input>
    <br>
    <label>密码：</label>
    <el-input :required="true"  type="password" v-model="password" style="width: 30%;" show-password clearable></el-input>
    <br>
    <button @click="register">点击注册</button>
    <Router-Link to="/user_login"><button>返回登录</button></Router-Link>
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

async function register(){
  let res = await axios.post("http://localhost:8888/register",
    {
      user:user.value,
      password:password.value
    }
  )
  if (res.status == 200) {
    successful.value = res.data
   

  }
}

</script>