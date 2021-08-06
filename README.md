Rust implementation of clvm.

Python Wheel
------------

Use `maturin` to build the python interface. First, install into current virtualenv with

```
$ pip install maturin
```

Build `clvm_rs` directly into the current virtualenv with

```
$ maturin develop --release --cargo-extra-args='--features extension-module,openssl'  # on Windows, drop `openssl`
```

To build the wheel, do

```
$ maturin build --release --no-sdist --cargo-extra-args='--features extension-module,openssl'
````



WASM
----

Use `wasm-pack` to build the wasm `pkg` file used with npm. Install it with:

```
$ cargo install wasm-pack
```

Then build with

```
$ wasm-pack build  --release -- --features=wasm-api
```


TESTS
-----

In order to run the unit tests, run:

```
cargo test
```
