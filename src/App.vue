<script setup>
import QAValue from './components/QAValue.vue'
import { ref } from 'vue'

import { useStore } from 'vuex';
import { computed } from 'vue';

const store = useStore();
const serverHost = computed(() => store.getters.getServerHost);

const input = ref('')
const qaList = ref([]);
const isLoading = ref(false); // 新增的状态变量

import axios from 'axios';

async function submitQuestion() {
  if (input.value != "" && isLoading.value === false) {
    isLoading.value = true;
    try {
      let question = input.value
      qaList.value.push({ question: question, answer: '' });
      const chat_url = serverHost.value + "/chat";
      let data = {
        msg1: question,
      }
      const resp = await axios.post(chat_url, data);
      if (resp.data.error) {
        alert(resp.data.error)
        qaList.value.pop();
      } else if (resp.data.ack) {
        qaList.value[qaList.value.length - 1].answer = resp.data.ack;
        input.value = ''
      } else {
        qaList.value.pop();
      }
    } catch (error) {
      console.log('Error fetching data:', error);
    }
    isLoading.value = false;
  }
}

</script>

<template>
  <div class="container">
    <div class="output-area">
      <QAValue v-for="(qa, index) in qaList" :key="index" :question="qa.question" :answer="qa.answer" />
    </div>
    <el-input class="input-size" v-model="input" maxlength="1000" type="textarea" placeholder="在我二十一岁的那一年，是我一生中的黄金时代" />
    <el-button type="primary" :disabled="isLoading" @click="submitQuestion">提交</el-button>
  </div>
</template>

<style scoped>
.output-area {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ebeef5;
  border-radius: 4px;
  /* background-color: aquamarine; */
}

.container {
  height: auto;
  width: 1100px;
  border: 5px solid #ffffff;
  background-color: #fff;
  /* 背景颜色设为白色 */
  box-shadow: 0 0 10px 5px rgba(0, 0, 0, 0.2);
  /* 添加阴影以模拟凸起效果 */
  position: relative;
  /* 使用相对定位以便于布局 */
}

.input-size {
  resize: none;
  /* 禁止调整大小 */
  overflow-wrap: break-word;
  /* 自动换行 */
  white-space: pre-wrap;
  /* 保留空格和换行符 */
  width: 1000px;
  /* 宽度占满容器 */
}



/*  */
</style>
