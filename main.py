import requests
import json


def get_data():

    cookies = {
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_TIMEZONE_OFFSET': '3',
        '_ym_uid': '168502595847674686',
        '_ym_d': '1685025958',
        'tmr_lvid': 'f62c6412a02430938d7d762ad54794d5',
        'tmr_lvidTS': '1685025960479',
        'uxs_uid': 'ddd60970-fb0a-11ed-86f0-772398eb862c',
        'afUserId': '38b0eb83-2bef-4d11-9fd4-38ceee799cfb-p',
        'flocktory-uuid': '7f33a92f-7a88-4226-af41-0031f424221f-0',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'cookie_ip_add': '109.252.120.176',
        '__lhash_': 'fe9ac3152b49f72b4fc7814c06dd028d',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'MVID_GUEST_ID': '22646864107',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'vQQ1kSCC3QZhhkSVTD0BPX5yp0rwRTgCSSCVYgdgT0kzMMCsRCyT!-1986495864',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'HINTS_FIO_COOKIE_NAME': '2',
        'searchType2': '2',
        'COMPARISON_INDICATOR': 'false',
        'CACHE_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80': '2936331274.20480.0000',
        'bIPs': '672961728',
        '_gid': 'GA1.2.1948375534.1687290405',
        '_sp_ses.d61c': '*',
        '_ym_isad': '1',
        'SMSError': '',
        'authError': '',
        'advcake_track_id': '014cc512-47b2-f98a-f9da-72a6b8ee0981',
        'advcake_session_id': '761572b7-01cb-bed9-eabc-f29bc4e2a3aa',
        'AF_SYNC': '1687290411949',
        '_ga': 'GA1.2.63361750.1685025957',
        'tmr_detect': '0%7C1687291618765',
        '__hash_': '61f2f160e88e8f6687549961dca7e0d3',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'gssc218': '',
        'gsscgib-w-mvideo': '+tTtdzBjh6W3XU58jmRNz82b4ygh5g+uqM1ph7i/x2hli0fxt2IzWxtDme/fL341Pr2apBDspsv9ih/WzxXmxK/mjwawMMVRdu0MJh3c8khtzeKzTkVr4pxlh5sPOBUhubamr6O8bsxw3zMQ2MSR6kmOq1ISMC19b868zFqfYoEfiRFGnSlhxDC/h8P5ipicZAu5U6qynloSvXIS0Ir4xJBVQuMEv5jz//f9KP4JUQntk5S3bMFXu/e7BKg4+w==',
        'gsscgib-w-mvideo': '+tTtdzBjh6W3XU58jmRNz82b4ygh5g+uqM1ph7i/x2hli0fxt2IzWxtDme/fL341Pr2apBDspsv9ih/WzxXmxK/mjwawMMVRdu0MJh3c8khtzeKzTkVr4pxlh5sPOBUhubamr6O8bsxw3zMQ2MSR6kmOq1ISMC19b868zFqfYoEfiRFGnSlhxDC/h8P5ipicZAu5U6qynloSvXIS0Ir4xJBVQuMEv5jz//f9KP4JUQntk5S3bMFXu/e7BKg4+w==',
        '_sp_id.d61c': 'a815b686-fd17-4aae-a3f0-068544ee2543.1685025958.3.1687292950.1685034125.76331b43-a03c-4fb4-9a75-9cc6807f1d7b.7a29e07e-f126-43fe-9173-02a106faaf29.c708d553-ceda-4a3e-b4d5-016744b12c99.1687290405557.36',
        'fgsscgib-w-mvideo': 'o4k7c524a017a3c9a7945b2726964a068e19dbb0',
        'fgsscgib-w-mvideo': 'o4k7c524a017a3c9a7945b2726964a068e19dbb0',
        'cfidsgib-w-mvideo': 'kSu9Jw2KdLVmzv8KYLCeuLzhHO0ZqvWhSGD2XD3FhF3zV22hxByXrBCHuNW8jYW05dSSs7aLjLIG8peyUix4mtEw9aSQIdQwPorQwcTf9uElOxFZayr/LU8/TtVgRmlHKcrn2p018AdJVsJTc7YLx9UITBkpjONIpwO/xQ==',
        '_ga_CFMZTSS5FM': 'GS1.1.1687290405.3.1.1687292953.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1687290405.3.1.1687292953.50.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=a675c7700fbd415a9b1a6635afc208af,sentry-sample_rate=0.5',
        'cookie': 'MVID_CITY_ID=CityCZ_975; MVID_KLADR_ID=7700000000000; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_TIMEZONE_OFFSET=3; _ym_uid=168502595847674686; _ym_d=1685025958; tmr_lvid=f62c6412a02430938d7d762ad54794d5; tmr_lvidTS=1685025960479; uxs_uid=ddd60970-fb0a-11ed-86f0-772398eb862c; afUserId=38b0eb83-2bef-4d11-9fd4-38ceee799cfb-p; flocktory-uuid=7f33a92f-7a88-4226-af41-0031f424221f-0; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; cookie_ip_add=109.252.120.176; __lhash_=fe9ac3152b49f72b4fc7814c06dd028d; MVID_AB_TOP_SERVICES=1; MVID_ACTOR_API_AVAILABILITY=true; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_SERVICES=111; MVID_SP=true; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; MVID_GUEST_ID=22646864107; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=vQQ1kSCC3QZhhkSVTD0BPX5yp0rwRTgCSSCVYgdgT0kzMMCsRCyT!-1986495864; MVID_CALC_BONUS_RUBLES_PROFIT=false; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=false; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; HINTS_FIO_COOKIE_NAME=2; searchType2=2; COMPARISON_INDICATOR=false; CACHE_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80=2936331274.20480.0000; bIPs=672961728; _gid=GA1.2.1948375534.1687290405; _sp_ses.d61c=*; _ym_isad=1; SMSError=; authError=; advcake_track_id=014cc512-47b2-f98a-f9da-72a6b8ee0981; advcake_session_id=761572b7-01cb-bed9-eabc-f29bc4e2a3aa; AF_SYNC=1687290411949; _ga=GA1.2.63361750.1685025957; tmr_detect=0%7C1687291618765; __hash_=61f2f160e88e8f6687549961dca7e0d3; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; gssc218=; gsscgib-w-mvideo=+tTtdzBjh6W3XU58jmRNz82b4ygh5g+uqM1ph7i/x2hli0fxt2IzWxtDme/fL341Pr2apBDspsv9ih/WzxXmxK/mjwawMMVRdu0MJh3c8khtzeKzTkVr4pxlh5sPOBUhubamr6O8bsxw3zMQ2MSR6kmOq1ISMC19b868zFqfYoEfiRFGnSlhxDC/h8P5ipicZAu5U6qynloSvXIS0Ir4xJBVQuMEv5jz//f9KP4JUQntk5S3bMFXu/e7BKg4+w==; gsscgib-w-mvideo=+tTtdzBjh6W3XU58jmRNz82b4ygh5g+uqM1ph7i/x2hli0fxt2IzWxtDme/fL341Pr2apBDspsv9ih/WzxXmxK/mjwawMMVRdu0MJh3c8khtzeKzTkVr4pxlh5sPOBUhubamr6O8bsxw3zMQ2MSR6kmOq1ISMC19b868zFqfYoEfiRFGnSlhxDC/h8P5ipicZAu5U6qynloSvXIS0Ir4xJBVQuMEv5jz//f9KP4JUQntk5S3bMFXu/e7BKg4+w==; _sp_id.d61c=a815b686-fd17-4aae-a3f0-068544ee2543.1685025958.3.1687292950.1685034125.76331b43-a03c-4fb4-9a75-9cc6807f1d7b.7a29e07e-f126-43fe-9173-02a106faaf29.c708d553-ceda-4a3e-b4d5-016744b12c99.1687290405557.36; fgsscgib-w-mvideo=o4k7c524a017a3c9a7945b2726964a068e19dbb0; fgsscgib-w-mvideo=o4k7c524a017a3c9a7945b2726964a068e19dbb0; cfidsgib-w-mvideo=kSu9Jw2KdLVmzv8KYLCeuLzhHO0ZqvWhSGD2XD3FhF3zV22hxByXrBCHuNW8jYW05dSSs7aLjLIG8peyUix4mtEw9aSQIdQwPorQwcTf9uElOxFZayr/LU8/TtVgRmlHKcrn2p018AdJVsJTc7YLx9UITBkpjONIpwO/xQ==; _ga_CFMZTSS5FM=GS1.1.1687290405.3.1.1687292953.0.0.0; _ga_BNX5WPP3YK=GS1.1.1687290405.3.1.1687292953.50.0.0',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'a675c7700fbd415a9b1a6635afc208af-ad4e82a7c4ca65de-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.2.625 Yowser/2.5 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-set-application-id': '98933b01-f6c4-4620-977f-42fc915bf6e6',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)

def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()