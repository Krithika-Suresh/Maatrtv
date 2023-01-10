import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, FlatList } from 'react-native';
import axios from 'axios';
import { useEffect, useState } from 'react';
// import React, { useState } from "react";
import {
  SafeAreaView,
  // Text,
  // View,
  // StyleSheet,
  Dimensions,
  ScrollView,
} from "react-native";

import { LineChart } from "react-native-chart-kit";

export default function App() {
  const [vitals, setVitals] = useState([])
  useEffect(()=>{
    async function getAllVitals(){
      try {
        const vitals = await axios.get('http://10.0.2.2:8000/vitals/')
        console.log(vitals.data)
        setVitals(vitals.data)
      } catch (error){
        console.log(error)
      }
    }
    getAllVitals()
  }, [])


  return (
    <View style={styles.container}>
      <FlatList
      data =  {vitals}
      renderItem = {({item})=><Text>{item.heart_beat}, {item.time}</Text>}
      />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


// import React, { useState } from "react";

// import {
//   SafeAreaView,
//   Text,
//   View,
//   StyleSheet,
//   Dimensions,
//   ScrollView,
// } from "react-native";

// import { LineChart } from "react-native-chart-kit";

// // const addValues = () => {
// //   setInterval(() => {
// //     setData([...data, Math.random() * 100 + 30]);
// //   }, 2000);
// // };

// const MyBezierLineChart = () => {
//   const [data, setData] = useState([66, 78, 86, 54, 87]);
//   //addValues();
//   setInterval(() => {
//     setData([...data, Math.random() * 100 + 30]);
//   }, 10000);

//   return (
//     <>
//       <Text style={styles.header}>Heart Rate Plot</Text>
//       <LineChart
//         data={{
//           labels: ["9:20", "9:21", "9:22", "9:23"],
//           datasets: [
//             {
//               data: data,
//             },
//           ],
//         }}
//         width={Dimensions.get("window").width - 16} // from react-native
//         height={220}
//         yAxisLabel={""}
//         chartConfig={{
//           backgroundColor: "#1cc910",
//           backgroundGradientFrom: "#eff3ff",
//           backgroundGradientTo: "#efefef",
//           decimalPlaces: 2,
//           color: (opacity = 255) => `rgba(0, 0, 0, ${opacity})`,
//           style: {
//             borderRadius: 16,
//           },
//         }}
//         bezier
//         style={{
//           marginVertical: 8,
//           borderRadius: 16,
//         }}
//       />
//     </>
//   );
// };

// const App = () => {
//   return (
//     <SafeAreaView style={{ flex: 1 }}>
//       <ScrollView>
//         <View style={styles.container}>
//           <View>
//             <MyBezierLineChart />
//           </View>
//         </View>
//       </ScrollView>
//     </SafeAreaView>
//   );
// };

// export default App;

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: "white",
//     justifyContent: "center",
//     alignItems: "center",
//     textAlign: "center",
//     padding: 10,
//   },
//   header: {
//     textAlign: "center",
//     fontSize: 18,
//     padding: 16,
//     marginTop: 16,
//   },
// });


