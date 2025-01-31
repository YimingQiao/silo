RESULTS = [({'scale_factor': 1, 'db': 'ndb-proto2', 'par_load': False, 'threads': 1, 'bench_opts': '',
             'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '4G',
             'persist': True},
            [(28037.0, 28037.0, 0.0355513, 80.7772, 0.0), (28591.2, 28591.2, 0.0348332, 83.3726, 0.0),
             (28174.9, 28174.9, 0.0353661, 80.9923, 0.0)]), (
               {'scale_factor': 4, 'db': 'ndb-proto2', 'par_load': False, 'threads': 4, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '16G',
                'persist': True},
               [(101575.0, 101575.0, 0.0392489, 100.616, 4.06351), (104315.0, 104315.0, 0.0382123, 92.747, 4.44552),
                (103600.0, 103600.0, 0.0384777, 104.11, 4.54582)]), (
               {'scale_factor': 8, 'db': 'ndb-proto2', 'par_load': False, 'threads': 8, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '32G',
                'persist': True},
               [(198630.0, 198630.0, 0.0401546, 114.32, 8.11104), (201243.0, 201243.0, 0.039627, 156.711, 7.31041),
                (199076.0, 199076.0, 0.0400534, 119.783, 8.10939)]), (
               {'scale_factor': 12, 'db': 'ndb-proto2', 'par_load': False, 'threads': 12, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '48G',
                'persist': True},
               [(298566.0, 298566.0, 0.0400453, 133.356, 12.1187), (298133.0, 298133.0, 0.040098, 99.2246, 13.4485),
                (296903.0, 296903.0, 0.0402781, 124.433, 12.3886)]), (
               {'scale_factor': 16, 'db': 'ndb-proto2', 'par_load': False, 'threads': 16, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '64G',
                'persist': True},
               [(391792.0, 391792.0, 0.0407065, 118.188, 17.0175), (391965.0, 391965.0, 0.0406917, 111.37, 16.8899),
                (390145.0, 390145.0, 0.0408607, 110.049, 15.7134)]), (
               {'scale_factor': 20, 'db': 'ndb-proto2', 'par_load': False, 'threads': 20, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '80G',
                'persist': True},
               [(490782.0, 490782.0, 0.0406097, 118.621, 19.6794), (491448.0, 491448.0, 0.0405582, 117.648, 19.7812),
                (490189.0, 490189.0, 0.0406614, 146.335, 19.8124)]), (
               {'scale_factor': 24, 'db': 'ndb-proto2', 'par_load': False, 'threads': 24, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '96G',
                'persist': True},
               [(579773.0, 579773.0, 0.0412569, 163.993, 23.5593), (582446.0, 582446.0, 0.0410567, 105.998, 25.318),
                (576929.0, 576929.0, 0.0414494, 104.131, 23.6849)]), (
               {'scale_factor': 28, 'db': 'ndb-proto2', 'par_load': False, 'threads': 28, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '112G',
                'persist': True},
               [(670070.0, 670070.0, 0.041655, 103.69, 27.1961), (669347.0, 669347.0, 0.0416867, 141.835, 27.8873),
                (669634.0, 669634.0, 0.0416696, 102.389, 26.9551)]), (
               {'scale_factor': 32, 'db': 'ndb-proto2', 'par_load': False, 'threads': 32, 'bench_opts': '',
                'log_fake_writes': False, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '128G',
                'persist': True},
               [(712434.0, 712434.0, 0.0447644, 214.95, 29.8936), (700382.0, 700382.0, 0.0455139, 240.664, 27.8856),
                (712480.0, 712480.0, 0.0447631, 234.26, 28.4791)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
                'numa_memory': '4G', 'persist': False, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(30286.9, 30286.9, 0.0329245, 0.0, 0.0), (30753.4, 30753.4, 0.0324305, 0.0, 0.0),
                (31151.2, 31151.2, 0.0320159, 0.0, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': False, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(112481.0, 112481.0, 0.0354717, 0.0, 5.06663), (111014.0, 111014.0, 0.0359431, 0.0, 5.14995),
                (112559.0, 112559.0, 0.035451, 0.0, 4.39996)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': False, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(209400.0, 209400.0, 0.0381135, 0.0, 9.3166), (209405.0, 209405.0, 0.0381132, 0.0, 9.03321),
                (214395.0, 214395.0, 0.0372271, 0.0, 9.49995)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': False, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(317759.0, 317759.0, 0.0376752, 0.0, 13.5665), (319487.0, 319487.0, 0.0374694, 0.0, 13.5165),
                (323316.0, 323316.0, 0.0370279, 0.0, 13.9331)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': False, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(420957.0, 420957.0, 0.0379212, 0.0, 18.2664), (419207.0, 419207.0, 0.0380766, 0.0, 18.8332),
                (421561.0, 421561.0, 0.0378607, 0.0, 17.6499)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': False, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(526460.0, 526460.0, 0.0378989, 0.0, 22.0331), (529197.0, 529197.0, 0.0377043, 0.0, 23.7497),
                (533214.0, 533214.0, 0.0374174, 0.0, 22.3831)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': False, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(625632.0, 625632.0, 0.0382689, 0.0, 26.5161), (631692.0, 631692.0, 0.0378988, 0.0, 26.8828),
                (622284.0, 622284.0, 0.038478, 0.0, 26.9162)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': False, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(728676.0, 728676.0, 0.0383326, 0.0, 30.5828), (731237.0, 731237.0, 0.0382001, 0.0, 32.2995),
                (724542.0, 724542.0, 0.0385532, 0.0, 32.4161)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': False, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(783983.0, 783983.0, 0.0407091, 0.0, 35.0656), (782308.0, 782308.0, 0.040797, 0.0, 33.7652),
                (715915.0, 715915.0, 0.0445905, 0.0, 31.1658)])]
