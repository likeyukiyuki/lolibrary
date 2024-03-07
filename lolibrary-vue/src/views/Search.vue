<template>
  <div class="common-layout">
    <el-container>

      <el-aside width="30%">
        <el-card class="box-card">
          <template #header>
            <div class="card-header">
              <span>条件查找</span>
            </div>
          </template>
          <label>类型:</label>
          <el-select v-model="v_category" clearable allow-create="true" multiple filterable  placeholder="选择类型">
            <el-option v-for="item in category" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <br>
          <label>品牌:</label>
          <el-select v-model="v_brand" clearable allow-create="true" multiple filterable placeholder="选择品牌">
            <el-option v-for="item in brand" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <br>
          <label>特点:</label>
          <el-select v-model="v_features" clearable allow-create="true" multiple filterable placeholder="选择特点">
            <el-option v-for="item in features" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <br>
          <label>配色:</label>
          <el-select v-model="v_colorway" clearable allow-create="true" multiple filterable placeholder="选择配色">
            <el-option v-for="item in colorway" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <br>
          <label>标签:</label>
          <el-select v-model="v_tags" clearable allow-create="true" multiple filterable placeholder="选择标签">
            <el-option v-for="item in tags" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <br>
          <label>年份:</label>
          <el-select v-model="years" clearable allow-create="true" multiple filterable placeholder="选择年份">
            <el-option v-for="item in getyears" :key="item.value" :value="item.value" />
          </el-select>
        </el-card>

      </el-aside>

      <el-main>
        <el-row>
          <el-col  :xs="22" :sm="12" :md="12" :lg="22" :xl="1">
             <el-input v-model="name" placeholder="Please input name" />
          </el-col>
          <el-col  :xs="2" :sm="12" :md="12" :lg="2" :xl="1">
            <button @click="name_search">查询</button>
          </el-col>
        
        </el-row>
        
        <el-row>
          <el-col v-for="data in newdata " :key="data[1]" :offset="0.5" :xs="15" :sm="12" :md="10" :lg="7" :xl="1">
            <el-card shadow="always" class="card">
              <div style=" text-align: center;">{{ data[1] }}</div>
              <el-image :src="data[7]" class="image" />
              <el-row :gutter="2">
                <el-col  class="color"  :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                  <div>brand</div>
                </el-col>
                <el-col  class="color"  :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                  <div>category</div>
                </el-col>
              </el-row>
              <el-row :gutter="2">
                <el-col  :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                  <div>{{ data[3] }}</div>
                </el-col>
                <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
                  <div>{{ data[2] }}</div>
                </el-col>
              </el-row>
              <div style="text-align: center;">

                <router-link :to="'/detail/' + data[0]"> <el-button type="primary" text="primary">点击查看</el-button>
                </router-link>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row>
          <el-col :xs="12" :sm="12" :md="12" :lg="9" :xl="1">
          </el-col>
          <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="1">
            <div class="example-pagination-block">
              <el-pagination layout="prev, pager, next" :total="successful.length" :page-size="10"
                v-model:current-page="page" />
            </div>
          </el-col>
        </el-row>

      </el-main>
    </el-container>



  </div>
</template>


<script lang="ts" setup>
import { computed, onBeforeMount, reactive, ref, watch, type Ref } from 'vue'
import type { FormProps } from 'element-plus'
import axios from 'axios';



const labelPosition = ref<FormProps['labelPosition']>('right')
const value3: Ref<Date> = ref(new Date())
const v_category = ref([])
const name = ref('')
const category = [{ value: 'jsk' }, { value: 'op' }, { value: 'sk' }, { value: '胸衣' }, { value: '大衣' }, { value: '伞' }, { value: '小物' }]
const v_brand = ref('')
const brand = [{ value: 'ap' }, { value: 'baby' }, { value: 'etc' }, { value: '古典玩偶' },{value:'etc'},{value:'anp'},{value:'rs'},{value:'婴梵塔'},{value:'魔法茶会'}]
const v_features = ref('')
const features = [{ value: '有素鸡' }, { value: '袖子可拆卸' }, { value: '姬袖' }, { value: '挂脖' }, { value: '开襟' },{value:'带纱'},{value:'泡泡袖'},{value:'烫金'},{value:'花瓣摆'}]
const v_colorway = ref('')
const colorway = [{ value: '浅粉色' }, { value: '芭比粉' }, { value: '生成色' }, { value: '黑色' },{value:'黄色'},{value:'若草色'},{value:'sax色'},{value:'bb蓝'},{value:'香槟金'}]
const v_tags = ref('')
const tags = [{ value: '纯色' },{value:'纯色：波点'},{value:'纯色：蕾丝'}, { value: '柄图：草莓' }, { value: '柄图：云' },{value:'柄图：天鹅'}, { value: '面料：丝绒' }, {value:'柄图：棉布'},{ value: '细节：钻石' }]
const successful = ref([])
const page = ref(1)


const years = ref('')

// 获取年份
const getyears = ref<{ value: string }[]>([]);

for (var i = 2030; i > 1980; i--) {
  var n = i.toString()
  getyears.value.push({ value: n })
}


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

async function search() {
  console.log(years)
  let res = await axios.post("http://localhost:8888/search",
    {
      sbrand: v_brand.value,
      scategory: v_category.value,
      sfeatures: v_features.value,
      scolorway: v_colorway.value,
      stags: v_tags.value,
      syears: years.value

    }
  )
  if (res.status == 200) {
    successful.value = res.data

  }
}

watch(name, (name, newname) => {
  name_search()
})

watch([v_brand, v_category, v_colorway, v_features, v_tags,years], ([a, b], [c, d]) => {
  search()
})



</script>
<style scoped>
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
}
.color{
  color: rgb(172, 163, 169);
 
}
</style>