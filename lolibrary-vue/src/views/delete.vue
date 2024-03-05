<template>
     <el-alert title="请谨慎进行删除！" type="error" effect="dark" />
     <br>
    <el-row>
        <el-col :xs="12" :sm="2" :md="2" :lg="5" :xl="1">
            <el-input v-model="name" placeholder="Please input name" />
        </el-col>
        <el-col :xs="2" :sm="12" :md="12" :lg="2" :xl="1">
            <el-button @click="name_search" type="primary">查询</el-button>
        </el-col>

    </el-row>
    <el-row>
        <el-col v-for="data in newdata " :key="data[1]" :offset="0.5" :xs="12" :sm="8" :md="6" :lg="5" :xl="1">
            <el-card shadow="always" class="card">
                <div style=" text-align: center;">{{ data[1] }}</div>
                <el-image :src="data[7]" class="image" />
                <el-row :gutter="2">
                    <el-col class="color" :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                        <div>brand</div>
                    </el-col>
                    <el-col class="color" :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                        <div>category</div>
                    </el-col>
                </el-row>
                <el-row :gutter="2">
                    <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                        <div>{{ data[3] }}</div>
                    </el-col>
                    <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                        <div>{{ data[2] }}</div>
                    </el-col>
                </el-row>
                <div style="text-align: center;">

                    <el-button @click="remove(data[1])" type="danger">点击进行删除</el-button>
                </div>
            </el-card>
        </el-col>
    </el-row>
    <el-row>
        <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
        </el-col>
        <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
            <div class="example-pagination-block">
                <el-pagination layout="prev, pager, next" :total="successful.length" :page-size="10"
                    v-model:current-page="page" />
            </div>
        </el-col>
    </el-row>
</template>
<script lang="ts" setup>
import router from '@/router';
import axios from 'axios';
import { computed, onBeforeMount, ref } from 'vue';

const name = ref('')
const successful = ref('')
const page = ref(1)

onBeforeMount(() => {
  name_search()


})

const newdata = computed(() => {
    return successful.value.slice((page.value - 1) * 10, page.value * 10 - 1)
})



async function name_search() {
    let res = await axios.post("http://localhost:8888/name_search",
        {
            onlyname: name.value,
        }
    )
    if (res.status == 200) {
        successful.value = res.data

    }
}
async function remove(name: string) {
    console.log()
    let res = await axios.post("http://localhost:8888/remove",
        {
            name: name
        }
    )
    if (res.status == 200) {
        successful.value = res.data
        name_search()
    }
}
function back() {
  router.push('/adminstration')
}
</script>
<style>
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.image {
  width: 180px;
  height: 230px;
}

.card {
  margin-top: 2%;
  width: 220px;
  height: 360px;
}

.example-pagination-block+.example-pagination-block {
  margin-top: 10px;
}

.example-pagination-block .example-demonstration {
  margin-bottom: 16px;
}</style>