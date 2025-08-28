"""
AUTARK Deep Thinking Demo
========================

Demonstriert die Deep Thinking Fähigkeiten für Video-Generierung.
"""

import asyncio
import logging
import time
from pathlib import Path
import json

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def demo_deep_thinking():
    """Demonstrate deep thinking capabilities."""
    
    print("🧠 AUTARK Deep Thinking Engine Demo")
    print("=" * 40)
    
    try:
        # Import AUTARK modules
        from autark.nlp.deep_thinking import DeepThinkingEngine, create_thinking_engine
        from autark.knowledge.graph import KnowledgeGraph
        
        # Initialize components
        print("\n🔧 Initializing Deep Thinking Engine...")
        thinking_engine = create_thinking_engine(creativity=0.9)
        
        print("📚 Loading Knowledge Graph...")
        knowledge_graph = KnowledgeGraph()
        
        # Demo concepts
        demo_concepts = [
            "The evolution of artificial intelligence",
            "A journey through the cosmos",
            "The secret life of quantum particles",
            "How music shapes human emotions",
            "The future of sustainable energy"
        ]
        
        print(f"\n🎯 Testing {len(demo_concepts)} concepts...")
        
        results = []
        
        for i, concept in enumerate(demo_concepts, 1):
            print(f"\n📝 Concept {i}: '{concept}'")
            
            start_time = time.time()
            
            # Apply deep thinking
            enhanced = await thinking_engine.enhance_concept(
                concept,
                style="cinematic",
                duration=8.0,
                structure="three_act"
            )
            
            # Get knowledge context
            context = await knowledge_graph.get_context(concept)
            
            processing_time = time.time() - start_time
            
            # Display results
            print(f"   ✨ Enhanced: '{enhanced['enhanced_concept'][:100]}...'")
            print(f"   🧠 Creativity Score: {enhanced['processing_metrics']['creativity_score']:.2f}")
            print(f"   🎯 Uniqueness: {enhanced['processing_metrics']['uniqueness_potential']:.2f}")
            print(f"   ⏱️ Processing Time: {processing_time:.2f}s")
            print(f"   🔗 Knowledge Depth: {context['knowledge_depth']}")
            
            results.append({
                "original": concept,
                "enhanced": enhanced,
                "knowledge_context": context,
                "processing_time": processing_time
            })
        
        # Generate summary
        print(f"\n📊 Deep Thinking Demo Summary")
        print("=" * 30)
        
        avg_creativity = sum(r['enhanced']['processing_metrics']['creativity_score'] for r in results) / len(results)
        avg_uniqueness = sum(r['enhanced']['processing_metrics']['uniqueness_potential'] for r in results) / len(results)
        avg_time = sum(r['processing_time'] for r in results) / len(results)
        
        print(f"   Average Creativity Score: {avg_creativity:.3f}")
        print(f"   Average Uniqueness Rating: {avg_uniqueness:.3f}")
        print(f"   Average Processing Time: {avg_time:.3f}s")
        print(f"   Total Concepts Processed: {len(results)}")
        
        # Save detailed results
        results_path = Path("deep_thinking_demo_results.json")
        with open(results_path, 'w', encoding='utf-8') as f:
            json.dump({
                "demo_metadata": {
                    "timestamp": time.time(),
                    "engine_settings": {
                        "creativity_level": 0.9,
                        "semantic_depth": 0.9
                    },
                    "summary_statistics": {
                        "avg_creativity": avg_creativity,
                        "avg_uniqueness": avg_uniqueness,
                        "avg_processing_time": avg_time
                    }
                },
                "results": results
            }, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"\n💾 Detailed results saved to: {results_path}")
        
        # Demonstrate video generation pipeline
        await demo_video_pipeline(results[0])
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure AUTARK modules are properly installed")
    except Exception as e:
        print(f"❌ Demo error: {e}")
        logger.exception("Demo failed")


