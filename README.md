# NLCommissioner

### Launch the app:

```bash
 git clone https://github.com/SCcagg5/NLCommissioner/; 		  	`# clone the repo`
 cd NLCommissioner;  							`# enter in the localdir`
 docker-compose up -d --build; 						`# launching the docker-compose`
```
### `Dockerfile` comportement:

the api's `dockerfile` is based on python:3.7-alpine, at launch it:
 * installs needed packages from `back-end/requirements.txt` using `pip3`
 * loads ***ENV*** from `back-end/CONFIG`

### ENV:

The setup is based on `back-end/CONFIG` it let you define:
```bash
API_HOST='0.0.0.0'				`# INSIDE CONTAINER api host`
API_PORT=8080					`# INSIDE CONTAINER port of the app`
API_WEBA='*'					`# cors request`
```

if the `API_PORT` is change you must change it also into `docker-compose`

`API_WEBA='*'` is not recommended


----------


### Routes's Basics:

Routes | Methods | Params | Return |
-|-|-|-|
`/compute_one/` | POST | pv, nb_clients |
`/compute_multi/` | POST | data |

### Parameters

```javascript
{
  pv: 1,                      //(unsigned int | max /// | min   0)
  nb_clients: 1,              //(unsigned int | max /// | min   0)
  data: []                    //(       array | max /// | min   0)
}
```

### Return template

```javascript
{
    "queryInfos": {
        "route": "/test/",
        "params": []
    },
    "status": 200,
    "error": null,
    "data": null,
    "succes": true
}
```

### Returns Exemples

* `BONUS` :
```javascript
  "bonus": {
            "ref": REF,
            "your_bonus": YOUR_BONUS
        },
```

* `DATA` :
```javascript
  "data": [
            {
                "pv": PV,
                "nb_clients": NB_CLIENTS,
                "totalpv": TOTALPV,
                "totalgain": TOTALGAIN
            }
        ],
```

* `NB_CLIENTS` :
```javascript
  "nb_clients": 2 //number of client (given)
```

* `REF` :
```javascript
  "ref": {      // %bonus per pv          
                "0": 0, // + 0% if 0 <= totalpv < 1000
                "1000": 7, // + 7% if 1000 <= totalpv < 2000
                "2000": 14, // + 14% if 2000 <= totalpv < 3000
                "3000": 21 // + 21% if 3000 <= totalpv
          }
```

* `TOTALGAIN` :
```javascript
  "totalgain": 123 //value (eur)
```

* `TOTALPV` :
```javascript
  "totalpv": 123 //value (pv)
```

* `PV` :
```javascript
  "pv": 123 //value (pv)(given)
```

* `YOUR_BONUS` :
```javascript
  "your_bonus": 7 // your bonus (%)
```

### Routes's JSON exemples:

Routes | Body |
-|-|
`/compute_one/` | {<br>"pv" : 36,<br>"nb_clients": 2<br>} |
`/compute_multi/` | {<br>"data": [{<br>"pv" : 36,<br>"nb_clients": 2<br>}]<br>} |
