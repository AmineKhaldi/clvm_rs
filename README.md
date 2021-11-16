Rust implementation of clvm.

Python Wheel
------------

Use `maturin` to build the python interface. First, install into current virtualenv with

```
$ pip install maturin
```

As we need `MPIR` for MSVC builds, prepare this dependency with

```
$ git clone https://github.com/Chia-Network/mpir_gc_x64.git --depth 1
```

Build `clvm_rs` directly into the current virtualenv with

```
$ maturin develop --release
```

To build the wheel, do

```
$ maturin build --release --no-sdist
````


WASM
----

Use `wasm-pack` to build the wasm `pkg` file used with npm. Install it with:

```
$ cargo install wasm-pack
```

Then build with

```
$ wasm-pack build  --release
```


TESTS
-----
In order to run the unit tests, run:

```
cargo test
```
