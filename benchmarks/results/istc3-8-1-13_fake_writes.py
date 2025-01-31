RESULTS = [({'scale_factor': 1, 'db': 'ndb-proto2', 'par_load': False, 'threads': 1, 'bench_opts': '',
             'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '4G',
             'persist': True}, [(29412.6, 29412.6, 0.033882, 81.7596, 0.0), (28554.8, 28554.8, 0.0349042, 81.5329, 0.0),
                                (28620.5, 28620.5, 0.0348216, 81.6942, 0.0)]), (
               {'scale_factor': 4, 'db': 'ndb-proto2', 'par_load': False, 'threads': 4, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '16G',
                'persist': True},
               [(104242.0, 104242.0, 0.0382459, 93.481, 4.3291), (103901.0, 103901.0, 0.0383728, 92.4471, 4.32914),
                (105468.0, 105468.0, 0.0378021, 92.8918, 4.47911)]), (
               {'scale_factor': 8, 'db': 'ndb-proto2', 'par_load': False, 'threads': 8, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '32G',
                'persist': True},
               [(197567.0, 197567.0, 0.0403659, 97.7048, 8.17584), (198024.0, 198024.0, 0.0402751, 98.1746, 8.15999),
                (196321.0, 196321.0, 0.0406066, 100.727, 8.45577)]), (
               {'scale_factor': 12, 'db': 'ndb-proto2', 'par_load': False, 'threads': 12, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '48G',
                'persist': True},
               [(301970.0, 301970.0, 0.0396107, 95.9425, 13.1208), (296951.0, 296951.0, 0.0402707, 101.857, 12.3516),
                (300682.0, 300682.0, 0.0397723, 100.84, 13.501)]), (
               {'scale_factor': 16, 'db': 'ndb-proto2', 'par_load': False, 'threads': 16, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '64G',
                'persist': True},
               [(390917.0, 390917.0, 0.0407861, 100.397, 16.1469), (390454.0, 390454.0, 0.0408575, 102.181, 15.0578),
                (393603.0, 393603.0, 0.0405154, 94.5263, 16.8823)]), (
               {'scale_factor': 20, 'db': 'ndb-proto2', 'par_load': False, 'threads': 20, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '80G',
                'persist': True},
               [(487936.0, 487936.0, 0.0408634, 101.266, 19.8535), (489413.0, 489413.0, 0.0407335, 97.2174, 20.2291),
                (487987.0, 487987.0, 0.0408372, 97.1397, 20.5744)]), (
               {'scale_factor': 24, 'db': 'ndb-proto2', 'par_load': False, 'threads': 24, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '96G',
                'persist': True},
               [(584191.0, 584191.0, 0.0409526, 103.392, 23.4635), (587157.0, 587157.0, 0.0407409, 102.503, 24.2748),
                (586074.0, 586074.0, 0.0408189, 104.875, 25.1599)]), (
               {'scale_factor': 28, 'db': 'ndb-proto2', 'par_load': False, 'threads': 28, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '112G',
                'persist': True},
               [(678667.0, 678667.0, 0.0411235, 99.0795, 27.6891), (677039.0, 677039.0, 0.0412212, 99.8785, 27.4051),
                (670260.0, 670260.0, 0.0416408, 105.28, 27.4072)]), (
               {'scale_factor': 32, 'db': 'ndb-proto2', 'par_load': False, 'threads': 32, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'name': 'scale_tpcc', 'bench': 'tpcc', 'numa_memory': '128G',
                'persist': True},
               [(722906.0, 722906.0, 0.0441231, 225.342, 28.614), (724204.0, 724204.0, 0.0440198, 236.26, 29.4157),
                (728319.0, 728319.0, 0.0437896, 237.912, 29.5433)]), (
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
