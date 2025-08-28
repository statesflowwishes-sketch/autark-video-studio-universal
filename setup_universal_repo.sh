#!/bin/bash

# 🚀 AUTARK Video Studio - Universal Repository Experience Setup
# Automated deployment script for the 7-layer documentation architecture

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Configuration
GITHUB_TOKEN="${GITHUB_TOKEN:-YOUR_GITHUB_TOKEN_HERE}"
REPO_URL="https://github.com/statesflowwishes-sketch"
CURRENT_DIR="$(pwd)"

echo -e "${PURPLE}🌟 AUTARK Video Studio - Universal Repository Experience Setup${NC}"
echo -e "${BLUE}================================================================${NC}"
echo ""

# Function to print status
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Step 1: Verify documentation structure
echo -e "${PURPLE}Step 1: Verifying 7-Layer Documentation Structure${NC}"
echo "=============================================="

check_file_exists() {
    local file="$1"
    local description="$2"
    
    if [ -f "$file" ]; then
        print_status "$description exists: $file"
        return 0
    else
        print_error "$description missing: $file"
        return 1
    fi
}

check_dir_exists() {
    local dir="$1"
    local description="$2"
    
    if [ -d "$dir" ]; then
        print_status "$description exists: $dir"
        return 0
    else
        print_error "$description missing: $dir"
        return 1
    fi
}

# Check 7-layer structure
layers_complete=true

# Layer 1: Gate
check_file_exists "README_NEW.md" "Gate Layer (Universal README)" || layers_complete=false

# Layer 2: Index  
check_file_exists "docs/navigation-hub.md" "Index Layer (Navigation Hub)" || layers_complete=false

# Layer 3: Atlas
check_dir_exists "docs/atlas" "Atlas Layer Directory" || layers_complete=false
check_file_exists "docs/atlas/architektur.md" "Atlas: Architecture" || layers_complete=false
check_file_exists "docs/atlas/konzepte.md" "Atlas: Concepts" || layers_complete=false
check_file_exists "docs/atlas/sicherheit.md" "Atlas: Security" || layers_complete=false
check_file_exists "docs/atlas/glossar.md" "Atlas: Glossary" || layers_complete=false

# Layer 4: Werkzeughof
check_file_exists "docs/tools/README.md" "Werkzeughof Layer (Tools)" || layers_complete=false

# Layer 5: Datenraum
check_file_exists "docs/data/README.md" "Datenraum Layer (Data)" || layers_complete=false

# Layer 6: Showfloor
check_file_exists "docs/demos/README.md" "Showfloor Layer (Demos)" || layers_complete=false

# Layer 7: Governance
check_file_exists "docs/governance/README.md" "Governance Layer" || layers_complete=false

if [ "$layers_complete" = true ]; then
    print_status "All 7 layers complete! 🎉"
else
    print_error "Some layers are missing. Please run the documentation creation script first."
    exit 1
fi

echo ""

# Step 2: Git repository preparation
echo -e "${PURPLE}Step 2: Git Repository Preparation${NC}"
echo "==================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    print_info "Initializing Git repository..."
    git init
    print_status "Git repository initialized"
else
    print_status "Git repository found"
fi

# Check if we have a remote
if ! git remote | grep -q origin; then
    print_warning "No origin remote found. You may need to set this manually:"
    echo "  git remote add origin $REPO_URL/<your-repo-name>.git"
else
    print_status "Git remote 'origin' configured"
fi

echo ""

# Step 3: Backup and replace README
echo -e "${PURPLE}Step 3: README Migration${NC}"
echo "========================"

if [ -f "README.md" ] && [ ! -f "README_OLD.md" ]; then
    print_info "Backing up existing README.md..."
    cp README.md README_OLD.md
    print_status "Existing README backed up as README_OLD.md"
fi

if [ -f "README_NEW.md" ]; then
    print_info "Activating new universal README..."
    cp README_NEW.md README.md
    print_status "Universal README activated! 🌟"
