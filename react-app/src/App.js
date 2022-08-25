import React, {useState} from 'react';

import Graph from './graph.js';
import Upload from './upload.js';

import './App.css';

function App() {
  const [graphData, setGraphData] = useState();

  return (
    <div className="App">
      <header className="App-header">
        <h1>Does your data match Benson's law?</h1>
      </header>
      <Graph graphData={graphData}/>
      <Upload graphData={setGraphData}/>
    </div>
  );
}

export default App;
