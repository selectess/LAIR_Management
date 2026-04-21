# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

#!/usr/bin/env python3
"""
LAIRM Cryptographic Security Module
Signatures RSA-4096, Chiffrement AES-256, Certificats Numériques
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Tuple
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID
import os

logger = logging.getLogger(__name__)


class CryptoSignature:
    """Gestion des signatures cryptographiques RSA-4096"""

    def __init__(self, key_size: int = 4096):
        """Initialiser avec génération de clés RSA"""
        self.key_size = key_size
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()
        logger.info(f"Generated RSA-{key_size} key pair")

    def sign_audit_record(self, record: Dict) -> str:
        """Signer un enregistrement d'audit avec RSA-4096"""
        record_bytes = json.dumps(record, sort_keys=True).encode()
        signature = self.private_key.sign(
            record_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature.hex()

    def verify_signature(self, record: Dict, signature: str) -> bool:
        """Vérifier une signature RSA"""
        record_bytes = json.dumps(record, sort_keys=True).encode()
        try:
            self.public_key.verify(
                bytes.fromhex(signature),
                record_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            logger.error(f"Signature verification failed: {e}")
            return False

    def export_public_key(self) -> str:
        """Exporter la clé publique en PEM"""
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode()

    def export_private_key(self, password: bytes = None) -> str:
        """Exporter la clé privée en PEM (optionnellement chiffrée)"""
        if password:
            encryption = serialization.BestAvailableEncryption(password)
        else:
            encryption = serialization.NoEncryption()
        
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption
        )
        return pem.decode()


class CryptoEncryption:
    """Gestion du chiffrement AES-256"""

    def __init__(self):
        """Initialiser le module de chiffrement"""
        self.backend = default_backend()
        logger.info("Initialized AES-256 encryption module")

    def encrypt_audit_log(self, data: str, key: bytes = None) -> Tuple[str, str]:
        """Chiffrer un log d'audit avec AES-256-CBC"""
        if key is None:
            key = os.urandom(32)  # 256 bits
        
        # Handle both bytes and string keys for compatibility
        if isinstance(key, str):
            key_bytes = bytes.fromhex(key)
        else:
            key_bytes = key
        
        iv = os.urandom(16)  # 128 bits
        cipher = Cipher(
            algorithms.AES(key_bytes),
            modes.CBC(iv),
            backend=self.backend
        )
        encryptor = cipher.encryptor()
        
        # Padding PKCS7
        data_bytes = data.encode()
        padding_length = 16 - (len(data_bytes) % 16)
        padded_data = data_bytes + bytes([padding_length] * padding_length)
        
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        encrypted_data = (iv + ciphertext).hex()
        
        return encrypted_data, key_bytes.hex()

    def decrypt_audit_log(self, encrypted_data: str, key: bytes) -> str:
        """Déchiffrer un log d'audit"""
        data = bytes.fromhex(encrypted_data)
        
        # Handle both bytes and string keys for compatibility
        if isinstance(key, str):
            key_bytes = bytes.fromhex(key)
        else:
            key_bytes = key
        
        iv = data[:16]
        ciphertext = data[16:]
        
        cipher = Cipher(
            algorithms.AES(key_bytes),
            modes.CBC(iv),
            backend=self.backend
        )
        decryptor = cipher.decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Retirer le padding PKCS7
        padding_length = padded_plaintext[-1]
        plaintext = padded_plaintext[:-padding_length]
        
        return plaintext.decode()

    @staticmethod
    def generate_key() -> str:
        """Générer une clé AES-256 aléatoire (returns hex string)"""
        return os.urandom(32).hex()


class DigitalCertificate:
    """Gestion des certificats numériques"""

    def __init__(self):
        """Initialiser le module de certificats"""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        logger.info("Initialized digital certificate module")

    def create_agent_certificate(
        self,
        agent_id: str,
        organization: str = "LAIRM",
        country: str = "UN",
        validity_days: int = 365
    ) -> x509.Certificate:
        """Créer un certificat numérique pour un agent"""
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, agent_id),
        ])
        
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            self.private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.utcnow()
        ).not_valid_after(
            datetime.utcnow() + timedelta(days=validity_days)
        ).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName(f"{agent_id}.lairm.local"),
            ]),
            critical=False,
        ).sign(self.private_key, hashes.SHA256(), default_backend())
        
        logger.info(f"Created certificate for agent {agent_id}")
        return cert

    def export_certificate(self, cert: x509.Certificate) -> str:
        """Exporter un certificat en PEM"""
        pem = cert.public_bytes(serialization.Encoding.PEM)
        return pem.decode()

    def export_certificate_chain(self, cert: x509.Certificate) -> str:
        """Exporter la chaîne de certificats"""
        # Pour un certificat auto-signé, la chaîne contient juste le certificat
        return self.export_certificate(cert)


