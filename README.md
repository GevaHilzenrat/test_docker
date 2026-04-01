# ML Jupyter Docker Image

A ready-to-use JupyterLab environment with a full ML/data science stack, available in CPU and CUDA flavours.

## Structure
```
test-docker/
│
├── .github/
│   └── workflows/
│       └── docker-build.yml      # CI: build & push to GHCR
│
├── docker/
│   ├── Dockerfile.cpu            # CPU image
│   └── Dockerfile.cuda           # CUDA image
│
├── notebooks/
│
├── src/
│   ├── minimal_cpu.py
│   └── minimal_torch.py
│
├── docker-compose.yml            # For running locally
├── README.md                     # Usage docs
└── .dockerignore                 # Keeps the build context clean

```

## Included libraries

| Category | Libraries |
|---|---|
| Data | NumPy, Pandas, SciPy |
| ML | Scikit-learn, PyTorch, TorchVision, TorchAudio |
| NLP | HuggingFace Transformers, Datasets, Accelerate |
| Viz | Matplotlib, Seaborn |
| Jupyter | JupyterLab, ipywidgets |
| Utilities | Pillow, tqdm, requests |

---

## Quickstart

### Pull from GitHub Container Registry

```bash
# CPU
docker pull ghcr.io/GevaHilzenrat/test_docker:cpu-latest

# CUDA
docker pull ghcr.io/GevaHilzenrat/test_docker:cuda-latest
```

### Run

```bash
# CPU — opens JupyterLab on http://<host-ip>:8888
docker run -p 8888:8888 -v $(pwd)/notebooks:/workspace ghcr.io/GevaHilzenrat/test_docker:cpu-latest

# CUDA (requires nvidia-container-toolkit)
docker run --gpus all -p 8888:8888 -v $(pwd)/notebooks:/workspace ghcr.io/GevaHilzenrat/test_docker:cuda-latest
```

> No token or password is required. Any user on your network can open `http://<host-ip>:8888` in a browser.

### With docker compose

```bash
# CPU
docker compose --profile cpu up

# GPU
docker compose --profile gpu up
```

---

## Build locally

```bash
# CPU
docker build -f docker/Dockerfile.cpu -t ml-jupyter:cpu .

# CUDA
docker build -f docker/Dockerfile.cuda -t ml-jupyter:cuda .
```

---

## Security note

JupyterLab is configured without authentication (`token` and `password` are both empty) to make network sharing easy. **Do not expose port 8888 to the public internet** — use this only on trusted local or private cloud networks.

---

## GitHub Actions

On every push to `main`, two images are built and pushed to the GitHub Container Registry automatically:

- `ghcr.io/GevaHilzenrat/test_docker:cpu-latest`
- `ghcr.io/GevaHilzenrat/test_docker:cuda-latest`

No secrets need to be configured — the workflow uses the built-in `GITHUB_TOKEN`.

To enable the package registry for your repo, go to **Settings → Actions → General → Workflow permissions** and set it to **Read and write permissions**.
