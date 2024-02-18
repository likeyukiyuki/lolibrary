<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <label>欢迎使用搜索~</label>
      </el-header>
      <el-container>
        <el-aside width="30%">
          <el-radio-group v-model="labelPosition" label="top" />

          <div style="margin: 10px" />
          <br>
          <br>
          <label>类型:</label>
          <el-select v-model="v_category" clearable allow-create="true"  filterable placeholder="选择类型" style="width: 240px">
            <el-option v-for="item in category" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <label>品牌:</label>
          <el-select v-model="v_brand"  clearable allow-create="true" filterable placeholder="选择品牌" style="width: 240px">
            <el-option v-for="item in brand" :key="item.value" :value="item.value" />
          </el-select>
          <br>
        
          <label>特点:</label>
          <el-select v-model="v_features"  clearable allow-create="true" filterable placeholder="选择特点" style="width: 240px">
            <el-option v-for="item in features" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <label>配色:</label>
          <el-select v-model="v_colorway"  clearable allow-create="true" filterable placeholder="选择配色" style="width: 240px">
            <el-option v-for="item in colorway" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <label>标签:</label>
          <el-select v-model="v_tags"  clearable allow-create="true" filterable placeholder="选择标签" style="width: 240px">
            <el-option v-for="item in tags" :key="item.value" :value="item.value" />
          </el-select>
          <br>
          <label>年份:</label>
          <el-select v-model="years"  clearable allow-create="true" filterable placeholder="选择年份" style="width: 240px">
            <el-option v-for="item in getyears" :key="item.value" :value="item.value" />
          </el-select>
          <!-- <label>生产年份：</label>
          <el-date-picker v-model="selectedyears" type="year" clearable editable="true" placeholder /> -->

          <button @click="search">搜索</button>
        </el-aside>

        <el-main>
          <el-input v-model="name"  placeholder="Please input name" />
          <button @click="name_search">查询</button>
          <el-row>
            <el-col v-for="data in newdata " :key="data[1]" :span="6" :offset="2" style=" margin-bottom: 5%; margin-left: 5%;">
              <el-card shadow="always" style="height: 100%; width: 110%;">
                <div style="padding: 0px;font-size: 100%; " >{{ data[1] }}</div>
                <el-image style="height: 100%;width: 100%;" :src="data[7]"
                  class="image" />
                <div style="height: 15%;">
                  <span style="font-size: 15%;">brand</span>
                  <span style="font-size: 15%; margin-left: 40%;">category</span>
                  
                    <div style="height: 0%;">
                      <span style="font-size: 15%;height: 5%;" >{{ data[3] }}</span>
                      <span style="font-size: 15%;margin-left:60%;">{{ data[2] }}</span>
                      <div style="text-align: center;">
                        
                       <router-link :to="'/detail/'+data[0]"> <el-button text class="button" >点击查看</el-button> </router-link>
                
                    </div>
                  </div>
                </div>
              </el-card>
            </el-col>
          </el-row>

          <div class="example-pagination-block" style="margin-left: 30%;">
            <el-pagination layout="prev, pager, next" :total="successful.length" :page-size="10" v-model:current-page="page"/>
          </div>
        </el-main>
      </el-container>

    </el-container>

  </div>
</template>


<script lang="ts" setup>
import { computed, onBeforeMount, reactive, ref, watch, type Ref } from 'vue'
import type { FormProps } from 'element-plus'
import axios from 'axios';



const labelPosition = ref<FormProps['labelPosition']>('right')
const value3: Ref<Date> = ref(new Date())
const v_category = ref('')
const name = ref('')
const category = [{ value: 'jsk' }, { value: 'op' }, { value: 'sk' }, { value: '胸衣' }, { value: '大衣' }, { value: '伞' }, { value: '小物' }]
const v_brand = ref('')
const brand = [{ value: 'ap' }, { value: 'baby' }, { value: 'etc' }, { value: '古典玩偶' }]
const v_features = ref('')
const features = [{ value: '有素鸡' }, { value: '袖子可拆卸' }, { value: '姬袖' }, { value: '挂脖' }, { value: '开襟' }]
const v_colorway = ref('')
const colorway = [{ value: '浅粉色' }, { value: '芭比粉' }, { value: '生成色' }, { value: '黑色' }]
const v_tags = ref('')
const tags = [{ value: '纯色' }, { value: '柄图：草莓' }, { value: '柄图：云' }, { value: '面料：丝绒' }, { value: '细节：钻石' }]
const successful = ref([])
const page=ref(1)


const years=ref('')

// 获取年份
const getyears =ref<{ value: string }[]>([]);

  for(var i=2030;i>1980;i--){
    var n=i.toString()
    getyears.value.push({value : n })
  }


onBeforeMount(() => {
   name_search()


})
   const newdata=computed(()=>{
    return successful.value.slice((page.value-1)*10,page.value*10-1)
})


async function name_search(){
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

watch(name,(name,newname)=>{
    name_search()
})

watch([v_brand,v_category,v_colorway,v_features,v_tags],([a,b],[c,d])=>{
  search()
})

</script>