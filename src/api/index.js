const axios = require('axios');

const seamApi = ""
const enchanceApi = ""

async function getSeam(data,noOfSeams){

    const response = axios.post(seamApi,{
        dataURI:data,
        seams:noOfSeams
    })

   
}

async function getEnhance(data){

    const response = axios.post(enchanceApi,{
        dataURI:data
    })

}

export  {getSeam , getEnhance }