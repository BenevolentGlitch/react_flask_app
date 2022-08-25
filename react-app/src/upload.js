import React, {useState} from 'react';

const Upload = ({ graphData }) => {
  const [selectedFile, setSelectedFile] = useState();

  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const postFile = () => {
    const formData = new FormData();
    formData.append('File', selectedFile);
    fetch('/upload',
      {
        method: 'POST',
        body: formData,
      }
    )
      .then((response) => (response.json()))
      .then((result) => {
        graphData(result);
        console.log('Success:', result);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return(
    <div>
      <div>
        <p> Please select a valid CSV </p>
        <input type="file" name="file" onChange={changeHandler} />
        <button disabled={!selectedFile} onClick={postFile}>Submit</button>
      </div>
    </div>
  )
}

export default Upload;
