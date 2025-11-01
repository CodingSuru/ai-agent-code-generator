from agents.coordinator import CoordinatorAgent
import os

def display_menu():
    """Display project options menu"""
    print("\n" + "=" * 60)
    print("AI AGENT CODE GENERATOR SYSTEM")
    print("=" * 60)
    print("\nSelect a project type to generate:\n")
    print("1. 📝 Notes App")
    print("   - CRUD application with add, search, edit, delete")
    print("   - Categories and timestamps")
    print("   - Full-stack (Frontend + Backend)")
    print()
    print("2. 📊 DataViz Dashboard")
    print("   - Interactive charts (Line, Bar, Scatter, Pie)")
    print("   - ML-powered anomaly detection")
    print("   - Drag & drop file upload (CSV/JSON/Excel)")
    print()
    print("3. 🌍 World Clock")
    print("   - Live clocks for multiple timezones")
    print("   - Auto location detection")
    print("   - Real-time updates")
    print()
    print("=" * 60)

def get_project_brief(choice):
    """Return project brief based on user choice"""
    briefs = {
        '1': "Build a Notes App with add, search, edit, delete, and categories features",
        '2': "Create a DataViz dashboard for crop and rainfall data with charts and anomaly detection",
        '3': "Create a World Clock app with all timezones and auto location detection"
    }
    return briefs.get(choice, None)

def main():
    display_menu()
    
    # Get user choice
    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice in ['1', '2', '3']:
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
    
    # Get corresponding project brief
    project_brief = get_project_brief(choice)
    
    print()
    print("✅ Selected Project:")
    if choice == '1':
        print("   📝 Notes App")
    elif choice == '2':
        print("   📊 DataViz Dashboard with ML")
    elif choice == '3':
        print("   🌍 World Clock")
    
    print()
    print("Starting AI Agent System...")
    print()
    
    # Create coordinator and run
    coordinator = CoordinatorAgent(project_brief)
    coordinator.run()
    
    print()
    print("=" * 60)
    print("✅ PROJECT GENERATION COMPLETE!")
    print("=" * 60)
    print()
    print("Generated files are in the 'outputs/' folder")
    print()
    
    # Display specific instructions based on project type
    if choice == '1':
        print("To run the Notes App:")
        print("  1. cd outputs/backend")
        print("  2. npm install")
        print("  3. node server.js")
        print("  4. Open http://localhost:5000 in browser")
    elif choice == '2':
        print("To run the DataViz Dashboard:")
        print("  1. cd outputs")
        print("  2. npm install")
        print("  3. node server.js")
        print("  4. Open http://localhost:5000 in browser")
        print()
        print("💡 Optional Enhancement:")
        print("   For advanced Python-based ML features:")
        print("   pip install scikit-learn pandas")
        print("   (Recommended but not required)")
    elif choice == '3':
        print("To run the World Clock:")
        print("  1. cd outputs")
        print("  2. npm install")
        print("  3. node server.js")
        print("  4. Open http://localhost:5000 in browser")
    
    print()

if __name__ == "__main__":
    # Create outputs directory
    os.makedirs("outputs/frontend", exist_ok=True)
    os.makedirs("outputs/backend", exist_ok=True)
    os.makedirs("outputs/backend/models", exist_ok=True)
    os.makedirs("outputs/backend/routes", exist_ok=True)
    
    main()