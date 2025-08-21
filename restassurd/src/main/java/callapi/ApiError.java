package callapi;

public class ApiError {
    private String message;
    private String error;
    private int status;

    public ApiError(String message, String error, int status) {
        this.message = message;
        this.error = error;
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public String getError() {
        return error;
    }

    public int getStatus() {
        return status;
    }
}
