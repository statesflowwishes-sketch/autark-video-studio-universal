# Datenschutzerklärung
## Nach DSGVO (EU) 2016/679

### 🛡️ Datenschutz bei AUTARK Video Studio

**Verantwortlicher**: AUTARK Video Studio Repository  
**Kontakt**: GitHub Issues mit Label `privacy`  
**Datenschutzbeauftragter**: Verfügbar über Repository-Kontakt  

---

## 📋 1. Allgemeine Informationen

### Grundsätze der Datenverarbeitung (Art. 5 DSGVO)

Wir verarbeiten Ihre personenbezogenen Daten nach folgenden Grundsätzen:

- **Rechtmäßigkeit**: Nur mit gültiger Rechtsgrundlage
- **Zweckbindung**: Ausschließlich für den angegebenen Zweck
- **Datenminimierung**: Nur notwendige Daten
- **Richtigkeit**: Korrekte und aktuelle Daten
- **Speicherbegrenzung**: Nur solange wie nötig
- **Integrität**: Sicherheit durch technische Maßnahmen
- **Rechenschaftspflicht**: Nachweis der Compliance

---

## 📊 2. Datenverarbeitung im Detail

### 2.1 Welche Daten verarbeiten wir?

| Datentyp | Beispiele | Rechtsgrundlage | Zweck |
|----------|-----------|-----------------|-------|
| **Nutzereingaben** | Text-Prompts, Upload-Dateien | Art. 6 Abs. 1 lit. a (Einwilligung) | Video-Generierung |
| **Technische Daten** | IP-Adresse, Browser-Info | Art. 6 Abs. 1 lit. f (berechtigtes Interesse) | System-Stabilität |
| **Nutzungsstatistiken** | Verwendete Features, Häufigkeit | Art. 6 Abs. 1 lit. a (Einwilligung) | Service-Verbesserung |
| **Qualitätsmetriken** | Output-Bewertungen, Feedback | Art. 6 Abs. 1 lit. a (Einwilligung) | AI-Optimierung |

### 2.2 Keine Verarbeitung besonderer Kategorien

❌ Wir verarbeiten **KEINE** besonderen Kategorien personenbezogener Daten (Art. 9 DSGVO):
- Ethnische Herkunft
- Politische Meinungen  
- Religiöse Überzeugungen
- Gesundheitsdaten
- Sexuelle Orientierung
- Biometrische Daten zur Identifikation

---

## ⚖️ 3. Rechtsgrundlagen (Art. 6 DSGVO)

### 3.1 Einwilligung (Art. 6 Abs. 1 lit. a)

```python
# Beispiel: Einwilligungsmanagement
class ConsentManager:
    def __init__(self):
        self.consent_types = {
            "content_generation": "Für AI-Content-Generierung",
            "analytics": "Für Nutzungsanalyse",
            "quality_improvement": "Für Service-Verbesserung"
        }
    
    def request_consent(self, user_id, consent_type):
        """Explizite, informierte Einwilligung einholen"""
        return {
            "consent_id": generate_consent_id(),
            "timestamp": current_timestamp(),
            "revocable": True,
            "specific": True,
            "informed": True,
            "unambiguous": True
        }
```

### 3.2 Berechtigtes Interesse (Art. 6 Abs. 1 lit. f)

**Unser berechtigtes Interesse**: Bereitstellung und Verbesserung der AI-Services

**Interessensabwägung**:
- ✅ Unser Interesse: Stabile, sichere Services anbieten
- ✅ Nutzerinteresse: Funktionierende, verbesserte AI-Tools
- ✅ Verhältnismäßigkeit: Minimale Datenerhebung
- ✅ Betroffenenrechte: Widerspruchsrecht gewährleistet

---

## 🕒 4. Speicherdauer

### Automatische Löschung

