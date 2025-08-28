# Nutzungsrechte und Urheberrecht

## 📝 AI-Generated Content Rights & Usage

### 🎯 Übersicht der Rechte

Diese Richtlinie regelt die Nutzungsrechte an AI-generierten Inhalten und stellt die Einhaltung des deutschen und EU-Urheberrechts sicher.

---

## ⚖️ 1. Rechtlicher Rahmen

### 1.1 Anwendbare Gesetze

- **Deutschland**: Urheberrechtsgesetz (UrhG)
- **EU**: Richtlinie 2001/29/EG (InfoSoc-Richtlinie)
- **International**: Berner Übereinkunft, WIPO-Verträge

### 1.2 AI und Urheberrecht

```python
class AIContentRights:
    """Rechtsstatus von AI-generierten Inhalten"""
    
    def __init__(self):
        self.legal_status = {
            "ai_generated": "no_copyright_protection",  # Keine Schöpfungshöhe
            "human_assisted": "conditional_protection", # Abhängig von menschlichem Input
            "human_created": "full_copyright_protection" # Voller Urheberrechtsschutz
        }
    
    def determine_copyright_status(self, content_type, human_contribution):
        """Bestimmung des Urheberrechtsstatus"""
        if human_contribution > 0.7:  # Signifikanter menschlicher Beitrag
            return "human_authorship_likely"
        elif human_contribution > 0.3:  # Moderate menschliche Mitwirkung
            return "collaborative_work"
        else:  # Minimaler menschlicher Input
            return "ai_generated_no_protection"
```

---

## 🏗️ 2. Rechtekategorien

### 2.1 AI-Generierte Inhalte (Vollautomatisch)

**Rechtsstatus**: ❌ Kein Urheberrechtsschutz  
**Begründung**: Fehlende Schöpfungshöhe, kein menschlicher Urheber

```yaml
ai_generated_content:
  copyright_protection: false
  public_domain: true
  usage_rights: "unrestricted"
  attribution_required: false
  commercial_use: "permitted"
  modification: "permitted"
  redistribution: "permitted"
```

**Beispiele**:
- Automatisch generierte Texte ohne menschliche Bearbeitung
- KI-Bilder aus reinen Text-Prompts
- Synthetische Videos ohne kreative Nachbearbeitung

### 2.2 Human-Assisted AI Content

**Rechtsstatus**: ⚡ Bedingter Schutz  
**Begründung**: Menschliche Kreativität erkennbar

```python
class HumanAssistedContent:
    """Bewertung menschlicher Beiträge zu AI-Content"""
    
    protection_criteria = {
        "creative_input": 0.4,      # Kreative Eingaben/Prompts
        "post_processing": 0.3,     # Nachbearbeitung
        "curation": 0.2,           # Auswahl und Anordnung
        "conceptual_design": 0.1    # Konzeptuelle Gestaltung
    }
    
    def calculate_human_contribution(self, content_metadata):
        score = 0
        for criterion, weight in self.protection_criteria.items():
            if content_metadata.get(criterion, False):
                score += weight
        
        return {
            "human_contribution_score": score,
            "copyright_likely": score > 0.5,
            "protection_level": self.get_protection_level(score)
        }
    
    def get_protection_level(self, score):
        if score > 0.7:
            return "full_protection"
        elif score > 0.4:
            return "limited_protection"
        else:
            return "no_protection"
```

### 2.3 Traditional Creative Works

**Rechtsstatus**: ✅ Vollschutz  
**Begründung**: Menschliche Schöpfung

```yaml
traditional_content:
  copyright_protection: true
  duration: "70_years_after_author_death"
  moral_rights: "inalienable"
  economic_rights: "transferable"
  fair_use_exceptions: "research_education_criticism"
```

---

## 📜 3. Lizenzmodelle

### 3.1 Standard AI Content License

```yaml
# autark_ai_content_license_v1.0.yaml
license:
  name: "AUTARK AI Content License"
  version: "1.0"
  type: "permissive"
  
permissions:
  commercial_use: true
  modification: true
  distribution: true
  private_use: true
  patent_use: false
  
conditions:
  include_copyright: false  # Kein Copyright vorhanden
  include_license: true     # Diese Lizenz beilegen
  document_changes: true    # Änderungen dokumentieren
  
limitations:
  liability: false
  warranty: false
  trademark_use: false
```

### 3.2 Enhanced Rights für Human-Assisted Content

```python
class EnhancedContentLicense:
    """Erweiterte Lizenz für human-assisted AI content"""
    
    def __init__(self):
        self.license_terms = {
            "attribution": "required_if_copyright_exists",
            "share_alike": "optional",
            "non_commercial": "optional",
            "no_derivatives": "optional"
        }
    
    def generate_license(self, content_analysis):
        """Dynamische Lizenzgenerierung basierend auf Content-Analyse"""
        
        base_license = "CC0-1.0"  # Public Domain für AI-Content
        
        if content_analysis["human_contribution"] > 0.5:
            # Signifikanter menschlicher Beitrag = Copyright möglich
            base_license = "CC-BY-4.0"  # Attribution required
        
        if content_analysis["commercial_sensitivity"]:
            base_license += "-NC"  # Non-Commercial
        
        if content_analysis["derivative_concerns"]:
            base_license += "-ND"  # No Derivatives
            
        return {
            "license": base_license,
            "human_contribution_score": content_analysis["human_contribution"],
            "reasoning": self.explain_license_choice(base_license)
        }
```

