import { useDropzone } from "react-dropzone";

export default function UploadArea({onFileUpload}) {

    const { getRootProps, getInputProps } = useDropzone({ onDrop: files => {

            if(files.length > 0){onFileUpload(files[0]);}
        }
    });

    return (
        <div {...getRootProps()} className="upload-area">
            <input {...getInputProps()}/>
            <h2 className="text-2xl font-semibold"> Arraste seu arquivo</h2>
            <p className=" text-slate-400 mt-2"> CSV ou XLSX </p>
        </div>
    );
}