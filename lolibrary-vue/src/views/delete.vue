<template>
    <el-input v-model="name" placeholder="Please input name" @change="(_: string) => name_search()" style="width: 30%;" />
    <button @click="name_search">查询</button>


    <el-row>
        <el-col v-for="data in newdata " :key="data[1]" :span="6" :offset="2" style=" margin-bottom: 5%; margin-left: 5%;">
            <el-card shadow="always" style="height: 100%; width: 110%;">
                <div style="padding: 0px;font-size: 100%; ">{{ data[1] }}</div>
                <el-image style="height: 100%;width: 100%;" :src="data[7]" class="image" />
                <div style="height: 15%;">
                    <span style="font-size: 15%;">brand</span>
                    <span style="font-size: 15%; margin-left: 40%;">category</span>

                    <div style="height: 0%;">
                        <span style="font-size: 15%;height: 5%;">{{ data[3] }}</span>
                        <span style="font-size: 15%;margin-left:60%;">{{ data[2] }}</span>
                        <div style="text-align: center;">

                            <el-button @click="remove(data[1])" text class="button">点击进行删除</el-button>

                        </div>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>
    <div class="example-pagination-block" style="margin-left: 30%; bottom: 10%;">
        <el-pagination layout="prev, pager, next" :total="successful.length" :page-size="10" v-model:current-page="page" />
    </div>
</template>
<script lang="ts" setup>
import axios from 'axios';
import { computed, onBeforeMount, ref } from 'vue';

const name = ref('')
const successful = ref('')
const page = ref(1)



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
</script>