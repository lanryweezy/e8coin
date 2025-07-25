# 🧠 E8Coin – Post-Quantum Cryptocurrency using E8/Leech Lattices

**E8Coin** is an experimental, post-quantum cryptocurrency built entirely on **exceptional high-dimensional lattice mathematics**, namely the **E8 lattice** and **Leech lattice**.

This project explores how advanced lattice structures can be used as the foundation for:
- Quantum-resistant digital signatures
- Lattice-based wallets
- Private transactions
- Post-quantum consensus mechanisms
- Verifiable computation and zero-knowledge proofs

---

## 🔐 Why Lattices?

Unlike traditional crypto (ECDSA, RSA), E8Coin uses mathematical structures that resist attacks even from quantum computers:
- **E8 Lattice**: 248-dimensional symmetry space with rich geometric/algebraic properties
- **Leech Lattice**: 24-dimensional perfect packing used for dense code theory
- **LWE/SIS**-like problems as computational foundation

---

## 📦 Project Modules

| Module       | Description                              |
|--------------|------------------------------------------|
| `crypto/`    | Keygen, signatures, encryption with lattices |
| `ledger/`    | Blockchain structure, mempool, transaction logic |
| `consensus/` | Proof-of-Lattice-Work or PoS (modular)   |
| `wallet/`    | Create/send/receive funds securely       |
| `network/`   | P2P networking, gossip propagation       |
| `cli/`       | Command-line node and wallet control     |
| `web/`       | Web dashboard, block explorer (optional) |
| `docs/`      | Protocol specifications and whitepapers  |

---

## 🧪 Quickstart (WIP)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/e8coin
cd e8coin

# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run CLI
python cli/main.py
