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
                    <el-image style="width: 100%; height: 60%" :src="url" :fit="fit" />
                
                    <div style="color: darkgray;">该信息由<b>{{ submitter }}</b>提供,由<b>{{ aduit }}</b>审核</div>
               
                </el-aside>
                <el-main>
                    <div id="item">
                        <h3>详细信息</h3><br />
                        发售于{{ year}} 年
                        <br>
                        生产编号：{{ product }}
                        <br>
                        价格：{{ price }}
                    </div>
                    <div id="size information">
                        <h3>胸围</h3>
                        {{ bust }}
                        <br>
                        <h3>腰围</h3>
                        {{ waist }}
                        <br>
                        <h3>裙长</h3>
                        {{ length }}
                    </div>
                    <div id="brand">
                        <h3>品牌</h3>
                        {{ brand }}
                    </div>
                    <div id="category">
                        <h3>分类</h3>
                        {{ category }}
                    </div>
                    <div id="features">
                        <h3>特征</h3>
                        {{ features }}
                    </div>
                    <div id="colorway">
                        <h3>颜色</h3>
                        {{ colorway }}
                    </div>
                    <div id="tags">
                        <h3>标签</h3>
                        {{ tags }}
                    </div>
                    
                </el-main>
                
            </el-container>
        </el-container>
        <el-container direction="horizontal">
            <el-footer style="width: 100%; height: 20%;">
                <div v-for="item in imageslist " style="float: left;">
                    <el-image style="width: 150px; height: 200px" :src="item" :fit="fit"></el-image>

                </div>
            </el-footer>
        </el-container>

    </div>
</template>
  
<script lang="ts" setup>
import axios from 'axios';
import { onBeforeMount, ref } from 'vue';
import { useRoute } from 'vue-router';

const fit = "fill"
const url = ref('')

const imageslist = ref([])
const name = ref("")

const successful=ref([])
const year=ref('')
const product=ref('')
const price=ref('')
const bust = ref('')
const length = ref('')
const waist = ref('')
const brand = ref('')
const category = ref('')
const features = ref('')
const tags = ref('')
const colorway =ref('')
const note=ref('')
const data=ref([])
const submitter=ref('')
const aduit=ref('')

onBeforeMount(() => {
    detail_search()
})



async function detail_search(){
    const route = useRoute()
    console.log("detail_search route",route.params)
    const id=route.params.id
    let res = await axios.post("http://localhost:8888/detail_search",
        {
        id: id,
        }
    )
    if (res.status == 200) {
        successful.value = res.data
        data.value=successful.value
        name.value=data.value[1]
        category.value=data.value[2]
        brand.value=data.value[3]
        colorway.value=data.value[4]
        features.value=data.value[5]
        tags.value=data.value[6]
        url.value=data.value[7]
        year.value=data.value[8]
        product.value=data.value[9]
        price.value=data.value[10]
        bust.value=data.value[11]
        waist.value=data.value[12]
        length.value=data.value[13]
        note.value=data.value[14]
        imageslist.value=data.value.slice(19)
        aduit.value=data.value[16]
        submitter.value=data.value[18]
    }
}

</script>


