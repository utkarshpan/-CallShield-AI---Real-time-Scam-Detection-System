# detection_engine.py

import re
from typing import Dict, List, Tuple

class CallShieldEngine:
    def __init__(self):
        self.reset()
        
        # 📊 Keyword libraries (real detection)
        self.authority_keywords = {
            'bank': 10, 'rbi': 15, 'police': 20, 'cbi': 20,
            'income tax': 15, 'government': 10, 'official': 5,
            'sbi': 10, 'hdfc': 10, 'icici': 10, 'axis': 10
        }
        
        self.fear_keywords = {
            'block': 20, 'suspend': 20, 'close': 15, 'freeze': 25,
            'legal action': 30, 'arrest': 35, 'case filed': 30,
            'fine': 20, 'penalty': 20, 'recovery': 15,
            'will be': 5, 'immediately': 10, 'urgent': 10
        }
        
        self.action_keywords = {
            'otp': 50, 'password': 45, 'pin': 40, 'cvv': 45,
            'share': 30, 'send': 25, 'click': 20, 'install': 20,
            'transfer': 40, 'payment': 35, 'upi': 40,
            'batao': 30, 'do': 10, 'karo': 10
        }
        
        self.greeting_keywords = {
            'hello': -5, 'good morning': -5, 'how are you': -5,
            'myself': -3, 'calling from': 0
        }
        
        # 🎯 Pattern sequence weights
        self.pattern_weights = {
            ('AUTHORITY', 'FEAR'): 15,
            ('FEAR', 'ACTION'): 25,
            ('AUTHORITY', 'FEAR', 'ACTION'): 40,
            ('AUTHORITY', 'ACTION'): 20,
            ('FEAR', 'ACTION'): 25,
        }
    
    def reset(self):
        self.risk_score = 0
        self.pattern_sequence = []
        self.conversation_log = []
        self.detected_features = []
        
    def detect_intent(self, text: str) -> Dict:
        """Detect intentions from text"""
        text_lower = text.lower()
        scores = {'AUTHORITY': 0, 'FEAR': 0, 'ACTION': 0, 'GREETING': 0}
        
        # Authority detection
        for word, weight in self.authority_keywords.items():
            if word in text_lower:
                scores['AUTHORITY'] += weight
        
        # Fear detection
        for word, weight in self.fear_keywords.items():
            if word in text_lower:
                scores['FEAR'] += weight
        
        # Action detection
        for word, weight in self.action_keywords.items():
            if word in text_lower:
                scores['ACTION'] += weight
        
        # Greeting detection (reduces risk)
        for word, weight in self.greeting_keywords.items():
            if word in text_lower:
                scores['GREETING'] += weight
        
        # Normalize and threshold
        result = {}
        for intent, score in scores.items():
            if score > 5:  # Minimum threshold
                result[intent] = min(score, 100)  # Cap at 100
        
        return result
    
    def update_sequence(self, intents: Dict):
        """Update pattern sequence"""
        if intents:
            # Get highest scoring intent
            primary_intent = max(intents, key=intents.get)
            if primary_intent != 'GREETING':
                if not self.pattern_sequence or self.pattern_sequence[-1] != primary_intent:
                    self.pattern_sequence.append(primary_intent)
                    # Keep last 5 for pattern matching
                    if len(self.pattern_sequence) > 5:
                        self.pattern_sequence.pop(0)
    
    def calculate_risk(self, intents: Dict, text: str) -> int:
        """Calculate current risk score"""
        # Base score from intents
        intent_score = sum(intents.values())
        
        # Pattern bonus
        pattern_bonus = 0
        seq_tuple = tuple(self.pattern_sequence)
        
        # Check all pattern combinations
        for pattern, bonus in self.pattern_weights.items():
            if len(pattern) <= len(seq_tuple):
                # Check if pattern matches end of sequence
                if seq_tuple[-len(pattern):] == pattern:
                    pattern_bonus = max(pattern_bonus, bonus)
        
        # Specific high-risk triggers
        high_risk_triggers = 0
        if 'otp' in text.lower() and ('AUTHORITY' in intents or 'FEAR' in intents):
            high_risk_triggers = 30
        
        # Calculate final score (capped at 100)
        total = intent_score + pattern_bonus + high_risk_triggers
        self.risk_score = min(total, 100)
        
        return self.risk_score
    
    def get_alert_level(self) -> Tuple[str, str]:
        """Get alert level and message"""
        if self.risk_score >= 80:
            return ('CRITICAL', '🔴 IMMEDIATE SCAM DETECTED! DO NOT SHARE ANY INFORMATION!')
        elif self.risk_score >= 60:
            return ('HIGH', '🟠 HIGH RISK: Scam pattern detected. Be very careful.')
        elif self.risk_score >= 40:
            return ('MEDIUM', '🟡 MEDIUM RISK: Suspicious behavior detected.')
        elif self.risk_score >= 20:
            return ('LOW', '🟢 LOW RISK: Be cautious but no immediate threat.')
        else:
            return ('SAFE', '✅ SAFE: No scam patterns detected.')
    
    def get_pattern_explanation(self) -> str:
        """Generate human-readable pattern explanation"""
        if not self.pattern_sequence:
            return "No patterns detected yet"
        
        pattern_str = " → ".join(self.pattern_sequence)
        
        if self.risk_score >= 80:
            return f"🚨 SCAM PATTERN: {pattern_str}\nThis matches known fraud sequences."
        elif self.risk_score >= 60:
            return f"⚠️ SUSPICIOUS PATTERN: {pattern_str}\nTypical manipulation behavior."
        else:
            return f"📊 CURRENT PATTERN: {pattern_str}"
    
    def process_chunk(self, text: str) -> Dict:
        """Main processing function for each audio chunk"""
        # Detect intents
        intents = self.detect_intent(text)
        
        # Update sequence
        self.update_sequence(intents)
        
        # Calculate risk
        risk = self.calculate_risk(intents, text)
        
        # Get alert
        alert_level, alert_message = self.get_alert_level()
        
        # Log conversation
        self.conversation_log.append({
            'text': text,
            'intents': intents,
            'risk': risk,
            'timestamp': len(self.conversation_log)
        })
        
        return {
            'text': text,
            'intents': intents,
            'risk_score': risk,
            'alert_level': alert_level,
            'alert_message': alert_message,
            'pattern_sequence': self.pattern_sequence.copy(),
            'pattern_explanation': self.get_pattern_explanation()
        }

# Test the engine
if __name__ == "__main__":
    engine = CallShieldEngine()
    
    test_phrases = [
        "Hello sir, I'm calling from your bank",
        "Your account will be blocked today",
        "Please share the OTP immediately"
    ]
    
    for phrase in test_phrases:
        result = engine.process_chunk(phrase)
        print(f"\n📝 Text: {phrase}")
        print(f"🎯 Intents: {result['intents']}")
        print(f"📊 Risk: {result['risk_score']}%")
        print(f"🔄 Pattern: {result['pattern_sequence']}")