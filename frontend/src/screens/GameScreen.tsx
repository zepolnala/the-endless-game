import React, { useState } from "react";
import { View, Text, TextInput, Button, ScrollView, StyleSheet, KeyboardAvoidingView, Platform } from "react-native";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/generate-story"; // Asegúrate de usar la IP correcta si usas un emulador o un dispositivo físico

const GameScreen: React.FC = () => {
    const [messages, setMessages] = useState<{ sender: string; text: string }[]>([]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        if (!input.trim()) return;

        const newMessages = [...messages, { sender: "user", text: input }];
        setMessages(newMessages);
        setInput("");

        try {
            const response = await axios.post(API_URL, {
                user_id: "player1",
                message: input,
            });
            setMessages([...newMessages, { sender: "AI", text: response.data.response }]);
        } catch (error) {
            console.error("Error al enviar mensaje:", error);
        }
    };

    return (
        <KeyboardAvoidingView 
            behavior={Platform.OS === "ios" ? "padding" : "height"} 
            style={styles.container}
        >
            <ScrollView style={styles.chatContainer} contentContainerStyle={{ flexGrow: 1, justifyContent: "flex-end" }}>
                {messages.map((msg, index) => (
                    <Text key={index} style={msg.sender === "user" ? styles.userText : styles.aiText}>
                        {msg.text}
                    </Text>
                ))}
            </ScrollView>
            <View style={styles.inputContainer}>
                <TextInput
                    style={styles.input}
                    value={input}
                    onChangeText={setInput}
                    placeholder="Escribe tu decisión..."
                    placeholderTextColor="#888"
                />
                <Button title="Enviar" onPress={sendMessage} />
            </View>
        </KeyboardAvoidingView>
    );
};

const styles = StyleSheet.create({
    container: { flex: 1, padding: 10, backgroundColor: "#fff" },
    chatContainer: { flex: 1 },
    userText: { alignSelf: "flex-end", backgroundColor: "#DCF8C6", padding: 8, borderRadius: 5, marginVertical: 4 },
    aiText: { alignSelf: "flex-start", backgroundColor: "#ECECEC", padding: 8, borderRadius: 5, marginVertical: 4 },
    inputContainer: { flexDirection: "row", alignItems: "center", padding: 10, borderTopWidth: 1, borderColor: "#ccc" },
    input: { flex: 1, borderWidth: 1, borderColor: "#ccc", padding: 10, borderRadius: 5, marginRight: 10 },
});

export default GameScreen;
