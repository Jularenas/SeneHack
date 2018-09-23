const url = 'https://p2poolserver.herokuapp.com';
const Http = new XMLHttpRequest();

export function login(username, passwd, callback) {
    Http.open('POST', url + '/login', true);
    Http.setRequestHeader('Content-Type', "application/json");
    Http.setRequestHeader('Access-Control-Request-Method', "POST");
    Http.onreadystatechange = function () {
        callback(this.responseText);
    }
    Http.send(JSON.stringify({
        'usuario': username,
        'passwd': passwd
    }))
}

export function register(name, username, passwd, cellphone, fun) {
    fetch(url + '/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'nombre': name,
            'usuario': username,
            'passwd': passwd,
            'celular': cellphone
        })

    }).then(res => res.text()).then(text => {
        fun(text);
    });
}

export function adyacentes(username, origenLat, origenLon, destinoLat
    , destinoLon, radioSalida, radioLlegada, cbk) {
    console.log("ADYACENTES");
    Http.open('POST', url + '/adyacentes', true);
    Http.setRequestHeader('Content-Type', "application/json");
    Http.setRequestHeader('Access-Control-Request-Method', "POST");
    Http.onreadystatechange = function () {
        cbk(this.responseText);
    }
    Http.send(JSON.stringify({
        'user': username,
        'origen': {
            'latitud': origenLat,
            'longitud': origenLon
        },
        "destino": {
            'latitud': destinoLat,
            'longitud': destinoLon
        },
        'radioSalida': radioSalida,
        'radioLlegada': radioLlegada
    }))
}



