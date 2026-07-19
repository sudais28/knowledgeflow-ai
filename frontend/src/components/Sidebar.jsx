export default function Sidebar() {
    return (
        <div className="w-72 bg-white border-r p-5">
            <h1 className="text-2xl font-bold mb-8">
                KnowledgeFlow AI
            </h1>

            <button
                className="w-full bg-blue-600 text-white py-3 rounded-lg mb-8"
            >
                Upload PDF
            </button>

            <h2 className="font-semibold mb-3">
                Uploaded Documents
            </h2>

            <div className="space-y-2">
                <div className="border rounded p-2">
                    No documents yet
                </div>
            </div>
        </div>
    );
}