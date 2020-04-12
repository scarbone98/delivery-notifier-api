walmart_header_string = """
            authority: grocery.walmart.com
            :method: GET
            :path: /v4/api/accessPoints/16bf163b-3e2e-4822-b9a4-6b8250289c62/slots?contractId=875c0921-070e-49f1-a07a-7a543bcb0cb3&fulfillmentType=DELIVERY&storeId=1735&plans=true&express=true&mergedSlots=true&restrictedSlots=true
            :scheme: https
            accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            accept-encoding: gzip, deflate, br
            accept-language: en-US,en;q=0.9
            cache-control: max-age=0
            cookie: vtc=UkwHV3gKonDwn_EKdxL2m8; TS013ed49a=01538efd7c263361c6b42ae96911960299e86711da8710566cc525e5d0812398d42438e5dc0b52e2bd755f5d86fb9e4e2ca7718a4e; sw_supported=true; sw_registered=true; DL=60004%2C%2C%2Cip%2C60004%2C%2C; tb_sw_supported=true; tb_sw_registered=true; nd_sess=0|1; TB_DNS_Perf_Test=1; TB_DC_Dist_Test=1; bstc=VR_OlXEIGGf4CptAWKZj2k; dfp_exp_8=buybox_reposition_variantB; mobileweb=0; ndcache=b; TS01af768b=01538efd7c5700e88769bea78f5e743eec3cad95af135396bfd859784616f80d8cd951f8fbc6c9aa2fdae11e7d2e8612c8a89794d1; hasGCRT=1; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1586036251316@firstcreate:1586036242045"; TS01e3f36f=01c5a4e2f904451bcf96e39fa7932965b52509b9a8fe3803d3700fb0912c81693a7b13e489a51e920f0654a68ad28e81e3b9452796; TS018dc926=01c5a4e2f904451bcf96e39fa7932965b52509b9a8fe3803d3700fb0912c81693a7b13e489a51e920f0654a68ad28e81e3b9452796; TS012c809b=01538efd7c5700e88769bea78f5e743eec3cad95af135396bfd859784616f80d8cd951f8fbc6c9aa2fdae11e7d2e8612c8a89794d1; auth=MTAyOTYyMDE4Pn2Jdwcu3%2BvbYd6xLkfZdNGxzedjxs2VuEul6XMMiQVWS1Q3rH2o8NtewDGg8ViYy3DtzcdS9CIwJBQ%2BQmNwPATDYOU0PrjG7JjV%2FVwsqaTo6mXHNZsK5dw5NbVI6tJjb4AjdT%2Bb8lXGgN8uKXRv0S1ioTq7mKggCoHT9g55RqPMljNf4uVScjrqBP8eGXDoMYIwvpvxb3rRMYV6QeBSyY2khORJXFdhxwDrjXlKAGbKJOp%2B%2Fh2tVpphfB662UTnncoxdt1KwnHjP%2FELTlwQjh6P6X5D2LhHUjmKnXGjrTphlB40LIYx%2BqIBKzDYjn%2FHgjBAl98o8aoXMzfzid957rD%2FjuwkGDy2daT2WK6crybeY1r0jdDxAXGdQPjW%2FXMK; rtoken=MDgyNTUyMDE4z7s%2F%2BgQzL8nhcv5vj%2B76hY%2FwlNpuVzM05zq4147kwCCh%2FVZrjnPx%2BJXI6q9snjgOpT3iVtkFXnPpFGogxiO4d5lD%2FFcSGUq60jXbeZ%2B3TfVrtdlpP8b8eiwyDfOe3AVxoGlevG2X9LGEOrHiS%2FNuu3SfGQhHImX%2BVnJoWTnhbelLNEc8QU7S%2FOgs1uQkyROsp%2F9lhJ0OBIOxATuj3CGrrPkbWOGVhQg4poQ2eXh8t8DKzxZ8gcNl9t9L47QPtWckDmYz7vMMn%2BZzd%2B1upg0y3r98gpSpf047xM6LZ1odnHB5ri3aYqP0RLHzytvaZHWC8NHDcZnMqOeLtKm6WcjfAkBIItaZ5C2uE5a%2BON1vvtMP8A3zXm2EKmlZvXbZOnZcROzO0TK6E15goxXSPApOOA%3D%3D; SPID=94117fb355fd0d766375ab678a028465efb9e1fcb8eeb43bdd53a47391085d033533862ea567324e64a38db653245c79wmart; CID=0c4d055a-f332-49a3-b58b-4cad78dd48eb; hasCID=1; customer=%7B%22firstName%22%3A%22Samuel%22%2C%22lastNameInitial%22%3A%22C%22%7D; type=REGISTERED; WMP=4; xpa=-8Uum|QtYkP|R7_eT; exp-ck=QtYkP1R7_eT1; xpm=1%2B1586036484%2BUkwHV3gKonDwn_EKdxL2m8~0c4d055a-f332-49a3-b58b-4cad78dd48eb%2B1; GCRT=8e55a6ec-d916-4f41-8fc5-511913849f44; akavpau_gp2=1586037695~id=94cc39ccfaaceb91af0db1e7ff80a2d9; wm_grocery=Fe26.2**a608f8bbf47bca57d9621cc342f868db5097b752869c3b08c970d0d66b863975*XCimDdBi-97BEjwtlndLtg*2czfKsYhIxePBFWbB5Dfk50n8BUESMUTqWGBzB8R8ISoUX4S9udSenceI2dguuKETQqcbzt4rGS9ORE_r29qSU_zjk3s1jpmDkQI4W6sl6Gz1OxMmvTwVYeSpNZth0ab4Qx_Cur_un1_2PIfoMVyeqTKEHsoy_xCdiBhv3gt9W6bSFYVXQHqBLStV_WnbF0YmcUuMvEgn_cyglcauf9C6RYRv-ldOnh2jIgYpokLt2pln8SfOB4xk2ix8PkwApQzxA2gMslkdp7ytFEB5tp4B2ZtLm6SrvUaLGyJtiJICrA2OqQLxKd6N4PEFd2LZ4PmqIZVvR4Hnt92G1kID2CIR1zjY8i3ahtcar1HjRy66EgXOBFV3UoY0kCaKAe0txFDNt08BXbIsGHM7ELspPTouIgSPfp7TXkm9kLpxDRXXluxwGPn9aVfrm9JvXp4ew7CukeC2n9Ccl1h1CUDU3LqUHZkycZH7F7rlFCFbPlEgZVowLpekXq6T5X0_1AtaNumT_HD3ZRZD83JJDny6vpex51i7AqNDfW93kqn7Pwo2EX3hft6UF15mAE_8_t4D3vpyHaEsYMQucU5xfyJjQdCNeP987XKf7hdt8drHkv1UKX1Isrp4qH-x9pzPYQ7pTPG5UIvxtrbLOGopuH3wCBUYpfigGfJNinU8UHHZ6Vn31rKa5J9FbA55GE4CVJRA1hcg-qmrfAellFsfVFrUL4KOt65-LzO9gvsJrBAHkkOJ_mID6QnnHqhYRpSX9pOzjh-XlSSH0wPXd7Y9z9S_lWl17fbaoyhyoQ_kLAdhJT4ReIbNbc3lRmTY_JHQQoTj_L8EBEB-WivUICBVMiRKpNXlFvbDyqBrJewe81X-jGamzE**86ea605347d41d0c1506d182bbd7c4b627ab8c9d9ae2b90a1e67fa1a0db29c6f*flER0VzgWgFh-BdTM1JS8e08y6_WeA1YmkArUFFdoto; akavpau_gp1=1586037754~id=f9acc83a86b6bfb54acbdfda8f33df82; TS01f4281b=0130aff232c11a89a91dc9c0ec260c9f713f27b58d95cb24f149683aaad51bdcab4ccfc88b13ed95e9b1790b691f62811971e012ca; TS01e1b9cb=0130aff232c11a89a91dc9c0ec260c9f713f27b58d95cb24f149683aaad51bdcab4ccfc88b13ed95e9b1790b691f62811971e012ca; TS01624fdb=0130aff232c11a89a91dc9c0ec260c9f713f27b58d95cb24f149683aaad51bdcab4ccfc88b13ed95e9b1790b691f62811971e012ca; TS01bae75b=01538efd7c8065ce3225abd8e3d3324f4b42cb56f379ef445d144d75c98980acdd1b6cf7cd13e6e6dd23d5ab183ed122d80df619f8; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiY29va2llIiwidXVpZCI6IjQ4ZWQzZTAwLTc2YmYtMTFlYS1iN2M4LThiMjA3NWYyMjgwMSIsImlhdCI6MTU4NjAzNzQ1MiwiZXhwIjoxNTg3MTE3NDUyfQ.dm7ob3oQy1tpQ7wWuZZcAOgUqweiSYnptkaDrML_OLA; akavpau_gp4=1586038052~id=b290e676f01fd24a9f8397fd3b473ce2
            sec-fetch-dest: document
            sec-fetch-mode: navigate
            sec-fetch-site: none
            sec-fetch-user: ?1
            upgrade-insecure-requests: 1
            user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36
        """


def header_generator(headers_string):
    headers_string = headers_string.replace('\n', '#').split('#')
    headers_string = [string.strip() for string in headers_string if string.strip()]

    headers = {}

    for header in headers_string:
        p, v = header.split(' ', 1)
        if ':' != p[0]:
            headers[p[:-1]] = v

    return headers
