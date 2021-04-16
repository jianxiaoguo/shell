# pip inestall pyjwt requests cryptography

import jwt
from cryptography.hazmat.primitives import serialization
import requests
from jwt import PyJWKClient
import sys

def to_rsa_pem(key):
    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
    pubk_bytes = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
    return pubk_bytes.decode()

def get_key_from_url(url):
    # {
    #     "keys": [
    #         {
    #         "alg": "RS256",
    #         "use": "sig",
    #         "kid": "1LCB7g0Wz_goBFlf32BHFIg3II4eKRRh_yFzeBdMcvg",
    #         "e": "AQAB",
    #         "kty": "RSA",
    #         "n": "wSF0Be7Pq2VnOLN735fqdt5CAPTDYgjz3kqrRuc7T1IF55SRcp3cu8nxByGR_UQBiZVOniuhnZP1swn5Q7-d5QqSX-Bof2oAWPGvNHW6YxDowZpphYvHvMhdCIckSRavQ4o4mZ7D24Q9DB7SYxDUrwHwYX5IN_pvjCcwf9rWW8s63rsLjhhfx565VjM-N3ar_Bs9pEmwkngJ3PUWrrk9Ri4TTsy8J63gdTEiZItls5HiFXRvkfH_m_MzZ6E1wWQRrgG8cD0Ob6-Sk0w3sCgclrqAJyV-mU7gJvIbGaNhnVFPtkSyPhiokoILirR5dqQH2XcuRUxu-vLD_Aw20G7qKH0ATxdmJv_d6W-NSwQB1mDugvSrPry5MBBzm8DXTbZqbH6_Ivf3M3jhY39t0fCl43kEHFEv9AbsN9XnfEgbovBrmV8cAVT-0nHGmR65zop7rRJr9u0XjZDVbH6T4fjhyH2ieEN8juwNTQ6sPw_czgBTNL1SWHMMpe3jHsGtRRso0uL_0Rpi-pW0aVw_BOJYqYVWFpdvH6MWSizeTbL-Tg-HEBrAILQtbLZc8H48CENIuSaoqCbYLwx5z_zL9UVr9tUsri45kTYKt_6zRunMxz58vyoNCf7XgLefhiA6yWRcQ41w9MYIN6UpkT1FIjvIEiesMFGQvP8ad167G10YHss"
    #         }
    #     ]
    # }
    for k in requests.get(url).json()['keys']:
        pem = to_rsa_pem(k)
        print(pem)
        return pem