else
    print_error "README_NEW.md not found. Cannot activate new README."
    exit 1
fi

echo ""

# Step 4: Create GitHub-specific files
echo -e "${PURPLE}Step 4: Creating GitHub Configuration${NC}"
echo "===================================="

# Create .github directory structure
mkdir -p .github/{ISSUE_TEMPLATE,workflows}

# Create issue templates
print_info "Creating issue templates..."

cat > .github/ISSUE_TEMPLATE/feature_request.md << 'EOF'
---
name: 🚀 Feature Request
about: Suggest a new feature for AUTARK Video Studio
title: '[FEATURE] '
labels: ['type/feature']
assignees: ''
---

## 🎯 Feature Description
<!-- Klare Beschreibung der gewünschten Funktionalität -->

## 💡 Use Case
<!-- Warum wird diese Funktion benötigt? -->

## 🎨 Proposed Solution
<!-- Wie sollte die Funktion implementiert werden? -->

## 🏗️ Implementation Ideas
<!-- Technische Ideen zur Umsetzung -->

## 📊 Success Criteria
<!-- Wann ist das Feature erfolgreich? -->

## 📈 Additional Context
<!-- Screenshots, Links, weitere Informationen -->
EOF

cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: 🐛 Bug Report
about: Report a bug in AUTARK Video Studio
title: '[BUG] '
labels: ['type/bug']
assignees: ''
---

## 🐛 Bug Description
<!-- Klare Beschreibung des Problems -->

## 🔄 Steps to Reproduce
1. 
2. 
3. 

## ✅ Expected Behavior
<!-- Was sollte passieren? -->

## ❌ Actual Behavior  
<!-- Was passiert stattdessen? -->

## 🖥️ Environment
- OS: 
- Python Version:
- GPU: 
- AUTARK Version:

## 📊 Additional Context
<!-- Logs, Screenshots, weitere Informationen -->
EOF

print_status "Issue templates created"

# Create GitHub Actions workflow
print_info "Creating GitHub Actions workflow..."

