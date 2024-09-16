<template>
    <div class="converter">

        <h2>Excel ↔ JSON Converter</h2>
        <p>Select a file to convert between Excel and JSON formats.</p>
        <div class="dropzone" @dragover.prevent @drop.prevent="handleDrop" @click="triggerFileSelect">
            <p>Drag and drop a file here or</p>
            <button @click.stop="triggerFileSelect">Choose a File</button>
            <input type="file" ref="fileInput" @change="handleFileChange" />
        </div>

        <div v-if="loading" class="progress-bar">
            <div class="progress" :style="{ width: progress + '%' }"></div>
        </div>

        <div v-if="previewData" class="preview-section">
            <h3>Preview:</h3>
            <pre>{{ previewData }}</pre>
        </div>

        <div v-if="downloadUrl" class="download-section">
            <a :href="downloadUrl" download>Download Converted File</a>
        </div>

        <div v-if="error" class="error-message">
            {{ error }}
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import * as XLSX from 'xlsx';

const downloadUrl = ref(null);
const loading = ref(false);
const progress = ref(0);
const error = ref(null);
const previewData = ref(null);
const fileInput = ref(null);

const handleFile = async (file) => {
    error.value = null;
    downloadUrl.value = null;
    previewData.value = null;
    loading.value = true;
    progress.value = 0;

    const formData = new FormData();
    formData.append('file', file);

    let url = '';
    let isExcelToJson = false;

    if (file.name.endsWith('.xlsx')) {
        url = 'http://localhost:8000/api/convert/excel-to-json/';
        isExcelToJson = true;
    } else if (file.name.endsWith('.json')) {
        url = 'http://localhost:8000/api/convert/json-to-excel/';
    } else {
        error.value = 'Unsupported file format.';
        loading.value = false;
        return;
    }

    // Preview the file
    try {
        if (isExcelToJson) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const data = e.target.result;
                const workbook = XLSX.read(data, { type: 'binary' });
                const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
                const jsonData = XLSX.utils.sheet_to_json(firstSheet, { header: 1 });
                previewData.value = JSON.stringify(jsonData, null, 2);
            };
            reader.readAsBinaryString(file);
        } else {
            const reader = new FileReader();
            reader.onload = (e) => {
                try {
                    const data = e.target.result;
                    const jsonData = JSON.parse(data);
                    previewData.value = JSON.stringify(jsonData, null, 2);
                } catch (parseError) {
                    console.error(parseError);
                    error.value = 'Invalid JSON file format.';
                }
            };
            reader.readAsText(file);
        }
    } catch (previewError) {
        console.error(previewError);
        error.value = 'Failed to preview the file.';
    }

    try {
        const response = await axios.post(url, formData, {
            responseType: 'blob',
            onUploadProgress: (progressEvent) => {
                progress.value = Math.round(
                    (progressEvent.loaded * 100) / progressEvent.total
                );
            },
        });
        const blob = new Blob([response.data], { type: response.headers['content-type'] });
        downloadUrl.value = URL.createObjectURL(blob);
    } catch (err) {
        console.error(err);
        if (err.response && err.response.data && err.response.data.error) {
            error.value = `Conversion failed: ${err.response.data.error}`;
        } else {
            error.value = 'Conversion failed due to a network error.';
        }
    } finally {
        loading.value = false;
    }
};

const handleDrop = (event) => {
    const file = event.dataTransfer.files[0];
    if (file) {
        handleFile(file);
    }
};

const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
        handleFile(file);
    }
};

const triggerFileSelect = () => {
    fileInput.value.click();
};
</script>

<style scoped>
.converter {
    text-align: center;
    margin-top: 50px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    font-family: Arial, sans-serif;
}

.dropzone {
    border: 2px dashed #4CAF50;
    border-radius: 10px;
    padding: 40px;
    cursor: pointer;
    position: relative;
    transition: background-color 0.3s, border-color 0.3s;
}

.dropzone:hover {
    background-color: #f9f9f9;
    border-color: #45a049;
}

.dropzone p {
    margin: 0 0 10px 0;
    font-size: 16px;
    color: #555;
}

.dropzone button {
    padding: 10px 20px;
    background-color: #4CAF50;
    border: none;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

.dropzone button:hover {
    background-color: #45a049;
}

.dropzone input {
    display: none;
}

.progress-bar {
    width: 100%;
    background-color: #f3f3f3;
    border-radius: 5px;
    margin-top: 20px;
}

.progress {
    height: 20px;
    background-color: #4CAF50;
    width: 0%;
    border-radius: 5px;
    transition: width 0.4s ease;
}

.preview-section {
    text-align: left;
    margin: 20px 0;
}

.preview-section h3 {
    color: #4CAF50;
}

.preview-section pre {
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    max-height: 300px;
    overflow-y: auto;
}

.download-section {
    margin-top: 20px;
}

.download-section a {
    padding: 10px 20px;
    background-color: #2196F3;
    color: white;
    border-radius: 5px;
    text-decoration: none;
}

.download-section a:hover {
    background-color: #0b7dda;
}

.error-message {
    color: red;
    margin-top: 20px;
}
</style>