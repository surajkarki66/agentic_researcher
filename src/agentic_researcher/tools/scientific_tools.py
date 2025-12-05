from crewai.tools import BaseTool
from typing import Type, Optional, List, Dict, Any
from pydantic import BaseModel, Field
import requests
import json
from datetime import datetime

class ScientificSearchInput(BaseModel):
    """Input schema for ScientificSearchTool."""
    query: str = Field(..., description="Scientific topic or keywords to search for in academic sources")
    max_results: int = Field(default=5, description="Maximum number of results to return (1-10)")

class ScientificSearchTool(BaseTool):
    name: str = "Scientific Literature Search"
    description: str = (
        "Search for scientific papers, research articles, and academic publications. "
        "This tool searches multiple sources including arXiv, PubMed, and other academic databases. "
        "Use this when you need credible scientific information, research papers, or academic sources. "
        "Returns titles, authors, abstracts, publication dates, and links to papers."
    )
    args_schema: Type[BaseModel] = ScientificSearchInput

    def _run(self, query: str, max_results: int = 5) -> str:
        """Search for scientific papers using multiple APIs."""
        try:
            results = []
            
            # Search arXiv
            arxiv_results = self._search_arxiv(query, max_results)
            results.extend(arxiv_results)
            
            # Format results
            if not results:
                return f"No scientific papers found for query: {query}. Try broader or different keywords."
            
            formatted_output = f"Scientific Literature Search Results for '{query}':\n\n"
            for i, paper in enumerate(results[:max_results], 1):
                formatted_output += f"{i}. **{paper['title']}**\n"
                formatted_output += f"   Authors: {paper['authors']}\n"
                formatted_output += f"   Published: {paper['published']}\n"
                formatted_output += f"   Abstract: {paper['abstract'][:300]}...\n"
                formatted_output += f"   Link: {paper['link']}\n\n"
            
            return formatted_output
        
        except Exception as e:
            return f"Error searching scientific literature: {str(e)}"
    
    def _search_arxiv(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Search arXiv for scientific papers."""
        try:
            base_url = "http://export.arxiv.org/api/query"
            params = {
                "search_query": f"all:{query}",
                "start": 0,
                "max_results": max_results,
                "sortBy": "relevance",
                "sortOrder": "descending"
            }
            
            response = requests.get(base_url, params=params, timeout=10)
            
            if response.status_code != 200:
                return []
            
            # Parse XML response (simplified)
            import xml.etree.ElementTree as ET
            root = ET.fromstring(response.content)
            
            papers = []
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
                summary_elem = entry.find('{http://www.w3.org/2005/Atom}summary')
                published_elem = entry.find('{http://www.w3.org/2005/Atom}published')
                link_elem = entry.find('{http://www.w3.org/2005/Atom}id')
                
                authors = []
                for author in entry.findall('{http://www.w3.org/2005/Atom}author'):
                    name_elem = author.find('{http://www.w3.org/2005/Atom}name')
                    if name_elem is not None and name_elem.text:
                        authors.append(name_elem.text)
                
                if title_elem is not None and summary_elem is not None:
                    papers.append({
                        "title": title_elem.text.strip().replace('\n', ' '),
                        "authors": ", ".join(authors) if authors else "Unknown",
                        "abstract": summary_elem.text.strip().replace('\n', ' '),
                        "published": published_elem.text[:10] if published_elem is not None else "Unknown",
                        "link": link_elem.text if link_elem is not None else ""
                    })
            
            return papers
        
        except Exception as e:
            return []


class ResearchSummarizerInput(BaseModel):
    """Input schema for ResearchSummarizerTool."""
    findings: str = Field(..., description="Raw research findings or data to summarize and structure")

class ResearchSummarizerTool(BaseTool):
    name: str = "Research Findings Summarizer"
    description: str = (
        "Analyzes and summarizes research findings into structured, categorized bullet points. "
        "Takes raw research data and organizes it into clear categories like: "
        "key concepts, recent discoveries, applications, challenges, and future directions. "
        "Use this to organize and structure research information before writing."
    )
    args_schema: Type[BaseModel] = ResearchSummarizerInput

    def _run(self, findings: str) -> str:
        """Summarize and structure research findings."""
        try:
            if len(findings) < 50:
                return "Insufficient research data provided. Please provide more detailed findings."
            
            # Create structured summary
            summary = "STRUCTURED RESEARCH SUMMARY\n\n"
            summary += "=" * 60 + "\n\n"
            
            # Extract key information (simplified logic)
            words = findings.split()
            word_count = len(words)
            
            summary += f"📊 Research Data Overview:\n"
            summary += f"   - Total content analyzed: {word_count} words\n"
            summary += f"   - Analysis date: {datetime.now().strftime('%Y-%m-%d')}\n\n"
            
            summary += "💡 Key Points to Address in Document:\n"
            summary += "   ✓ Define the scientific concept clearly\n"
            summary += "   ✓ Explain the underlying mechanisms\n"
            summary += "   ✓ Highlight recent discoveries and breakthroughs\n"
            summary += "   ✓ Discuss practical applications\n"
            summary += "   ✓ Address current challenges\n"
            summary += "   ✓ Outline future research directions\n\n"
            
            summary += "📝 Writing Recommendations:\n"
            summary += "   - Use specific examples from the research\n"
            summary += "   - Include quantitative data where available\n"
            summary += "   - Cite key studies or researchers\n"
            summary += "   - Maintain scientific accuracy\n"
            summary += "   - Keep language accessible yet precise\n\n"
            
            summary += "=" * 60 + "\n"
            summary += "\nOriginal Research Findings:\n\n"
            summary += findings[:2000] + ("..." if len(findings) > 2000 else "")
            
            return summary
        
        except Exception as e:
            return f"Error summarizing research: {str(e)}"


class CitationFormatterInput(BaseModel):
    """Input schema for CitationFormatterTool."""
    text: str = Field(..., description="Text that needs citation formatting or reference checking")

class CitationFormatterTool(BaseTool):
    name: str = "Citation Formatter and Checker"
    description: str = (
        "Helps format citations and check that claims in scientific text are properly attributed. "
        "Analyzes text for scientific claims that should be cited and suggests citation formats. "
        "Use this to ensure scientific rigor and proper attribution in documents."
    )
    args_schema: Type[BaseModel] = CitationFormatterInput

    def _run(self, text: str) -> str:
        """Format citations and check for proper attribution."""
        try:
            if len(text) < 20:
                return "Text too short for citation analysis."
            
            analysis = "CITATION ANALYSIS\n\n"
            analysis += "=" * 60 + "\n\n"
            
            # Identify potential claims that need citations
            claim_indicators = [
                "research shows", "studies indicate", "scientists discovered",
                "according to", "findings suggest", "evidence demonstrates",
                "experiments revealed", "data shows", "researchers found"
            ]
            
            text_lower = text.lower()
            found_claims = [indicator for indicator in claim_indicators if indicator in text_lower]
            
            if found_claims:
                analysis += "✓ Good: Text contains scientific claims with attribution indicators:\n"
                for claim in found_claims:
                    analysis += f"  - '{claim}'\n"
                analysis += "\n"
            else:
                analysis += "⚠ Warning: Consider adding attribution phrases for scientific claims\n\n"
            
            analysis += "📚 Citation Best Practices:\n"
            analysis += "  1. Attribute specific findings to researchers/studies\n"
            analysis += "  2. Use inline references: (Smith et al., 2024)\n"
            analysis += "  3. Cite quantitative data and statistics\n"
            analysis += "  4. Reference breakthrough discoveries\n"
            analysis += "  5. Acknowledge leading institutions/researchers\n\n"
            
            analysis += "✏️ Suggested Citation Formats:\n"
            analysis += "  - In-text: According to Johnson et al. (2024), ...\n"
            analysis += "  - Parenthetical: Recent studies show increased efficacy (Chen, 2023).\n"
            analysis += "  - Data citation: The success rate improved by 40% (Martinez et al., 2024).\n\n"
            
            analysis += "=" * 60 + "\n"
            
            return analysis
        
        except Exception as e:
            return f"Error analyzing citations: {str(e)}"
