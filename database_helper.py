from firebase import db
from requests import get
from helpers import header_generator
import constants


def check_zip_store_exists(zip_code):
    try:
        return {"time_slots": db.collection('stores').document('Walmart').collection('zips').document(zip_code).get().to_dict()["time_slots"], "error_message": None}
    except:
        return {"time_slots": None, "error_message": None}


def add_new_store(zip_code):
    address_data_response = get(
        'https://grocery.walmart.com/v4/api/serviceAvailability?postalCode={}'.format(zip_code))
    if address_data_response.status_code < 300:
        address_data_response = address_data_response.json()
        if 'accessPointList' not in address_data_response:
            return {"error_message": 'No nearby Walmarts', "time_slots": None}

        access_points = address_data_response['accessPointList']
        if len(access_points):
            nearest_delivery_stores = list(filter(lambda x: x['fulfillmentType'] == 'DELIVERY', access_points))
            if not len(nearest_delivery_stores):
                return {"error_message": 'No nearby Walmarts that offer delivery', "time_slots": None}
            nearest_store = nearest_delivery_stores[0]
            access_point_id = nearest_store['accessPointId']
            dispense_store_id = nearest_store['dispenseStoreId']
            available_slots = get(
                """
                    https://grocery.walmart.com/v4/api/accessPoints/{}/slots?
                    contractId=9be66b06-c556-4d58-ac92-b84c35ee822f&
                    fulfillmentType=DELIVERY&storeId={}
                    &plans=true&express=true&mergedSlots=true&restrictedSlots=true
                """.replace('\n', '').replace(' ', '').format(access_point_id, dispense_store_id),
                headers=header_generator(constants.walmart_header_string)
            )
            if available_slots.status_code < 300:
                available_slots = available_slots.json()
                available_delivery_slots = []
                for slots_day in available_slots['slotDays']:
                    for slot in slots_day['slots']:
                        if slot['available']:
                            new_slot_dict = dict(slot)
                            new_slot_dict['day'] = slots_day['day']
                            available_delivery_slots.append(new_slot_dict)
                db.collection('stores').document('Walmart').collection('zips').document(zip_code).set(
                    {'time_slots': available_delivery_slots, 'access_point_id': access_point_id, 'store_id': dispense_store_id})
                return {"error_message": None, "time_slots": available_delivery_slots}
            else:
                return {"error_message": 'No nearby Walmarts', "time_slots": None}
        else:
            return {"error_message": 'Error loading data', "time_slots": None}
