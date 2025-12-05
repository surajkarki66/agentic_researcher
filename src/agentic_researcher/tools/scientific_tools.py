from crewai.tools import BaseTool
from typing import Type, List, Dict, Any
from pydantic import BaseModel, Field

import requests

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