```python
class DataRetentionPolicy:
    """Automatisierte Datenaufbewahrung nach DSGVO"""
    
    retention_periods = {
        "user_inputs": timedelta(days=30),      # Nutzer-Prompts
        "generated_content": timedelta(days=90), # AI-Outputs  
        "technical_logs": timedelta(days=30),    # System-Logs
        "analytics_data": timedelta(days=365),   # Anonymisierte Metriken
        "consent_records": timedelta(years=3)    # Einwilligungsnachweise
    }
    
    def auto_delete_expired_data(self):
        """Tägliche automatische Löschung abgelaufener Daten"""
        for data_type, retention_period in self.retention_periods.items():
            cutoff_date = datetime.now() - retention_period
            self.delete_data_older_than(data_type, cutoff_date)
```

---

## 🔒 5. Technische und organisatorische Maßnahmen

### 5.1 IT-Sicherheit (Art. 32 DSGVO)

#### Verschlüsselung
```yaml
encryption_standards:
  data_in_transit: "TLS 1.3"
  data_at_rest: "AES-256"
  key_management: "HSM-based"
  key_rotation: "quarterly"
```

#### Zugriffskontrolle
```python
class AccessControl:
    """Rollenbasierte Zugriffskontrolle"""
    
    def __init__(self):
        self.principle = "least_privilege"
        self.authentication = "multi_factor"
        self.audit_logging = "comprehensive"
    
    def authorize_data_access(self, user_role, data_type):
        permissions = {
            "user": ["own_data_read", "own_data_delete"],
            "admin": ["system_logs_read", "anonymized_analytics"],
            "dpo": ["all_data_audit", "consent_management"]
        }
        return data_type in permissions.get(user_role, [])
```

### 5.2 Organisatorische Maßnahmen

- **Schulungen**: Regelmäßige DSGVO-Schulungen für Entwicklerteam
- **Dokumentation**: Vollständige Verarbeitungsverzeichnisse
- **Incident Response**: 24/7 Bereitschaft für Datenschutz-Vorfälle
- **Privacy by Design**: Datenschutz von Anfang an mitgedacht

---

## 👥 6. Ihre Rechte als betroffene Person

### 6.1 Auskunftsrecht (Art. 15 DSGVO)

```python
def provide_data_overview(user_id):
    """Vollständige Auskunft über verarbeitete Daten"""
    return {
        "personal_data": get_user_personal_data(user_id),
        "processing_purposes": get_processing_purposes(user_id),
        "legal_basis": get_legal_basis_per_purpose(user_id),
        "retention_periods": get_retention_periods(),
        "recipients": get_data_recipients(),
        "your_rights": get_user_rights_info()
    }
```

### 6.2 Recht auf Berichtigung (Art. 16 DSGVO)

Sie können jederzeit die Berichtigung unrichtiger personenbezogener Daten verlangen.

### 6.3 Recht auf Löschung (Art. 17 DSGVO)

```python
def delete_user_data(user_id, deletion_reason):
    """Sichere Löschung aller Nutzerdaten"""
    
    valid_reasons = [
        "data_no_longer_necessary",
        "consent_withdrawn", 
        "unlawful_processing",
        "legal_obligation"
    ]
    
    if deletion_reason in valid_reasons:
        return {
            "status": "deleted",
            "confirmation": secure_delete_all_data(user_id),
            "retention_only": ["legal_compliance_records"],
            "deletion_certificate": generate_deletion_certificate()
        }
```

### 6.4 Recht auf Datenübertragbarkeit (Art. 20 DSGVO)

```python
def export_user_data(user_id):
    """Datenexport in strukturiertem, maschinenlesbarem Format"""
    return {
        "format": "JSON",
        "encoding": "UTF-8", 
        "data": {
            "user_inputs": get_user_inputs(user_id),
            "generated_content": get_user_generated_content(user_id),
            "preferences": get_user_preferences(user_id),
            "consent_history": get_consent_history(user_id)
        },
        "metadata": {
            "export_date": datetime.now().isoformat(),
            "data_version": "1.0"
        }
    }
```

