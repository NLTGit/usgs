
from usgs import api

class ERSClient():
    last_error = ""
    catalog_id = None
    api_version = None
    api_key = None
    api_key_timeout = None
    access_level = None
    api_userid = None

    def __init__(self, userid, password, catalog_id):
        self.api_userid = userid
        self.catalog_id = catalog_id
        # login
        self.api_key = api.login(userid, password, save=False, catalogId=catalog_id)

    def logout(self):
        resp = api.logout(self.apikey)
        self.api_key = None
        return resp
        
    def datasets(self, dataset, node, ll=None, ur=None, start_date=None, end_date=None, api_key=None):
        resp = api.datasets(dataset, node, ll, ur, start_date, end_date, api_key=self.api_key)
        if resp > '':
            return resp
        else:
            return '[]'
    
    def search(self, dataset, node, lat=None, lng=None, distance=100, ll=None, ur=None, start_date=None, end_date=None,
           where=None, max_results=50000, starting_number=1, sort_order="DESC", extended=False):
        return api.search(dataset, node, lat, lng, distance, ll, ur, start_date, end_date,
           where, max_results, starting_number, sort_order, extended=extended, api_key=self.api_key)
    
    def metadata(self, dataset, node, entityids, extended=False):
        return api.metadata(dataset, node, entityids, extended=extended, api_key=self.api_ley)
    
    def dataset_fields(self, dataset, node):
        return api.dataset_fields(dataset, node, api_key=self.api_key)

