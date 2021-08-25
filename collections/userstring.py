import re
from collections import UserString

uri_format = r"(?P<scheme>.+)://(?P<host>[^:]+)(:(?P<port>[0-9]+))?(?P<path>[^\?]*)?(\?(?P<query>.*))?"


class URI(UserString):
    @property
    def scheme(self):
        return re.match(uri_format, self.data).groupdict()["scheme"]

    @property
    def host(self):
        return re.match(uri_format, self.data).groupdict()["host"]

    @property
    def port(self):
        return re.match(uri_format, self.data).groupdict().get("port")

    @property
    def path(self):
        return re.match(uri_format, self.data).groupdict().get("path")

    @property
    def query(self):
        return re.match(uri_format, self.data).groupdict().get("query")


google = URI("http://google.com")
query = URI("https://my.cool.app:4242/restaurant/eat?food=pizza")
print(google + ", " + query)

print(google.scheme, google.host)
print(query.path, query.query)
