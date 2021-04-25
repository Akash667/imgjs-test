const axios = require('axios');

const seamApi = ""
const enchanceApi = ""

const api = axios.create({
    baseURL: 'http://0.0.0.0:105/',
    timeout: 0
})

async function getSeam(data,noOfSeams){

    const response = await axios.post(seamApi+"/seam",{
        imgData:data,
        seams:noOfSeams
    })
    console.log(response.data)
    return response
   
}

async function getEnhance(data){

    const response = await axios.post(enchanceApi,{
        dataURI:data
    })

}

export  {getSeam , getEnhance }

getSeam("asdsadasdasd",1000);