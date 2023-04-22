import axios from "axios";

const axiosApiInstance = axios.create(
  {
    baseURL: process.env.VUE_APP_EQUIPMENT_API
  }
);

axiosApiInstance.interceptors.request.use(
  async config => {
    config.headers = {
      "Authorization": `Bearer ${localStorage.token}`,
      "Content-type": "application/json",
    }
    return config;
  },
  error => {
    Promise.reject(error)
});

axiosApiInstance.interceptors.response.use((response) => {
  return response
}, async function (error) {

  if (error.response.status === 401) {
    window.location.href = '/login';
  }

  return Promise.reject(error);
});

export default axiosApiInstance