async def demo_video_pipeline(thinking_result):
    """Demonstrate full video generation pipeline."""
    
    print(f"\n🎬 Video Generation Pipeline Demo")
    print("=" * 35)
    
    try:
        from autark.core.studio import AutarkStudio
        
        # Initialize studio
        print("🏗️ Initializing AUTARK Studio...")
        studio = AutarkStudio()
        
        # Use enhanced concept from deep thinking
        enhanced_concept = thinking_result['enhanced']['enhanced_concept']
        
        print(f"🎯 Generating video for: '{enhanced_concept[:60]}...'")
        
        # Generate video
        video_result = await studio.generate_video(
            prompt=enhanced_concept,
            duration_minutes=2.0,
            style="cinematic",
            quality="1080p",
            deep_thinking=False  # Already enhanced
        )
        
        if video_result['success']:
            print(f"✅ Video generated successfully!")
            print(f"   📁 Output: {video_result['video_path']}")
            print(f"   ⏱️ Generation Time: {video_result['metadata']['generation_time']:.2f}s")
            print(f"   🛠️ Tools Used: {', '.join(video_result['metadata']['tools_used'])}")
            print(f"   ⭐ Quality Score: {video_result['analytics']['creativity_score']:.2f}")
        else:
            print(f"❌ Video generation failed: {video_result['error']}")
    
    except Exception as e:
        print(f"❌ Video pipeline error: {e}")


def demo_quick_functions():
    """Demonstrate quick access functions."""
    
    print(f"\n⚡ Quick Functions Demo")
    print("=" * 25)
    
    try:
        from autark import create_studio, deep_think
        
        # Quick studio creation
        studio = create_studio()
        print(f"✅ Studio created: {type(studio).__name__}")
        
        # Quick deep thinking (sync wrapper would be needed)
        print("🧠 Quick deep thinking would work with async wrapper")
        
    except Exception as e:
        print(f"❌ Quick functions error: {e}")


async def interactive_demo():
    """Interactive demo allowing user input."""
    
    print(f"\n🎮 Interactive Deep Thinking Demo")
    print("=" * 35)
    
    try:
        from autark.nlp.deep_thinking import create_thinking_engine
        
        engine = create_thinking_engine(creativity=0.8)
        
        while True:
            print(f"\n💭 Enter a concept for deep thinking (or 'quit' to exit):")
            user_input = input("   > ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if not user_input:
                continue
            
            print(f"🧠 Applying deep thinking to: '{user_input}'")
            
            result = await engine.enhance_concept(
                user_input,
                style="cinematic",
                duration=5.0
            )
            
            print(f"✨ Enhanced concept:")
            print(f"   {result['enhanced_concept']}")
            print(f"🎯 Creativity Score: {result['processing_metrics']['creativity_score']:.2f}")
            print(f"🌟 Uniqueness Potential: {result['processing_metrics']['uniqueness_potential']:.2f}")
    
    except Exception as e:
        print(f"❌ Interactive demo error: {e}")


def main():
    """Main demo function."""
    
    print("🎬 AUTARK Deep Thinking & Video Generation Demo")
    print("=" * 50)
    print("🧠 Demonstrating advanced NLP capabilities for video creation")
    print("🎯 Testing semantic analysis, creative enhancement, and narrative structuring")
    print()
    
    # Run demos
    try:
        # Async demo
        asyncio.run(demo_deep_thinking())
        
        # Quick functions demo
        demo_quick_functions()
        
        # Interactive demo (optional)
        response = input(f"\n🎮 Run interactive demo? (y/n): ").lower().strip()
        if response == 'y':
            asyncio.run(interactive_demo())
        
        print(f"\n🎉 Demo completed successfully!")
        print("📚 Check the generated files for detailed results")
        
    except KeyboardInterrupt:
        print(f"\n⏹️ Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        logger.exception("Main demo error")


if __name__ == "__main__":
    main()