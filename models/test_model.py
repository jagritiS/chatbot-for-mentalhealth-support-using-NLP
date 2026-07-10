from mental_health_model import predict_condition



text = (
"I feel hopeless and "
"cannot sleep anymore"
)



result = predict_condition(
    text
)



print(result)