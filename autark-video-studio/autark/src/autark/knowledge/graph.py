"""
AUTARK Knowledge Graph System
=============================

Semantic knowledge management and integration for video generation.
"""

import logging
import json
import asyncio
from typing import Dict, List, Any, Set
from pathlib import Path
from dataclasses import dataclass, asdict
import time

logger = logging.getLogger(__name__)


@dataclass
class KnowledgeNode:
    """Represents a node in the knowledge graph."""
    
    id: str
    concept: str
    category: str
    relationships: List[str]
    metadata: Dict[str, Any]
    relevance_score: float = 0.0


class KnowledgeGraph:
    """
    AUTARK Knowledge Graph for semantic understanding and content enrichment.
    
    Provides context, relationships, and enhanced understanding for video concepts.
    """
    
    def __init__(self, base_path: str = "./knowledge-base"):
        self.base_path = Path(base_path)
        self.nodes = {}
        self.relationships = {}
        self.categories = set()
        
        # Initialize knowledge base
        self._initialize_knowledge_base()
        
        logger.info("📚 Knowledge Graph initialized")
    
    def _initialize_knowledge_base(self):
        """Initialize the knowledge base with core concepts."""
        
        # Core video generation concepts
        core_concepts = [
            {
                "id": "video_narrative",
                "concept": "Video Storytelling",
                "category": "narrative",
                "relationships": ["cinematography", "audio_design", "pacing"],
                "metadata": {
                    "importance": 0.9,
                    "complexity": 0.7,
                    "ai_tools": ["cog_video", "stable_video_diffusion"]
                }
            },
            {
                "id": "cinematography",
                "concept": "Visual Composition",
                "category": "visual",
                "relationships": ["color_theory", "lighting", "camera_movement"],
                "metadata": {
                    "importance": 0.8,
                    "complexity": 0.6,
                    "ai_tools": ["hunyuan_video", "stable_video_diffusion"]
                }
            },
            {
                "id": "audio_design",
                "concept": "Sound and Music",
                "category": "audio",
                "relationships": ["tts", "background_music", "sound_effects"],
                "metadata": {
                    "importance": 0.8,
                    "complexity": 0.5,
                    "ai_tools": ["bark_tts", "coqui_tts", "musicgen"]
                }
            }
        ]
        
        for concept_data in core_concepts:
            node = KnowledgeNode(**concept_data)
            self.add_node(node)
    
    def add_node(self, node: KnowledgeNode):
        """Add a node to the knowledge graph."""
        self.nodes[node.id] = node
        self.categories.add(node.category)
        
        # Update relationships
        for related_id in node.relationships:
            if node.id not in self.relationships:
                self.relationships[node.id] = set()
            self.relationships[node.id].add(related_id)
    
    async def get_context(self, concept: str) -> Dict[str, Any]:
        """Get semantic context and related knowledge for a concept."""
        
        logger.info(f"📚 Retrieving context for: '{concept[:50]}...'")
        
        # Find relevant nodes
        relevant_nodes = self._find_relevant_nodes(concept)
        
        # Calculate semantic relationships
        relationships = self._calculate_relationships(relevant_nodes)
        
        # Generate contextual enhancements
        enhancements = self._generate_enhancements(concept, relevant_nodes)
        
        context = {
            "primary_concept": concept,
            "relevant_nodes": [asdict(node) for node in relevant_nodes],
            "semantic_relationships": relationships,
            "contextual_enhancements": enhancements,
            "recommended_tools": self._recommend_tools(relevant_nodes),
            "knowledge_depth": len(relevant_nodes),
            "context_confidence": self._calculate_confidence(relevant_nodes)
        }
        
        logger.info(f"📊 Context generated with {len(relevant_nodes)} relevant concepts")
        return context
    
    def _find_relevant_nodes(self, concept: str) -> List[KnowledgeNode]:
        """Find nodes relevant to the given concept."""
        relevant = []
        concept_lower = concept.lower()
        
        for node in self.nodes.values():
            relevance = 0.0
            
            # Direct concept match
            if node.concept.lower() in concept_lower:
                relevance += 0.8
            
            # Category relevance
            category_keywords = {
                "narrative": ["story", "tale", "journey", "character"],
                "visual": ["visual", "color", "light", "scene"],
                "audio": ["sound", "music", "voice", "audio"],
                "technical": ["quality", "resolution", "format"]
            }
            
            if node.category in category_keywords:
                for keyword in category_keywords[node.category]:
                    if keyword in concept_lower:
                        relevance += 0.3
            
            # Metadata relevance
            if "keywords" in node.metadata:
                for keyword in node.metadata["keywords"]:
                    if keyword.lower() in concept_lower:
                        relevance += 0.2
            
            if relevance > 0.1:
                node.relevance_score = relevance
                relevant.append(node)
        
        # Sort by relevance
        relevant.sort(key=lambda x: x.relevance_score, reverse=True)
        return relevant[:10]  # Top 10 most relevant
    
    def _calculate_relationships(self, nodes: List[KnowledgeNode]) -> Dict[str, Any]:
        """Calculate semantic relationships between nodes."""
        relationships = {
            "direct_connections": 0,
            "cluster_strength": 0.0,
            "relationship_map": {}
        }
        
        node_ids = {node.id for node in nodes}
        
        for node in nodes:
            connected = set(node.relationships) & node_ids
            if connected:
                relationships["direct_connections"] += len(connected)
                relationships["relationship_map"][node.id] = list(connected)
        
        # Calculate cluster strength
        if len(nodes) > 1:
            max_possible = len(nodes) * (len(nodes) - 1)
            actual_connections = relationships["direct_connections"]
            relationships["cluster_strength"] = actual_connections / max_possible
        
        return relationships
    
    def _generate_enhancements(self, concept: str, nodes: List[KnowledgeNode]) -> Dict[str, Any]:
        """Generate contextual enhancements based on knowledge."""
        enhancements = {
            "thematic_suggestions": [],
            "technical_recommendations": [],
            "creative_opportunities": []
        }
        
        # Thematic suggestions based on categories
        categories_present = {node.category for node in nodes}
        
        if "narrative" in categories_present:
            enhancements["thematic_suggestions"].append(
                "Consider developing character arcs and story progression"
            )
        
        if "visual" in categories_present:
            enhancements["thematic_suggestions"].append(
                "Focus on visual storytelling and composition"
            )
        
        if "audio" in categories_present:
            enhancements["thematic_suggestions"].append(
                "Integrate meaningful audio design and sound"
            )
        
        # Technical recommendations
        high_importance_nodes = [n for n in nodes if n.metadata.get("importance", 0) > 0.7]
        if high_importance_nodes:
            enhancements["technical_recommendations"].append(
                "Prioritize high-quality rendering for key elements"
            )
        
        # Creative opportunities
        if len(set(node.category for node in nodes)) > 2:
            enhancements["creative_opportunities"].append(
                "Multi-dimensional approach combining different creative aspects"
            )
        
        return enhancements
    
    def _recommend_tools(self, nodes: List[KnowledgeNode]) -> List[str]:
        """Recommend AI tools based on relevant knowledge nodes."""
        tools = set()
        
        for node in nodes:
            if "ai_tools" in node.metadata:
                tools.update(node.metadata["ai_tools"])
        
        # Add weight based on relevance
        weighted_tools = {}
        for node in nodes:
            if "ai_tools" in node.metadata:
                for tool in node.metadata["ai_tools"]:
                    if tool not in weighted_tools:
                        weighted_tools[tool] = 0
                    weighted_tools[tool] += node.relevance_score
        
        # Sort by weight and return top tools
        sorted_tools = sorted(weighted_tools.items(), key=lambda x: x[1], reverse=True)
        return [tool[0] for tool in sorted_tools[:5]]
    
    def _calculate_confidence(self, nodes: List[KnowledgeNode]) -> float:
        """Calculate confidence in the knowledge context."""
        if not nodes:
            return 0.0
        
        avg_relevance = sum(node.relevance_score for node in nodes) / len(nodes)
        coverage = min(len(nodes) / 5.0, 1.0)  # 5 nodes = full coverage
        
        confidence = (avg_relevance * 0.7) + (coverage * 0.3)
        return min(confidence, 1.0)
    
    def expand_knowledge(self, new_concepts: List[Dict[str, Any]]):
        """Expand the knowledge base with new concepts."""
        for concept_data in new_concepts:
            if "id" not in concept_data:
                concept_data["id"] = f"concept_{int(time.time())}"
            
            node = KnowledgeNode(**concept_data)
            self.add_node(node)
        
        logger.info(f"📚 Added {len(new_concepts)} new concepts to knowledge base")
    
    def save_knowledge_base(self, file_path: str = None):
        """Save the knowledge base to disk."""
        if file_path is None:
            file_path = self.base_path / "knowledge_graph.json"
        
        data = {
            "nodes": {node_id: asdict(node) for node_id, node in self.nodes.items()},
            "relationships": {k: list(v) for k, v in self.relationships.items()},
            "categories": list(self.categories)
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"💾 Knowledge base saved to {file_path}")
    
    def load_knowledge_base(self, file_path: str = None):
        """Load knowledge base from disk."""
        if file_path is None:
            file_path = self.base_path / "knowledge_graph.json"
        
        if not Path(file_path).exists():
            logger.warning(f"Knowledge base file not found: {file_path}")
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Load nodes
            for node_id, node_data in data.get("nodes", {}).items():
                node = KnowledgeNode(**node_data)
                self.nodes[node_id] = node
            
            # Load relationships
            for node_id, related_ids in data.get("relationships", {}).items():
                self.relationships[node_id] = set(related_ids)
            
            # Load categories
            self.categories = set(data.get("categories", []))
            
            logger.info(f"📚 Knowledge base loaded from {file_path}")
            
        except Exception as e:
            logger.error(f"❌ Failed to load knowledge base: {e}")
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get knowledge graph statistics."""
        return {
            "total_nodes": len(self.nodes),
            "total_relationships": sum(len(rels) for rels in self.relationships.values()),
            "categories": list(self.categories),
            "avg_connections_per_node": (
                sum(len(rels) for rels in self.relationships.values()) / len(self.nodes)
                if self.nodes else 0
            )
        }


# Convenience functions
def create_knowledge_graph(base_path: str = "./knowledge-base") -> KnowledgeGraph:
    """Create a new knowledge graph instance."""
    return KnowledgeGraph(base_path)


async def get_concept_context(concept: str, kb_path: str = "./knowledge-base") -> Dict[str, Any]:
    """Quick context retrieval for a concept."""
    kg = KnowledgeGraph(kb_path)
    return await kg.get_context(concept)