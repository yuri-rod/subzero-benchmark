# subzero-benchmark

Measure inference throughput, latency, memory usage, and translation quality across LLM models and quantizations for subtitle translation.

Originally created as an internal evaluation harness for [Subzero](https://github.com/yuri-rod/subzero), this tool runs fixed subtitle workloads through Ollama or OpenAI-compatible inference servers (`llama-server`, `mlx_lm.server`, vLLM), then writes machine-readable JSON and Markdown comparison tables.

## Quickstart

Requires Python 3.10 or newer.

```console
git clone https://github.com/yuri-rod/subzero-benchmark.git
cd subzero-benchmark
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run a benchmark from a JSON configuration file:

```console
subzero-benchmark --config config.json --output report.json
```

The tool writes detailed telemetry to `report.json` and a formatted summary table to `report.md`.

## Workload and metrics

The default workload translates a fixed set of dialogue cues into Brazilian Portuguese. For each model variant, the harness measures:

- p50 and p95 end-to-end workload latency in seconds
- Cues per second and completion tokens per second reported by the inference engine
- Deterministic guardrail pass rate, catching untranslated text, formatting defects, and SDH noise
- Optional LLM-as-judge semantic adequacy scores on a 1 to 5 scale
- Host memory and swap usage sampled during translation

## Example configuration

```json
{
  "repeats": 3,
  "warmup": 1,
  "batch_size": 4,
  "sample_interval": 0.25,
  "variants": [
    {
      "provider": "openai",
      "model": "qwen3.5-9b",
      "url": "http://127.0.0.1:8080/v1",
      "label": "Qwen3.5 9B Q8_0",
      "precision": "Q8_0"
    }
  ]
}
```

Optional LLM-as-judge evaluation can be enabled by configuring a judge endpoint:

```json
{
  "judge": {
    "provider": "ollama",
    "model": "qwen3.5:9b",
    "url": "http://127.0.0.1:11434"
  }
}
```

See [docs/benchmarks/README.md](docs/benchmarks/README.md) for published reference runs comparing BF16 against Q8_0 on Apple Silicon.

## Development

Run tests with pytest:

```console
pip install -e ".[dev]"
pytest
```

## License

[MIT](LICENSE). Copyright 2026 Yuri Barreira.
