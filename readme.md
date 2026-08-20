# Physics

A personal computational physics environment for studying physics through **mathematics, computation, simulation, and visualization**.

The repository brings together tools and projects that support learning, experimentation, and future research in physics.

## Repository Structure

```text
physics/
│
├── quantum-espresso/
│   └── First-principles and computational materials physics
│
├── manim/
│   └── Mathematical and physics visualization
│
├── .devcontainer/
│   └── GitHub Codespaces configuration
│
├── .gitignore
└── README.md
```

## Projects

### Quantum ESPRESSO

`quantum-espresso/` contains work related to **first-principles computational physics**, particularly electronic-structure calculations using Quantum ESPRESSO.

Areas of interest include:

* Density Functional Theory (DFT)
* Electronic structure
* Structural relaxation
* Phonons and lattice dynamics
* Molecular dynamics
* Computational materials physics
* Numerical analysis of simulation results

The computational workflow is intended to develop from:

```text
Physical system
      ↓
Mathematical model
      ↓
Computational model
      ↓
Quantum ESPRESSO calculation
      ↓
Numerical results
      ↓
Python analysis
      ↓
Physical interpretation
```

Official resources:

* [Quantum ESPRESSO](https://www.quantum-espresso.org/)
* [User's Guide](https://www.quantum-espresso.org/Doc/user_guide/)
* [Documentation](https://www.quantum-espresso.org/documentation/)

---

### Manim

`manim/` contains mathematical and physics visualizations created with the **Manim Community Edition**.

The purpose is not simply to create animations, but to use visualization as a tool for understanding mathematical structures and physical models.

Topics will include:

* Coordinate systems and vectors
* Linear algebra
* Matrix transformations
* Eigenvalues and eigenvectors
* Calculus
* Differential equations
* Classical mechanics
* Electromagnetism
* Waves
* Quantum mechanics
* Numerical methods
* Computational physics

The intended progression is:

```text
Mathematical concept
        ↓
Mathematical model
        ↓
Python implementation
        ↓
Manim visualization
        ↓
Physical interpretation
```

Official resource:

* [Manim Community](https://www.manim.community/)

## Development Environment

The repository is developed primarily through **GitHub Codespaces**.

The environment is intended to support both computational and visualization work, including:

* Python
* NumPy
* SciPy
* Matplotlib
* Manim
* Fortran/C/C++ compilers
* MPI
* BLAS/LAPACK
* FFT libraries
* Quantum ESPRESSO
* Git and related development tools

Python dependencies are isolated in a virtual environment.

```bash
source venv/bin/activate
```

The virtual environment is not tracked by Git.

## Reproducibility

A major goal of this repository is to develop reproducible computational workflows.

Where practical:

* Keep source code under version control
* Record software versions
* Preserve computational inputs
* Document important parameters
* Separate generated output from source code
* Automate repetitive calculations
* Keep analysis scripts with the work they analyze

Generated files such as Manim's rendered media and local Python environments are excluded from version control.

## Learning → Computation → Research

The broader purpose of this repository is to connect different levels of physics practice:

```text
             MATHEMATICS
                  │
                  ▼
              PHYSICS
                  │
                  ▼
         COMPUTATIONAL MODELS
                  │
          ┌───────┴───────┐
          ▼               ▼
       MANIM        NUMERICAL METHODS
          │               │
          │               ▼
          │       SCIENTIFIC COMPUTING
          │               │
          └───────┬───────┘
                  ▼
              RESEARCH
```

Manim provides a way to make mathematical and physical ideas visually explicit.

Quantum ESPRESSO provides a pathway toward realistic computational physics problems.

Python connects the two through numerical analysis, automation, and data processing.

## Current Focus

The current work is focused on:

1. Establishing a reproducible GitHub Codespaces environment
2. Installing and configuring Quantum ESPRESSO
3. Learning Manim systematically
4. Developing mathematical visualizations for physics
5. Building Python-based scientific computing workflows
6. Connecting simulations with analysis and visualization
7. Preparing the foundation for future research projects

## Status

**Active development**

This repository is a long-term learning and research environment. Its structure and projects will evolve as new computational and physics problems are explored.

