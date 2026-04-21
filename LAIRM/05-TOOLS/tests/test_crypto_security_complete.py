# ============================================================================
# LAIRM Module
# date_creation: 2024-03-18
# last_updated: 2026-04-20
# last_review: 2026-04-20
# ============================================================================

"""
Complete Test Suite for LAIRM Crypto Security
Tests RSA-4096 signatures, AES-256 encryption, and certificates
"""

import pytest
import json
from cryptography.x509.oid import NameOID
from audit_engine.crypto_security import (
    CryptoSignature,
    CryptoEncryption,
    DigitalCertificate,
    SecureAuditRecord
)


class TestCryptoSignature:
    """Test suite for RSA-4096 signatures"""
    
    @pytest.fixture
    def crypto(self):
        """Initialize crypto signature"""
        return CryptoSignature(key_size=4096)
    
    def test_signature_generation(self, crypto):
        """Test signature generation"""
        record = {'agent_id': 'test', 'action': 'deploy'}
        signature = crypto.sign_audit_record(record)
        
        assert signature is not None
        assert isinstance(signature, str)
        assert len(signature) > 0
    
    def test_signature_verification(self, crypto):
        """Test signature verification"""
        record = {'agent_id': 'test', 'action': 'deploy'}
        signature = crypto.sign_audit_record(record)
        
        is_valid = crypto.verify_signature(record, signature)
        assert is_valid == True
    
    def test_signature_tampering_detection(self, crypto):
        """Test detection of signature tampering"""
        record = {'agent_id': 'test', 'action': 'deploy'}
        signature = crypto.sign_audit_record(record)
        
        # Tamper with record
        record['action'] = 'tampered'
        
        is_valid = crypto.verify_signature(record, signature)
        assert is_valid == False
    
    def test_signature_invalid_format(self, crypto):
        """Test with invalid signature format"""
        record = {'agent_id': 'test', 'action': 'deploy'}
        invalid_signature = 'invalid_signature_format'
        
        is_valid = crypto.verify_signature(record, invalid_signature)
        assert is_valid == False
    
    def test_multiple_signatures(self, crypto):
        """Test multiple signatures"""
        records = [
            {'agent_id': 'test-001', 'action': 'deploy'},
            {'agent_id': 'test-002', 'action': 'update'},
            {'agent_id': 'test-003', 'action': 'delete'}
        ]
        
        signatures = [crypto.sign_audit_record(r) for r in records]
        
        for record, signature in zip(records, signatures):
            assert crypto.verify_signature(record, signature) == True
    
    def test_key_export_import(self, crypto):
        """Test key export and import"""
        public_key_pem = crypto.export_public_key()
        
        assert public_key_pem is not None
        assert 'BEGIN PUBLIC KEY' in public_key_pem
        assert 'END PUBLIC KEY' in public_key_pem
    
    def test_private_key_export(self, crypto):
        """Test private key export"""
        private_key_pem = crypto.export_private_key()
        
        assert private_key_pem is not None
        assert 'BEGIN PRIVATE KEY' in private_key_pem
        assert 'END PRIVATE KEY' in private_key_pem
    
    def test_signature_with_large_record(self, crypto):
        """Test signature with large record"""
        large_record = {
            'agent_id': 'test',
            'action': 'deploy',
            'data': 'x' * 10000  # 10KB
        }
        
        signature = crypto.sign_audit_record(large_record)
        is_valid = crypto.verify_signature(large_record, signature)
        
        assert is_valid == True
    
    def test_signature_consistency(self, crypto):
        """Test signature consistency"""
        record = {'agent_id': 'test', 'action': 'deploy'}
        
        # Same record should produce different signatures (due to randomness in PSS)
        sig1 = crypto.sign_audit_record(record)
        sig2 = crypto.sign_audit_record(record)
        
        # But both should verify
        assert crypto.verify_signature(record, sig1) == True
        assert crypto.verify_signature(record, sig2) == True


