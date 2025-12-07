# Agentic Researcher

A CrewAI-powered multi-agent system that automatically generates comprehensive 1-page scientific documents on any concrete scientific topic. This intelligent research assistant combines the expertise of specialized AI agents to produce high-quality, evidence-based scientific summaries.

## 🚀 Features

- **Automated Research Pipeline**: Three specialized AI agents work together to research, write, and edit scientific documents
- **Academic Literature Search**: Custom tool for searching arXiv and peer-reviewed papers
- **Web Research Integration**: Combines academic sources with web search for comprehensive coverage
- **Professional Editing**: Quality assurance ensures accuracy, clarity, and optimal length
- **Interactive CLI**: Simple command-line interface for easy topic input
- **Structured Output**: Well-formatted markdown documents ready for sharing or presentation

## 📋 How It Works

The system employs three specialized AI agents in a sequential workflow:

1. **Scientific Researcher** 🔬: Conducts comprehensive research using academic databases and web sources
2. **Scientific Writer** ✍️: Transforms research findings into clear, engaging 1-page documents
3. **Editor** ✅: Reviews and polishes the document for publication-ready quality

## 🛠️ Installation

### Prerequisites
- Python 3.10 - 3.13
- UV package manager (recommended)

### Setup Steps

1. **Install UV** (if not already installed):
   ```bash
   pip install uv
   ```

2. **Clone and navigate to the project**:
   ```bash
   cd agentic_researcher
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

   **Required API Keys:**
   - `OPENAI_API_KEY`: For AI agent functionality ([get from OpenAI](https://platform.openai.com/api-keys))
   - `SERPER_API_KEY`: For web search functionality ([get free key at Serper.dev](https://serper.dev/))

## 🎯 Usage

### Interactive Mode (Recommended)
```bash
uv run crewai run
```

You'll be prompted to enter a scientific topic:
```
Enter a scientific topic (e.g., 'CRISPR gene editing', 'quantum entanglement', 'neuroplasticity'):
```

### Command Line Mode
```bash
uv run crewai run "Support Vector Machines"
```

### Examples
```bash
# Machine Learning
uv run crewai run "Neural Networks and Deep Learning"

# Physics
uv run crewai run "Quantum Computing Fundamentals"

# Biology
uv run crewai run "CRISPR Gene Editing Technology"

