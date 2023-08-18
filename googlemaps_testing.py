import http.client, urllib.parse
import time
import json

conn = http.client.HTTPConnection('api.positionstack.com')
elapsed_time = []
start_time = time.time()
fail = []

with open("address.txt") as file:
    for item in file:
        print(item)
        params = urllib.parse.urlencode({
            'access_key': 'c9a995c8844a6635acbbbe286ab4410d',
            'query': item,
            'limit': 1,
        })

        conn.request('GET', '/v1/forward?{}'.format(params))
        res = conn.getresponse()
        data = res.read()
        time.sleep(3)
        pos_stack_api = data.decode('utf8').replace("'", '"')
        json_output = json.loads(pos_stack_api)
        lat, long = json_output["data"][0]['latitude'], json_output["data"][0]['longitude']
        print(lat)
        print(long)
        # if len(json_output['data']) > 0:
        #     try:
        #         lat, long = json_output["data"][0]['latitude'], json_output["data"][0]['longitude']
        #         print(lat)
        #         print(long)
        #     except TypeError:
        #         print("\nOverloading server. Retrying after pause...\n")
        #         elapsed_time.append(time.time() - start_time)
        #         fail.append(1)
        #         time.sleep(60)
        #         continue
        #     else:
        #         print("\nLocation added!\n")
        #         elapsed_time.append(time.time() - start_time)
        #         fail.append(0)
        #         break
