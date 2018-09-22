import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LandingPage from '@/components/LandingPage/LandingPage'
import Explorer from '@/components/Explorer/Explorer'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LandingPage',
      component: LandingPage
    },
    {
      path: '/Explore',
      name: 'Explorer',
      component: Explorer
    },
    {
      path: '/',  
      name: 'LandingPage',
      component: LandingPage
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
