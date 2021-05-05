import requests
import logging


def create_order():
    """[Create order function to create new order on enviame api]"""
    url = "https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries"

    headers = {
        "Accept": "application/json",
        "api-key": "7JuXLvWuhXrDQfyltN9I7mWSByNnla",
        "Content-Type": "application/json",
    }

    payload = {
        "shipping_order": {
            "n_packages": "1",
            "content_description": "ORDEN 255826267",
            "imported_id": "255826267",
            "order_price": "24509.0",
            "weight": "0.98",
            "volume": "1.0",
            "type": "delivery",
        },
        "shipping_origin": {"warehouse_code": "401"},
        "shipping_destination": {
            "customer": {
                "name": "Bernardita Tapia Riquelme",
                "email": "b.tapia@outlook.com",
                "phone": "977623070",
            },
            "delivery_address": {
                "home_address": {
                    "place": "Puente Alto",
                    "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto",
                }
            },
        },
        "carrier": {"carrier_code": "", "tracking_number": ""},
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        result = response.json()
    except Exception as e:
        logging.error(e)
        return e

    return result


print(create_order())
