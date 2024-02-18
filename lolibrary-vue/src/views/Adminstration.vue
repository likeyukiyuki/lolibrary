<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        欢迎来到管理页面
      </el-header>
      <el-container>

        <el-aside width="30%">

          <h1>请添加信息</h1>

          <el-input :required="true" v-model="name" placeholder="Please input name" style="width: 80%;" /><label
            style="color: rgb(227, 72, 72);">*必填</label>
          <br>
          <el-input :required="true" v-model="category" placeholder="Please input category" style="width: 80%;" /><label
            style="color: rgb(227, 72, 72);">*必填</label>
          <br>
          <el-input :required="true" v-model="brand" placeholder="Please input Brand" style="width: 80%;" /><label
            style="color: rgb(227, 72, 72);">*必填</label>
          <br>
          <el-input :required="true" v-model="colorway" placeholder="Please input colorway" style="width: 80%;" /><label
            style="color: rgb(227, 72, 72);">*必填</label>
          <br>
          <el-input v-model="features" placeholder="Please input Features" style="width: 80%;" />
          <br>
          <el-input v-model="tags" placeholder="Please input Tags" style="width: 80%;" />





          <el-upload :class="{ disabled: noUpload }" action="http://localhost:8888/insert" :auto-upload="false"
            list-type="picture-card" :on-preview="handlePictureCardPreview" :on-change="checkImageFormat"
            :on-remove="handleRemove" :limit="1" ref="businessLicense" :file-list="faceList">
            <el-icon v-if="faceList.length == 0">
              <Plus />
            </el-icon>
          </el-upload> <label style="color: rgb(227, 72, 72);">*必填</label>

          <el-dialog v-model="dialogVisible">
            <img w-full :src="dialogImageUrl" alt="Preview Image" />
          </el-dialog>

          <br>
          <button @click="click">提交</button>
        </el-aside>
        <el-main>
          <label>添加附加信息</label><br>
          <label>年份:</label><br>
          <el-date-picker v-model="value3" type="year" />
          <br><label>生产编号：</label>
          <el-input v-model="product" style="width: 30%;" />

          <br><label>发售价格:</label>
          <el-input v-model="price" style="width: 30%;" />
          <br><label>添加尺寸信息：</label>
          <br><label>胸围:</label>
          <el-input v-model="bust" style="width: 30%;"></el-input>
          <br><label>腰围:</label>
          <el-input v-model="waist" style="width: 30%;"></el-input>
          <br><label>长度:</label>
          <el-input v-model="length" style="width: 30%;"></el-input>
          <br><label>添加特殊说明:</label>
          <el-input v-model="note" style="width: 30%;"></el-input>
          <br><label>除主图以外的其他图片：</label>
          <el-upload action="http://localhost:8888/insert" list-type="picture-card" :auto-upload="false"
            :on-change="flist" :on-preview="handlePictureCardPreview" :on-remove="handleRemove">
            <el-icon>
              <Plus />
            </el-icon>
          </el-upload>
  
            {{ successful }}
            <Router-Link to="/delete">点击进行删除</Router-Link>
            
            <button @click="a">a</button>
        </el-main>
      </el-container>
    </el-container>
  </div>
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


const dialogImageUrl = ref('')
const dialogVisible = ref(false)

const handleRemove: UploadProps['onRemove'] = (uploadFile, uploadFiles) => {
  console.log(uploadFile, uploadFiles)
}

const handlePictureCardPreview: UploadProps['onPreview'] = (uploadFile) => {
  dialogImageUrl.value = uploadFile.url!
  dialogVisible.value = true
}



const value3: Ref<Date> = ref(new Date())
const name = ref('')
const category = ref('')
const brand = ref('')
const features = ref('')
const tags = ref('')
const colorway = ref('')
const product = ref('')
const price = ref('')
const bust = ref('')
const waist = ref('')
const length = ref('')
const note = ref('')
//上传主图




const faceList = ref([])//图片列表
const noUpload = ref(false)//不再上传

const ifile = ref()

//上传图片列表

const disabled = ref(false)
const images: Ref<UploadFile | null> = ref(null)
const validImageFormats = ["jpg", "jpeg", "png"];//允许的文件后缀
//选择文件格式校验//并限制上传数量
const checkImageFormat = (file: UploadFile, _: UploadFiles) => {
  images.value = file
  console.log("文件格式校验");
  console.log(file);
  // noUpload.value = true
  const fileFormat = file.name.split(".").pop()?.toLowerCase(); // 获取文件格式
  if (fileFormat && !validImageFormats.includes(fileFormat)) {
    ElMessage({ type: "error", message: "商品图片格式必须为 jpg/jpeg/png" });
    faceList.value = []; //删除格式不符合的文件
    return false; // 阻止文件上传

  }

  noUpload.value = true//设置为true阻止继续上传
  return true; // 允许文件上传



};





const handleDownload = (file: UploadFile) => {
  console.log(file)
}
const rawfiles: Ref<(UploadRawFile | undefined)[]> = ref([])
const images1: Ref<UploadFiles | null> = ref(null)
const flist = (_: UploadFile, filelist: UploadFiles) => {

  rawfiles.value = filelist.map(
    (x) => x.raw
  )
  console.log()
}

function getyear() {
  var years = value3.value.getFullYear();
  const stryears = years.toString()
  return stryears
}



// 获取年份
var years = getyear()


//请求
const successful = ref("");
function click() {
  if (name.value != "" && category.value != "" && brand.value != "" && colorway.value != "" && images.value != null && rawfiles.value != null) {
    insert()
  } else if (images.value == null) {

    alert("必须上传主图")
  } else {
    alert("必填项不能为空")
  }
}




async function insert() {
  let f = new FormData();
  rawfiles.value.forEach(
    (x) => f.append("fileslist", x as Blob)
  )
  f.append("name", name.value)
  f.append("category", category.value)
  f.append("brand", brand.value)
  f.append("colorway", colorway.value)
  f.append("features", features.value)
  f.append("tags", tags.value)

  f.append("images", images.value?.raw as Blob)
  f.append("years", years)
  f.append("product", product.value)
  f.append("price", price.value)
  f.append("bust", bust.value)
  f.append("waist", waist.value)
  f.append("length", length.value)
  f.append("note", note.value)


  let res = await axios.post("http://localhost:8888/insert", f, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
  if (res.status == 200) {
    successful.value = res.data
    setTimeout(() => {
      successful.value = ""
    }, 3000);
  }

}
</script>

<style scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>
<style>
.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  text-align: center;
}
</style>