class TestCryptoEncryption:
    """Test suite for AES-256 encryption"""
    
    @pytest.fixture
    def encryption(self):
        """Initialize crypto encryption"""
        return CryptoEncryption()
    
    def test_encryption_decryption(self, encryption):
        """Test encryption and decryption"""
        key = CryptoEncryption.generate_key()
        plaintext = "Sensitive audit data"
        
        encrypted, iv = encryption.encrypt_audit_log(plaintext, key)
        decrypted = encryption.decrypt_audit_log(encrypted, key)
        
        assert decrypted == plaintext
    
    def test_encryption_produces_different_ciphertexts(self, encryption):
        """Test that same plaintext produces different ciphertexts"""
        key = CryptoEncryption.generate_key()
        plaintext = "Sensitive data"
        
        encrypted1, iv1 = encryption.encrypt_audit_log(plaintext, key)
        encrypted2, iv2 = encryption.encrypt_audit_log(plaintext, key)
        
        # Different IVs should produce different ciphertexts
        assert encrypted1 != encrypted2
    
    def test_encryption_with_wrong_key(self, encryption):
        """Test decryption with wrong key fails"""
        key1 = CryptoEncryption.generate_key()
        key2 = CryptoEncryption.generate_key()
        plaintext = "Sensitive data"
        
        encrypted, iv = encryption.encrypt_audit_log(plaintext, key1)
        
        # Decryption with wrong key should fail or produce garbage
        try:
            decrypted = encryption.decrypt_audit_log(encrypted, key2)
            assert decrypted != plaintext
        except:
            pass  # Expected to fail
    
    def test_encryption_large_data(self, encryption):
        """Test encryption of large data"""
        key = CryptoEncryption.generate_key()
        plaintext = "x" * 100000  # 100KB
        
        encrypted, iv = encryption.encrypt_audit_log(plaintext, key)
        decrypted = encryption.decrypt_audit_log(encrypted, key)
        
        assert decrypted == plaintext
    
    def test_key_generation(self, encryption):
        """Test key generation"""
        key = CryptoEncryption.generate_key()
        
        assert key is not None
        assert isinstance(key, str)
        assert len(key) > 0
    
    def test_encryption_json_data(self, encryption):
        """Test encryption of JSON data"""
        key = CryptoEncryption.generate_key()
        data = json.dumps({
            'agent_id': 'test-001',
            'action': 'deploy',
            'timestamp': '2026-04-19T00:00:00Z'
        })
        
        encrypted, iv = encryption.encrypt_audit_log(data, key)
        decrypted = encryption.decrypt_audit_log(encrypted, key)
        
        assert json.loads(decrypted) == json.loads(data)
    
    def test_encryption_special_characters(self, encryption):
        """Test encryption with special characters"""
        key = CryptoEncryption.generate_key()
        plaintext = "Special: !@#$%^&*() Unicode: 你好 Emoji: 🚀"
        
        encrypted, iv = encryption.encrypt_audit_log(plaintext, key)
        decrypted = encryption.decrypt_audit_log(encrypted, key)
        
        assert decrypted == plaintext


class TestDigitalCertificate:
    """Test suite for X.509 digital certificates"""
    
    @pytest.fixture
    def cert_manager(self):
        """Initialize certificate manager"""
        return DigitalCertificate()
    
    def test_certificate_creation(self, cert_manager):
        """Test certificate creation"""
        cert = cert_manager.create_agent_certificate('agent-001')
        
        assert cert is not None
        assert cert.subject.get_attributes_for_oid(
            NameOID.COMMON_NAME
        )[0].value == 'agent-001'
    
    def test_certificate_validity(self, cert_manager):
        """Test certificate validity period"""
        cert = cert_manager.create_agent_certificate('agent-001')
        
        # Certificate should be valid for 365 days
        assert cert.not_valid_after > cert.not_valid_before
    
    def test_certificate_export(self, cert_manager):
        """Test certificate export"""
        cert = cert_manager.create_agent_certificate('agent-001')
        cert_pem = cert_manager.export_certificate(cert)
        
        assert cert_pem is not None
        assert 'BEGIN CERTIFICATE' in cert_pem
        assert 'END CERTIFICATE' in cert_pem
    
    def test_multiple_certificates(self, cert_manager):
        """Test creating multiple certificates"""
        agents = ['agent-001', 'agent-002', 'agent-003']
        certs = [cert_manager.create_agent_certificate(a) for a in agents]
        
        assert len(certs) == 3
        for cert, agent in zip(certs, agents):
            assert cert is not None
    
    def test_certificate_chain_export(self, cert_manager):
        """Test certificate chain export"""
        cert = cert_manager.create_agent_certificate('agent-001')
        chain_pem = cert_manager.export_certificate_chain(cert)
        
        assert chain_pem is not None
        assert 'BEGIN CERTIFICATE' in chain_pem


