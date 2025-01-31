RESULTS = [({'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
             'numa_memory': '4G', 'persist': True, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
            [(29381.4, 29381.4, 0.0339166, 83.9258, 0.0), (28600.6, 28600.6, 0.0348584, 82.6534, 0.0),
             (28147.4, 28147.4, 0.0354085, 85.7701, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
                'numa_memory': '4G', 'persist': False, 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(30286.9, 30286.9, 0.0329245, 0.0, 0.0), (30753.4, 30753.4, 0.0324305, 0.0, 0.0),
                (31151.2, 31151.2, 0.0320159, 0.0, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': True, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(104443.0, 104443.0, 0.0381788, 96.0151, 4.16338), (105184.0, 105184.0, 0.0379089, 107.722, 4.34632),
                (101418.0, 101418.0, 0.0393277, 97.5319, 4.39737)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '16G', 'persist': False, 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(112481.0, 112481.0, 0.0354717, 0.0, 5.06663), (111014.0, 111014.0, 0.0359431, 0.0, 5.14995),
                (112559.0, 112559.0, 0.035451, 0.0, 4.39996)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': True, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(195183.0, 195183.0, 0.0408511, 165.482, 8.40715), (195429.0, 195429.0, 0.0407978, 116.612, 7.95758),
                (198778.0, 198778.0, 0.040128, 141.342, 8.44383)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '32G', 'persist': False, 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(209400.0, 209400.0, 0.0381135, 0.0, 9.3166), (209405.0, 209405.0, 0.0381132, 0.0, 9.03321),
                (214395.0, 214395.0, 0.0372271, 0.0, 9.49995)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': True, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(295485.0, 295485.0, 0.0404785, 160.172, 11.622), (294952.0, 294952.0, 0.040542, 137.536, 12.9175),
                (298367.0, 298367.0, 0.0400908, 152.179, 11.6397)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '48G', 'persist': False, 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(317759.0, 317759.0, 0.0376752, 0.0, 13.5665), (319487.0, 319487.0, 0.0374694, 0.0, 13.5165),
                (323316.0, 323316.0, 0.0370279, 0.0, 13.9331)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': True, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(392681.0, 392681.0, 0.0406083, 178.028, 16.3166), (390808.0, 390808.0, 0.0408062, 134.08, 15.9497),
                (392443.0, 392443.0, 0.0406377, 143.774, 15.5671)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '64G', 'persist': False, 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(420957.0, 420957.0, 0.0379212, 0.0, 18.2664), (419207.0, 419207.0, 0.0380766, 0.0, 18.8332),
                (421561.0, 421561.0, 0.0378607, 0.0, 17.6499)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': True, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(487133.0, 487133.0, 0.040897, 182.749, 20.3996), (482100.0, 482100.0, 0.0413421, 149.776, 19.9923),
                (482364.0, 482364.0, 0.0413235, 147.405, 18.6297)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '80G', 'persist': False, 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(526460.0, 526460.0, 0.0378989, 0.0, 22.0331), (529197.0, 529197.0, 0.0377043, 0.0, 23.7497),
                (533214.0, 533214.0, 0.0374174, 0.0, 22.3831)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': True, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(576874.0, 576874.0, 0.0414611, 190.94, 23.9386), (568120.0, 568120.0, 0.0420953, 199.285, 22.8701),
                (580741.0, 580741.0, 0.0411825, 255.775, 23.1551)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '96G', 'persist': False, 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(625632.0, 625632.0, 0.0382689, 0.0, 26.5161), (631692.0, 631692.0, 0.0378988, 0.0, 26.8828),
                (622284.0, 622284.0, 0.038478, 0.0, 26.9162)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': True, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(666090.0, 666090.0, 0.0418768, 120.662, 27.6226), (652526.0, 652526.0, 0.0427807, 184.736, 27.5441),
                (664060.0, 664060.0, 0.0420135, 121.436, 26.78)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'persist': False, 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(728676.0, 728676.0, 0.0383326, 0.0, 30.5828), (731237.0, 731237.0, 0.0382001, 0.0, 32.2995),
                (724542.0, 724542.0, 0.0385532, 0.0, 32.4161)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': True, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(675819.0, 675819.0, 0.0471086, 385.01, 27.8739), (681825.0, 681825.0, 0.0466471, 564.667, 28.1586),
                (677843.0, 677843.0, 0.0469547, 344.102, 27.9294)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '128G', 'persist': False, 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(783983.0, 783983.0, 0.0407091, 0.0, 35.0656), (782308.0, 782308.0, 0.040797, 0.0, 33.7652),
                (715915.0, 715915.0, 0.0445905, 0.0, 31.1658)])]
