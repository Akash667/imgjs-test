import React, { useEffect, useState, useRef } from "react";
import {getEnhance, getSeam} from './api'; 
import './App.css';
import { Button, Card, CardContent, Input, Paper,  Slider,  TextField, Typography,} from "@material-ui/core";


function App() {

  const [seamValue, setSeamValue] = useState(20);
  const [offsets,setOffsets] = useState({});
  const [notProcessing, setProcessing]  = useState(true);

  const canvasRef = useRef(null);
  const imgRef = useRef(null);
  const contextRef = useRef(null);

  function downloadImage(data, filename = 'untitled.jpeg') {
    var a = document.createElement('a');
    a.href = data;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
}

  function canvasSave(){
    let canvas = canvasRef.current;
    let img = imgRef.current;

    let newCanvas = document.createElement('canvas');
    newCanvas.width = offsets.w;
    newCanvas.height = offsets.h;
    let newContext = newCanvas.getContext("2d");

    newContext.drawImage(canvas,offsets.x,offsets.y,offsets.w,offsets.h,0,0,offsets.w,offsets.h)

    let dataURL = newCanvas.toDataURL("image/jpeg",1.0);
    
    downloadImage(dataURL, 'my-canvas.jpeg');
  }

  function drawImageScaled(img,ctx) {
    let canvas = ctx.canvas;
    let hRatio = canvas.width / img.width;
    let vRatio = canvas.height / img.height;
    let ratio = Math.min(hRatio, vRatio);
    let centerShift_x = (canvas.width - img.width * ratio) / 2;
    let centerShift_y = (canvas.height - img.height * ratio) / 2;
    setOffsets({
      x:centerShift_x,
      y:centerShift_y,
      h:img.height*ratio,
      w:img.width*ratio
    })
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(
      img,
      0,
      0,
      img.width,
      img.height,
      centerShift_x,
      centerShift_y,
      img.width * ratio,
      img.height * ratio
    );
  }
  useEffect(() => {


    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    let img = new Image();
    let filename = "";

    const uploadBtn = document.getElementById("uploadfile");

    const menuDiv = document.getElementById("menu");

    uploadBtn.addEventListener("change", (e) => {

      const uploadFile = document.getElementById(
        "uploadfile"
      );

      const imageFiles = uploadFile.files;

      const file = imageFiles[0];

      const reader = new FileReader();

      if (file) {
        filename = file.name;

        reader.readAsDataURL(file);
      }

      reader.addEventListener(
        "load",
        () => {
          //create image
          img = new Image();
          img.src = reader.result;
          
          
          img.onload = function () {

            canvas.width = canvas.parentElement.clientWidth * 0.95;

            canvas.height = canvas.parentElement.clientHeight * 0.95;

            drawImageScaled(img, ctx);

            canvas.removeAttribute("data-caman-id");

            imgRef.current = img;
          };
        },
        false
      );
    });

  },[]);

  function onProcess(){

      const img = imgRef.current;
      const canvas = canvasRef.current;
      const ctx = canvas.getContext("2d");
      drawImageScaled(img,ctx);
    
  }


  return (
    <div className="app">
      <label className="uploadlabel">
        <Button>
          <input
            type="file"
            id="uploadfile"
            className="uploadbutton"
          ></input>
        </Button>
        <Button onClick={canvasSave}>
          Save
        </Button>

      </label>

      <Paper elevation={4} className="menu">

      {notProcessing && <canvas className="canva" id="canvas" ref={canvasRef}></canvas> }  

      </Paper>

      <Paper elevation={4} id="menu" className="toolbar">

        <div id="seamvalue">
        <Typography variant="h6" align="center" >Seams Reduction:<span id="valueOfSeam"> {seamValue} </span></Typography>
        </div>

        <Button id="leftslider" 
        variant="contained" color="primary" onClick={() => seamValue-10>0?setSeamValue(seamValue - 10):setSeamValue(0)}>
          <Typography >{"<"}</Typography>
        </Button>

        <Button id="rightslider"
          variant="contained" color="primary" onClick={() => setSeamValue(seamValue + 10)}>
          <Typography >{">"}</Typography>
        </Button>

        <Button id="process"
         variant="contained" color="primary" onClick={onProcess}  >
          <Typography >Carve</Typography>
        </Button>

        <Button id="illuminate"
         variant="contained" color="primary" >
          <Typography >Illuminate</Typography>
        </Button>


      </Paper>

    </div>
  );
}

export default App;
