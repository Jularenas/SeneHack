const url = 'http://157.253.222.204:5000';
const Http=new XMLHttpRequest();

export function login(username,passwd,callback)
{
    Http.open('POST',url+'/login',true);
    Http.setRequestHeader('Content-Type',"application/json");
    Http.setRequestHeader('Access-Control-Request-Method',"POST");
    Http.onreadystatechange=function(){
        callback(this.responseText);
    }
    Http.send(JSON.stringify({
        'usuario':username,
        'passwd':passwd
      }))
}

export function register(name,username,passwd,cellphone,fun)
{
    Http.open('POST',url+'/register',true);
    Http.setRequestHeader('Content-Type',"application/json");
    Http.onreadystatechange=function(){
         fun(this.responseText);
    }
    Http.send(JSON.stringify({
        'nombre':name,
        'usuario':username,
        'passwd':passwd,
        'celular':cellphone
      }))
}

 export  function adyacentes(username,origenLat,origenLon,destinoLat
,destinoLon,radioSalida,radioLlegada, cbk) {
    console.log("ADYACENTES");
    Http.open('POST',url+'/adyacentes',true);
    Http.setRequestHeader('Content-Type',"application/json");
    Http.setRequestHeader('Access-Control-Request-Method',"POST");
    Http.onreadystatechange=function(){
        cbk(this.responseText);
    }
    Http.send(JSON.stringify({
        'user':username,
          'origen':{
              'latitud':origenLat,
              'longitud':origenLon
          },
          "destino":{
              'latitud':destinoLat,
              'longitud':destinoLon
          },
          'radioSalida':radioSalida,
          'radioLlegada':radioLlegada
      }))
  }

 

