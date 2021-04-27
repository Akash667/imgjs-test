const axios = require('axios');

const seamApi = "http://localhost:105"
const enchanceApi = ""

const api = axios.create({
    baseURL: 'http://localhost:105/',
    timeout: 0
})

async function getSeam(data,noOfSeams){

    const response = await axios.post(seamApi+"/seam/",{
        imgData:data,
        seams:noOfSeams
    })

    return response.data
   
}

async function getEnhance(data){

    const response = await axios.post(seamApi+"/seam/",{
        "imgData":data
    })
 
    return response.data

}

export  {getSeam , getEnhance };