### 6.5 Widerspruchsrecht (Art. 21 DSGVO)

Bei Verarbeitung aufgrund berechtigten Interesses können Sie **jederzeit** widersprechen.

---

## 🌍 7. Internationale Datenübertragung

### 7.1 Datenübertragung außerhalb der EU

Falls Datenübertragung in Drittländer erforderlich:

```python
class InternationalTransfer:
    """DSGVO-konforme internationale Datenübertragung"""
    
    def __init__(self):
        self.adequacy_decisions = ["UK", "Switzerland", "Canada"]
        self.standard_contractual_clauses = True
        self.binding_corporate_rules = True
    
    def validate_transfer(self, destination_country):
        if destination_country in self.adequacy_decisions:
            return "adequate_protection_level"
        elif self.standard_contractual_clauses:
            return "appropriate_safeguards_scc"
        else:
            return "transfer_not_permitted"
```

### 7.2 Verwendete Cloud-Services

| Service | Anbieter | Standort | Schutzmaßnahmen |
|---------|----------|----------|-----------------|
| GitHub | Microsoft | EU/US | Standard Contractual Clauses |
| HuggingFace | Hugging Face | EU | DSGVO-konform |
| Compute | Regional Provider | Deutschland | Auftragsverarbeitung |

---

## 📧 8. Kontakt und Beschwerden

### 8.1 Datenschutzbeauftragter

**Kontakt**: GitHub Issues mit Label `privacy`  
**Reaktionszeit**: Maximal 72 Stunden  
**Sprachen**: Deutsch, Englisch  

### 8.2 Beschwerderecht (Art. 77 DSGVO)

Sie haben das Recht, sich bei einer Aufsichtsbehörde zu beschweren:

**Deutschland**: Bundesbeauftragte für den Datenschutz und die Informationsfreiheit  
**Adresse**: Graurheindorfer Str. 153, 53117 Bonn  
**Website**: https://www.bfdi.bund.de  

**Ihr Bundesland**: Jeweilige Landesdatenschutzbehörde  

---

## 🔄 9. Änderungen dieser Datenschutzerklärung

### Versionskontrolle

```yaml
privacy_policy_version:
  current: "1.0"
  last_updated: "2025-08-28"
  next_review: "2025-11-28"
  changelog:
    - "2025-08-28: Erstversion erstellt"
```

### Benachrichtigung bei Änderungen

- **Wesentliche Änderungen**: Aktive Benachrichtigung der Nutzer
- **Redaktionelle Änderungen**: Information im Repository
- **Neue Rechtsgrundlagen**: Neue Einwilligung erforderlich

---

## 📋 10. Verarbeitungsverzeichnis (Art. 30 DSGVO)

### Übersicht aller Verarbeitungstätigkeiten

| ID | Zweck | Kategorien | Rechtsgrundlage | Empfänger | Löschfrist |
|----|-------|------------|-----------------|-----------|------------|
| V001 | Content-Generierung | Textprompts | Einwilligung | AI-Models | 30 Tage |
| V002 | System-Monitoring | IP, Logs | Berechtigtes Interesse | Intern | 30 Tage |
| V003 | Service-Optimierung | Nutzungsmetriken | Einwilligung | Intern | 1 Jahr |

---

## ⚖️ Rechtliche Hinweise

### Disclaimer
Diese Datenschutzerklärung entspricht dem aktuellen Stand der DSGVO. Bei Rechtsunsicherheiten wenden Sie sich an unseren Datenschutzbeauftragten.

### Salvatorische Klausel
Sollten einzelne Bestimmungen unwirksam sein, bleibt die Gültigkeit der übrigen Bestimmungen unberührt.

---

**Stand**: 28. August 2025  
**Version**: 1.0  
**Nächste Überprüfung**: 28. November 2025  
**Geltungsbereich**: EU, EWR, Deutschland