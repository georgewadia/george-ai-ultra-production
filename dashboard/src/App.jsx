import { useEffect, useState } from "react";
import axios from "axios";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts";

function App() {

  const [stats, setStats] = useState(null);

  const [customers, setCustomers] = useState([]);

  const [search, setSearch] = useState("");

  const [filter, setFilter] = useState("ALL");

  useEffect(() => {

  loadDashboard();

  const interval = setInterval(() => {

    loadDashboard();

  }, 10000);

  return () => clearInterval(interval);

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

  const filteredCustomers = customers.filter((customer) => {

    const matchesSearch =
      customer.facebook_id.includes(search);

    const matchesFilter =
      filter === "ALL"
      || customer.lead_status === filter;

    return matchesSearch && matchesFilter;

  });

  return (

    <div className="min-h-screen bg-gray-100 p-8">

      <h1 className="text-4xl font-bold mb-8">
        George AI Dashboard 🚀
      </h1>

      {stats && (

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">

          <div className="bg-white rounded-2xl p-6 shadow-lg">
            <h2 className="text-gray-500 text-lg">
              Total Customers
            </h2>

            <p className="text-4xl font-bold mt-4">
              {stats.total_customers}
            </p>
          </div>

          <div className="bg-red-500 text-white rounded-2xl p-6 shadow-lg">
            <h2 className="text-lg">
              Hot Leads
            </h2>

            <p className="text-4xl font-bold mt-4">
              {stats.hot_leads}
            </p>
          </div>

          <div className="bg-blue-500 text-white rounded-2xl p-6 shadow-lg">
            <h2 className="text-lg">
              Total Messages
            </h2>

            <p className="text-4xl font-bold mt-4">
              {stats.total_messages}
            </p>
          </div>

        </div>
      )}

      <div className="flex gap-4 mb-6">

        <input
          type="text"
          placeholder="Search Customer ID..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="p-3 rounded-xl border w-full"
        />

        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="p-3 rounded-xl border"
        >

          <option value="ALL">
            All
          </option>

          <option value="HOT">
            HOT
          </option>

          <option value="WARM">
            WARM
          </option>

          <option value="COLD">
            COLD
          </option>

        </select>

      </div>

      <div className="bg-white rounded-2xl shadow-lg p-6 mb-8">

  <h2 className="text-2xl font-bold mb-6">
    Lead Analytics
  </h2>

  <div style={{ width: "100%", height: 300 }}>

    <ResponsiveContainer>

      <PieChart>

        <Pie
          data={[
            {
              name: "HOT",
              value: customers.filter(
                c => c.lead_status === "HOT"
              ).length
            },
            {
              name: "WARM",
              value: customers.filter(
                c => c.lead_status === "WARM"
              ).length
            },
            {
              name: "COLD",
              value: customers.filter(
                c => c.lead_status === "COLD"
              ).length
            }
          ]}
          dataKey="value"
          outerRadius={100}
          label
        >

          <Cell fill="#ef4444" />
          <Cell fill="#facc15" />
          <Cell fill="#9ca3af" />

        </Pie>

        <Tooltip />

      </PieChart>

    </ResponsiveContainer>

  </div>

</div>

      <div className="bg-white rounded-2xl shadow-lg p-6">

        <h2 className="text-2xl font-bold mb-6">
          Customers
        </h2>

        <div className="space-y-4">

          {filteredCustomers.map((customer, index) => (

            <div
              key={index}
              className="border rounded-xl p-4 flex justify-between items-center"
            >

              <div>

                <p className="font-bold">
                  {customer.facebook_id}
                </p>

                <p className="text-gray-500">
                  Lead Score:
                  {" "}
                  {customer.lead_score}
                </p>

              </div>

              <div>

                <span
                  className={
                    customer.lead_status === "HOT"
                    ? "bg-red-500 text-white px-4 py-2 rounded-full"
                    : customer.lead_status === "WARM"
                    ? "bg-yellow-400 px-4 py-2 rounded-full"
                    : "bg-gray-300 px-4 py-2 rounded-full"
                  }
                >
                  {customer.lead_status}
                </span>

              </div>

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default App;