class SecureAuditRecord:
    """Enregistrement d'audit sécurisé avec signature et chiffrement"""

    def __init__(self):
        """Initialiser le module d'audit sécurisé"""
        self.signature = CryptoSignature()
        self.encryption = CryptoEncryption()
        self.certificate = DigitalCertificate()

    def create_secure_record(
        self,
        agent_id: str,
        action_type: str = None,
        action: str = None,
        details: Dict = None,
        encrypt: bool = True,
        encryption_key: str = None
    ) -> Dict:
        """Créer un enregistrement d'audit sécurisé"""
        # Support both action_type and action parameters for compatibility
        if action is not None and action_type is None:
            action_type = action
        elif action_type is None:
            action_type = "unknown"
            
        record = {
            'timestamp': datetime.now().isoformat(),
            'agent_id': agent_id,
            'action': action_type,  # Use 'action' as the key for compatibility
            'details': details or {},
            'version': '1.0'
        }
        
        # Signer l'enregistrement
        signature = self.signature.sign_audit_record(record)
        
        # Chiffrer si demandé
        if encrypt:
            if encryption_key is None:
                encryption_key = self.encryption.generate_key()
            
            record_json = json.dumps(record)
            encrypted_data, used_key = self.encryption.encrypt_audit_log(
                record_json,
                encryption_key
            )
            
            # Extract IV from encrypted_data (first 32 hex chars = 16 bytes)
            iv = encrypted_data[:32]
            
            return {
                'encrypted_data': encrypted_data,
                'encryption_key': used_key,
                'signature': signature,  # Include signature outside encryption
                'iv': iv,
                'encrypted': True
            }
        
        # For unencrypted records, add signature
        record['signature'] = signature
        return record

    def verify_secure_record(self, record: Dict) -> bool:
        """Vérifier un enregistrement d'audit sécurisé"""
        # Handle encrypted records
        if record.get('encrypted'):
            # For encrypted records, we need to decrypt first to verify
            try:
                decrypted, is_valid = self.decrypt_and_verify(record)
                return is_valid
            except Exception as e:
                logger.error(f"Failed to verify encrypted record: {e}")
                return False
        
        # Handle unencrypted records
        if 'signature' not in record:
            logger.error("Record missing signature")
            return False
        
        signature = record.pop('signature')
        is_valid = self.signature.verify_signature(record, signature)
        record['signature'] = signature  # Restaurer la signature
        
        return is_valid

    def decrypt_and_verify(self, encrypted_record: Dict) -> Tuple[Dict, bool]:
        """Déchiffrer et vérifier un enregistrement"""
        if not encrypted_record.get('encrypted'):
            return encrypted_record, False
        
        try:
            decrypted_json = self.encryption.decrypt_audit_log(
                encrypted_record['encrypted_data'],
                encrypted_record['encryption_key']
            )
            record = json.loads(decrypted_json)
            
            # Verify the signature (stored outside encryption)
            if 'signature' in encrypted_record:
                signature = encrypted_record['signature']
                is_valid = self.signature.verify_signature(record, signature)
                record['signature'] = signature  # Add signature to decrypted record
            else:
                logger.error("Encrypted record missing signature")
                is_valid = False
            
            return record, is_valid
        except Exception as e:
            logger.error(f"Failed to decrypt and verify: {e}")
            return {}, False


def main():
    """Test du module de sécurité cryptographique"""
    print("=" * 80)
    print("LAIRM CRYPTOGRAPHIC SECURITY MODULE - TEST")
    print("=" * 80)
    print()
    
    # Test 1: Signatures RSA-4096
    print("1. Testing RSA-4096 Signatures")
    print("-" * 40)
    crypto_sig = CryptoSignature()
    record = {
        'agent_id': 'agent-001',
        'action': 'test_action',
        'timestamp': datetime.now().isoformat()
    }
    
    signature = crypto_sig.sign_audit_record(record)
    print(f"Signature: {signature[:32]}...")
    
    is_valid = crypto_sig.verify_signature(record, signature)
    print(f"Signature valid: {is_valid}")
    
    # Tenter de modifier le record
    record['action'] = 'tampered'
    is_valid_after_tampering = crypto_sig.verify_signature(record, signature)
    print(f"Signature valid after tampering: {is_valid_after_tampering}")
    print()
    
    # Test 2: Chiffrement AES-256
    print("2. Testing AES-256 Encryption")
    print("-" * 40)
    crypto_enc = CryptoEncryption()
    data = "Sensitive audit log data"
    
    encrypted_data, key = crypto_enc.encrypt_audit_log(data)
    print(f"Encrypted: {encrypted_data[:32]}...")
    print(f"Key: {key[:32]}...")
    
    decrypted_data = crypto_enc.decrypt_audit_log(encrypted_data, key)
    print(f"Decrypted: {decrypted_data}")
    print(f"Match: {decrypted_data == data}")
    print()
    
    # Test 3: Certificats Numériques
    print("3. Testing Digital Certificates")
    print("-" * 40)
    cert_manager = DigitalCertificate()
    cert = cert_manager.create_agent_certificate('agent-001')
    
    cert_pem = cert_manager.export_certificate(cert)
    print(f"Certificate created for: {cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value}")
    print(f"Valid from: {cert.not_valid_before}")
    print(f"Valid until: {cert.not_valid_after}")
    print()
    
    # Test 4: Enregistrements d'audit sécurisés
    print("4. Testing Secure Audit Records")
    print("-" * 40)
    secure_audit = SecureAuditRecord()
    
    secure_record = secure_audit.create_secure_record(
        agent_id='agent-001',
        action_type='critical_action',
        details={'result': 'success'},
        encrypt=True
    )
    
    print(f"Encrypted record created")
    print(f"Encrypted data: {secure_record['encrypted_data'][:32]}...")
    
    decrypted, is_valid = secure_audit.decrypt_and_verify(secure_record)
    print(f"Decrypted successfully: {bool(decrypted)}")
    print(f"Signature valid: {is_valid}")
    print()
    
    print("=" * 80)
    print("✅ LAIRM Cryptographic Security Module Ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
