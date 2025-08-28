"""
AUTARK Knowledge Integration System
===================================

High-Performance NLP Deep Thinking Engine for Video Generation

This package provides:
- NLP Deep Thinking capabilities for creative content generation
- Knowledge Graph integration for semantic understanding
- Pre-trained learning curves for 33+ AI video tools
- High-performance video generation pipeline

Author: HolyThreeKingsTreesCrowns Team
Version: 1.0.0
License: MIT
"""

__version__ = "1.0.0"
__author__ = "HolyThreeKingsTreesCrowns Team"
__email__ = "team@video-studio.ai"

# Core exports
from .core.studio import AutarkStudio
from .nlp.deep_thinking import DeepThinkingEngine
from .knowledge.graph import KnowledgeGraph
from .video.generator import VideoGenerator

# Quick access functions
def create_studio(config=None):
    """Create a new AUTARK Studio instance with optional configuration."""
    return AutarkStudio(config)

def generate_video(prompt, **kwargs):
    """Quick video generation with default settings."""
    studio = AutarkStudio()
    return studio.generate_video(prompt, **kwargs)

def deep_think(concept, **kwargs):
    """Apply deep thinking to a concept for creative enhancement."""
    engine = DeepThinkingEngine()
    return engine.process(concept, **kwargs)

# Package metadata
__all__ = [
    'AutarkStudio',
    'DeepThinkingEngine', 
    'KnowledgeGraph',
    'VideoGenerator',
    'create_studio',
    'generate_video',
    'deep_think'
]