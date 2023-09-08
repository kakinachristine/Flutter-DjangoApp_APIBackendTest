from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import json

# Replace this connection string with your actual MongoDB server connection string
MONGODB_CONNECTION_STRING = ""
DB_NAME = ""
COLLECTION_NAME = ""

@csrf_exempt
def save_contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            phone_number = data.get('phone_number')

            if email and phone_number:
                client = MongoClient(MONGODB_CONNECTION_STRING)
                db = client[DB_NAME]
                collection = db[COLLECTION_NAME]

                # Prepare user data
                user_data = {
                    "email": email,
                    "phone_number": phone_number,
                }

                # Insert user data into MongoDB
                collection.insert_one(user_data)
                client.close()
                return JsonResponse({"message": "Contact saved successfully"})
            else:
                return JsonResponse({"error": "Invalid data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid request method")

@csrf_exempt
def get_contacts(request):
    if request.method == 'GET':
        try:
            client = MongoClient(MONGODB_CONNECTION_STRING)
            db = client[DB_NAME]
            collection = db[COLLECTION_NAME]

            # Retrieve all user data from MongoDB
            contacts = list(collection.find({}, {'_id': 0}))
            client.close()

            return JsonResponse({"contacts": contacts})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Invalid request method")
