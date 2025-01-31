RESULTS = [({'scale_factor': 1, 'db': 'ndb-proto2', 'par_load': False, 'threads': 1, 'bench_opts': '',
             'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
             'numa_memory': '4G', 'persist': True},
            [(29161.1, 29161.1, 0.0341828, 79.6502, 0.0), (29596.2, 29596.2, 0.033672, 78.2933, 0.0),
             (30294.6, 30294.6, 0.0328931, 80.0015, 0.0)]), (
               {'scale_factor': 4, 'db': 'ndb-proto2', 'par_load': False, 'threads': 4, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '16G', 'persist': True},
               [(104680.0, 104680.0, 0.0380678, 93.543, 4.26127), (105357.0, 105357.0, 0.037833, 93.479, 4.24594),
                (105311.0, 105311.0, 0.0378461, 92.8869, 4.39667)]), (
               {'scale_factor': 8, 'db': 'ndb-proto2', 'par_load': False, 'threads': 8, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '32G', 'persist': True},
               [(199130.0, 199130.0, 0.040013, 100.575, 8.08887), (200940.0, 200940.0, 0.0396728, 100.988, 8.22472),
                (200066.0, 200066.0, 0.0398625, 100.844, 8.84284)]), (
               {'scale_factor': 12, 'db': 'ndb-proto2', 'par_load': False, 'threads': 12, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '48G', 'persist': True},
               [(300183.0, 300183.0, 0.0398305, 104.51, 14.0334), (302015.0, 302015.0, 0.0396003, 105.269, 12.0563),
                (301133.0, 301133.0, 0.0397071, 105.661, 12.3025)]), (
               {'scale_factor': 16, 'db': 'ndb-proto2', 'par_load': False, 'threads': 16, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '64G', 'persist': True},
               [(394222.0, 394222.0, 0.0404486, 110.365, 16.5004), (396748.0, 396748.0, 0.0401852, 106.095, 15.9532),
                (394091.0, 394091.0, 0.0404697, 107.902, 16.0202)]), (
               {'scale_factor': 20, 'db': 'ndb-proto2', 'par_load': False, 'threads': 20, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '80G', 'persist': True},
               [(492902.0, 492902.0, 0.0404255, 110.144, 20.2965), (493765.0, 493765.0, 0.0403417, 112.555, 19.5578),
                (492462.0, 492462.0, 0.0404569, 108.249, 19.24)]), (
               {'scale_factor': 24, 'db': 'ndb-proto2', 'par_load': False, 'threads': 24, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '96G', 'persist': True},
               [(588773.0, 588773.0, 0.0406194, 111.398, 24.3063), (590348.0, 590348.0, 0.0404954, 112.12, 25.0197),
                (583694.0, 583694.0, 0.0409702, 112.481, 23.4229)]), (
               {'scale_factor': 28, 'db': 'ndb-proto2', 'par_load': False, 'threads': 28, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '112G', 'persist': True},
               [(680396.0, 680396.0, 0.0410039, 112.546, 28.3629), (679657.0, 679657.0, 0.0410506, 114.858, 27.5391),
                (680564.0, 680564.0, 0.0410109, 115.396, 27.794)]), (
               {'scale_factor': 32, 'db': 'ndb-proto2', 'par_load': False, 'threads': 32, 'bench_opts': '',
                'log_fake_writes': True, 'retry': False, 'log_nofsync': False, 'name': 'scale_tpcc', 'bench': 'tpcc',
                'numa_memory': '128G', 'persist': True},
               [(652861.0, 652861.0, 0.048789, 276.402, 27.5094), (651525.0, 651525.0, 0.0488993, 279.703, 27.6233),
                (654939.0, 654939.0, 0.0485726, 289.37, 27.9035)]), (
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
