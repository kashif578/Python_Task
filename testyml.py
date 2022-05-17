
from pyats.topology import loader
testbed = loader.load('testbed1.yaml')


testbed.devices
LEAF_1 = testbed.devices['LEAF1']
LEAF_2 = testbed.devices['LEAF2']


for link in LEAF_1.find_links(ios_2):
    print(repr(link))


LEAF_1.connect()


print(LEAF1.execute('show version'))
LEAF_1.configure('''
    interface GigabitEthernet0/0
        ip address 131.226.217.151 
''')

LEAF_2.connect(alias = 'console', via = 'a')
LEAF_2.connect(alias = 'vty_1', via = 'vty')


LEAF_2.vty_1.execute('show running')
LEAF_2.console.execute('reload')


LEAF_2.start_pool(alias = 'pool', size = 2)


def sleep(seconds):
    LEAF_2.pool.execute('sleep %s' % seconds)
import multiprocessing
p1 = multiprocessing.Process(target=sleep, args = (10, ))
p2 = multiprocessing.Process(target=sleep, args = (10, ))
p3 = multiprocessing.Process(target=sleep, args = (10, ))
p1.start(); p2.start(); p3.start()
p1.join(); p2.join(); p3.join()
