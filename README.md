# bun-c-luajit-bench

bun ffi benchmark (vs c, node, luajit)
based on https://bun.sh/blog/compile-and-run-c-in-js

## Usage

### Bun

```bash
$ bun install
$ bun run bench.js
```

### Node.js

```bash
$ yarn install
$ yarn global add node-gyp
$ node-gyp rebuild
$ node bench_napi.cjs
```

### C

- note: using google benchmark library. below is example for macos.

```bash
$ brew install google-benchmark
$ clang++ ./bench.cpp -L/opt/homebrew/lib -l benchmark -O3 -I/opt/homebrew/include -o bench
$ ./bench
```

### Luajit

```bash
$ clang -shared -fPIC -O3 -o libmyRandom.dylib myRandom.c
$ luajit bench.lua
```

## Result

Tested on M1 Macbook Air.

- C: 7.05 ns /iter
- bun: 12.54 ns /iter
- node: 11.47 ns /iter
- luajit: 16.84 ns /iter

(Used environment)

- clang: 19.1.2
- bun: 1.1.34
- node: v22.9.0
- node-gyp: v10.2.0
- LuaJIT: 2.1.1710088188