cat > .github/workflows/universal-repo-check.yml << 'EOF'
name: 🌟 Universal Repository Experience Check

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  documentation-structure:
    name: 📚 7-Layer Documentation Check
    runs-on: ubuntu-latest
    
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4
      
      - name: 🏗️ Verify 7-layer structure
        run: |
          echo "🔍 Checking 7-layer documentation structure..."
          
          # Layer 1: Gate
          test -f README.md || (echo "❌ Gate layer missing (README.md)" && exit 1)
          echo "✅ Gate layer found"
          
          # Layer 2: Index
          test -f docs/navigation-hub.md || (echo "❌ Index layer missing" && exit 1)
          echo "✅ Index layer found"
          
          # Layer 3: Atlas
          test -d docs/atlas || (echo "❌ Atlas layer missing" && exit 1)
          test -f docs/atlas/architektur.md || (echo "❌ Atlas architecture missing" && exit 1)
          test -f docs/atlas/konzepte.md || (echo "❌ Atlas concepts missing" && exit 1) 
          test -f docs/atlas/sicherheit.md || (echo "❌ Atlas security missing" && exit 1)
          test -f docs/atlas/glossar.md || (echo "❌ Atlas glossary missing" && exit 1)
          echo "✅ Atlas layer complete"
          
          # Layer 4: Werkzeughof
          test -f docs/tools/README.md || (echo "❌ Werkzeughof layer missing" && exit 1)
          echo "✅ Werkzeughof layer found"
          
          # Layer 5: Datenraum  
          test -f docs/data/README.md || (echo "❌ Datenraum layer missing" && exit 1)
          echo "✅ Datenraum layer found"
          
          # Layer 6: Showfloor
          test -f docs/demos/README.md || (echo "❌ Showfloor layer missing" && exit 1)
          echo "✅ Showfloor layer found"
          
          # Layer 7: Governance
          test -f docs/governance/README.md || (echo "❌ Governance layer missing" && exit 1)
          echo "✅ Governance layer found"
          
          echo "🎉 All 7 layers verified successfully!"

  universal-experience:
    name: 🎯 Universal Experience Validation
    runs-on: ubuntu-latest
    
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4
        
      - name: 🕒 Check 30-second understand principle
        run: |
          # Check if README has quick overview section
          if grep -q "30 Sekunden" README.md; then
            echo "✅ 30-second principle implemented"
          else
            echo "⚠️ 30-second principle not clearly implemented"
          fi
          
      - name: 🔍 Check 5-minute find principle  
        run: |
          # Check navigation completeness
          if grep -q "navigation-hub" README.md; then
            echo "✅ 5-minute find principle implemented"
          else
            echo "⚠️ Navigation system not linked"
          fi
          
      - name: 👥 Check 60-minute contribute principle
        run: |
          # Check governance documentation
          if test -f docs/governance/README.md; then
            echo "✅ 60-minute contribute principle implemented"
          else
            echo "❌ Contribution guidelines missing"
            exit 1
          fi

  accessibility-check:
    name: ♿ Accessibility Validation
    runs-on: ubuntu-latest
    
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4
        
      - name: 🔍 Check accessibility features
        run: |
          echo "♿ Checking accessibility features..."
          
          # Check for alt texts in images
          if grep -r "alt=" docs/ README.md; then
            echo "✅ Alt texts found"
          else
            echo "⚠️ No alt texts found - consider adding for images"
          fi
          
          # Check for ARIA labels
          if grep -r "aria-" docs/ README.md; then
            echo "✅ ARIA labels found"
          else
            echo "ℹ️ No ARIA labels found (optional but recommended)"
          fi
          
          # Check for keyboard navigation hints
          if grep -r "keyboard" docs/ README.md; then
            echo "✅ Keyboard navigation mentioned"
          else
            echo "ℹ️ Keyboard navigation not explicitly mentioned"
          fi
          
          echo "✅ Accessibility check completed"

  quality-metrics:
    name: 📊 Quality Metrics
    runs-on: ubuntu-latest
    
    steps:
      - name: 📥 Checkout code
        uses: actions/checkout@v4
        
      - name: 📈 Calculate documentation coverage
        run: |
          echo "📊 Calculating documentation metrics..."
          
          # Count documentation files
          DOC_FILES=$(find docs/ -name "*.md" | wc -l)
          echo "📄 Documentation files: $DOC_FILES"
          
          # Count total lines in documentation
          DOC_LINES=$(find docs/ -name "*.md" -exec wc -l {} + | tail -1 | awk '{print $1}')
          echo "📝 Documentation lines: $DOC_LINES"
          
          # Check README size (should be substantial but not overwhelming)
          README_LINES=$(wc -l < README.md)
          echo "📋 README lines: $README_LINES"
          
          if [ $README_LINES -gt 50 ] && [ $README_LINES -lt 300 ]; then
            echo "✅ README size optimal ($README_LINES lines)"
          else
            echo "⚠️ README might be too short (<50) or too long (>300) lines"
          fi
          
          echo "✅ Quality metrics calculated"
EOF

print_status "GitHub Actions workflow created"

echo ""

# Step 5: Git staging and commit preparation
echo -e "${PURPLE}Step 5: Preparing Git Commit${NC}"
echo "============================="

print_info "Staging new documentation structure..."

# Stage all new documentation files
git add README.md
git add docs/
git add .github/
git add IMPLEMENTATION.md

# Stage backup files if they exist
[ -f "README_OLD.md" ] && git add README_OLD.md

print_status "Files staged for commit"

# Check if there are changes to commit
if git diff --cached --quiet; then
    print_warning "No changes to commit. All files may already be committed."
