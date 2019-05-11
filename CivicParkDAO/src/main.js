import Vue from 'vue';
import './plugins/vuetify';
import App from './App.vue';
import router from './router';
import '@fortawesome/fontawesome-free/css/all.css'; // Ensure you are using css-loader
import './registerServiceWorker';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);

Vue.config.productionTip = false;

new Vue({
  iconfont: 'fa',
  router,
  render: h => h(App),
}).$mount('#app');
