const axios = require('axios');

const seamApi = "http://localhost:105/"
const enchanceApi = ""

const api = axios.create({
    baseURL: 'http://0.0.0.0:105/',
    timeout: 0
})

async function getSeam(data,noOfSeams){

    const response = await axios.post(seamApi+"/hello/",{
        imgData:data,
        seams:noOfSeams
    })
    
    return response.data
   
}

async function getEnhance(data){

    const response = await axios.post(enchanceApi,{
        dataURI:data
    })

}

export  {getSeam , getEnhance };

