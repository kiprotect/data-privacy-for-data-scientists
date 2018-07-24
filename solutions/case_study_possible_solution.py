
# scenario three: possible implementation (to hide as solution for hints)# scena 


## pseudonymize hospital, age and admitted timestamp
import json
import requests


SHARED_KEY = '42a2d3fc1cc449e2a27ddd457e056012'

item_list = list(df.T.to_dict().values())

actions = [
    {
        "name": "pseudonymize-hospital",
        "transform-value" : {
            "key": "hospital",
            "pseudonymize" : {
                "method": "merengue",
                "key": "89f7dklnvkldhiwokdljklsnm,qip72", 
            }
        }
    },
    {
        "name": "pseudonymize-age",
        "transform-value": {
            "key": "age",
            "pseudonymize": {
                "method": "structured",
                "key": "320fidsjkl8wy8uiofme#908",
                "type": "integer",
                "format": "raw",
                "typeParams": {
                    "min": 16,
                    "max": 100
                }
            }
        }
    },
    {
        "name": "pseudonymize-admitted-ts",
        "transform-value": {
            "key": "admitted_ts",
            "pseudonymize": {
                "method": "structured",
                "key": "320fidsjkl8wy8uiofme#908",
                "type": "date",
                "preservePrefix": True,
                "format": "%(2000-2019)Y-%m-%d %H:%M:%S"
            }
        }
    }
]

pseudonymized_data = requests.post(
    'https://api.kiprotect.com/v1/transform', 
    data = json.dumps(
        {"actions": actions, "items": item_list}, 
        allow_nan=False),
    headers = {'Authorization': 'Bearer {}'.format(
        SHARED_KEY)}
)


protected_df = pd.DataFrame(pseudonymized_data.json()['items'])

