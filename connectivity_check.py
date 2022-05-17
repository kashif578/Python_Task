from pyats import aetest

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       leaf1_name = 'LEAF1',
                       leaf2_name = 'LEAF2'):
        leaf1 = testbed.devices[leaf1_name]
        leaf2 = testbed.devices[leaf2_name]

        # add them to testscript parameters
        self.parent.parameters.update(leaf1 = leaf1, leaf2 = leaf2)

        # get corresponding links
        links = leaf1.find_links(leaf2)

        assert len(links) >= 1, 'require one link between ios1 and ios2'


    @aetest.subsection
    def establish_connections(self, steps, leaf1,leaf2):
        with steps.start('Connecting to %s' % leaf1.name):
            ios1.connect()

        with steps.start('Connecting to %s' % leaf2.name):
            ios2.connect()

@aetest.loop(device=('leaf1', 'leaf2'))
class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination=('131.226.217.151', '131.226.217.152'))
    def ping(self, device, destination):
        try:
            result = self.parameters[device].ping(destination)

        except Exception as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')

            logger.info('Ping {} with success rate of {}%'.format(
                                        destination,
                                        success_rate,
                                    )
                               )

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, leaf1, leaf2):
        with steps.start('Disconnecting from %s' % leaf1.name):
            leaf1.disconnect()

        with steps.start('Disconnecting from %s' % leaf2.name):
            leaf2.disconnect()

'''if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)
                        

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))'''
