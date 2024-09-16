<template>
  <div id="app">
    <header>
      <h1>Excelerate</h1>
    </header>
    <FileConverter />
  </div>
</template>

<script setup>
import FileConverter from './components/FileConverter.vue';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin: 0;
  padding: 0;
}

header {
  background-color: #4CAF50;
  padding: 20px 0;
  color: white;
  margin-bottom: 30px;
}

header h1 {
  margin: 0;
  font-size: 2.5em;
}

header p {
  margin: 10px 0 0 0;
  font-size: 1.2em;
  color: #dff0d8;
}
</style>