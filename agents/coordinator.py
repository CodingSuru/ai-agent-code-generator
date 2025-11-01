import os
import json
from datetime import datetime
from agents.frontend_agent import FrontendAgent
from agents.backend_agent import BackendAgent

class CoordinatorAgent:
    def __init__(self, project_brief):
        self.brief = project_brief
        self.frontend_agent = FrontendAgent()
        self.backend_agent = BackendAgent()
        self.project_spec = {}
        
    def analyze_brief(self):
        """Parse the project brief and extract requirements"""
        print("COORDINATOR: Analyzing project brief...")
        
        brief_lower = self.brief.lower()
        
        # === PROJECT TYPE DETECTION ===
        if "dataviz" in brief_lower or "dashboard" in brief_lower or "chart" in brief_lower or "visualization" in brief_lower:
            self.project_spec['type'] = 'dataviz'
        elif "world clock" in brief_lower or "timezone" in brief_lower or "clock" in brief_lower:
            self.project_spec['type'] = 'worldclock'
        else:
            self.project_spec['type'] = 'crud'
        
        # === PROJECT NAME ===
        if "called" in brief_lower:
            words = self.brief.split()
            idx = [i for i, w in enumerate(words) if w.lower() == "called"]
            if idx and idx[0] + 1 < len(words):
                self.project_spec['name'] = words[idx[0] + 1].replace(',', '').replace('.', '')
        
        if 'name' not in self.project_spec:
            if self.project_spec['type'] == 'dataviz':
                self.project_spec['name'] = "AgriDataViz"
            elif self.project_spec['type'] == 'worldclock':
                self.project_spec['name'] = "WorldClock"
            elif "notes" in brief_lower:
                self.project_spec['name'] = "NotesApp"
            elif "todo" in brief_lower or "task" in brief_lower:
                self.project_spec['name'] = "TodoApp"
            else:
                self.project_spec['name'] = "GeneratedApp"
        
        # === ENTITY & FEATURES ===
        if self.project_spec['type'] == 'crud':
            features = []
            if "add" in brief_lower or "create" in brief_lower:
                features.append("add")
            if "search" in brief_lower or "filter" in brief_lower:
                features.append("search")
            if "list" in brief_lower or "view" in brief_lower or "display" in brief_lower:
                features.append("list")
            if "edit" in brief_lower or "update" in brief_lower:
                features.append("edit")
            if "delete" in brief_lower or "remove" in brief_lower:
                features.append("delete")
            if "auth" in brief_lower or "login" in brief_lower:
                features.append("auth")
            if "categories" in brief_lower or "category" in brief_lower:
                features.append("categories")
            
            self.project_spec['features'] = features if features else ["add", "list", "search"]
            
            if "notes" in brief_lower or "note" in brief_lower:
                self.project_spec['entity'] = "note"
            elif "todo" in brief_lower or "task" in brief_lower:
                self.project_spec['entity'] = "task"
            elif "user" in brief_lower:
                self.project_spec['entity'] = "user"
            else:
                self.project_spec['entity'] = "item"
        else:
            self.project_spec['entity'] = "data"
            self.project_spec['features'] = ["visualize", "ml"]
        
        self.project_spec['brief'] = self.brief
        self.project_spec['timestamp'] = datetime.now().isoformat()
        
        print(f"   Project Type: {self.project_spec['type'].upper()}")
        print(f"   Project Name: {self.project_spec['name']}")
        if self.project_spec['type'] == 'crud':
            print(f"   Entity Type: {self.project_spec['entity']}")
            print(f"   Features: {', '.join(self.project_spec['features'])}")
        print()
        
        return self.project_spec
    
    def delegate_tasks(self):
        """Delegate tasks to specialized agents"""
        print("COORDINATOR: Delegating tasks to agents...")
        print()
        
        if self.project_spec['type'] == 'dataviz':
            from agents.dataviz_agent import DataVizAgent
            agent = DataVizAgent()
            files = agent.generate(self.project_spec)
            print(f"   Generated {len(files)} DataViz files")
            return files
            
        elif self.project_spec['type'] == 'worldclock':
            from agents.worldclock_agent import WorldClockAgent
            agent = WorldClockAgent()
            files = agent.generate(self.project_spec)
            print(f"   Generated {len(files)} WorldClock files")
            return files
            
        else:
            print("Task 1: Assigning Frontend Generation to Frontend Agent")
            frontend_task = {
                "type": "frontend",
                "project_name": self.project_spec['name'],
                "entity": self.project_spec['entity'],
                "features": self.project_spec['features']
            }
            frontend_files = self.frontend_agent.generate(frontend_task)
            print(f"   Generated {len(frontend_files)} frontend files")
            print()
            
            print("Task 2: Assigning Backend Generation to Backend Agent")
            backend_task = {
                "type": "backend",
                "project_name": self.project_spec['name'],
                "entity": self.project_spec['entity'],
                "features": self.project_spec['features']
            }
            backend_files = self.backend_agent.generate(backend_task)
            print(f"   Generated {len(backend_files)} backend files")
            print()
            
            return {
                "frontend": frontend_files,
                "backend": backend_files
            }
    
    def save_project_metadata(self):
        """Save project metadata for traceability"""
        metadata = {
            "project_name": self.project_spec['name'],
            "project_type": self.project_spec['type'],
            "brief": self.brief,
            "generated_at": datetime.now().isoformat(),
            "features": self.project_spec.get('features', []),
            "entity": self.project_spec.get('entity', 'N/A'),
            "agents_used": ["CoordinatorAgent", "FrontendAgent", "BackendAgent"] if self.project_spec['type'] == 'crud' else ["CoordinatorAgent", f"{self.project_spec['type'].capitalize()}Agent"]
        }
        
        with open("outputs/project_metadata.json", "w", encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
        
        print("COORDINATOR: Saved project metadata")
        print()
    
    def generate_readme(self):
        """Generate README with instructions"""
        if self.project_spec['type'] == 'dataviz':
            readme_content = f"""# {self.project_spec['name']}

**Auto-generated by AI Agent System**

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Project Brief
{self.brief}

## Features
- Interactive data visualizations (charts)
- ML-powered anomaly detection
- Real-time data analysis
- Drag & drop file upload (CSV/JSON/Excel)

## How to Run

### Step 1: Navigate to Outputs
```bash
cd outputs
```

### Step 2: Install Node Dependencies
```bash
npm install
```

### Step 3: Start the Server
```bash
node server.js
```

### Step 4: Open Browser
Open your browser and navigate to:
```
http://localhost:5000
```

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Chart.js, PapaParse
- **Backend**: Node.js, Express.js
- **ML**: Client-side statistical anomaly detection (Z-score)

## Optional Enhancement
For advanced ML features with Python-based anomaly detection, you may optionally install:
```bash
pip install scikit-learn pandas
```
(Recommended but not required - the dashboard works fully with client-side ML)

## Generated by AI Agents

- 🧠 **Coordinator Agent**: Orchestrated the generation process
- 📊 **DataViz Agent**: Generated dashboard with ML integration

---

*This project was automatically generated. Modify as needed for your requirements.*
"""
        elif self.project_spec['type'] == 'worldclock':
            readme_content = f"""# {self.project_spec['name']}

**Auto-generated by AI Agent System**

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Project Brief
{self.brief}

## Features
- Live world clocks for multiple timezones
- Auto-detection of user location
- Real-time clock updates

## How to Run

### Step 1: Navigate to Outputs
```bash
cd outputs
```

### Step 2: Install Dependencies
```bash
npm install
```

### Step 3: Start the Server
```bash
node server.js
```

### Step 4: Open Browser
Open your browser and navigate to:
```
http://localhost:5000
```

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Node.js, Express.js
- **API**: ipapi.co for geolocation

## Generated by AI Agents

- 🧠 **Coordinator Agent**: Orchestrated the generation process
- 🌍 **WorldClock Agent**: Generated live clock application

---

*This project was automatically generated. Modify as needed for your requirements.*
"""
        else:
            readme_content = f"""# {self.project_spec['name']}

**Auto-generated by AI Agent System**

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Project Brief
{self.brief}

## Features
{chr(10).join([f'- {feature.capitalize()}' for feature in self.project_spec['features']])}

## How to Run

### Step 1: Navigate to Backend
```bash
cd outputs/backend
```

### Step 2: Install Dependencies
```bash
npm install
```

### Step 3: Start the Server
```bash
node server.js
```

**IMPORTANT:** Use `node server.js` command (NOT just `server.js`)

### Step 4: Open Browser
Open your browser and navigate to:
```
http://localhost:5000
```

The frontend is automatically served by the backend!

## API Endpoints

- `GET /api/{self.project_spec['entity']}s` - Get all items
- `POST /api/{self.project_spec['entity']}s` - Create new item
- `GET /api/{self.project_spec['entity']}s/:id` - Get item by ID
- `PUT /api/{self.project_spec['entity']}s/:id` - Update item
- `DELETE /api/{self.project_spec['entity']}s/:id` - Delete item
- `GET /api/search?q=query` - Search items

## Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Node.js, Express.js
- **Database**: In-memory storage (easily replaceable with MongoDB)

## Troubleshooting

### If you see "server.js is not recognized"
Make sure you're using the `node` command:
```bash
node server.js
```

NOT just:
```bash
server.js
```

### If port 5000 is already in use
1. Stop the process using port 5000, OR
2. Change the PORT in server.js

## Generated by AI Agents

- 🧠 **Coordinator Agent**: Orchestrated the generation process
- 🎨 **Frontend Agent**: Generated UI components
- ⚙️ **Backend Agent**: Generated API and data models

---

*This project was automatically generated. Modify as needed for your requirements.*
"""
        
        with open("outputs/README.md", "w", encoding='utf-8') as f:
            f.write(readme_content)
        
        print("COORDINATOR: Generated README.md")
        print()
    
    def run(self):
        """Main execution flow"""
        self.analyze_brief()
        generated_files = self.delegate_tasks()
        self.save_project_metadata()
        self.generate_readme()
        
        print("COORDINATOR: Generation Summary")
        if self.project_spec['type'] == 'crud':
            print(f"   - Frontend files: {len(generated_files['frontend'])}")
            print(f"   - Backend files: {len(generated_files['backend'])}")
            print(f"   - Total files: {len(generated_files['frontend']) + len(generated_files['backend'])}")
        else:
            print(f"   - Total files: {len(generated_files)}")