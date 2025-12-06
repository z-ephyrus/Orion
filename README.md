# 🔱 ORION — Optimal Real-Time Intelligent Prompt Generator
A hybrid rule-based + LLM powered system for **prompt optimization**, **safety enhancement**, and **adaptive refinement**.  
ORION intelligently analyzes user prompts, understands intent, injects missing details, enforces structure, eliminates ambiguity, and enhances clarity — all while learning from its own performance through a transparent feedback loop.

---

## ⚡ Features
### **🔍 Intelligent Task Recognition**
ORION classifies user prompts into task types:
- Coding  
- Academic writing  

### **🧠 Hybrid Optimization Engine**
Combines:
- **Rule-Based Expert System** (structure, constraints, templates)  
- **LLM Enhancer** (style, coherence, flow, chain-of-thought)  

### **📏 Multi-Dimensional Scoring Engine**
Evaluates prompts on:
- Clarity  
- Specificity  
- Completeness  
- Task Alignment  
- Safety  
- Structural Quality  

### **🔁 Adaptive Feedback Loop**
Learns over time by adjusting:
- Rule weights  
- Constraint enforcement strength  
- Detail-injection intensity  
- Safety rule strictness  
- Classification patterns  

This allows ORION to improve without retraining any machine learning model.

### **🛡 Advanced Safety Layer**
- Jailbreak pattern detection  
- Harmful intent neutralization  
- Safe reformulation of risky inputs  

---
## 🏗 System Architecture (High-Level)
ORION’s pipeline:
User Input
↓
Preprocessor ──→ Task Classifier
↓
Rule-Based Optimizer ──→ Template Builder ──→ Constraint Injector
↓
LLM Enhancer (polishing, CoT, clarity)
↓
Scoring Engine (original vs optimized)
↓
Evaluation Module
↓
Adaptive Feedback Loop (updates rule weights)
↓
Final Output


A full PDF architecture diagram is included in `/docs`.

---

## 📘 Modules Overview

### **1. Preprocessing Layer**
- Cleans text  
- Detects ambiguity  
- Extracts context  
- Normalizes user intent  

### **2. Task Classification**
Deterministic (rule-based) classification using keyword patterns and structural cues.

### **3. Rule-Based Optimizer**
Injects:
- Missing constraints  
- Role + goal + context structure  
- Examples  
- Formatting  
- Edge-case questions  

### **4. LLM Enhancer**
Refines wording using an external LLM (OpenAI / Anthropic / local models).

### **5. Scoring Engine**
Generates:
- Original Score  
- Optimized Score  
- Difference Matrix  
Used for continuous improvement.

### **6. Evaluation & Feedback Loop**
Updates:
- Rule weights  
- Detail injection intensity  
- Safety strictness  
- Classification patterns  
- Template selection logic  

---
