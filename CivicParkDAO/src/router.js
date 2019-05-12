import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Browse from './views/Browse.vue';
import CreateCampaign from './views/CreateCampaign';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/browse',
      name: 'browse',
      component: Browse,
    },
      {
          path: '/create',
          name: 'create',
          component: CreateCampaign,
      },
  ],
});
