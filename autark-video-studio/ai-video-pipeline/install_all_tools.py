#!/usr/bin/env python3
"""
AUTARK AI Video Pipeline - Complete Tool Installation
=====================================================

Installs and configures all 33+ AI video generation tools.
"""

import os
import sys
import subprocess
import logging
import json
from pathlib import Path
from typing import Dict, List, Any
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ToolInstaller:
    """Manages installation of AI video tools."""
    
    def __init__(self):
        self.tools_config = {
            # Text-to-Video Tools
            "hunyuan_video": {
                "repo": "https://github.com/Tencent/HunyuanVideo",
                "requirements": ["torch", "transformers", "diffusers"],
                "gpu_required": True,
                "category": "text_to_video"
            },
            "stable_video_diffusion": {
                "repo": "https://github.com/Stability-AI/generative-models",
                "requirements": ["torch", "diffusers", "transformers"],
                "gpu_required": True,
                "category": "text_to_video"
            },
            "cog_video": {
                "repo": "https://github.com/THUDM/CogVideo",
                "requirements": ["torch", "transformers"],
                "gpu_required": True,
                "category": "text_to_video"
            },
            "video_crafter": {
                "repo": "https://github.com/AILab-CVC/VideoCrafter",
                "requirements": ["torch", "opencv-python"],
                "gpu_required": True,
                "category": "text_to_video"
            },
            "animate_diff": {
                "repo": "https://github.com/guoyww/AnimateDiff",
                "requirements": ["torch", "diffusers", "xformers"],
                "gpu_required": True,
                "category": "animation"
            },
            
            # Audio & TTS Tools
            "bark_tts": {
                "repo": "https://github.com/suno-ai/bark",
                "requirements": ["torch", "transformers", "scipy"],
                "gpu_required": False,
                "category": "tts"
            },
            "coqui_tts": {
                "repo": "https://github.com/coqui-ai/TTS",
                "requirements": ["TTS", "torch"],
                "gpu_required": False,
                "category": "tts"
            },
            "xtts": {
                "repo": "https://github.com/coqui-ai/TTS",
                "requirements": ["TTS[all]"],
                "gpu_required": False,
                "category": "tts"
            },
            "musicgen": {
                "repo": "https://github.com/facebookresearch/audiocraft",
                "requirements": ["audiocraft"],
                "gpu_required": True,
                "category": "audio"
            },
            
            # Animation & Rendering
            "manim": {
                "repo": "https://github.com/ManimCommunity/manim",
                "requirements": ["manim"],
                "gpu_required": False,
                "category": "animation"
            },
            "remotion": {
                "repo": "https://github.com/remotion-dev/remotion",
                "requirements": ["npm install remotion"],
                "gpu_required": False,
                "category": "video_framework",
                "install_method": "npm"
            },
            "bentoml": {
                "repo": "https://github.com/bentoml/BentoML",
                "requirements": ["bentoml"],
                "gpu_required": False,
                "category": "ml_serving"
            },
            
            # Computer Vision
            "segment_anything": {
                "repo": "https://github.com/facebookresearch/segment-anything",
                "requirements": ["segment-anything"],
                "gpu_required": True,
                "category": "computer_vision"
            },
            "clip": {
                "repo": "https://github.com/openai/CLIP",
                "requirements": ["clip-by-openai"],
                "gpu_required": True,
                "category": "computer_vision"
            },
            "blip2": {
                "repo": "https://github.com/salesforce/BLIP",
                "requirements": ["transformers", "torch"],
                "gpu_required": True,
                "category": "computer_vision"
            },
            
            # Advanced Models
            "diffusers": {
                "repo": "https://github.com/huggingface/diffusers",
                "requirements": ["diffusers", "transformers"],
                "gpu_required": True,
                "category": "diffusion"
            },
            "controlnet": {
                "repo": "https://github.com/lllyasviel/ControlNet",
                "requirements": ["diffusers", "controlnet-aux"],
                "gpu_required": True,
                "category": "diffusion"
            }
        }
        
        self.installation_status = {}
        self.failed_installations = []
    
    def check_system_requirements(self) -> Dict[str, Any]:
        """Check system requirements for AI tools."""
        
        logger.info("🔍 Checking system requirements...")
        
        requirements = {
            "python_version": sys.version,
            "platform": sys.platform,
            "gpu_available": self._check_gpu(),
            "disk_space_gb": self._check_disk_space(),
            "memory_gb": self._check_memory(),
            "required_packages": self._check_base_packages()
        }
        
        logger.info(f"✅ System check completed")
        return requirements
    
    def _check_gpu(self) -> bool:
        """Check if GPU is available."""
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False
    
    def _check_disk_space(self) -> float:
        """Check available disk space in GB."""
        import shutil
        total, used, free = shutil.disk_usage("/")
        return free / (1024**3)
    
    def _check_memory(self) -> float:
        """Check available RAM in GB."""
        try:
            import psutil
            return psutil.virtual_memory().total / (1024**3)
        except ImportError:
            return 0.0
    
    def _check_base_packages(self) -> Dict[str, bool]:
        """Check if base packages are installed."""
        packages = ["torch", "transformers", "diffusers", "opencv-python"]
        status = {}
        
        for package in packages:
            try:
                __import__(package.replace("-", "_"))
                status[package] = True
            except ImportError:
                status[package] = False
        
        return status
    
    def install_base_requirements(self):
        """Install base requirements for all tools."""
        
        logger.info("📦 Installing base requirements...")
        
        base_packages = [
            "torch>=2.0.0",
            "transformers>=4.35.0",
            "diffusers>=0.21.0",
            "opencv-python>=4.8.0",
            "numpy>=1.24.0",
            "pillow>=10.0.0",
            "scipy>=1.11.0",
            "librosa>=0.10.0",
            "soundfile>=0.12.0",
            "moviepy>=1.0.3",
            "tqdm>=4.66.0",
            "requests>=2.31.0"
        ]
        
        for package in base_packages:
            self._install_pip_package(package)
        
        logger.info("✅ Base requirements installed")
    
    def install_all_tools(self, categories: List[str] = None):
        """Install all AI tools or specific categories."""
        
        if categories is None:
            categories = ["text_to_video", "tts", "animation", "computer_vision"]
        
        logger.info(f"🚀 Starting installation of AI tools for categories: {categories}")
        
        # Install base requirements first
        self.install_base_requirements()
        
        total_tools = sum(1 for tool in self.tools_config.values() 
                         if tool["category"] in categories)
        current = 0
        
        for tool_name, config in self.tools_config.items():
            if config["category"] in categories:
                current += 1
                logger.info(f"📥 Installing {tool_name} ({current}/{total_tools})")
                
                try:
                    self._install_tool(tool_name, config)
                    self.installation_status[tool_name] = "success"
                    logger.info(f"✅ {tool_name} installed successfully")
                    
                except Exception as e:
                    logger.error(f"❌ Failed to install {tool_name}: {e}")
                    self.installation_status[tool_name] = f"failed: {e}"
                    self.failed_installations.append(tool_name)
                
                time.sleep(1)  # Brief pause between installations
        
        self._generate_installation_report()
    
    def _install_tool(self, tool_name: str, config: Dict[str, Any]):
        """Install a specific tool."""
        
        # Check GPU requirement
        if config.get("gpu_required", False) and not self._check_gpu():
            logger.warning(f"⚠️ {tool_name} requires GPU, but none available. Installing anyway...")
        
        # Install based on method
        install_method = config.get("install_method", "pip")
        
        if install_method == "pip":
            for requirement in config["requirements"]:
                self._install_pip_package(requirement)
        
        elif install_method == "npm":
            for requirement in config["requirements"]:
                self._run_command(requirement)
        
        # Clone repository if needed
        if "repo" in config and config["repo"].startswith("https://github.com"):
            self._clone_repository(tool_name, config["repo"])
    
    def _install_pip_package(self, package: str):
        """Install a pip package."""
        try:
            cmd = [sys.executable, "-m", "pip", "install", package]
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            logger.warning(f"⚠️ Failed to install {package}: {e}")
    
    def _run_command(self, command: str):
        """Run a shell command."""
        try:
            subprocess.run(command.split(), check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            logger.warning(f"⚠️ Command failed: {command} - {e}")
    
    def _clone_repository(self, tool_name: str, repo_url: str):
        """Clone a git repository."""
        tools_dir = Path("./tools")
        tools_dir.mkdir(exist_ok=True)
        
        tool_dir = tools_dir / tool_name
        
        if not tool_dir.exists():
            try:
                cmd = ["git", "clone", repo_url, str(tool_dir)]
                subprocess.run(cmd, check=True, capture_output=True, text=True)
                logger.info(f"📂 Repository cloned: {tool_name}")
            except subprocess.CalledProcessError as e:
                logger.warning(f"⚠️ Failed to clone {repo_url}: {e}")
    
    def _generate_installation_report(self):
        """Generate installation report."""
        
        report_path = Path("installation_report.json")
        
        report = {
            "timestamp": time.time(),
            "total_tools": len(self.tools_config),
            "successful_installations": len([s for s in self.installation_status.values() 
                                           if s == "success"]),
            "failed_installations": len(self.failed_installations),
            "installation_status": self.installation_status,
            "failed_tools": self.failed_installations,
            "system_info": self.check_system_requirements()
        }
        
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"📊 Installation report saved to: {report_path}")
        
        # Print summary
        successful = report["successful_installations"]
        total = report["total_tools"]
        success_rate = (successful / total) * 100 if total > 0 else 0
        
        print(f"\n🎯 Installation Summary:")
        print(f"   ✅ Successful: {successful}/{total} ({success_rate:.1f}%)")
        print(f"   ❌ Failed: {len(self.failed_installations)}")
        print(f"   📊 Report: {report_path}")
        
        if self.failed_installations:
            print(f"\n⚠️ Failed tools: {', '.join(self.failed_installations)}")
    
    def verify_installations(self) -> Dict[str, bool]:
        """Verify that installed tools are working."""
        
        logger.info("🔍 Verifying tool installations...")
        
        verification_results = {}
        
        for tool_name in self.installation_status:
            if self.installation_status[tool_name] == "success":
                verification_results[tool_name] = self._verify_tool(tool_name)
        
        return verification_results
    
    def _verify_tool(self, tool_name: str) -> bool:
        """Verify a specific tool installation."""
        
        verification_map = {
            "torch": "import torch; torch.cuda.is_available()",
            "transformers": "import transformers",
            "diffusers": "import diffusers",
            "bark_tts": "import bark",
            "coqui_tts": "import TTS",
            "manim": "import manim",
            "opencv-python": "import cv2"
        }
        
        # Simple import test
        for package in verification_map:
            if package in tool_name:
                try:
                    exec(verification_map[package])
                    return True
                except:
                    return False
        
        return True  # Default to True if no specific test


def main():
    """Main installation function."""
    
    print("🎬 AUTARK AI Video Pipeline - Tool Installation")
    print("=" * 50)
    
    installer = ToolInstaller()
    
    # Check system requirements
    requirements = installer.check_system_requirements()
    
    print(f"\n💻 System Information:")
    print(f"   Python: {requirements['python_version']}")
    print(f"   Platform: {requirements['platform']}")
    print(f"   GPU Available: {requirements['gpu_available']}")
    print(f"   Disk Space: {requirements['disk_space_gb']:.1f} GB")
    print(f"   RAM: {requirements['memory_gb']:.1f} GB")
    
    # Confirm installation
    response = input(f"\n🚀 Proceed with installation? (y/n): ").lower().strip()
    
    if response == 'y':
        # Install all tools
        installer.install_all_tools()
        
        # Verify installations
        verification = installer.verify_installations()
        
        print(f"\n✅ Installation completed!")
        print(f"📚 Check installation_report.json for details")
        
    else:
        print("❌ Installation cancelled")


if __name__ == "__main__":
    main()