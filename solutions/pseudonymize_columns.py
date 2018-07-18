def pseudonymize_columns(dataframe, cols,
                         ps_key='test',
                         api_key=SHARED_KEY):
    actions = [
        {    "name": "pseudonymize-{}".format(c),
            "transform-value" : {
                "key": c,
                "pseudonymize" : {
                    "method": "merengue",
                    "key": ps_key,
                }
            }
        } for c in cols]
    items = dataframe.fillna('').T.to_dict()
    item_list = list(items.values())
    data = requests.post(
        'https://api.kiprotect.com/v1/transform',
        data = json.dumps(
            {"actions": actions, "items": item_list},
        allow_nan=False),
    headers = {
        'Authorization': 'Bearer {}'.format(api_key)})
    return pd.DataFrame(data.json()['items'])
