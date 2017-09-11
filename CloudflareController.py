import CloudFlare


class CloudFlareController:

    def __init__(self, email, token):
        self.cf = CloudFlare.CloudFlare(email=email, token=token)

    def set_zone(self, subdomain, ip):
        print('Mock Setting zone')