if __name__ == '__main__':
    pem = get_key_from_url("https://p.uucin.com/oauth/.well-known/jwks.json")

    encoded = 'eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiIsICJraWQiOiAiMUxDQjdnMFd6X2dvQkZsZjMyQkhGSWczSUk0ZUtSUmhfeUZ6ZUJkTWN2ZyJ9.eyJhdWQiOiAiQjZ5UTR0Vzl3Z1IxMGJscmtsOVZkNWwzNzFsVWhDRzk4U01yemZ3UyIsICJpYXQiOiAxNjE4NDQ3OTEyLCAiYXRfaGFzaCI6ICJPY1B6ZzRxanZtU2Q4MUpWc19IMG1BIiwgInN1YiI6ICIxOCIsICJpc3MiOiAiaHR0cDovL3AudXVjaW4uY29tL29hdXRoIiwgImV4cCI6IDE2MjEwMzk5MTIsICJhdXRoX3RpbWUiOiAxNjE4NDQ3OTA4LCAianRpIjogIjU4MGIzODJlLWMzODctNDY4OC04MTVmLWQzYTdiOTM4ODkwNSJ9.t4GrmCUa6SuHczFyyEDkc8t1Cow6dO1L4jaFa81WfMTxKMoi9qjJTfEdN6aPlivIJwkmVD_Isxp7EHRJKR0VZ7zy7EoNueuB8LTKVfQqMqYpXwAPry7mbv5oy8KOod2hK7CfNp8P25V82_IruDusj6tuFzcFJiM-f2ukYfwqTHqYI8-TebvC-5pujOWtQTuwRcsX7nQjMayr-0TQpEmsPCq2IEinBpzOUzJY6YYZw2oRpr922rJdza11Npn5pRbgNOli3CYlyVzn_FzvWnWThDR6NgmuD--2iAsFjIFNbogcGukk7Sc5D7aUuVy-e6Ug9ATXDmGCPZq00P_iQ2IVikWoABhfVxir5zpinYza8exX_WUH9wKJ6fDclbW1SkiuUnhTkg1KNYuU44eoRmcy3gMz3CBDhnjipo7JHXHftw1A0LX7WfZUoiV6N_wHPUXZpyRO2LBf5Uy986ISnVO7jUDfS5xyO2mKDyhovIBX4vUN2K4JWlXE9_2e4luywsmVbHUGnOjLGGWwTdA6Flkkp_A6kVHrTWxI2NQiVYzQYTdU1Zmq57ammF9FJJrCLPCubX_UgFz9tJeXkpobl-Qz9rzTPRj-i-sDP--dOn73LzS6YLCmbHSKrVnbb7_tpCMZzWW_VDxxcGntTnNrBtdPsoaoyZIN6MR5Hos5YLVcVsE'
    # id_token['aud'] = request.client_id   # django-oauth-toolkit
    aud = 'B6yQ4tW9wgR10blrkl9Vd5l371lUhCG98SMrzfwS' 
    decoded = jwt.decode(encoded, pem, algorithms=["RS256"], audience=aud, options={"verify_signature": True})


# import jwt
# from jwt import PyJWKClient
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5FRTFRVVJCT1RNNE16STVSa0ZETlRZeE9UVTFNRGcyT0Rnd1EwVXpNVGsxUWpZeVJrUkZRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi04N2V2eDlydS5hdXRoMC5jb20vIiwic3ViIjoiYVc0Q2NhNzl4UmVMV1V6MGFFMkg2a0QwTzNjWEJWdENAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZXhwZW5zZXMtYXBpIiwiaWF0IjoxNTcyMDA2OTU0LCJleHAiOjE1NzIwMDY5NjQsImF6cCI6ImFXNENjYTc5eFJlTFdVejBhRTJINmtEME8zY1hCVnRDIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.PUxE7xn52aTCohGiWoSdMBZGiYAHwE5FYie0Y1qUT68IHSTXwXVd6hn02HTah6epvHHVKA2FqcFZ4GGv5VTHEvYpeggiiZMgbxFrmTEY0csL6VNkX1eaJGcuehwQCRBKRLL3zKmA5IKGy5GeUnIbpPHLHDxr-GXvgFzsdsyWlVQvPX2xjeaQ217r2PtxDeqjlf66UYl6oY6AqNS8DH3iryCvIfCcybRZkc_hdy-6ZMoKT6Piijvk_aXdm7-QQqKJFHLuEqrVSOuBqqiNfVrG27QzAPuPOxvfXTVLXL2jek5meH6n-VWgrBdoMFH93QEszEDowDAEhQPHVs0xj7SIzA"
# kid = "NEE1QURBOTM4MzI5RkFDNTYxOTU1MDg2ODgwQ0UzMTk1QjYyRkRFQw"
# url = "https://p.uucin.com/oauth/.well-known/jwks.json"
# jwks_client = PyJWKClient(url)
# signing_key = jwks_client.get_signing_key_from_jwt(token)
# data = jwt.decode(
#     token,
#     signing_key.key,
#     algorithms=["RS256"],
#     audience=client_id,
#     options={"verify_exp": False},
# )
# print(data)
# {'iss': '***', 'sub': 'aW4Cca79xReLWUz0aE2H6kD0O3cXBVtC@clients', 'aud': ***, 'iat': 1572006954, 'exp': 1572006964, 'azp': 'aW4Cca79xReLWUz0aE2H6kD0O3cXBVtC', 'gty': 'client-credentials'}