else
    print_info "Ready to commit universal repository experience..."
fi

echo ""

# Step 6: Create commit
echo -e "${PURPLE}Step 6: Creating Commit${NC}"
echo "======================"

read -p "$(echo -e "${YELLOW}Create commit for Universal Repository Experience? (y/N): ${NC}")" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git commit -m "feat: implement Universal Repository Experience 🌟

🏗️ Architecture:
- Add 7-layer documentation structure (Gate/Index/Atlas/Werkzeughof/Datenraum/Showfloor/Governance)
- Implement 30-5-60 navigation principle
- Create comprehensive navigation system

📚 Documentation:
- Universal README with instant overview
- Interactive navigation hub
- Deep-dive architecture documentation
- Live tool demonstrations
- Data-driven transparency
- Community governance framework

🎯 Features:
- Multi-device responsive design
- Accessibility-first approach
- German-first with English expansion
- Interactive demos and live metrics
- Contributor-friendly onboarding

♿ Accessibility:
- Screen reader compatibility
- Keyboard navigation support
- Clear visual hierarchy
- Alternative text for images

🤖 Automation:
- GitHub Actions quality gates
- Issue templates for structured feedback
- Automated documentation checks

BREAKING CHANGE: Complete repository structure redesign for universal accessibility

Implements: 'Vom Kies zum Mosaik' - transforming scattered tools into cohesive experience"

    print_status "Commit created successfully! 🎉"
else
    print_info "Commit skipped. You can commit manually later with:"
    echo "  git commit -m 'feat: implement Universal Repository Experience 🌟'"
fi

echo ""

# Step 7: GitHub integration info
echo -e "${PURPLE}Step 7: GitHub Integration Ready${NC}"
echo "==============================="

print_info "GitHub Token configured: ${GITHUB_TOKEN:0:20}..."
print_info "Ready for GitHub operations"

echo ""
echo -e "${GREEN}🎊 Universal Repository Experience Setup Complete!${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. 🚀 Push to GitHub: ${YELLOW}git push origin main${NC}"
echo "2. 🏷️  Create GitHub labels (see IMPLEMENTATION.md)"  
echo "3. 💬 Enable GitHub Discussions"
echo "4. 📊 Set up GitHub Pages (optional)"
echo "5. 🎉 Announce to community"
echo ""
echo -e "${PURPLE}Documentation Structure:${NC}"
echo "📂 docs/"
echo "├── 🗺️  navigation-hub.md      # Central navigation"
echo "├── 📚 atlas/                  # Deep documentation"  
echo "│   ├── architektur.md"
echo "│   ├── konzepte.md"
echo "│   ├── sicherheit.md"
echo "│   └── glossar.md"
echo "├── 🛠️  tools/                 # Tool documentation"
echo "├── 📊 data/                   # Metrics & KPIs"
echo "├── 🎭 demos/                  # Live demonstrations"
echo "└── 🏛️  governance/            # Community management"
echo ""
echo -e "${GREEN}✨ From scattered stones to a beautiful mosaic - your repository is now a universal experience!${NC}"

# Optional: Show file sizes for verification
echo ""
echo -e "${BLUE}📊 File Statistics:${NC}"
echo "==================="
printf "%-40s %10s\n" "File" "Size"
echo "---------------------------------------- ----------"
[ -f "README.md" ] && printf "%-40s %10s\n" "README.md" "$(du -h README.md | cut -f1)"
[ -f "docs/navigation-hub.md" ] && printf "%-40s %10s\n" "docs/navigation-hub.md" "$(du -h docs/navigation-hub.md | cut -f1)"
[ -f "IMPLEMENTATION.md" ] && printf "%-40s %10s\n" "IMPLEMENTATION.md" "$(du -h IMPLEMENTATION.md | cut -f1)"
echo "Total docs/: $(du -sh docs/ | cut -f1)"

echo ""
print_status "Setup script completed successfully! 🌟"