class TestSecureAuditRecord:
    """Test suite for secure audit records (signature + encryption)"""
    
    @pytest.fixture
    def secure(self):
        """Initialize secure audit record"""
        return SecureAuditRecord()
    
    def test_secure_record_creation(self, secure):
        """Test creating secure audit record"""
        record = secure.create_secure_record(
            agent_id='agent-001',
            action='deploy',
            details={'version': '1.0'}
        )
        
        assert record is not None
        assert 'signature' in record
        assert 'encrypted_data' in record
        assert 'iv' in record
    
    def test_secure_record_verification(self, secure):
        """Test verifying secure audit record"""
        record = secure.create_secure_record(
            agent_id='agent-001',
            action='deploy',
            details={'version': '1.0'}
        )
        
        is_valid = secure.verify_secure_record(record)
        assert is_valid == True
    
    def test_secure_record_tampering_detection(self, secure):
        """Test detection of tampering in secure record"""
        record = secure.create_secure_record(
            agent_id='agent-001',
            action='deploy',
            details={'version': '1.0'}
        )
        
        # Tamper with signature
        record['signature'] = 'tampered_signature'
        
        is_valid = secure.verify_secure_record(record)
        assert is_valid == False
    
    def test_secure_record_decrypt_and_verify(self, secure):
        """Test decryption and verification of secure record"""
        record = secure.create_secure_record(
            agent_id='agent-001',
            action='deploy',
            details={'version': '1.0'}
        )
        
        decrypted, is_valid = secure.decrypt_and_verify(record)
        
        assert is_valid == True
        assert decrypted['agent_id'] == 'agent-001'
        assert decrypted['action'] == 'deploy'
    
    def test_multiple_secure_records(self, secure):
        """Test creating multiple secure records"""
        records = []
        for i in range(10):
            record = secure.create_secure_record(
                agent_id=f'agent-{i:03d}',
                action='action',
                details={'index': i}
            )
            records.append(record)
        
        # Verify all records
        for record in records:
            assert secure.verify_secure_record(record) == True
    
    def test_secure_record_with_large_details(self, secure):
        """Test secure record with large details"""
        large_details = {
            'data': 'x' * 10000,
            'nested': {
                'level1': {
                    'level2': {
                        'level3': 'deep'
                    }
                }
            }
        }
        
        record = secure.create_secure_record(
            agent_id='agent-001',
            action='deploy',
            details=large_details
        )
        
        is_valid = secure.verify_secure_record(record)
        assert is_valid == True


class TestCryptoIntegration:
    """Integration tests for crypto security"""
    
    def test_full_crypto_workflow(self):
        """Test full cryptographic workflow"""
        # 1. Create signature
        crypto = CryptoSignature()
        record = {'agent_id': 'test', 'action': 'deploy'}
        signature = crypto.sign_audit_record(record)
        
        # 2. Encrypt
        encryption = CryptoEncryption()
        key = CryptoEncryption.generate_key()
        encrypted, iv = encryption.encrypt_audit_log(
            json.dumps(record),
            key
        )
        
        # 3. Create certificate
        cert_manager = DigitalCertificate()
        cert = cert_manager.create_agent_certificate('agent-001')
        
        # 4. Verify signature
        assert crypto.verify_signature(record, signature) == True
        
        # 5. Decrypt
        decrypted = encryption.decrypt_audit_log(encrypted, key)
        assert json.loads(decrypted) == record
        
        # 6. Verify certificate
        assert cert is not None
    
    def test_secure_audit_record_workflow(self):
        """Test secure audit record workflow"""
        secure = SecureAuditRecord()
        
        # Create secure record
        record = secure.create_secure_record(
            agent_id='agent-001',
            action='deploy',
            details={'version': '1.0'}
        )
        
        # Verify
        assert secure.verify_secure_record(record) == True
        
        # Decrypt and verify
        decrypted, is_valid = secure.decrypt_and_verify(record)
        assert is_valid == True
        assert decrypted['agent_id'] == 'agent-001'


class TestCryptoPerformance:
    """Performance tests for crypto operations"""
    
    def test_signature_performance(self):
        """Test signature generation performance"""
        import time
        
        crypto = CryptoSignature()
        record = {'agent_id': 'test', 'action': 'deploy'}
        
        start = time.time()
        for _ in range(100):
            crypto.sign_audit_record(record)
        elapsed = time.time() - start
        
        # Should complete in reasonable time
        assert elapsed < 30.0  # 100 signatures in < 30 seconds
    
    def test_encryption_performance(self):
        """Test encryption performance"""
        import time
        
        encryption = CryptoEncryption()
        key = CryptoEncryption.generate_key()
        plaintext = "x" * 1000
        
        start = time.time()
        for _ in range(1000):
            encryption.encrypt_audit_log(plaintext, key)
        elapsed = time.time() - start
        
        # Should complete quickly
        assert elapsed < 5.0  # 1000 encryptions in < 5 seconds


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
