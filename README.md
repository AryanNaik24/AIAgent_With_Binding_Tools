# AI Web Agent with Firecrawl + LangGraph + LLaMA 3

This is a command-line AI assistant that uses **Firecrawl tools** via **LangGraph** to scrape, crawl, extract, and analyze web content. It runs LLaMA 3 (via Ollama or Groq) as the reasoning engine, and supports autonomous tool use to handle web tasks.

---

## Features

-  Autonomous tool usage via LangGraph's ReAct agent
-  Firecrawl-based scraping, crawling, and structured extraction
-  Uses `llama3.1:8b` via Ollama (or swap with Groq/OpenAI)
-  MCP-compatible tool loading (via `langchain_mcp_adapters`)
-  Interactive CLI agent that takes your input and responds with real-time results

---

## Requirements

- Python 3.10+
- Node.js (for `npx`)
- [Firecrawl MCP CLI](https://firecrawl.dev)
- [Ollama](https://ollama.com) or a Groq API key (optional swap)

---

## Installation

1. **Clone this repo** (or copy the script into your project)

2. **Install dependencies:**

```bash
pip install -r requirements.txt
