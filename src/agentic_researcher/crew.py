from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from .tools.scientific_tools import ScientificSearchTool
from typing import List


@CrewBase
class AgenticResearcher():
    """Agentic Researcher crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    @before_kickoff
    def before_test(self):
        print("Before Kickoff!!!!!")

    @after_kickoff
    def process_output(self):
        print("After Kickoff!!!!")
    
    @agent
    def scientific_researcher(self) -> Agent:
        """Scientific Researcher: Gathers research with tools"""
        return Agent(
            config=self.agents_config['scientific_researcher'], # type: ignore[index]
            tools=[
                SerperDevTool(), 
                ScrapeWebsiteTool(),
                ScientificSearchTool()
            ],
            verbose=True
        )

    @agent
    def scientific_writer(self) -> Agent:
        """Scientific Writer: Transforms research into documents"""
        return Agent(
            config=self.agents_config['scientific_writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        """Editor: Quality assurance and final polishing"""
        return Agent(
            config=self.agents_config['editor'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'], # type: ignore[index]
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Agentic Researcher crew"""
        
        # Configure Ollama embeddings for knowledge sources
        embedder_config = {
            "provider": "ollama",
            "config": {
                "model": "nomic-embed-text"
            }
        }

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,  # Research → Write → Edit, but Process.hierarchical: Complex Multi-Agent Collaboration, Manager agents coordinating worker agents, Dynamic task assignment based on complexity, Agents helping each other during execution
            verbose=True,
            knowledge_sources=[
                TextFileKnowledgeSource(
                    file_path="knowledge/citation_styles.txt",
                    metadata={"type": "citation_guidelines", "description": "Citation formatting and referencing standards"}
                )
            ],
            embedder=embedder_config
        )
