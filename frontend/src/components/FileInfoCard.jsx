export default function FileInfoCard({ preview }){
    if(!preview)
        return null
    return(
        <div className="info-card">
            <h2> Arquivo carregado </h2>
            <p> Linhas: {preview.total_rows} </p>
            <p> Colunas: {preview.total_columns}</p>
        </div>
    )
}