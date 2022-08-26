import { Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';

import { Bar } from 'react-chartjs-2';
import './graph.css'

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

const Graph = ({ graphData }) => {
  if(!graphData) {
    return;
  }

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: "Benford's Law",
      },
    },
  };

  const labels = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
  const actual_percentages = Object.values(graphData).map((value, index) => { return value.actual_percentage});
  const expected_percentages = Object.values(graphData).map((value, index) => { return value.expected_percentage});
  const data = {
    labels,
    datasets: [
      {
        label: 'Actual percentages',
        data: actual_percentages,
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
      },
      {
        label: 'Expected Percentages',
        data: expected_percentages,
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  };

  return <div className='Graph'>
          <Bar options={options} data={data}/>
         </div>
}

export default Graph;