---

## 🔍 4. Content-Analyse und Klassifikation

### 4.1 Automatische Rechteklassifikation

```python
class ContentRightsAnalyzer:
    """Automatische Analyse der Urheberrechtssituation"""
    
    def __init__(self):
        self.ml_model = load_copyright_classification_model()
        
    def analyze_content(self, content_data):
        """Comprehensive content rights analysis"""
        
        analysis = {
            "content_type": self.detect_content_type(content_data),
            "ai_contribution": self.measure_ai_contribution(content_data),
            "human_input": self.measure_human_input(content_data),
            "originality": self.assess_originality(content_data),
            "derivative_elements": self.detect_derivatives(content_data)
        }
        
        # ML-basierte Klassifikation
        rights_prediction = self.ml_model.predict(analysis)
        
        return {
            "analysis": analysis,
            "predicted_rights_status": rights_prediction,
            "confidence_score": rights_prediction.confidence,
            "recommended_license": self.recommend_license(analysis),
            "legal_considerations": self.get_legal_notes(analysis)
        }
    
    def measure_human_input(self, content_data):
        """Quantifizierung des menschlichen Beitrags"""
        
        factors = {
            "prompt_complexity": len(content_data.get("prompt", "")) > 100,
            "iterative_refinement": content_data.get("iterations", 0) > 3,
            "post_processing": bool(content_data.get("human_edits")),
            "creative_direction": bool(content_data.get("artistic_choices")),
            "technical_skill": bool(content_data.get("technical_parameters"))
        }
        
        return sum(factors.values()) / len(factors)
```

### 4.2 Dokumentation für Rechtssicherheit

```python
class RightsDocumentation:
    """Vollständige Dokumentation der Rechte-Entstehung"""
    
    def create_rights_certificate(self, content_id, analysis_result):
        """Rechtszertifikat für AI-generierten Content"""
        
        certificate = {
            "content_id": content_id,
            "creation_timestamp": datetime.now().isoformat(),
            "rights_analysis": {
                "methodology": "AUTARK Rights Analyzer v1.0",
                "ai_model_used": analysis_result["ai_model"],
                "human_contribution_score": analysis_result["human_score"],
                "copyright_status": analysis_result["copyright_status"],
                "legal_basis": analysis_result["legal_reasoning"]
            },
            "license_assignment": {
                "recommended_license": analysis_result["license"],
                "usage_permissions": analysis_result["permissions"],
                "restrictions": analysis_result["restrictions"]
            },
            "chain_of_custody": {
                "original_prompt": hash(analysis_result["prompt"]),
                "ai_model_version": analysis_result["model_version"],
                "generation_parameters": analysis_result["parameters"],
                "human_modifications": analysis_result["modifications"]
            },
            "legal_compliance": {
                "gdpr_compliant": True,
                "copyright_cleared": True,
                "attribution_complete": analysis_result["attribution_status"]
            }
        }
        
        # Digitale Signatur für Integrität
        certificate["digital_signature"] = self.sign_certificate(certificate)
        
        return certificate
```

---

## 🚫 5. Verbotene Nutzungen

### 5.1 Absolute Verbote

```python
class ProhibitedUses:
    """Definierte verbotene Nutzungen unabhängig vom Rechtsstatus"""
    
    absolute_prohibitions = [
        "hate_speech_generation",
        "disinformation_creation", 
        "deepfake_impersonation",
        "copyright_infringement_tool",
        "privacy_violation_content",
        "illegal_activity_assistance"
    ]
    
    conditional_prohibitions = {
        "commercial_use": "requires_enhanced_license",
        "derivative_works": "requires_permission_if_protected",
        "mass_distribution": "requires_compliance_check",
        "ai_training_data": "requires_explicit_consent"
    }
    
    def check_usage_compliance(self, intended_use, content_rights):
        """Prüfung der Nutzungskonformität"""
        
        violations = []
        
        # Absolute Verbote prüfen
        for prohibition in self.absolute_prohibitions:
            if self.matches_prohibition(intended_use, prohibition):
                violations.append(f"Absolute prohibition: {prohibition}")
        
        # Bedingte Verbote prüfen
        for use_case, requirement in self.conditional_prohibitions.items():
            if (self.matches_use_case(intended_use, use_case) and 
                not self.meets_requirement(content_rights, requirement)):
                violations.append(f"Conditional violation: {use_case} - {requirement}")
        
        return {
            "compliant": len(violations) == 0,
            "violations": violations,
            "required_actions": self.get_required_actions(violations)
        }
```

### 5.2 Besondere Schutzrechte

