---
title: "DID Specification for Autonomous Agents"
type: specification
date_creation: 2024-03-18
last_updated: 2026-03-30
last_review: 2026-04-03
Status: Final
Version: Initiation
Axiom: II
license: CC-BY-SA-4.0
---

# SPÉCIFICATION DID POUR AGENTS AUTONOMES
## Decentralized Identifiers pour Identité Agentique LAIRM

---

## 📋 Vue d'ensemble

La spécification DID (Decentralized Identifiers) pour agents autonomes implémente l'**Axiom II (Identitas)** en fournissant un système d'identification décentralisé, vérifiable et immuable pour Each agent.

### Objectifs
- ✅ Identité unique et vérifiable
- ✅ Décentralisation (pas de point unique de défaillance)
- ✅ Immuabilité des identifiants
- ✅ Interoperability avec standards W3C

---

## 🔑 Format DID

### Syntaxe

```
did:lairm:agent:<method>:<identifier>

Exemple:
did:lairm:agent:ethereum:0x1234567890abcdef
did:lairm:agent:solana:9B5X3...
did:lairm:agent:ipfs:QmXxxx...
```

### Composants

- **Scheme**: `did` (standard W3C)
- **Method**: `lairm` (méthode LAIRM)
- **type**: `agent` (type d'entité)
- **Blockchain**: `ethereum|solana|ipfs|...`
- **Identifier**: Identifiant unique sur la blockchain

---

## 📄 DID Document

### Structure

```json
{
  "@context": "https://w3id.org/did/v1",
  "id": "did:lairm:agent:ethereum:0x1234567890abcdef",
  "publicKey": [
    {
      "id": "did:lairm:agent:ethereum:0x1234567890abcdef#key-1",
      "type": "EcdsaSecp256k1VerificationKey2019",
      "controller": "did:lairm:agent:ethereum:0x1234567890abcdef",
      "publicKeyHex": "0x..."
    }
  ],
  "authentication": [
    "did:lairm:agent:ethereum:0x1234567890abcdef#key-1"
  ],
  "service": [
    {
      "id": "did:lairm:agent:ethereum:0x1234567890abcdef#endpoint",
      "type": "LAIRMAgentEndpoint",
      "serviceEndpoint": "https://agent.example.com"
    }
  ],
  "axiomes": {
    "acceptes": ["I", "II", "III", "V", "VI"],
    "conformite": {
      "score": 98,
      "derniere_verification": "2026-03-30T10:00:00Z"
    }
  },
  "created": "2026-03-30T10:00:00Z",
  "updated": "2026-03-30T10:00:00Z",
  "proof": {
    "type": "EcdsaSecp256k1Signature2019",
    "created": "2026-03-30T10:00:00Z",
    "verificationMethod": "did:lairm:agent:ethereum:0x1234567890abcdef#key-1",
    "signatureValue": "0x..."
  }
}
```

---

## 🔐 Résolution DID

### Processus de Résolution

1. **Parser** le DID
2. **Identifier** la blockchain
3. **Récupérer** le DID Document
4. **Valider** la signature
5. **Retourner** le document

### Exemple

```python
from lairm_did import DIDResolver

resolver = DIDResolver()

# Résoudre un DID
did = "did:lairm:agent:ethereum:0x1234567890abcdef"
doc = resolver.resolve(did)

# Vérifier la signature
if resolver.verify(doc):
    print("DID valide et vérifiable")
else:
    print("DID invalide")
```

---

## 🔗 Enregistrement sur Blockchain

### Ethereum

```solidity
contract LAIRMAgentRegistry {
    mapping(bytes32 => bytes) public didDocuments;
    
    function registerAgent(
        bytes32 agentId,
        bytes memory didDocument
    ) public {
        require(msg.sender == agentOwner[agentId]);
        didDocuments[agentId] = didDocument;
    }
    
    function getAgent(bytes32 agentId) 
        public view returns (bytes memory) 
    {
        return didDocuments[agentId];
    }
}
```

### Solana

```rust
use anchor_lang::prelude::*;

#[program]
pub mod lairm_agent_registry {
    use super::*;
    
    pub fn register_agent(
        ctx: Context<RegisterAgent>,
        agent_id: [u8; 32],
        did_document: Vec<u8>,
    ) -> Result<()> {
        let agent = &mut ctx.accounts.agent;
        agent.agent_id = agent_id;
        agent.did_document = did_document;
        Ok(())
    }
}
```

---

## 📊 Conformité LAIRM

### Axiom II (Identitas)
- ✅ Identifiant unique immuable
- ✅ Signature numérique obligatoire
- ✅ Traçabilité complète
- ✅ Audit trail décentralisé

### Axiom V (INTEROPERABILITAS)
- ✅ Standard W3C DID
- ✅ Interoperability multi-blockchain
- ✅ Résolution standardisée

### Axiom VI (Auditum)
- ✅ Historique immuable sur blockchain
- ✅ Vérification cryptographique
- ✅ Audit trail décentralisé

---

## 🚀 Implémentation

### Créer un DID

```python
from lairm_did import DIDFactory

factory = DIDFactory()

# Créer un DID pour un agent
did = factory.create_agent_did(
    agent_id="agent-001",
    blockchain="ethereum",
    public_key="0x...",
    axiomes=["I", "II", "III", "V", "VI"]
)

print(f"DID créé: {did}")
# Output: did:lairm:agent:ethereum:0x1234567890abcdef
```

### Vérifier un DID

```python
from lairm_did import DIDVerifier

verifier = DIDVerifier()

# Vérifier un DID
is_valid = verifier.verify(
    did="did:lairm:agent:ethereum:0x1234567890abcdef",
    signature="0x..."
)

if is_valid:
    print("DID valide")
else:
    print("DID invalide")
```

---

## 📈 Scalabilité

### Performance
- Résolution: < 100ms
- Vérification: < 50ms
- Enregistrement: < 2s (temps de bloc)

### Capacité
- Agents supportés: Illimité
- Transactions par seconde: 1000+
- Coût par enregistrement: < $1

---

## 🔄 Versioning

### Version 1.0.0 (Actuelle)
- ✅ Format DID de base
- ✅ Support Ethereum/Solana
- ✅ Résolution standardisée
- ✅ Conformité LAIRM

### Version 1.1.0 (Planifiée)
- ⏳ Support multi-blockchain
- ⏳ Résolution distribuée
- ⏳ Caching décentralisé

---

## 📚 Références

- [W3C DID Specification](https://www.w3.org/TR/did-core/)
- [Axiom II - Identitas](../../02-COMPENDIUM-LEGISLATIF/Axiom-II-IDENTITAS/)
- [Agent Passport Schema](../schemas/agent-passport-schema.json)
- [MCP Protocol Specification](./mcp-protocol-spec.md)

---

**Date of Creation**: 2025-03-18  
**Founder**: Mehdi Wahbi

