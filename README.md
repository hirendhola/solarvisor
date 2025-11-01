# SolarVisor

**AI-Powered Rooftop Solar Verification System**

A governance-ready digital pipeline for the PM Surya Ghar Muft Bijli Yojana scheme, using computer vision and machine learning to remotely verify rooftop solar installations across India.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Turborepo](https://img.shields.io/badge/Built%20with-Turborepo-purple.svg)](https://turbo.build/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

SolarVisor addresses the challenge of verifying rooftop solar installations at scale, ensuring subsidies reach genuine beneficiaries while maintaining public trust and operational efficiency.

### Problem Statement

Traditional field inspections face significant challenges:

- **Time-intensive**: Manual site visits take weeks to complete
- **High cost**: Maintaining field teams across states is expensive
- **Inconsistent quality**: Verification standards vary by region and inspector
- **Poor scalability**: Cannot keep pace with subsidy program demand

### Solution

An automated verification pipeline that processes geographic coordinates and returns comprehensive installation reports:
```
INPUT                    PROCESS                         OUTPUT
-------------------------------------------------------------------
Geographic coordinates → Image acquisition            → Detection status
(latitude, longitude)  → ML classification            → Panel count & area
                       → Quantification               → Capacity estimation
                       → Explainability generation    → Audit artifacts
```

---

## Features

### Automated Detection
- Binary classification (solar present/absent) with confidence scoring
- Support for diverse roof types (flat, sloped, mixed materials)
- Calibrated confidence thresholds for decision-making

### Quantification
- Automated panel counting using grid pattern detection
- Area estimation (m²) from segmentation masks
- Capacity calculation (kW) using transparent efficiency assumptions

### Explainability & Audit Trail
- Visual overlays with bounding boxes or polygon masks
- Human-readable reason codes (e.g., "module grid", "racking shadows")
- Quality control status flags: `VERIFIABLE` or `NOT_VERIFIABLE`

### Geographic Robustness
- Coordinate jitter handling with configurable buffer radius (±10-20m)
- Performance across India's diverse building architectures
- Graceful handling of occlusions, shadows, and poor image quality

### Governance Compliance
- Complete audit trail for every verification decision
- Transparent methodology documentation
- Documented bias detection and mitigation strategies

---

## Quick Start

### Prerequisites

- Python 3.9 or higher
- Node.js 18 or higher
- pnpm 8 or higher (alternatively: npm or yarn)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/solarvisor.git
cd solarvisor

# Install JavaScript dependencies
pnpm install

# Setup Python environment
cd packages/pipeline
./scripts/setup.sh
cd ../..

# Build all packages
pnpm build
```

### Running Your First Verification
```bash
# 1. Prepare input CSV file
cat > data/test_coords.csv << EOF
sample_id,latitude,longitude
1,23.0225,72.5714
2,19.0760,72.8777
3,21.1702,72.8311
EOF

# 2. Execute the pipeline
pnpm --filter @solarvisor/pipeline dev --input data/test_coords.csv

# 3. Review results
cat data/output/results.json
```

---

## Architecture

### System Flow
```
Input CSV → Image Fetcher → Preprocessor → ML Classifier → Quantifier → Explainer → Output (JSON + PNG)
```

### Repository Structure
```
solarvisor/
├── packages/
│   ├── pipeline/              # Core ML pipeline (Python)
│   │   ├── src/
│   │   │   ├── fetcher.py         # Satellite image acquisition
│   │   │   ├── classifier.py      # Solar panel detection
│   │   │   ├── quantifier.py      # Panel counting and sizing
│   │   │   └── explainer.py       # Audit artifact generation
│   │   ├── tests/                 # Unit and integration tests
│   │   └── scripts/               # Setup and utility scripts
│   └── config/                # Shared configuration constants
├── apps/
│   ├── web/                   # (Future) Web-based review dashboard
│   └── api/                   # (Future) REST API wrapper
├── data/                      # Data storage (gitignored)
│   ├── raw/                   # Downloaded satellite imagery
│   ├── processed/             # Preprocessed images
│   └── labels/                # Manual annotations
├── notebooks/                 # Jupyter notebooks for exploration
└── docs/                      # Comprehensive documentation
```

---

## Performance Targets

| Metric | Target Value |
|--------|-------------|
| Detection F1 Score | ≥ 0.90 |
| Area Estimation MAE | < 5 m² |
| Capacity Estimation RMSE | < 1 kW |
| Processing Time per Site | < 30 seconds |
| QC Flag Accuracy | > 95% |

---

## Development

### Workflow Philosophy

This project follows Andrej Karpathy's data-first approach:

1. **Explore in notebooks** - Understand data patterns interactively
2. **Build minimal pipeline** - Establish end-to-end functionality first
3. **Iterate based on learning** - Improve incrementally with evidence
4. **Scale when ready** - Add complexity only when justified

### Available Commands
```bash
# Development
pnpm dev                        # Run all packages in watch mode
pnpm --filter @solarvisor/pipeline dev    # Run Python pipeline only

# Building and Testing
pnpm build                      # Build all packages
pnpm test                       # Run all test suites
pnpm lint                       # Lint all code

# Maintenance
pnpm clean                      # Remove build artifacts
```

### Code Conventions

- **Commit messages**: Follow [Conventional Commits](https://www.conventionalcommits.org/) specification
- **Python style**: PEP 8 compliant, formatted with Black
- **Documentation**: Comprehensive docstrings for all public APIs
- **Testing**: Minimum 80% code coverage target

---

## Documentation

- [Getting Started Guide](docs/getting-started.md) - Detailed setup and first-run instructions
- [Model Training](docs/model-training.md) - Training pipeline and dataset requirements
- [API Reference](docs/api-reference.md) - Complete API documentation
- [Explainability Guide](docs/explainability.md) - Understanding model decisions
- [Deployment Guide](docs/deployment.md) - Production deployment instructions

---

## Contributing

Contributions are welcome. Please review our [Contributing Guide](CONTRIBUTING.md) for guidelines.

### High-Priority Areas

- Improving detection accuracy on edge cases (occlusions, unusual roof types)
- Adding support for additional satellite imagery providers
- Developing evaluation and monitoring dashboards
- Expanding documentation and examples
- Increasing test coverage

---

## Research & Methodology

### Model Architecture

- **Base models**: Fine-tuned CNNs (ResNet, EfficientNet) or Vision Transformers
- **Training data**: Combination of public datasets and India-specific annotations
- **Data augmentation**: Rotation, lighting variations, occlusion simulation

### Capacity Estimation Formula
```
Capacity (kW) = Panel Area (m²) × Panel Efficiency (Wp/m²) ÷ 1000

Default efficiency: 175 Wp/m² (configurable in packages/config/constants.json)
```

### Known Limitations

- **Urban bias**: Higher accuracy in urban areas due to training data distribution
- **Roof type sensitivity**: Flat roofs perform better than complex sloped roofs
- **Imagery recency**: Optimal performance requires imagery less than 1 year old
- **Resolution dependency**: Minimum 50cm/pixel resolution required for reliable detection

See [Bias Analysis Documentation](docs/bias-analysis.md) for comprehensive discussion.

---

## Acknowledgments

- **PM Surya Ghar Muft Bijli Yojana** - Source of the governance challenge
- **DeepSolar Project** - Methodological inspiration
- **Andrej Karpathy** - Data-first development philosophy

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

- **Project Maintainer**: [Your Name](mailto:your.email@example.com)
- **Issue Tracker**: [GitHub Issues](https://github.com/yourusername/solarvisor/issues)
- **Discussion Forum**: [GitHub Discussions](https://github.com/yourusername/solarvisor/discussions)

---

**Built for a sustainable future through transparent governance**