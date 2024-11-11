import React from 'react';
import { SafeAreaView, StyleSheet } from 'react-native';
import { WebView } from 'react-native-webview';

const App = () => {
  return (
    <SafeAreaView style={{ flex: 1 }}>
      <WebView source={{ uri: ' http://127.0.0.1:8000/' }} />
    </SafeAreaView>
  );
};

export default App; 