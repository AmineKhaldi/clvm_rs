fn main() {
    if cfg!(windows) {
        println!("cargo:rustc-link-lib=mpir");
        println!("cargo:rustc-link-search=mpir_gc_x64");
    } else {
        println!("cargo:rustc-link-lib=static=gmp");
        println!("cargo:rustc-link-search=/usr/local/lib");
    }
}
