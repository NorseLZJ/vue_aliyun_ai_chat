import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store from './store';

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)

app.provide('ELEMENT', { size: 'small', zIndex: 3000 });

app.use(store);
app.use(ElementPlus)
app.mount("#app")