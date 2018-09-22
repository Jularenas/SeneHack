const url = 'http://157.253.222.183:5000';
export function login(username,passwd) {
    console.log('Posting request to API');
    fetch(url+"/login", {
      method: 'POST',
      mode:'no-cors',
      body:JSON.stringify( {
          usuario:username,
          passwd:passwd
      })
    }).then(function(response) {
        console.log("Login successful? "+response)
      return response;
    });
  }

  export function register(username,passwd,cellphone) {
    console.log('Posting request to API');
    fetch(url+"/register", {
      method: 'POST',
      mode:'cors',
      body: {
          'usuario':username,
          'passwd':passwd,
          'celular':cellphone
      }
    }).then(function(response) {
        console.log("Register successful? "+response)
      return response;
    });
  }

  
 export  function adyacentes(username,origenLat,origenLon,destinoLat
,destinoLon,radioSalida,radioLlegada) {
    fetch(url+"/adyacentes", {
        method: 'POST',
        mode:'cors',
          body: {
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
        }
    }).then(function(response) {
        return response.json();
      }).then(function(data) {S
        console.log('Users list:', data);
        return data
      });
  }

 

