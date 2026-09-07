export async function sendMessage(
    text
){

    const response =
        await api.post(
            "/chat",
            {
                message:text
            }
        );

    return response.data;
}
