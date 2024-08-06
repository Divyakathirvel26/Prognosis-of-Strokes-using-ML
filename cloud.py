from sqlite3 import connect
from cloudant.client import Cloudant
client = Cloudant.iam("367e91e7-6150-4f63-92f4-24625af53457-bluemix", "EqKm5BOKxzGLIm9YsFnXKJ66ywOyL9tDVK9oN0_FPD4G", connect = True)
my_database = client.create_database('my_database')