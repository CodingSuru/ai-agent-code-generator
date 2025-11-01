# 🤖 AI Agent Code Generator System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**Turn text descriptions into fully functional web applications using specialized AI agents**

[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [Usage](#-usage) • [Examples](#-examples)

</div>

---

## 📋 Overview

A **multi-agent system** that automatically generates production-ready web applications from simple text briefs. The system uses specialized agents (Coordinator, Frontend, Backend, DataViz, WorldClock) that collaborate to produce complete full-stack applications with zero manual coding.

### What Can It Build?

- 📝 **CRUD Applications** - Full-stack notes/todo apps with add, edit, delete, search
- 📊 **DataViz Dashboards** - Interactive charts with ML-powered anomaly detection
- 🌍 **World Clock Apps** - Live timezone clocks with auto-location detection

---

## ✨ Features

### 🧠 Multi-Agent Architecture
- **Coordinator Agent** - Analyzes briefs and delegates tasks
- **Frontend Agent** - Generates HTML/CSS/JS interfaces
- **Backend Agent** - Creates Express.js APIs and data models
- **DataViz Agent** - Builds chart dashboards with ML integration
- **WorldClock Agent** - Generates real-time clock applications

### 🎯 Key Capabilities
- ✅ Natural language input → Complete applications
- ✅ Auto-generates frontend + backend code
- ✅ Built-in search, CRUD operations, categories
- ✅ ML-powered anomaly detection (Z-score algorithm)
- ✅ File upload support (CSV, JSON, Excel)
- ✅ Responsive design with modern UI
- ✅ RESTful API architecture
- ✅ Comprehensive documentation

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
Node.js 18+
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-agent-code-generator.git
cd ai-agent-code-generator
```

2. **Run the generator**
```bash
python main.py
```

3. **Select a project type**
```
1. 📝 Notes App
2. 📊 DataViz Dashboard
3. 🌍 World Clock
```

4. **Navigate to outputs and run**
```bash
cd outputs/backend  # For CRUD apps
# OR
cd outputs          # For DataViz/WorldClock

npm install
node server.js
```

5. **Open browser**
```
http://localhost:5000
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│              COORDINATOR AGENT                       │
│  - Analyzes project briefs                          │
│  - Detects project type (CRUD/DataViz/WorldClock)   │
│  - Delegates to specialized agents                   │
└──────────────┬──────────────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────▼──────┐  ┌────▼────────┐  ┌────────────┐
│  FRONTEND   │  │   BACKEND   │  │  DATAVIZ   │
│   AGENT     │  │    AGENT    │  │   AGENT    │
│             │  │             │  │            │
│ - HTML      │  │ - Express   │  │ - Charts   │
│ - CSS       │  │ - API       │  │ - ML       │
│ - JavaScript│  │ - Models    │  │ - Upload   │
└─────────────┘  └─────────────┘  └────────────┘
```

### Agent Responsibilities

| Agent | Input | Output |
|-------|-------|--------|
| **Coordinator** | Text brief | Project specification |
| **Frontend** | Features list | HTML, CSS, JavaScript |
| **Backend** | Entity model | Express server, routes, models |
| **DataViz** | Data requirements | Dashboard with charts + ML |
| **WorldClock** | Timezone needs | Live clock interface |

---

## 📖 Usage

### Method 1: Interactive Menu
```bash
python main.py
# Select from menu options
```

### Method 2: Direct Brief (Custom)
```python
from agents.coordinator import CoordinatorAgent

brief = "Build a task manager with search and categories"
coordinator = CoordinatorAgent(brief)
coordinator.run()
```

### Generated Project Structure

#### CRUD Application
```
outputs/
├── backend/
│   ├── server.js           # Express server
│   ├── package.json        # Dependencies
│   ├── models/
│   │   └── note.js         # Data model
│   └── routes/
│       └── note.js         # API routes
├── frontend/
│   ├── index.html          # UI structure
│   ├── styles.css          # Styling
│   └── app.js              # Frontend logic
├── README.md               # Instructions
└── project_metadata.json   # Generation info
```

#### DataViz Dashboard
```
outputs/
├── index.html              # Dashboard UI
├── styles.css              # Styling
├── app.js                  # Charts + ML logic
├── server.js               # Static file server
├── package.json            # Dependencies
└── README.md               # Instructions
```

---

## 💡 Examples

### Example 1: Notes App
**Input:**
```
"Build a Notes App with add, search, edit, delete, and categories features"
```

**Generated:**
- ✅ Full CRUD API with 5 endpoints
- ✅ Search functionality
- ✅ Category management
- ✅ Responsive UI with fire-themed design
- ✅ In-memory database (easily swappable)

**API Endpoints:**
```
GET    /api/notes        - Get all notes
POST   /api/notes        - Create note
GET    /api/notes/:id    - Get single note
PUT    /api/notes/:id    - Update note
DELETE /api/notes/:id    - Delete note
GET    /api/search?q=... - Search notes
```

### Example 2: DataViz Dashboard
**Input:**
```
"Create a DataViz dashboard for crop and rainfall data with charts and anomaly detection"
```

**Generated:**
- ✅ 4 chart types (Line, Bar, Scatter, Pie)
- ✅ Drag & drop file upload
- ✅ Supports CSV, JSON, Excel
- ✅ ML anomaly detection (Z-score > 2σ)
- ✅ Auto-detects numeric columns
- ✅ Interactive data preview

**Features:**
- PapaParse for CSV parsing
- SheetJS for Excel files
- Chart.js for visualizations
- Statistical ML algorithms

### Example 3: World Clock
**Input:**
```
"Create a World Clock app with all timezones and auto location detection"
```

**Generated:**
- ✅ 8+ major city clocks
- ✅ Real-time updates (1s interval)
- ✅ Auto-detects user location
- ✅ Beautiful gradient UI
- ✅ Responsive grid layout

---

## 🛠️ Tech Stack

### Backend
- **Node.js** - Runtime environment
- **Express.js** - Web framework
- **UUID** - Unique ID generation
- **CORS** - Cross-origin support

### Frontend
- **Vanilla JavaScript** - No frameworks needed
- **Chart.js** - Data visualization
- **PapaParse** - CSV parsing
- **SheetJS** - Excel file handling

### AI/ML
- **Statistical Analysis** - Z-score anomaly detection
- **Client-side ML** - No external dependencies

---

## 📊 Project Comparison

| Feature | Notes App | DataViz | World Clock |
|---------|-----------|---------|-------------|
| **Type** | CRUD | Visualization | Real-time |
| **Agents** | 3 | 2 | 2 |
| **Files** | 8 | 5 | 5 |
| **Database** | In-memory | N/A | N/A |
| **API** | RESTful | Static | Static |
| **Complexity** | Medium | High | Low |

---

## 🔧 Configuration

### Backend Port
Default: `5000` (Change in `server.js`)
```javascript
const PORT = process.env.PORT || 5000;
```

### Database
Default: In-memory storage
```javascript
// Easily swap with MongoDB
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/myapp');
```

### Features Toggle
Edit `coordinator.py` to customize feature detection:
```python
if "search" in brief_lower:
    features.append("search")
```

---

## 📚 File Descriptions

### Core Files
- **`main.py`** - Entry point with interactive menu
- **`coordinator.py`** - Orchestrates agent collaboration
- **`frontend_agent.py`** - Generates UI components
- **`backend_agent.py`** - Creates API and models
- **`dataviz_agent.py`** - Builds chart dashboards
- **`worldclock_agent.py`** - Generates clock apps

### Output Files
- **`README.md`** - Project-specific instructions
- **`project_metadata.json`** - Generation timestamp & config
- **`server.js`** - Express server
- **`package.json`** - npm dependencies

---

## 🎨 Design Themes

### Notes App - Fire Theme 🔥
```css
background: linear-gradient(135deg, #ff6b35 0%, #f7931e 50%, #fdc830 100%);
```

### DataViz - Agriculture Green 🌾
```css
background: linear-gradient(135deg, #2d5016 0%, #4a7c2e 50%, #6b9b47 100%);
```

### World Clock - Ocean Blue 🌊
```css
background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e92b7 100%);
```

---

## 🐛 Troubleshooting

### Issue: "Port 5000 already in use"
```bash
# Find and kill process
lsof -ti:5000 | xargs kill -9
# OR change port in server.js
```

### Issue: "Cannot find module 'express'"
```bash
cd outputs/backend  # or outputs/
npm install
```

### Issue: "Server.js not recognized"
```bash
# Use node command
node server.js
# NOT just: server.js
```

---

## 🚧 Roadmap

- [ ] React/Vue.js frontend option
- [ ] MongoDB/PostgreSQL integration
- [ ] Authentication & authorization
- [ ] Deployment scripts (Docker, Heroku)
- [ ] Advanced ML models (TensorFlow.js)
- [ ] Real-time collaboration features
- [ ] Mobile app generation (React Native)
- [ ] API documentation generation (Swagger)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@CodingSuru](https://github.com/CodingSuru)
- LinkedIn: [Suryansh Singh](https://www.linkedin.com/in/suryansh-singh-5857a0263)

---

## 🙏 Acknowledgments

- Express.js community
- Chart.js team
- PapaParse & SheetJS contributors
- All open-source libraries used

---

## 📞 Support

- 📧 Email: searchjob395@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/CodingSuru/ai-agent-code-generator/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/CodingSuru/ai-agent-code-generator/discussions)

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ using AI Agents

</div>