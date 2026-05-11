import { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [stats, setStats] = useState(null);

  const [customers, setCustomers] = useState([]);

  useEffect(() => {

    loadDashboard();

  }, []);

  async function loadDashboard() {

    try {

      const statsResponse = await axios.get(
        "https://gypsum-project-production.up.railway.app/dashboard/stats"
      );

      const customersResponse = await axios.get(
        "https://gypsum-project-production.up.railway.app/dashboard/customers"
      );

      setStats(statsResponse.data);

      setCustomers(customersResponse.data);

    } catch (error) {

      console.log(error);

    }
  }

  return (

    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        background: "#f5f7fa",
        minHeight: "100vh"
      }}
    >

      <h1>George AI Dashboard</h1>

      {stats && (

        <div
          style={{
            display: "flex",
            gap: "20px",
            marginBottom: "30px"
          }}
        >

          <div
            style={{
              background: "white",
              padding: "20px",
              borderRadius: "10px",
              width: "200px"
            }}
          >
            <h3>Total Customers</h3>
            <h2>{stats.total_customers}</h2>
          </div>

          <div
            style={{
              background: "white",
              padding: "20px",
              borderRadius: "10px",
              width: "200px"
            }}
          >
            <h3>Hot Leads</h3>
            <h2>{stats.hot_leads}</h2>
          </div>

          <div
            style={{
              background: "white",
              padding: "20px",
              borderRadius: "10px",
              width: "200px"
            }}
          >
            <h3>Total Messages</h3>
            <h2>{stats.total_messages}</h2>
          </div>

        </div>
      )}

      <h2>Customers</h2>

      <div
        style={{
          background: "white",
          padding: "20px",
          borderRadius: "10px"
        }}
      >

        {customers.map((customer, index) => (

          <div
            key={index}
            style={{
              padding: "10px",
              borderBottom: "1px solid #ddd"
            }}
          >

            <p>
              <strong>ID:</strong>
              {" "}
              {customer.facebook_id}
            </p>

            <p>
              <strong>Status:</strong>
              {" "}
              {customer.lead_status}
            </p>

            <p>
              <strong>Score:</strong>
              {" "}
              {customer.lead_score}
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}

export default App;