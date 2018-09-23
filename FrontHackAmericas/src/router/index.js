import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LandingPage from '@/components/LandingPage/LandingPage'
import Input from '@/components/Base/Input'
import Explorer from '@/components/Explorer/Explorer'
import Boton from '@/components/Base/Boton'

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
    },
    {
      path: '/Input',
      name: 'Input',
      component: Input
    },
    {
      path: '/Boton',
      name: 'Boton',
      component: Boton
    }
  ]
})
