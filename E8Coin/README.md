# E8Coin

E8Coin is a quantum-resistant cryptocurrency that integrates lattice-based cryptography, AI-driven security, and a novel consensus mechanism.

## Project Structure

- `src/lattice_crypto`: Mathematical Foundation (Rust Implementation)
- `src/ai_security`: AI-Enhanced Security System (Python Integration)
- `src/consensus`: Proof-of-Geometric-Structure Consensus (Hybrid Rust/Python)
- `src/smart_contracts`: Quantum-Resistant Smart Contracts (Rust Wasm)
- `src/tokenomics`: Tokenomics & Ecosystem (Python Simulation)
- `src/network`: Network Infrastructure (Rust Implementation)
- `src/developer_ecosystem`: Developer Ecosystem (Python + WebAssembly)
- `src/quantum_simulator`: Quantum Threat Simulator (Python AI)
- `src/dashboard`: Visualization Dashboard (JavaScript + WebGL)
- `src/ai_optimizer`: Continuous AI Optimization System
- `docs`: Project documentation and whitepaper.
- `tests`: Unit and integration tests.

## Setup

### Rust Components

To build the Rust components, you will need to have the Rust toolchain installed. You can install it from [https://rustup.rs/](https://rustup.rs/).

Once Rust is installed, you can build each component by navigating to its directory and running `cargo build`. For example:

```bash
cd src/lattice_crypto
cargo build
```

### Python Components

To run the Python components, you will need to have Python 3 installed. You can install the dependencies for each component using `pip`. It is recommended to use a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

(Note: `requirements.txt` files will need to be created for each Python component.)

### Web Dashboard

To run the web dashboard, you can open the `index.html` file in a web browser.

```bash
cd src/dashboard
# Open index.html in your browser
```
