from dynamorm import DynaModel, ProjectAll, LocalIndex

from marshmallow.fields import String, Integer, Date

from api.common.constants import TABLE_NAME


class Rave(DynaModel):
    class Table:
        name = TABLE_NAME
        hash_key = 'pk'
        range_key = 'sk'
        read = 1
        write = 1

    class ByAlternateKey(LocalIndex):
        name = 'alt-key'
        hash_key = 'alt_key'
        range_key = 'status_date'
        projection = ProjectAll()
        read = 1
        write = 1

    class ByStatusAddressKey(LocalIndex):
        name = 'status-addr-key'
        hash_key = 'status'
        range_key = 'addr_key'
        projection = ProjectAll()
        read = 1
        write = 1

    class ByGeoHash6(LocalIndex):
        name = 'geohash-6'
        hash_key = 'geohash_6'
        range_key = 'geohash_7'
        projection = ProjectAll()
        read = 1
        write = 1

    class ByGeoHash7(LocalIndex):
        name = 'geohash-7'
        hash_key = 'geohash_7'
        range_key = 'geohash_8'
        projection = ProjectAll()
        read = 1
        write = 1

    class ByGeoHash8(LocalIndex):
        name = 'geohash-8'
        hash_key = 'geohash_8'
        projection = ProjectAll()
        read = 1
        write = 1

    class ByStatusAge(LocalIndex):
        name = 'status-age'
        hash_key = 'status'
        range_key = 'status_date'
        projection = ProjectAll()
        read = 1
        write = 1

    # Define our data schema, each property here will become a property on instances of the BFC class
    class Schema:
        pk = String()
        sk = String()
        alt_key = String()
        addr_key = String()
        address = String()
        details = String()
        # list_sold_price = Integer()
        # arv = Integer()
        condition = String()
        status = String()
        status_date = Integer()
        geohash_8 = String()
        geohash_7 = String()
        geohash_6 = String()
