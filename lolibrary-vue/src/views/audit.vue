<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <div id="name" style="font-size: 200%; text-align: center; ">
                    {{ name }}

                </div>
            </el-header>
            <el-container>
                <el-aside width="40%">
                    <el-image class="image" :src="url" :fit="fit" />

                    <div style="color: darkgray;">该信息由<b>{{ submitter }}</b>提供,还未进行审核</div>

                </el-aside>
                <el-main>
                    <el-descriptions title="详细信息如下：" direction="vertical" :column="1" border>
                        <el-descriptions-item label="发售时间：">发售于{{ year }} 年</el-descriptions-item>
                        <el-descriptions-item label="生产编号：">{{ product }}</el-descriptions-item>
                        <el-descriptions-item label="胸围：">{{ bust }}cm</el-descriptions-item>
                        <el-descriptions-item label="腰围：">{{ waist }}cm</el-descriptions-item>
                        <el-descriptions-item label="裙长：">{{ length }}cm</el-descriptions-item>
                        <el-descriptions-item label="品牌：">{{ brand }}</el-descriptions-item>
                        <el-descriptions-item label="分类：">{{ category }}</el-descriptions-item>
                        <el-descriptions-item label="特征：">{{ features }}</el-descriptions-item>
                        <el-descriptions-item label="颜色：">{{ colorway }}</el-descriptions-item>
                        <el-descriptions-item label="标签：">{{ tags }}</el-descriptions-item>
                        <el-descriptions-item label="特殊说明：">{{ note }}</el-descriptions-item>
                    </el-descriptions>
                </el-main>

            </el-container>
        </el-container>
        <el-container direction="horizontal">
            <el-footer style="width: 100%; height: 20%;">
                <el-row>

                    <el-card v-for="item in imageslist " shadow="always">
                        <el-image :src="item" class="imagelist" />
                    </el-card>
                </el-row>
                <el-row>
                    <div style="margin: auto;">
                        <el-button :style="{ color: buttonTextColor }" style="float: left;"
                            @click="audit()">点击通过审核</el-button>
                        <div v-if="buttonTextColor == 'green'">
                            <el-button type="success" :icon="Check" circle />
                        </div>
                    </div>
                    {{ maessage }}
                </el-row>

            </el-footer>

        </el-container>

    </div>
</template>
  
<script lang="ts" setup>
import axios from 'axios';
import { onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';
import {
    Check,
    Delete,
    Edit,
    Message,
    Search,
    Star,
} from '@element-plus/icons-vue'
const fit = "fill"
const url = ref('')

const imageslist = ref([])
const name = ref("")
const maessage = ref("")
const successful = ref([])
const year = ref('')
const product = ref('')
const price = ref('')
const bust = ref('')
const length = ref('')
const waist = ref('')
const brand = ref('')
const category = ref('')
const features = ref('')
const tags = ref('')
const colorway = ref('')
const note = ref('')
const data = ref([])
const submitter = ref('')
const aduit = ref('')
const route = useRoute()
onBeforeMount(() => {
    detail_search()
})


const buttonTextColor = ref('black');

const changeColor = () => {
    buttonTextColor.value = 'green'; // 改变按钮文字颜色为绿色
};

async function detail_search() {

    console.log("detail_search route", route.params)
    const id = route.params.id
    let res = await axios.post("http://localhost:8888/detail_search",
        {
            id: id,
        }
    )
    if (res.status == 200) {
        successful.value = res.data
        data.value = successful.value
        name.value = data.value[1]
        category.value = data.value[2]
        brand.value = data.value[3]
        colorway.value = data.value[4]
        features.value = data.value[5]
        tags.value = data.value[6]
        url.value = data.value[7]
        year.value = data.value[8]
        product.value = data.value[9]
        price.value = data.value[10]
        bust.value = data.value[11]
        waist.value = data.value[12]
        length.value = data.value[13]
        note.value = data.value[14]
        imageslist.value = data.value.slice(19)
        aduit.value = data.value[16]
        submitter.value = data.value[18]
    }
}
async function audit() {

    const id = route.params.id
    const auditor = route.params.user
    console.log("a", auditor)
    let res = await axios.post("http://localhost:8888/audit",
        {
            id: id,
            auditor: auditor
        }
    )
    if (res.status == 200) {
        maessage.value = res.data
        changeColor()
    }

}
</script>
<style>
.imagelist{
    width: 150px;
    height: 200px;
}
.image{
    width: 100%; 
    height: 60%;
}
</style>

