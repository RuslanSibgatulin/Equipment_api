import http from "../http-common";

class EquipmentDataService {
  getAllTypes() {
    return http.get("/equipment-type/");
  }

  getAll() {
    return http.get("/equipment/");
  }

  get(id) {
    return http.get(`/equipment/${id}`);
  }

  create(data) {
    return http.post("/equipment/", data);
  }

  update(id, data) {
    return http.put(`/equipment/${id}`, data);
  }

  delete(id) {
    return http.delete(`/equipment/${id}`);
  }

  find(query) {
    return http.get(`/equipment?search=${query}`);
  }
}

export default new EquipmentDataService();
