export default function ChatWindow() {
    return (
        <div className="flex-1 p-8 overflow-y-auto">
            <div className="space-y-6">

                <div className="flex justify-end">
                    <div className="bg-blue-600 text-white p-3 rounded-xl max-w-lg">
                        Hello
                    </div>
                </div>

                <div className="flex justify-start">
                    <div className="bg-white shadow p-3 rounded-xl max-w-lg">
                        Hi! Upload a document to begin.
                    </div>
                </div>

            </div>
        </div>
    );
}