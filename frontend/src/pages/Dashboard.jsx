import { useState } from "react";

import UploadArea from "../components/UploadArea";
import ToolGrid from "../components/ToolGrid";
import FileInfoCard from "../components/FileInfoCard";
import DataPreview from "../components/DataPreview";

import api from "../services/api";
import { tools } from "../services/tools";

import "../styles/main.css";
import logo from "../assets/images/julyo_bp_logo.png";

export default function Dashboard() {
  const [file, setFile] = useState(null);

  const [preview, setPreview] = useState(null);

  const [selectedTools, setSelectedTools] = useState([]);

  const toggleTool = (id) => {
    setSelectedTools((prev) =>
      prev.includes(id)
        ? prev.filter((tool) => tool !== id)
        : [...prev, id]
    );
  };

  const uploadFile = async (file) => {
    try {
      setFile(file);

      const formData = new FormData();

      formData.append("file", file);

      const response = await api.post(
        "/preview",
        formData
      );

      setPreview(response.data);

      console.log("Preview carregado:");
      console.log(response.data);

    } catch (error) {
      console.error(
        "Erro ao gerar preview:",
        error
      );
    }
  };

  const processFile = async () => {
    try {
      if (!file) {
        alert(
          "Selecione um arquivo primeiro."
        );
        return;
      }

      const formData = new FormData();

      formData.append(
        "file",
        file
      );

      selectedTools.forEach((tool) => {
        formData.append(
          "operations",
          tool
        );
      });

      const response = await api.post(
        "/process",
        formData
      );

      console.log(
        "Resultado:",
        response.data
      );

      window.open(
        `http://localhost:5000/download/${response.data.filename}`,
        "_blank"
      );

    } catch (error) {
      console.error(
        "Erro ao processar arquivo:",
        error
      );
    }
  };

  return (
    <div className="dashboard">

      <div className="dashboard-header">
        <img src={logo} alt="Logo" className="logo-img" />

        <div className="dashboard-text">
          <h1 className="dashboard-title"> Julyo's Backpack </h1>
          <p className="dashboard-subtitle"> Caixa de Ferramentas para Analistas de Dados </p>
        </div>
        
      </div>
      <UploadArea onFileUpload={uploadFile}/>
      <FileInfoCard preview={preview} />
      <DataPreview preview={preview} />
      <ToolGrid tools={tools} selectedTools={selectedTools} toggleTool={toggleTool} />
      <button onClick={processFile} className="execute-btn"> Executar ETL </button>
    </div>
  );
}