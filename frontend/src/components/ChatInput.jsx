export default function ChatInput() {
    return (
        <div className="border-t bg-white p-4 flex gap-3">

            <input
                type="text"
                placeholder="Ask a question..."
                className="flex-1 border rounded-lg px-4 py-3"
            />

            <button
                className="bg-blue-600 text-white px-6 rounded-lg"
            >
                Send
            </button>

        </div>
    );
}