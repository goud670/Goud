import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";
import { Tabs, TabsList, TabsTrigger } from "@/components/ui/tabs";

const Dashboard = () => {
  const [data, setData] = useState([]);
  const [selectedMetric, setSelectedMetric] = useState("temperature");

  useEffect(() => {
    // Simulated fetch from sensor data API or preprocessed CSV
    fetch("/iot-data.json")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  const metrics = ["temperature", "humidity", "water_level", "nitrogen", "phosphorus", "potassium"];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-4">
      <Card className="col-span-2">
        <CardContent>
          <h2 className="text-xl font-semibold mb-2">IoT Agriculture Monitoring Dashboard</h2>
          <Tabs defaultValue={selectedMetric} onValueChange={setSelectedMetric}>
            <TabsList>
              {metrics.map((metric) => (
                <TabsTrigger key={metric} value={metric}>
                  {metric.charAt(0).toUpperCase() + metric.slice(1)}
                </TabsTrigger>
              ))}
            </TabsList>
          </Tabs>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
              <XAxis dataKey="timestamp" hide />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey={selectedMetric} stroke="#3b82f6" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h3 className="text-lg font-medium mb-2">Irrigation Prediction</h3>
          <p className="text-sm text-muted-foreground">System predicts optimal irrigation schedules based on current temperature, humidity, and water levels.</p>
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h3 className="text-lg font-medium mb-2">Maintenance Forecast</h3>
          <p className="text-sm text-muted-foreground">Equipment maintenance needs predicted from usage patterns and sensor anomalies.</p>
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;
