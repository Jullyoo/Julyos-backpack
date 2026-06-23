export default function DataPreview({preview}) {

    if(!preview)
        return null

    const columns = preview.columns

    return (
        <table className="preview-table">
            <thead>
                <tr> { columns.map(col => ( <th key={col}> {col} </th>) ) } </tr>
            </thead>
            <tbody>{ preview.rows.map( (row,index)=>( 
                <tr key={index}> { columns.map(col=>(
                     <td key={col}> { row[col] } </td>
                                ))
                            }
                        </tr>
                    ))
                }
            </tbody>
        </table>
    )
}