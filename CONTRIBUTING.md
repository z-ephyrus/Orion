# Contributing to ORION
Thank you for considering contributing to ORION — the Optimal Real-Time Intelligent Prompt Generator.  
This project follows a structured workflow to maintain code quality, stability, and collaboration among team members.

---

## 📌 Branching Model

We use a **feature-branch workflow**.

### Main Branches:
- **main** → production-ready, stable code  
- **dev** → integrated development branch  

### Feature Branches:
Create a new branch for every feature or fix:
git checkout -b feature/<module-name>


---

## 🛠 Workflow Summary
1. Pick an issue from the Kanban board  
2. Create a feature branch  
3. Write your code  
4. Commit frequently with clear messages  
5. Push the branch  
6. Open a Pull Request (PR) into `dev`  
7. Request review from teammates  
8. After approval → merge into dev  
9. Maintainers merge dev → main when stable  

---

## 🧪 Code Style Guidelines
- Use clear, descriptive variable and function names  
- Add docstrings and comments for non-obvious logic  
- Keep modules modular — one responsibility per file  
- Avoid hardcoding values; use config/constants  
- Run tests before pushing  
- Follow existing directory structure  

