RESULTS = [(
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 0', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(804585.0, 0.0), (801148.0, 0.0), (807541.0, 0.0)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 1', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(801033.0, 122.895), (799989.0, 122.113), (803801.0, 122.846)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 2', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(799259.0, 242.918), (797091.0, 242.774), (794599.0, 242.152)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 3', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(790597.0, 357.701), (790143.0, 361.526), (789851.0, 355.109)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 4', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(784611.0, 470.576), (785424.0, 475.99), (784797.0, 475.866)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 5', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(776102.0, 578.822), (782605.0, 587.097), (784011.0, 591.513)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 6', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(775516.0, 695.638), (777636.0, 694.746), (774385.0, 692.662)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 7', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(776174.0, 812.69), (769456.0, 800.863), (769434.0, 798.308)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 8', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(772895.0, 918.994), (772724.0, 916.723), (775404.0, 916.713)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 9', 'retry': False,
     'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
     'bench': 'tpcc'}, [(766380.0, 1014.59), (772520.0, 1021.4), (769013.0, 1013.95)]), (
    {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 10',
     'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
     'db': 'ndb-proto2', 'bench': 'tpcc'}, [(764523.0, 1123.01), (769060.0, 1128.28), (762434.0, 1117.84)]), (
    {'par_load': True,
     'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 0',
     'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
     'db': 'kvdb-st', 'bench': 'tpcc'}, [(1094020.0, 0.0), (1110840.0, 0.0), (1075520.0, 0.0)]), (
    {'par_load': True,
     'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 1',
     'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
     'db': 'kvdb-st', 'bench': 'tpcc'}, [(826353.0, 0.0), (852781.0, 0.0), (845913.0, 0.0)]), ({'par_load': True,
                                                                                                'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 2',
                                                                                                'retry': False,
                                                                                                'scale_factor': 28,
                                                                                                'name': 'multipart:pct',
                                                                                                'numa_memory': '112G',
                                                                                                'threads': 28,
                                                                                                'db': 'kvdb-st',
                                                                                                'bench': 'tpcc'},
                                                                                               [(671993.0, 0.0),
                                                                                                (706678.0, 0.0),
                                                                                                (
                                                                                                    656195.0, 0.0)]),
    ({'par_load': True,
      'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 3',
      'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
      'db': 'kvdb-st', 'bench': 'tpcc'}, [(550780.0, 0.0), (554407.0, 0.0), (536970.0, 0.0)]), (
        {'par_load': True,
         'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 4',
         'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
         'db': 'kvdb-st', 'bench': 'tpcc'}, [(440937.0, 0.0), (458112.0, 0.0), (460816.0, 0.0)]), ({'par_load': True,
                                                                                                    'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 5',
                                                                                                    'retry': False,
                                                                                                    'scale_factor': 28,
                                                                                                    'name': 'multipart:pct',
                                                                                                    'numa_memory': '112G',
                                                                                                    'threads': 28,
                                                                                                    'db': 'kvdb-st',
                                                                                                    'bench': 'tpcc'},
                                                                                                   [(389108.0, 0.0),
                                                                                                    (391405.0, 0.0),
                                                                                                    (
                                                                                                        390824.0,
                                                                                                        0.0)]),
    ({'par_load': True,
      'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 6',
      'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
      'db': 'kvdb-st', 'bench': 'tpcc'}, [(337935.0, 0.0), (336006.0, 0.0), (342643.0, 0.0)]), (
        {'par_load': True,
         'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 7',
         'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
         'db': 'kvdb-st', 'bench': 'tpcc'}, [(300376.0, 0.0), (288345.0, 0.0), (305941.0, 0.0)]), ({'par_load': True,
                                                                                                    'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 8',
                                                                                                    'retry': False,
                                                                                                    'scale_factor': 28,
                                                                                                    'name': 'multipart:pct',
                                                                                                    'numa_memory': '112G',
                                                                                                    'threads': 28,
                                                                                                    'db': 'kvdb-st',
                                                                                                    'bench': 'tpcc'},
                                                                                                   [(261991.0, 0.0),
                                                                                                    (269196.0, 0.0),
                                                                                                    (
                                                                                                        261985.0,
                                                                                                        0.0)]),
    ({'par_load': True,
      'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 9',
      'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
      'db': 'kvdb-st', 'bench': 'tpcc'}, [(237309.0, 0.0), (235877.0, 0.0), (231598.0, 0.0)]), (
        {'par_load': True,
         'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 10',
         'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
         'db': 'kvdb-st', 'bench': 'tpcc'}, [(214308.0, 0.0), (221298.0, 0.0), (213673.0, 0.0)])]