# Environmental Science
uv run crewai run "Climate Change Mitigation Strategies"
```

## 📄 Output

The system generates a comprehensive 1-page scientific document saved as `report.md` with:

- **Title**: Clear, descriptive heading
- **Introduction**: Context and significance (2-3 sentences)
- **Main Content**: Key concepts, recent findings, mechanisms, and applications (3-4 paragraphs)
- **Conclusion**: Summary and future outlook (2-3 sentences)
- **References**: Properly formatted citations with inline references [1], [2], etc.

Document length: 500-650 words, optimized for readability and scientific rigor.

## 🏗️ Project Structure

```
agentic_researcher/
├── src/agentic_researcher/
│   ├── __init__.py
│   ├── main.py              # Entry point and CLI interface
│   ├── crew.py              # CrewAI agent and task definitions
│   ├── config/
│   │   ├── agents.yaml      # Agent configurations (roles, goals, backstories)
│   │   └── tasks.yaml       # Task definitions and workflows
│   └── tools/
│       ├── __init__.py
│       └── scientific_tools.py  # Custom arXiv search tool
├── .env.example             # Environment variables template
├── pyproject.toml           # Project dependencies and scripts
├── README.md               # This file
└── uv.lock                # Dependency lock file
```

## 🤖 Agent Details

### 1. Scientific Researcher
- **Expertise**: PhD-level research specialist
- **Tools**:
  - 🔬 **Scientific Literature Search**: Custom arXiv API integration
  - 🌐 **Web Search**: SerperDevTool for general web research
  - 📄 **Web Scraping**: Content extraction from websites
- **Output**: Comprehensive research summary with findings, sources, and evidence

### 2. Scientific Writer
- **Expertise**: Accomplished science communicator
- **Capabilities**: Transforms complex research into accessible, engaging documents
- **Output**: Well-structured 1-page document with proper scientific formatting

### 3. Editor
- **Expertise**: Scientific editor and quality assurance specialist
- **Capabilities**: Ensures accuracy, clarity, structure, and optimal length
- **Output**: Publication-ready final document

## 🛠️ Custom Tools

### Scientific Literature Search Tool
- **Purpose**: Searches arXiv for peer-reviewed scientific papers
- **Coverage**: Physics, mathematics, computer science, biology, and related fields
- **Features**:
  - Returns titles, authors, abstracts, and publication links
  - Focuses on credible academic sources
  - No API key required (uses free arXiv API)
- **Location**: `src/agentic_researcher/tools/scientific_tools.py`

## ⚙️ Customization

Modify the following files to customize behavior:

- **`src/agentic_researcher/config/agents.yaml`**: Adjust agent roles, goals, and personalities
- **`src/agentic_researcher/config/tasks.yaml`**: Modify task descriptions and expected outputs
- **`src/agentic_researcher/crew.py`**: Add custom tools or modify agent logic
- **`src/agentic_researcher/main.py`**: Change input handling or output formatting

## 🔧 Development

### Running Tests
```bash
uv run python -m pytest
```

### Training Mode
```bash
uv run python -m agentic_researcher.main train
```

### Replay Mode
```bash
uv run python -m agentic_researcher.main replay
```

## 📚 Dependencies

- **crewai[tools]**: Multi-agent framework
- **litellm**: LLM provider abstraction
- **ollama**: Local LLM support
- **requests**: HTTP client for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **Documentation**: [CrewAI Docs](https://docs.crewai.com)
- **GitHub Issues**: [Report bugs or request features](https://github.com/surajkarki66/agentic_researcher/issues)
- **Discord**: [Join the CrewAI community](https://discord.com/invite/X4JWnZnxPb)

---

**Built with ❤️ using [CrewAI](https://crewai.com)**
   - `SERPER_API_KEY` - Required for web search functionality (get free key at [Serper.dev](https://serper.dev/))

Without these API keys, the research assistant will not function properly.

## Running the Project

### Interactive Mode

To run the assistant interactively (recommended):

```bash
crewai run
```

You'll be prompted to enter a scientific topic, for example:
- "CRISPR gene editing technology"
- "quantum entanglement and its applications"
- "neuroplasticity in adult brains"
- "carbon capture and storage methods"

### Command Line Mode

To provide a topic directly via command line:

```bash
crewai run "your scientific topic here"
```

For example:
```bash
crewai run "photosynthesis mechanisms in C4 plants"
```

### Output

The assistant will generate a 1-page scientific document saved as `report.md` in your project root. The document includes:
- A clear title
- Introduction (context and significance)
- Main content (key concepts, findings, applications)
- Conclusion (summary and future outlook)

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Scientific Research Assistant is composed of three specialized AI agents:

### 1. Scientific Researcher
- **Role**: PhD-level research specialist
- **Capabilities**: Gathers comprehensive scientific information from credible sources
- **Tools**:
  - 🔬 **Scientific Literature Search** (Custom): Searches arXiv for peer-reviewed papers
  - 🌐 **Web Search**: General web search via SerperDevTool
  - 📄 **Web Scraping**: Content extraction via ScrapeWebsiteTool
- **Output**: Comprehensive research summary with background, findings, applications, and challenges

### 2. Scientific Writer
- **Role**: Accomplished science writer
- **Capabilities**: Transforms research into clear, engaging 1-page documents
- **Output**: Well-structured 500-600 word document with proper formatting

### 3. Editor
- **Role**: Scientific editor and quality assurance specialist
- **Capabilities**: Reviews for accuracy, clarity, structure, and length
- **Output**: Publication-ready final document

These agents collaborate sequentially as defined in `config/tasks.yaml`, with each agent building upon the work of the previous one to create a polished scientific summary.

## Custom Tools

This project includes a specialized custom tool built for scientific research:

### Scientific Literature Search Tool 🔬
- **Purpose**: Searches arXiv for peer-reviewed scientific papers
- **Used by**: Scientific Researcher agent
- **Features**:
  - Searches physics, mathematics, computer science, biology, and more
  - Returns titles, authors, abstracts, and publication links
  - Focuses on credible academic sources
  - Perfect for finding recent research and breakthrough studies
- **API**: Uses free arXiv API (no key required)

The tool is located in `src/agentic_researcher/tools/scientific_tools.py` and can be extended to include additional academic databases like PubMed or Semantic Scholar.

### Why This Approach?

Instead of using complex multi-tool workflows that can cause validation errors, we've focused on:
- ✅ **One reliable custom tool** for academic search
- ✅ **Standard CrewAI tools** for web search and scraping
- ✅ **Clear task descriptions** that guide agents without tool dependencies
- ✅ **Simple, robust workflow** that produces consistent results

## Customizing

**Add your `OPENAI_API_KEY` or other LLM API keys into the `.env` file**

You can customize the behavior by modifying:
- `src/agentic_researcher/config/agents.yaml` - Adjust agent roles, goals, and backstories
- `src/agentic_researcher/config/tasks.yaml` - Modify task descriptions and expected outputs
- `src/agentic_researcher/crew.py` - Add custom tools or logic
- `src/agentic_researcher/main.py` - Change input handling or output formatting

The Agentic_Researcher Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the AgenticResearcher Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
