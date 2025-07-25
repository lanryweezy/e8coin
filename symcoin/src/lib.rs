pub mod crypto;

use crypto::e8::E8Lattice;
use crypto::leech::LeechLattice;

pub struct SymCoinCrypto {
    pub e8: E8Lattice,
    pub leech: LeechLattice,
}

impl SymCoinCrypto {
    pub fn new() -> Self {
        SymCoinCrypto {
            e8: E8Lattice::generate(),
            leech: LeechLattice::construct(),
        }
    }

    pub fn quantum_safe_sign(&self, message: &[u8]) -> Signature {
        let point = self.leech.hash_to_point(message);
        let signature = self.leech.closest_vector(point);
        Signature::new(signature)
    }

    pub fn generate_address(&self) -> Address {
        let public_vector = self.e8.random_short_vector();
        Address::from_e8(public_vector)
    }
}

pub struct Signature {
    pub value: Vec<u8>,
}

impl Signature {
    pub fn new(value: Vec<u8>) -> Self {
        Signature { value }
    }
}

pub struct Address {
    pub value: Vec<u8>,
}

impl Address {
    pub fn from_e8(value: Vec<u8>) -> Self {
        Address { value }
    }
}
