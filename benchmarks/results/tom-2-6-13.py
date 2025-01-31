DBS = ('ndb-proto1', 'ndb-proto2')
THREADS = (1, 2, 4, 8, 16, 24, 32, 40, 48)
TXN_FLAGS = (1,)
SCALE_FACTORS = (10,)
BENCHMARKS = ('tpcc',)
RESULTS = [({'scale_factor': 10, 'threads': 1, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 1484.09),
           ({'scale_factor': 10, 'threads': 2, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 2890.06),
           ({'scale_factor': 10, 'threads': 4, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 5741.49),
           ({'scale_factor': 10, 'threads': 8, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 11037.6),
           ({'scale_factor': 10, 'threads': 16, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 18200.4),
           ({'scale_factor': 10, 'threads': 24, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 23739.9),
           ({'scale_factor': 10, 'threads': 32, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 28485.0),
           ({'scale_factor': 10, 'threads': 40, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 32868.2),
           ({'scale_factor': 10, 'threads': 48, 'txn_flags': 1, 'db': 'ndb-proto1', 'bench': 'tpcc'}, 36221.4),
           ({'scale_factor': 10, 'threads': 1, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 1479.2),
           ({'scale_factor': 10, 'threads': 2, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 2928.76),
           ({'scale_factor': 10, 'threads': 4, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 5767.42),
           ({'scale_factor': 10, 'threads': 8, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 11211.6),
           ({'scale_factor': 10, 'threads': 16, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 19651.7),
           ({'scale_factor': 10, 'threads': 24, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 26213.1),
           ({'scale_factor': 10, 'threads': 32, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 31440.7),
           ({'scale_factor': 10, 'threads': 40, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 35715.4),
           ({'scale_factor': 10, 'threads': 48, 'txn_flags': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'}, 40504.7)]
