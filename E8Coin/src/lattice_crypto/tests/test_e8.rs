use lattice_crypto::E8Lattice;

#[test]
fn test_random_short_vector_length() {
    let e8 = E8Lattice::generate();
    let vec = e8.random_short_vector();
    assert_eq!(vec.len(), 8);
}
