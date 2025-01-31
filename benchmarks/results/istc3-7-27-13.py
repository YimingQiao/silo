RESULTS = [({'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
             'numa_memory': '4G', 'persist': True, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
            [(27932.9, 25707.6, 0.0357025, 43.6693, 0.0), (27225.1, 25056.8, 0.0366308, 44.4688, 0.0),
             (26066.5, 23989.5, 0.038259, 51.7758, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
                'numa_memory': '4G', 'persist': False, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(30559.4, 0.0, 0.0326457, 0.0, 0.0), (30975.7, 0.0, 0.0322002, 0.0, 0.0),
                (30263.2, 0.0, 0.0329574, 0.0, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': True, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(104089.0, 95747.0, 0.0383247, 52.3198, 4.4979), (103967.0, 95633.5, 0.0383704, 65.3959, 4.14833),
                (104624.0, 96239.2, 0.0381277, 52.0013, 4.71454)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': False, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(112168.0, 0.0, 0.0355806, 0.0, 5.63329), (111897.0, 0.0, 0.0356603, 0.0, 4.69996),
                (112498.0, 0.0, 0.0354715, 0.0, 4.73329)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': True, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(187507.0, 172508.0, 0.042552, 153.726, 7.24524), (193159.0, 177704.0, 0.0413084, 94.652, 8.22911),
                (186911.0, 171962.0, 0.042691, 127.489, 7.61311)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': False, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(215159.0, 0.0, 0.0371015, 0.0, 9.03326), (215075.0, 0.0, 0.0371126, 0.0, 9.09989),
                (215787.0, 0.0, 0.0369858, 0.0, 9.3166)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': True, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(274235.0, 252266.0, 0.0436398, 166.333, 11.3754), (273407.0, 251499.0, 0.0437674, 201.409, 10.809),
                (269463.0, 247877.0, 0.0444047, 248.662, 11.0905)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': False, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(319060.0, 0.0, 0.0375294, 0.0, 13.3831), (313453.0, 0.0, 0.0381976, 0.0, 13.5831),
                (314425.0, 0.0, 0.0380777, 0.0, 13.5998)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': True, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(331782.0, 305201.0, 0.0477054, 859.518, 12.9499), (325504.0, 299429.0, 0.0486297, 898.045, 12.6247),
                (330611.0, 304123.0, 0.0479017, 897.195, 12.4785)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': False, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(412063.0, 0.0, 0.0387433, 0.0, 17.3998), (412653.0, 0.0, 0.0386915, 0.0, 17.7665),
                (414960.0, 0.0, 0.0384705, 0.0, 18.1831)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': True, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(351266.0, 323144.0, 0.0562856, 1207.4, 12.566), (358881.0, 330150.0, 0.054982, 1246.28, 12.3676),
                (356129.0, 327621.0, 0.055508, 1230.4, 11.84)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': False, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(503789.0, 0.0, 0.0396117, 0.0, 23.033), (502896.0, 0.0, 0.0396838, 0.0, 22.1998),
                (491385.0, 0.0, 0.0406139, 0.0, 22.6164)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': True, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(377349.0, 347108.0, 0.0623337, 1848.23, 12.2314), (384724.0, 353894.0, 0.0610587, 2023.77, 12.5417),
                (380727.0, 350213.0, 0.0620179, 1863.16, 11.978)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': False, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(572058.0, 0.0, 0.0418715, 0.0, 25.5163), (595977.0, 0.0, 0.0401823, 0.0, 25.7497),
                (570526.0, 0.0, 0.0419793, 0.0, 24.783)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': True, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(392417.0, 360987.0, 0.0696299, 2461.2, 12.0009), (391837.0, 360453.0, 0.0695999, 2344.58, 12.6564),
                (390281.0, 359022.0, 0.069838, 2547.39, 11.9206)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': False, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(649335.0, 0.0, 0.0430346, 0.0, 28.4162), (652786.0, 0.0, 0.0428061, 0.0, 28.8829),
                (646301.0, 0.0, 0.0432359, 0.0, 29.3662)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': True, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(380778.0, 350266.0, 0.0815702, 5329.71, 11.6806), (381149.0, 350607.0, 0.0806715, 4643.52, 12.0704),
                (380764.0, 350254.0, 0.080364, 5234.89, 11.7478)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': False, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(714670.0, 0.0, 0.0446695, 0.0, 32.466), (731601.0, 0.0, 0.0436383, 0.0, 32.7657),
                (717230.0, 0.0, 0.0445168, 0.0, 31.9157)])]
