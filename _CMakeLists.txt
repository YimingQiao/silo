cmake_minimum_required(VERSION 3.15)

project(Silo)

set(CMAKE_CXX_STANDARD 11)

### Options ###

option(DEBUG "Enable Debug Mode" OFF)
option(CHECK_INVARIANTS "Enable Invariants Check" OFF)
option(EVENT_COUNTERS "Enable Event Counters" OFF)

# Select Malloc Mode
set(USE_MALLOC_MODE "jemalloc" CACHE STRING "Select Malloc Mode: libc, jemalloc, tcmalloc, flow")

# Mode
set(MODE "perf" CACHE STRING
        "Select Mode: perf, backoff, factor-gc, factor-gc-nowriteinplace, factor-fake-compression, sandbox")

# Masstree
option(MASSTREE " Enable Masstree" ON)

###############

set(MASSTREE_CONFIG "--enable-max-key-len=1024")

if (DEBUG)
    set(OSUFFIX_D ".debug")
    list(APPEND MASSTREE_CONFIG "--enable-assertions")
else ()
    list(APPEND MASSTREE_CONFIG "--disable-assertions")
endif ()

if (CHECK_INVARIANTS)
    set(OSUFFIX_S ".check")
    list(APPEND COMMON_FLAGS "--enable-invariants --enable-preconditions")
else ()
    list(APPEND COMMON_FLAGS "--disable-invariants --disable-preconditions")
endif ()

if (EVENT_COUNTERS)
    set(OSUFFIX_E ".ectrs")
endif ()

set(OSUFFIX "${OSUFFIX_D}${OSUFFIX_S}")

if (${MODE} STREQUAL "perf")
    set(O "out-perf${OSUFFIX}")
    set(CONFIG_H "config/config-perf.h")
elseif (${MODE} STREQUAL "backoff")
    set(O "out-backoff${OSUFFIX}")
    set(CONFIG_H "config/config-backoff.h")
elseif (${MODE} STREQUAL "factor-gc")
    set(O "out-factor-gc${OSUFFIX}")
    set(CONFIG_H "config/config-factor-gc.h")
elseif (${MODE} STREQUAL "factor-gc-nowriteinplace")
    set(O "out-factor-gc-nowriteinplace$(OSUFFIX)")
    set(CONFIG_H "config/config-factor-gc-nowriteinplace.h")
elseif (${MODE} STREQUAL "factor-fake-compression")
    set(O "factor-fake-compression$(OSUFFIX)")
    set(CONFIG_H "config/factor-fake-compression.h")
elseif (${MODE} STREQUAL "sandbox")
    set(O "sandbox$(OSUFFIX)")
    set(CONFIG_H "config/sandbox.h")
else ()
    message(FATAL_ERROR "Invalid Mode. Please select one of perf, backoff, factor-gc, factor-gc-nowriteinplace, factor-fake-compression, sandbox")
endif ()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -w -g -Wall -std=c++0x")
list(APPEND CMAKE_CXX_FLAGS "-MD -Ithird-party/lz4 -DCONFIG_H=\"$(CONFIG_H)\"")

if (DEBUG)
    list(APPEND CMAKE_CXX_FLAGS "-fno-omit-frame-pointer -DDEBUG")
else ()
    list(APPEND CMAKE_CXX_FLAGS "-w -O2 -funroll-loops -fno-omit-frame-pointer")
endif ()

if (CHECK_INVARIANTS)
    list(APPEND CMAKE_CXX_FLAGS "-DINVARIANTS")
endif ()

if (EVENT_COUNTERS)
    list(APPEND CMAKE_CXX_FLAGS "-DENABLE_EVENT_COUNTERS")
endif ()

if (MASSTREE)
    list(APPEND CMAKE_CXX_FLAGS "-DNDB_MASSTREE -include masstree/config.h")
    set(O "${O}.masstree")
else ()
    set(O "${O}.silotree")
endif ()

set(LDFLAGS "-lpthread -lnuma -lrt")
set(LZ4LDFLAGS "-L${CMAKE_SOURCE_DIR}/third-party/lz4 -llz4 -Wl,-rpath,${CMAKE_SOURCE_DIR}/third-party/lz4")

if (USE_MALLOC_MODE STREQUAL "jemalloc")
    list(APPEND CMAKE_CXX_FLAGS "-DUSE_JEMALLOC")
    list(APPEND LDFLAGS "-ljemalloc")
    list(APPEND MASSTREE_CONFIG "--with-malloc=jemalloc")
elseif (USE_MALLOC_MODE STREQUAL "tcmalloc")
    list(APPEND CMAKE_CXX_FLAGS "-DUSE_TCMALLOC")
    list(APPEND LDFLAGS "-ltcmalloc")
    list(APPEND MASSTREE_CONFIG "--with-malloc=tcmalloc")
elseif (USE_MALLOC_MODE STREQUAL "flow")
    list(APPEND CMAKE_CXX_FLAGS "-DUSE_FLOW")
    list(APPEND LDFLAGS "-lflow")
    list(APPEND MASSTREE_CONFIG "--with-malloc=flow")
else ()
    list(APPEND MASSTREE_CONFIG "--with-malloc=malloc")
endif ()

file(GLOB SRCFILES allocator.cc btree.cc core.cc counter.cc memory.cc rcu.cc stats_server.cc thread.cc ticker.cc tuple.cc txn_btree.cc txn.cc txn_proto2_impl.cc varint.cc)

if (MASSTREE)
    file(GLOB MASSTREE_SRCFILES masstree/compiler.cc masstree/str.cc masstree/string.cc masstree/straccum.cc masstree/json.cc)
endif ()

file(GLOB OBJFILES *.cc, ${O}/*.o, ${SRCFILES})
set(BENCH_CXXFLAGS ${CMAKE_CXX_FLAGS} -DNO_MYSQL)
set(BENCH_LDFLAGS ${LDFLAGS} -ldb_cxx -lz -lrt -lcrypt -laio -ldl -lssl -lcrypto)

file(GLOB BENCH_SRCFILES benchmarks/bdb_wrapper.cc benchmarks/bench.cc
        benchmarks/encstress.cc
        benchmarks/bid.cc
        benchmarks/masstree/kvrandom.cc
        benchmarks/queue.cc
        benchmarks/tpcc.cc
        benchmarks/ycsb.cc)

file(GLOB NEWBENCH_SRCFILES new-benchmarks/bench.cc new-benchmarks/tpcc.cc)

# Setup executable or library here
add_executable(MyProject ${SRCFILES})

target_link_libraries(MyProject PRIVATE ${LINKER_FLAGS})

# Add third-party libraries
add_subdirectory(third-party/lz4)

# Add more targets for other executables or tests as needed

