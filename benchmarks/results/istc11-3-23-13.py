RESULTS = [({'bench_opts': '--enable-separate-tree-per-partition --enable-partition-locks', 'scale_factor': 8,
             'name': 'multipart:cpu', 'db': 'kvdb', 'bench': 'tpcc', 'par_load': True, 'threads': 8},
            [(222921.0, 0.0), (227359.0, 0.0), (229843.0, 0.0)]), (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 8}, [(195168.0, 9.73322), (194644.0, 9.84993), (194702.0, 9.44992)]), (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 12}, [(237444.0, 37277.3), (234301.0, 36610.4), (236327.0, 36780.5)]), (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 16}, [(284964.0, 73789.8), (290414.0, 74756.3), (276865.0, 71355.9)]), (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 20}, [(301047.0, 123422.0), (282959.0, 115540.0), (287034.0, 115244.0)]),
           (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 24}, [(296876.0, 159299.0), (298336.0, 159218.0), (302464.0, 162004.0)]),
           (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 28}, [(246765.0, 157871.0), (270421.0, 171978.0), (254094.0, 160962.0)]),
           (
               {'bench_opts': '', 'scale_factor': 8, 'name': 'multipart:cpu', 'db': 'ndb-proto2', 'bench': 'tpcc',
                'par_load': False, 'threads': 32}, [(230114.0, 167878.0), (226383.0, 165009.0), (227876.0, 165982.0)])]
