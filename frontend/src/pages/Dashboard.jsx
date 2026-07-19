import DashboardLayout from "../layouts/DashboardLayout";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

export default function Dashboard() {
    return (
        <DashboardLayout>
            <ChatWindow />
            <ChatInput />
        </DashboardLayout>
    );
}