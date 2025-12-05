# Scientific Research Assistant

A CrewAI-powered research assistant that helps you write comprehensive 1-page scientific documents on any concrete scientific topic. This multi-agent system combines the expertise of a scientific researcher, content writer, and editor to produce high-quality, evidence-based scientific summaries.

## Features

- **Automated Research**: Gathers current, credible scientific information from authoritative sources
- **Expert Writing**: Transforms complex research into clear, engaging 1-page documents
- **Quality Assurance**: Professional editing ensures accuracy, clarity, and optimal length
- **Interactive Mode**: Simply input any scientific topic and get a polished document
- **Structured Output**: Well-formatted markdown documents ready to share or present

## How It Works

The system uses three specialized AI agents working in sequence:

1. **Scientific Researcher**: Conducts comprehensive research on your topic, gathering key findings from credible sources
2. **Scientific Writer**: Crafts a well-structured 1-page document (500-600 words) with introduction, main content, and conclusion
3. **Editor**: Reviews and refines the document for accuracy, clarity, and optimal length

Welcome to the AgenticResearcher Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Environment Setup

**IMPORTANT: Configure your API keys in the `.env` file**

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Add your API keys to `.env`:
   - `OPENAI_API_KEY` - Required for AI agents (get from [OpenAI](https://platform.openai.com/api-keys))
   - `SERPER_API_KEY` - Required for web search functionality (get free key at [Serper.dev](https://serper.dev/))

Without these API keys, the research assistant will not function properly.

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/agentic_researcher/config/agents.yaml` to define your agents
- Modify `src/agentic_researcher/config/tasks.yaml` to define your tasks
- Modify `src/agentic_researcher/crew.py` to add your own logic, tools and specific args
- Modify `src/agentic_researcher/main.py` to add custom inputs for your agents and tasks

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

The Scientific Research Assistant is composed of three specialized AI agents with custom-built tools:

### 1. Scientific Researcher
- **Role**: PhD-level research specialist
- **Capabilities**: Gathers comprehensive scientific information from credible sources
- **Custom Tools**:
  - 🔬 **Scientific Literature Search**: Searches arXiv and academic databases for peer-reviewed papers
  - 📊 **Research Summarizer**: Organizes findings into structured categories
  - 🌐 **Web Search & Scraping**: General web search and content extraction
- **Output**: 8-12 key findings with supporting evidence and source attributions

### 2. Scientific Writer
- **Role**: Accomplished science writer
- **Capabilities**: Transforms research into clear, engaging 1-page documents
- **Custom Tools**:
  - 📊 **Research Summarizer**: Helps structure and organize content effectively
- **Output**: Well-structured 500-600 word document with proper formatting

### 3. Editor
- **Role**: Scientific editor and quality assurance specialist
- **Capabilities**: Reviews for accuracy, clarity, structure, and length
- **Custom Tools**:
  - ✏️ **Citation Formatter**: Checks for proper attribution and citation formatting
- **Output**: Publication-ready final document

These agents collaborate sequentially as defined in `config/tasks.yaml`, with each agent building upon the work of the previous one to create a polished scientific summary.

## Custom Tools

This project includes three specialized custom tools built specifically for scientific research:

### Scientific Literature Search Tool
- Searches arXiv for peer-reviewed scientific papers
- Returns titles, authors, abstracts, and publication links
- Focuses on credible academic sources
- Perfect for finding recent research and breakthrough studies

### Research Summarizer Tool
- Analyzes and structures research findings
- Organizes information into clear categories
- Provides writing recommendations
- Ensures comprehensive coverage of key points

### Citation Formatter Tool
- Analyzes text for proper scientific attribution
- Suggests citation formats (in-text, parenthetical, data citations)
- Identifies claims that need citations
- Ensures scientific rigor and credibility

You can find these tools in `src/agentic_researcher/tools/scientific_tools.py`.

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
