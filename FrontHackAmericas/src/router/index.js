import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import LandingPage from '@/components/LandingPage/LandingPage'
import Input from '@/components/Base/Input'
import Explorer from '@/components/Explorer/Explorer'
import Boton from '@/components/Base/Boton'
import Registrar from '@/components/Register/Register'
import RealTime from '@/components/Explorer/RealTime/RealTime'
import RegisterSatisfactorio from '@/components/Register/RegisterSatisfactorio'

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
      name: 'Explore',
      component: Explorer,
      props: true
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
    },
    {
      path: '/Registrar',
      name: 'Registrar',
      component: Registrar
    },
    {
      path: '/RealTime',
      name:'RealTime',
      component: RealTime,
      props: true
    },
    {
      path: '/RegisterSatisfactorio',
      name:'RegisterSatisfactorio',
      component: RegisterSatisfactorio,
      props: true
    }
  ]
})
