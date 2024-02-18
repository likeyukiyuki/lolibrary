<template>
<button @click="a">a</button>
</template>

<script lang="ts" setup>

import { reactive, ref, type Ref } from 'vue'
import type { FormProps, UploadFile, UploadFiles, UploadProps, UploadRawFile } from 'element-plus'
import { ElMessage, dateEquals } from 'element-plus'
import axios from 'axios';
import { Delete, Download, Plus, ZoomIn } from '@element-plus/icons-vue'
import {useRoute} from 'vue-router';

function a(){
  const route = useRoute()
  console.log(route)
  const id=route.params.user
  console.log(id)
}
</script>