from typing import Dict, Any


def get_stack_data():
    """Get all the stack data

    This is a testing utility to oganize data required by the troposhpere stack generation.


    RUNTIME (execution modes, credentials, verbosity, etc)

    GLOBAL (extra-environment data like connection mapping,  default enviroment data, environment list): an
    organization of environments and the data that connets them

    ENVIRONMENT (env) : an environemtn is a organization of resources that have common data. often a closed topology
    like a VPC, customer network, air-gapped network, etc. that has so


    :rtype: Dict[str, Any]
    """
    data = {'GLOBAL':
                {'mesh_vpc_peers': ['triangle_1', 'triangle_2', 'triangle_3' ],
                 'star_vpc_peers': {'middle': ['north', 'south', 'east', 'west']},
                 'one_to_one_vpc_peers': {'left_vpc': 'right_vpc', 'up_vpc': 'down_vpc'}
                 },
            'MANAGEMENT_VPC': {'vpc_peers': ['PRODUCTION_VPC', 'DEVELOPMENT_VPC', 'INTEGRATION_TEST_VPC'],


            }

    }
