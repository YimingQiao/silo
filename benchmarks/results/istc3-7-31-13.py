RESULTS = [({'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
             'numa_memory': '4G', 'persist': True, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
            [(29172.5, 29172.5, 0.0341824, 43.0112, 0.0), (29398.3, 29398.3, 0.0339165, 42.9486, 0.0),
             (28847.7, 28847.7, 0.0345633, 42.8973, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
                'numa_memory': '4G', 'persist': False, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(30468.6, 30468.6, 0.0327431, 0.0, 0.0), (29992.4, 29992.4, 0.0332567, 0.0, 0.0),
                (31170.2, 31170.2, 0.0320002, 0.0, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': True, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(103422.0, 103422.0, 0.0385643, 85.2116, 4.06392), (105666.0, 105666.0, 0.0377509, 60.8138, 3.93148),
                (104045.0, 104045.0, 0.0383381, 69.674, 4.63118)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': False, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(113136.0, 113136.0, 0.0352708, 0.0, 4.78329), (114626.0, 114626.0, 0.0348127, 0.0, 4.7333),
                (114772.0, 114772.0, 0.0347643, 0.0, 5.1833)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': True, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(197185.0, 197185.0, 0.0404586, 94.891, 8.41167), (197842.0, 197842.0, 0.0403221, 115.439, 7.94573),
                (197553.0, 197553.0, 0.0402832, 145.298, 8.4924)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': False, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(216956.0, 216956.0, 0.0367886, 0.0, 9.64994), (216944.0, 216944.0, 0.0367856, 0.0, 9.98321),
                (215150.0, 215150.0, 0.0370956, 0.0, 9.59995)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': True, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(296988.0, 296988.0, 0.0402945, 167.935, 12.127), (297616.0, 297616.0, 0.0402009, 213.303, 12.1242),
                (295502.0, 295502.0, 0.0404885, 258.694, 12.6107)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': False, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(316547.0, 316547.0, 0.0377822, 0.0, 13.4998), (321822.0, 321822.0, 0.0371894, 0.0, 13.4833),
                (318126.0, 318126.0, 0.037625, 0.0, 13.4665)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': True, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(391746.0, 391746.0, 0.0407244, 169.879, 16.0217), (386561.0, 386561.0, 0.041277, 181.483, 15.2751),
                (389939.0, 389939.0, 0.0409258, 162.949, 15.6935)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': False, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(423632.0, 423632.0, 0.0376798, 0.0, 18.3165), (425391.0, 425391.0, 0.0375244, 0.0, 18.3499),
                (422392.0, 422392.0, 0.0377958, 0.0, 17.9999)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': True, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(477401.0, 477401.0, 0.0417748, 99.8102, 18.5246), (484175.0, 484175.0, 0.0411903, 195.776, 19.9578),
                (485011.0, 485011.0, 0.0411185, 265.607, 20.8213)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': False, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(536948.0, 536948.0, 0.0371455, 0.0, 22.483), (538513.0, 538513.0, 0.0370509, 0.0, 23.383),
                (532447.0, 532447.0, 0.0374746, 0.0, 22.3997)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': True, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(573385.0, 573385.0, 0.0413281, 431.492, 23.0567), (570228.0, 570228.0, 0.041975, 220.776, 22.7373),
                (573395.0, 573395.0, 0.0417394, 145.422, 23.4863)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': False, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(632495.0, 632495.0, 0.0378555, 0.0, 27.383), (638658.0, 638658.0, 0.0374896, 0.0, 26.983),
                (631381.0, 631381.0, 0.0379224, 0.0, 26.5997)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': True, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(644206.0, 644206.0, 0.0427002, 1196.09, 26.5088), (635368.0, 635368.0, 0.0431587, 940.665, 26.4838),
                (645459.0, 645459.0, 0.0421841, 1584.15, 25.8248)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': False, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(728954.0, 728954.0, 0.0383087, 0.0, 31.2495), (730546.0, 730546.0, 0.0382386, 0.0, 30.0829),
                (731333.0, 731333.0, 0.0381883, 0.0, 32.0495)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': True, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(681638.0, 681638.0, 0.0464162, 935.341, 28.1929), (683559.0, 683559.0, 0.0464315, 731.81, 29.2552),
                (678029.0, 678029.0, 0.0468788, 612.582, 27.1238)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': False, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(799321.0, 799321.0, 0.0399277, 0.0, 34.0809), (799648.0, 799648.0, 0.0399073, 0.0, 35.415),
                (803230.0, 803230.0, 0.0397377, 0.0, 34.6826)])]
