export default function ToolCard({ tool, selected, toggle}) {
    return (
        <div onClick={() => toggle(tool.id) } className={ selected ? "tool-card selected" : "tool-card" } >
            <h3> {tool.name} </h3>
        </div>
    );
}