import ToolCard from "./ToolCard";

export default function ToolGrid({ tools, selectedTools, toggleTool}) {

    return (
        <div className="tools-grid"> { tools.map(tool => (
                    <ToolCard 
                        key={tool.id}
                        tool={tool}
                        selected={selectedTools.includes(tool.id)}
                        toggle={toggleTool} 
                    />
                ))
            }
        </div>
    );
}