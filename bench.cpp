#include <stdio.h>
#include <stdlib.h>
#include <benchmark/benchmark.h>

int myRandom() {
    return rand() + 42;
}

static void BM_MyRandom(benchmark::State& state) {
  for (auto _ : state) {
    benchmark::DoNotOptimize(myRandom());
  }
}
BENCHMARK(BM_MyRandom);

BENCHMARK_MAIN();