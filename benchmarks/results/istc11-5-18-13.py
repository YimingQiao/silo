RESULTS = [({'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
             'name': 'scale', 'numa_memory': '101G', 'threads': 1, 'db': 'kvdb', 'bench': 'ycsb'},
            [(620600.0, 0.0), (621420.0, 0.0), (622727.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '101G', 'threads': 1, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(605937.0, 0.0), (606707.0, 0.0), (615925.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '101G', 'threads': 1, 'db': 'kvdb', 'bench': 'ycsb'},
               [(518197.0, 0.0), (518351.0, 0.0), (517762.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '101G', 'threads': 1, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(516004.0, 0.0), (515056.0, 0.0), (515394.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '105G', 'threads': 4, 'db': 'kvdb', 'bench': 'ycsb'},
               [(2507000.0, 0.0), (2515440.0, 0.0), (2515880.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '105G', 'threads': 4, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(2440110.0, 0.0), (2438170.0, 0.0), (2444660.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '105G', 'threads': 4, 'db': 'kvdb', 'bench': 'ycsb'},
               [(2103950.0, 0.0), (2108650.0, 0.0), (2101390.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '105G', 'threads': 4, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(2021630.0, 0.0), (2051260.0, 0.0), (2062360.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '111G', 'threads': 8, 'db': 'kvdb', 'bench': 'ycsb'},
               [(4698460.0, 0.0), (4701020.0, 0.0), (4697040.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '111G', 'threads': 8, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(4594410.0, 0.0), (4585480.0, 0.0), (4585570.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '111G', 'threads': 8, 'db': 'kvdb', 'bench': 'ycsb'},
               [(3953090.0, 0.0), (3952270.0, 0.0), (3956260.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '111G', 'threads': 8, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(3893480.0, 0.0166664), (3832850.0, 0.0), (3888720.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '116G', 'threads': 12, 'db': 'kvdb', 'bench': 'ycsb'},
               [(6420760.0, 0.0), (6438670.0, 0.0), (6433960.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '116G', 'threads': 12, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(6363770.0, 0.0), (6379600.0, 0.0), (6389300.0, 0.0166661)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '116G', 'threads': 12, 'db': 'kvdb', 'bench': 'ycsb'},
               [(5401450.0, 0.0), (5407930.0, 0.0), (5392230.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '116G', 'threads': 12, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(5402250.0, 0.0333321), (5376760.0, 0.0166661), (5390240.0, 0.0333322)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '122G', 'threads': 16, 'db': 'kvdb', 'bench': 'ycsb'},
               [(8338980.0, 0.0), (8334610.0, 0.0), (8328680.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '122G', 'threads': 16, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(8257480.0, 0.0), (8226600.0, 0.0), (8277980.0, 0.0333317)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '122G', 'threads': 16, 'db': 'kvdb', 'bench': 'ycsb'},
               [(6984660.0, 0.0), (6980250.0, 0.0), (6980670.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '122G', 'threads': 16, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(6999110.0, 0.0166657), (6994190.0, 0.0166658), (6998980.0, 0.0166659)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '128G', 'threads': 20, 'db': 'kvdb', 'bench': 'ycsb'},
               [(10199100.0, 0.0), (10189900.0, 0.0), (10186000.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '128G', 'threads': 20, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(10127800.0, 0.0), (10161500.0, 0.0), (10109000.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '128G', 'threads': 20, 'db': 'kvdb', 'bench': 'ycsb'},
               [(8543690.0, 0.0), (8551340.0, 0.0), (8535590.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '128G', 'threads': 20, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(8579520.0, 0.049996), (8561890.0, 0.0333303), (8576020.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '133G', 'threads': 24, 'db': 'kvdb', 'bench': 'ycsb'},
               [(11904400.0, 0.0), (11904800.0, 0.0), (11895800.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '133G', 'threads': 24, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(11820400.0, 0.0), (11836000.0, 0.0166648), (11816400.0, 0.0166651)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '133G', 'threads': 24, 'db': 'kvdb', 'bench': 'ycsb'},
               [(9960240.0, 0.0), (9946770.0, 0.0), (9967100.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '133G', 'threads': 24, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(10030400.0, 0.0999886), (10022700.0, 0.0499943), (10023500.0, 0.0166643)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '139G', 'threads': 28, 'db': 'kvdb', 'bench': 'ycsb'},
               [(14055700.0, 0.0), (14064700.0, 0.0), (14048200.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '139G', 'threads': 28, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(13991000.0, 0.0), (13987400.0, 0.0), (13974900.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '139G', 'threads': 28, 'db': 'kvdb', 'bench': 'ycsb'},
               [(11775200.0, 0.0), (11773500.0, 0.0), (11763400.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '139G', 'threads': 28, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(11841300.0, 0.0333278), (11859000.0, 0.099985), (11843500.0, 0.0499928)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '144G', 'threads': 32, 'db': 'kvdb', 'bench': 'ycsb'},
               [(15886600.0, 0.0), (15883900.0, 0.0), (15914600.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '144G', 'threads': 32, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(15709800.0, 0.0166588), (15721400.0, 0.0166599), (15791500.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '144G', 'threads': 32, 'db': 'kvdb', 'bench': 'ycsb'},
               [(13298200.0, 0.0), (13284200.0, 0.0), (13316600.0, 0.0)]), (
               {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale_rmw', 'numa_memory': '144G', 'threads': 32, 'db': 'ndb-proto2', 'bench': 'ycsb'},
               [(13258000.0, 0.133309), (13318500.0, 0.116649), (13318900.0, 0.14997)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 1, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 1, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(30985.9, 0.0), (29673.8, 0.0166664), (32070.4, 0.0)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 4, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 4, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(112760.0, 5.03329), (112690.0, 5.29995), (113504.0, 4.89996)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 8, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 8, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(208462.0, 8.96661), (212875.0, 10.0832), (212539.0, 9.33326)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 12, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 12, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(325661.0, 14.4332), (328256.0, 13.6332), (327681.0, 14.5498)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 16, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 16, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(430089.0, 19.7165), (421372.0, 18.4498), (432434.0, 17.8832)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 20, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 20, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(543340.0, 23.1331), (545883.0, 23.9497), (546608.0, 23.5831)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 24, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 24, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(648722.0, 29.233), (633469.0, 26.3663), (644658.0, 27.2329)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 28, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(750691.0, 34.5494), (743953.0, 32.9328), (741685.0, 32.2494)]), (
               {'par_load': False, 'bench_opts': '', 'retry': False, 'scale_factor': 32, 'name': 'scale_tpcc',
                'numa_memory': '112G', 'threads': 32, 'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(810975.0, 35.2974), (813899.0, 36.0823), (803711.0, 35.4822)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 0',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(787305.0, 0.0), (783427.0, 0.0), (787891.0, 0.0)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 1',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(757735.0, 114.1), (773002.0, 118.563), (772284.0, 117.997)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 2',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(765908.0, 233.027), (766292.0, 235.925), (772907.0, 233.54)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 3',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(767204.0, 348.752), (757182.0, 345.413), (762173.0, 347.066)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 4',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(762240.0, 465.634), (766427.0, 461.286), (764470.0, 463.978)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 5',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(758053.0, 569.597), (755356.0, 568.032), (749486.0, 562.348)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 6',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(750449.0, 675.393), (760504.0, 671.979), (753789.0, 676.568)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 7',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(757352.0, 795.228), (754869.0, 782.752), (733751.0, 770.558)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 8',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(750816.0, 890.491), (733219.0, 858.385), (753169.0, 902.858)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 9',
                'retry': False,
                'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(744790.0, 988.435), (748771.0, 990.238), (745841.0, 975.928)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 100,0,0,0,0 --new-order-remote-item-pct 10',
                'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(745825.0, 1092.56), (743188.0, 1079.22), (749344.0, 1090.5)]), (
               {'par_load': True,
                'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 0',
                'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
                'db': 'kvdb-st', 'bench': 'tpcc'}, [(1098950.0, 0.0), (1119710.0, 0.0), (1072420.0, 0.0)]), (
               {'par_load': True,
                'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 1',
                'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
                'db': 'kvdb-st', 'bench': 'tpcc'}, [(889236.0, 0.0), (898120.0, 0.0), (900607.0, 0.0)]),
           ({'par_load': True,
             'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 2',
             'retry': False,
             'scale_factor': 28,
             'name': 'multipart:pct',
             'numa_memory': '112G',
             'threads': 28,
             'db': 'kvdb-st',
             'bench': 'tpcc'},
            [(722596.0, 0.0),
             (711485.0, 0.0),
             (
                 712563.0, 0.0)]),
           ({'par_load': True,
             'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 3',
             'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
             'db': 'kvdb-st', 'bench': 'tpcc'}, [(582426.0, 0.0), (578095.0, 0.0), (583767.0, 0.0)]), (
               {'par_load': True,
                'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 4',
                'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
                'db': 'kvdb-st', 'bench': 'tpcc'}, [(482736.0, 0.0), (483404.0, 0.0), (487373.0, 0.0)]),
           ({'par_load': True,
             'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 5',
             'retry': False,
             'scale_factor': 28,
             'name': 'multipart:pct',
             'numa_memory': '112G',
             'threads': 28,
             'db': 'kvdb-st',
             'bench': 'tpcc'},
            [(414524.0, 0.0),
             (415143.0, 0.0),
             (
                 415969.0, 0.0)]),
           ({'par_load': True,
             'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 6',
             'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
             'db': 'kvdb-st', 'bench': 'tpcc'}, [(350162.0, 0.0), (352123.0, 0.0), (352476.0, 0.0)]), (
               {'par_load': True,
                'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 7',
                'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
                'db': 'kvdb-st', 'bench': 'tpcc'}, [(311676.0, 0.0), (311529.0, 0.0), (307683.0, 0.0)]),
           ({'par_load': True,
             'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 8',
             'retry': False,
             'scale_factor': 28,
             'name': 'multipart:pct',
             'numa_memory': '112G',
             'threads': 28,
             'db': 'kvdb-st',
             'bench': 'tpcc'},
            [(274936.0, 0.0),
             (274880.0, 0.0),
             (
                 269893.0, 0.0)]),
           ({'par_load': True,
             'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 9',
             'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
             'db': 'kvdb-st', 'bench': 'tpcc'}, [(240224.0, 0.0), (244346.0, 0.0), (244626.0, 0.0)]), (
               {'par_load': True,
                'bench_opts': '--workload-mix 100,0,0,0,0 --enable-separate-tree-per-partition --enable-partition-locks --new-order-remote-item-pct 10',
                'retry': False, 'scale_factor': 28, 'name': 'multipart:pct', 'numa_memory': '112G', 'threads': 28,
                'db': 'kvdb-st', 'bench': 'tpcc'}, [(220897.0, 0.0), (224565.0, 0.0), (224131.0, 0.0)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 50,0,0,0,50 --new-order-remote-item-pct 0',
                'retry': True,
                'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(200114.0, 2302.91), (199003.0, 2297.07), (200227.0, 2319.16)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 50,0,0,0,50 --new-order-remote-item-pct 20',
                'retry': True,
                'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(194843.0, 2323.13), (186419.0, 2159.79), (194520.0, 2306.21)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 50,0,0,0,50 --new-order-remote-item-pct 40',
                'retry': True,
                'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(192514.0, 2365.37), (193027.0, 2379.28), (193225.0, 2340.44)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 50,0,0,0,50 --new-order-remote-item-pct 60',
                'retry': True,
                'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(191380.0, 2385.91), (191342.0, 2390.18), (190192.0, 2357.07)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 50,0,0,0,50 --new-order-remote-item-pct 80',
                'retry': True,
                'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16, 'db': 'ndb-proto2',
                'bench': 'tpcc'}, [(191257.0, 2400.22), (180790.0, 2180.2), (190691.0, 2383.46)]), (
               {'par_load': False, 'bench_opts': '--workload-mix 50,0,0,0,50 --new-order-remote-item-pct 100',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(189927.0, 2360.62), (180441.0, 2180.87), (190903.0, 2394.66)]),
           (
               {'par_load': False,
                'bench_opts': '--disable-read-only-snapshots --workload-mix 50,0,0,0,50 --new-order-remote-item-pct 0',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(162328.0, 14288.5), (165077.0, 14635.6), (165270.0, 14658.5)]),
           (
               {'par_load': False,
                'bench_opts': '--disable-read-only-snapshots --workload-mix 50,0,0,0,50 --new-order-remote-item-pct 20',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(158432.0, 15909.9), (158501.0, 15990.8), (156767.0, 15640.1)]),
           (
               {'par_load': False,
                'bench_opts': '--disable-read-only-snapshots --workload-mix 50,0,0,0,50 --new-order-remote-item-pct 40',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(153417.0, 17102.2), (154920.0, 17297.1), (153161.0, 16958.5)]),
           (
               {'par_load': False,
                'bench_opts': '--disable-read-only-snapshots --workload-mix 50,0,0,0,50 --new-order-remote-item-pct 60',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(150880.0, 18313.4), (143189.0, 17586.6), (152049.0, 18577.0)]),
           (
               {'par_load': False,
                'bench_opts': '--disable-read-only-snapshots --workload-mix 50,0,0,0,50 --new-order-remote-item-pct 80',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'}, [(149056.0, 19671.2), (150192.0, 19849.1), (150495.0, 19815.7)]),
           (
               {'par_load': False,
                'bench_opts': '--disable-read-only-snapshots --workload-mix 50,0,0,0,50 --new-order-remote-item-pct 100',
                'retry': True, 'scale_factor': 8, 'name': 'readonly', 'numa_memory': '64G', 'threads': 16,
                'db': 'ndb-proto2', 'bench': 'tpcc'},
               [(147858.0, 20842.0), (146716.0, 20584.7), (147927.0, 20903.4)])] + [(
    {
        'par_load': False,
        'bench_opts': '',
        'retry': False,
        'scale_factor': 1,
        'name': 'scale_tpcc',
        'numa_memory': '112G',
        'threads': 1,
        'db': 'ndb-proto1',
        'bench': 'tpcc'},
    [
        (
            32240.8,
            0.0),
        (
            31026.7,
            0.0),
        (
            30438.4,
            0.0)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 4,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 4,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          112148.0,
                          4.91663),
                      (
                          113832.0,
                          5.29995),
                      (
                          113486.0,
                          5.19994)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 8,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 8,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          212410.0,
                          8.81654),
                      (
                          212020.0,
                          9.64986),
                      (
                          213780.0,
                          8.94986)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 12,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 12,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          320426.0,
                          13.3998),
                      (
                          327475.0,
                          14.4498),
                      (
                          321080.0,
                          14.6498)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 16,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 16,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          431773.0,
                          18.8163),
                      (
                          432635.0,
                          18.3997),
                      (
                          430719.0,
                          18.383)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 20,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 20,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          542721.0,
                          23.7831),
                      (
                          529936.0,
                          21.7331),
                      (
                          538936.0,
                          23.8329)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 24,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 24,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          642353.0,
                          28.483),
                      (
                          643512.0,
                          28.7329),
                      (
                          643497.0,
                          29.6495)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 28,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 28,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          743009.0,
                          32.7986),
                      (
                          729192.0,
                          32.7657),
                      (
                          728048.0,
                          31.4827)]),
              (
                  {
                      'par_load': False,
                      'bench_opts': '',
                      'retry': False,
                      'scale_factor': 32,
                      'name': 'scale_tpcc',
                      'numa_memory': '112G',
                      'threads': 32,
                      'db': 'ndb-proto1',
                      'bench': 'tpcc'},
                  [
                      (
                          790212.0,
                          34.2826),
                      (
                          805566.0,
                          35.166),
                      (
                          804736.0,
                          34.3825)])] + [
              ({'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
                'name': 'scale', 'numa_memory': '101G', 'threads': 1, 'db': 'ndb-proto1', 'bench': 'ycsb'},
               [(614240.0, 0.0), (616696.0, 0.0), (616061.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '101G', 'threads': 1, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(521324.0, 0.0), (519604.0, 0.0), (516847.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '105G', 'threads': 4, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(2463990.0, 0.0), (2465270.0, 0.0), (2467840.0, 0.0166664)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '105G', 'threads': 4, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(2064040.0, 0.0), (2035160.0, 0.0), (2014690.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '111G', 'threads': 8, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(4632640.0, 0.0), (4628850.0, 0.0), (4642110.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '111G', 'threads': 8, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(3917340.0, 0.0), (3918600.0, 0.0166663), (3906720.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '116G', 'threads': 12, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(6392020.0, 0.0), (6261500.0, 0.0166661), (6373530.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '116G', 'threads': 12, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(5383630.0, 0.0), (5386750.0, 0.0), (5349580.0, 0.0166662)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '122G', 'threads': 16, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(8197750.0, 0.0), (8202670.0, 0.0166657), (8212610.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '122G', 'threads': 16, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(6964480.0, 0.0), (6962350.0, 0.0), (6964480.0, 0.0333319)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '128G', 'threads': 20, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(9569340.0, 0.0), (9545470.0, 0.0), (9525760.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '128G', 'threads': 20, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(8327020.0, 0.016665), (8351850.0, 0.0666599), (8327510.0, 0.0499968)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '133G', 'threads': 24, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(9695090.0, 0.0), (9715240.0, 0.0), (9725800.0, 0.0166652)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '133G', 'threads': 24, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(9238990.0, 0.0333301), (9226620.0, 0.0666602), (9170780.0, 0.0999898)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '139G', 'threads': 28, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(8925020.0, 0.0166638), (8880120.0, 0.0), (9184000.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '139G', 'threads': 28, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(9286140.0, 0.0666553), (8793640.0, 0.049994), (9385870.0, 0.11665)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,20,0,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale', 'numa_memory': '144G', 'threads': 32, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(5234880.0, 0.0), (8694640.0, 0.0), (8797910.0, 0.0)]), (
        {'par_load': True, 'bench_opts': '--workload-mix 80,0,20,0', 'retry': False, 'scale_factor': 320000,
         'name': 'scale_rmw', 'numa_memory': '144G', 'threads': 32, 'db': 'ndb-proto1', 'bench': 'ycsb'},
        [(8860080.0, 0.0666507), (8879010.0, 0.0833041), (8945930.0, 0.0)])]