```yaml
special_protections:
  personality_rights:
    - "Real person depictions require consent"
    - "Voice synthesis of real persons prohibited"
    - "Likeness rights must be respected"
    
  trademark_protection:
    - "No trademark infringement in AI content"
    - "Brand name usage requires permission"
    - "Logo reproduction prohibited"
    
  trade_secrets:
    - "No proprietary information in training"
    - "Confidential data must be excluded"
    - "NDAs apply to AI-generated insights"
```

---

## 📊 6. Monitoring und Compliance

### 6.1 Automated Rights Monitoring

```python
class RightsComplianceMonitor:
    """Kontinuierliche Überwachung der Rechtekonformität"""
    
    def __init__(self):
        self.monitoring_active = True
        self.alert_thresholds = {
            "potential_copyright_violation": 0.8,
            "personality_rights_risk": 0.7,
            "trademark_similarity": 0.9
        }
    
    def scan_generated_content(self, content_batch):
        """Batch-Scanning für Rechteverletzungen"""
        
        results = []
        for content in content_batch:
            scan_result = {
                "content_id": content["id"],
                "copyright_risk": self.assess_copyright_risk(content),
                "personality_risk": self.assess_personality_risk(content),
                "trademark_risk": self.assess_trademark_risk(content),
                "overall_risk_score": 0
            }
            
            scan_result["overall_risk_score"] = np.mean([
                scan_result["copyright_risk"],
                scan_result["personality_risk"], 
                scan_result["trademark_risk"]
            ])
            
            if scan_result["overall_risk_score"] > 0.7:
                scan_result["action_required"] = "manual_review"
                self.flag_for_review(content["id"])
            
            results.append(scan_result)
        
        return results
    
    def generate_compliance_report(self, time_period):
        """Regelmäßige Compliance-Berichte"""
        
        return {
            "period": time_period,
            "total_content_generated": self.count_generated_content(time_period),
            "flagged_content": self.count_flagged_content(time_period),
            "resolved_issues": self.count_resolved_issues(time_period),
            "compliance_rate": self.calculate_compliance_rate(time_period),
            "top_risk_categories": self.get_top_risks(time_period),
            "recommendations": self.generate_recommendations()
        }
```

---

## 📞 7. Support und Rechtshilfe

### 7.1 Rights Support Team

**Kontakt**: GitHub Issues mit Label `rights` oder `legal`  
**Reaktionszeit**: 
- Dringende Rechtsfragen: 4 Stunden
- Standard-Anfragen: 24 Stunden
- Komplexe Analyse: 3 Werktage

### 7.2 Rechtsberatung

```python
class LegalSupportSystem:
    """Systematische Rechtsberatung für Nutzer"""
    
    def __init__(self):
        self.support_levels = {
            "automated": "AI-powered basic guidance",
            "expert": "Human legal expert consultation", 
            "external": "External law firm referral"
        }
    
    def provide_legal_guidance(self, query_type, complexity_level):
        """Stufenweise Rechtsberatung"""
        
        if complexity_level == "basic":
            return self.automated_legal_guidance(query_type)
        elif complexity_level == "intermediate":
            return self.schedule_expert_consultation(query_type)
        else:
            return self.refer_to_external_counsel(query_type)
    
    def automated_legal_guidance(self, query):
        """KI-gestützte Rechtsberatung für Standardfälle"""
        
        guidance_database = {
            "commercial_use": "AI-generated content is generally free for commercial use unless human contribution creates copyright.",
            "attribution": "Attribution not required for pure AI content, but recommended for transparency.",
            "modification": "Modifications permitted for AI content. Document changes for clarity.",
            "redistribution": "Free redistribution allowed for AI content under our license terms."
        }
        
        return guidance_database.get(query, "Please contact expert support for this query.")
```

---

## 🔄 8. Updates und Änderungen

### 8.1 Versioning der Rechterichtlinien

```yaml
rights_policy_version:
  current: "1.0"
  effective_date: "2025-08-28"
  next_review: "2025-11-28"
  change_log:
    - "2025-08-28: Initial comprehensive rights framework"
    - "Future: Regular updates based on legal developments"
```

### 8.2 Rechtsprechung und Anpassungen

Wir überwachen kontinuierlich:
- Neue Gerichtsurteile zu AI und Urheberrecht
- Gesetzesänderungen (EU AI Act, UrhG-Novellen)
- Internationale Entwicklungen (WIPO, TRIPS)
- Best Practices der Industrie

---

## ⚠️ Rechtliche Hinweise

### Disclaimer

Diese Rechterichtlinie stellt keine Rechtsberatung dar. Bei spezifischen Rechtsfragen konsultieren Sie einen qualifizierten Anwalt.

### Haftungsausschluss

AUTARK Video Studio übernimmt keine Haftung für Rechtsverletzungen durch Nutzer. Jeder Nutzer ist selbst für die rechtskonforme Verwendung der generierten Inhalte verantwortlich.

### Gerichtsstand

Für alle Streitigkeiten aus dieser Rechterichtlinie gilt deutsches Recht. Gerichtsstand ist [Ihr Gerichtsstand].

---

**Stand**: 28. August 2025  
**Version**: 1.0  
**Geltungsbereich**: Alle über AUTARK Video Studio generierten Inhalte