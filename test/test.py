import os
import requests

from qubell.api.testing import *
@environment({
    "default": {}
})
class ApacheKafkaComponent(BaseComponentTestCase):
    name = "component-kafka"
    destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))
    meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml'))
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
  }]

    @classmethod
    def timeout(cls):
        return 30

    @instance(byApplication=name)
    def test_kafka_manager(self, instance):
        host = instance.returnValues['output.ui']
        resp = requests.get(host, verify=False)
        assert resp.status_code == 200

